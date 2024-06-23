import os
import traceback
from datetime import datetime
import pandas as pd
from django.core.management.base import BaseCommand
from core_app.models import User
from devices_app.models import Devices, UserDevice
from glucose_level_app.models import GlucoseLevel

class Command(BaseCommand):
    """
    This class will generat glucose level data from csv file and populate to database.
    It will first check if the user exists, otherwise it creates an new user.
    Then it will checks if the devise type and serial number exists, otherwise it creates them.
    Finaly, it iterates over the the file rows and creates them one by one.
    """
    help = 'Loads sample data into GlucoseLevel model'

    def add_arguments(self, parser):
        parser.add_argument("sample_data", type=str)

    def handle(self, *args, **options):
        print('loading the sample data into the database...')
        sample_data = options["sample_data"]
        for file in os.listdir(sample_data):
            if file.endswith(".csv"):
                file_path = os.path.join(sample_data, file)
                user_abbreviation = os.path.basename(file_path)
                user_abbreviation, extension = os.path.splitext(file)
                
                # Checking if the user exists
                user_ids = User.objects.filter(user_abbreviation=user_abbreviation).values_list('id', flat=True)
                if user_ids:
                        user_id = user_ids[0]
                        print(f"User {user_abbreviation} has been found on the database")
                else:
                    """
                    Prepare user's data for insertion (I assume that users already exist in the production,
                    but this is to make a smooth and fast data upload for testing purposes)
                    """
                    username = user_abbreviation
                    password = user_abbreviation
                    email = f'{user_abbreviation}@test.com'
                    # create the user
                    print ("Creating a new user...")
                    user_instance = User(username = username,
                                        password = password,
                                        email = email,
                                        user_abbreviation=user_abbreviation
                    )
                    user_instance.save()
                    user_id = user_instance.id
                    print(f'The user {user_abbreviation} has been created successfully')
                
                # Reading CSV file
                df = pd.read_csv(file_path, skiprows=1)
                
                # creating a counter to track row numbers for identifying issues
                counter = 0
                # Iterate through the DataFrame
                for index, row in df.iterrows():
                    counter = counter+1
                    print(f"------------ row number: {str(counter)}, from the file {user_abbreviation}.csv ------------")
                    device_type = row['Gerät']
                    serial_number = row['Seriennummer']
                    
                    # Checking if the device_type exists
                    device_id = Devices.objects.filter(device_type=device_type).values_list('id', flat=True)
                    if device_id:
                        device_id = device_id[0]
                        print(f"Device {device_type} has been found on the database")
                    else:
                        print("Creating a new device...")
                        device_instance = Devices(device_type=device_type)
                        device_instance.save()
                        device_id = device_instance.id
                        print(f'The device {device_type} has been created successfully')

                    # Checking if the serial_number exists
                    serial_number_id = UserDevice.objects.filter(serial_number=serial_number).values_list('id', flat=True)
                    if serial_number_id:
                        serial_number_id = serial_number_id[0]
                        print(f"Device serial number {serial_number} has been found on the database")
                    else:
                        print("Creating a new serial number...")

                        userdevice_instance = UserDevice(serial_number=serial_number)
                        userdevice_instance.device_type_id = int(device_id)
                        userdevice_instance.user_id_id = int(user_id)
                        userdevice_instance.save()

                        serial_number_id = userdevice_instance.id
                        print(f'The Serial number {serial_number} has been created successfully')
                    
                    # convert the timestamp format in the Gerätezeitstempel from string to datetime
                    time_stamp = datetime.strptime(row['Gerätezeitstempel'], "%d-%m-%Y %H:%M")

                # inserting  glucose levels  into the model GlucoseLevel
                    print(f"Creating a new glucose level record for the user: {user_abbreviation}. Timestamp: {time_stamp}")

                    glucoselevel_instance = GlucoseLevel(
                                        device_timestamp = time_stamp,
                                        record_type = row['Aufzeichnungstyp'],
                                        glucose_history_mg_dL = row['Glukosewert-Verlauf mg/dL'],
                                        glucose_scan_mg_dL = row['Glukose-Scan mg/dL'],
                                        non_numeric_rapid_acting_insulin  = row['Nicht numerisches schnellwirkendes Insulin'],
                                        rapid_acting_insulin_units = row['Schnellwirkendes Insulin (Einheiten)'],
                                        non_numeric_food_data = row['Nicht numerische Nahrungsdaten'],
                                        carbohydrates_grams = row['Kohlenhydrate (Gramm)'],
                                        carbohydrates_servings = row['Kohlenhydrate (Portionen)'],
                                        non_numeric_depot_insulin = row['Nicht numerisches Depotinsulin'],
                                        depot_insulin_units = row['Depotinsulin (Einheiten)'],
                                        notes = row['Notizen'],
                                        glucose_test_strip_mg_dL = row['Glukose-Teststreifen mg/dL'],
                                        ketone_mmol_L = row['Keton mmol/L'],
                                        mealtime_insulin_units = row['Mahlzeiteninsulin (Einheiten)'],
                                        correction_insulin_units = row['Korrekturinsulin (Einheiten)'],
                                        user_insulin_change_units = row['Insulin-Änderung durch Anwender (Einheiten)']
                    )
                    glucoselevel_instance.device_id = int(serial_number_id)
                    glucoselevel_instance.save()
                print(f"================ End of the file {user_abbreviation}.csv ================")
                
        self.stdout.write(
                    self.style.SUCCESS('Successfully created new glucose levels data for the user "%s"' % user_abbreviation)
            )
