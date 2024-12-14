<h1 align="center"> Exploring Glucose Levels datasets using Django REST framework </h1>

<h2 id="table-of-contents"> 📋 Table of Contents</h2>
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#overview"> ➤ Overview</a></li>
    <li><a href="#data_sets"> ➤ Data Sets</a></li>
    <li><a href="#technologies-used"> ➤ Technologies Used</a></li>
    <li><a href="#setup_and_installation"> ➤ Setup and Installation</a></li>
    <li><a href="#API_usage"> ➤ API Usage </a></li>
    <li><a href="#Further_Ideas"> ➤ Further Ideas </a></li>
    <li><a href="#references"> ➤ References</a></li>
  </ol>
</details>

<br>
<h2 id="overview"> 📖 Overview</h2>
<p align="justify"> 
  This is an API Endpoint developed to upload CSV dataset using managment command and list the records from the database using APIs.
</p>

<br>
<h2 id="data_sets"> 📈 Data Sets</h2>
<p align="justify"> 
  The data sets used for this application are the glucose levels data exported from FreeStyle LibreLink devices.
</p>

<br>
<h2 id="technologies-used"> 🌐 Technologies Used</h2>
<ul>
  <li><b>Backend:</b></li>
    <ul>
      <li><b>Python</b></li>
      <li><b>Django</b></li>
    </ul>
  <li><b>Database:</b></li>
    <ul>
      <li><b>sqlite3</b></li>
    </ul>
  <li><b>Dockerizing Tool</b> </li>
    <ul>
      <li><b>Docker</b></li>
    </ul>
</ul>

<br>
<h2 id="setup_and_installation"> ⚙️ Setup and Installation</h2>

<ol>
  <li><b>Create a virtual environment<pre><code>virtualenv venv </code></pre></b></li>
  <li><b>Activate a virtual environment<pre><code>source venv/bin/activate </code></pre></b></li>
  <li><b>Clone This repository<pre><code>git clone https://github.com/wail-abbas/Django_app_upload_glucose_level_dataset.git</code></pre></b></li>
  <li><b>Go to the project Directory<pre><code> cd Django_app_upload_glucose_level_dataset</code></pre></b></li>
  <li><b>Install requirements<pre><code> pip install -r requirements.txt </code></pre></b></li>
  <li><b>Makemigrations<pre><code>python manage.py makemigrations </code></pre></b></li>
  <li><b>Migrate<pre><code>python manage.py migrate </code></pre></b></li>
  <li><b>Create super user<pre><code>python manage.py createsuperuser </code></pre></b></li>
  <li><b>Load the sample data into the database<pre><code>python manage.py import_data <path/to/sample-data-folder> </code></pre></b></li>
  <li><b>Run tests <pre><code> pytest </code></pre></b></li>
  <li><b>Run the app <pre><code>python manage.py runserver </code></pre></b></li>
  <li><b>Open the admin panle in the browser, and add some data<pre><code>http://127.0.0.1:8000/admin </code></pre></b></li>
  <li><b> Run with Docker </b></li>
  <ol>
    <li><b>Run the App using Docker<pre><code>docker-compose up -d --build </code></pre></b></li>
    <li><b>Shut down the App <pre><code>docker-compose down </code></pre></b></li>
  </ol>
</ol>

<br>
<h2 id="API_usage"> 🖥️ API Usage</h2>
<ul>
<ul>
  <li><b>List all records:</b></li><pre><code>http://127.0.0.1:8000/api/v1/levels</code></pre></b></li>
  <li><b>Retrieve ( GET ) a list of glucose levels for a given user_id:</b></li><pre><code>http://127.0.0.1:8000/api/v1/levels/?user_id=cccccccc-cccc-cccc-cccc-cccccccccccc</code></pre></b></li>
  <li><b>Filter by start and stop timestamps:</b></li><pre><code>http://127.0.0.1:8000/api/v1/levels/?device_timestamp__gt=2021-02-10T08%3A07%3A00Z&device_timestamp__lt=2021-02-11T08%3A07%3A00Z</code></pre></b></li>
  <li><b>Pagination:</b></li><pre><code>http://127.0.0.1:8000/api/v1/levels/?page=3</code></pre></b></li>
  <li><b>Ascending ordering by user ID:</b></li><pre><code>http://127.0.0.1:8000/api/v1/levels/?ordering=device__user_id__user_abbreviation</code></pre></b></li>
  <li><b>Descending ordering by user ID:</b></li><pre><code>http://127.0.0.1:8000/api/v1/levels/?ordering=-device__user_id__user_abbreviation</code></pre></b></li>
  <li><b>Ascending ordering by timestamps:</b></li><pre><code>http://127.0.0.1:8000/api/v1/levels/?ordering=device_timestamp</code></pre></b></li>
  <li><b>Descending ordering by timestamps:</b></li><pre><code>http://127.0.0.1:8000/api/v1/levels/?ordering=-device_timestamp</code></pre></b></li>
  <li><b>Search by user ID:</b></li><pre><code>http://127.0.0.1:8000/api/v1/levels/?search=aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa</code></pre></b></li>
  <li><b>Search by timestamps:</b></li><pre><code>http://127.0.0.1:8000/api/v1/levels/?search=2021-02-11</code></pre></b></li>
  <li><b>Retrieve ( GET ) a particular glucose level by id:</b></li><pre><code>http://127.0.0.1:8000/api/v1/levels/2500/</code></pre></b></li>
</ul>
</ul>

<h2 id="further_ideas"> 💡 Further Ideas</h2>
<ul>
  <li> Add Users Permissions</li>
  <li> Store sensitive data in environment variable </li>
  <li> Generate API documentation using drf spectacular, <a href="https://drf-spectacular.readthedocs.io/en/latest/"> documentation</a></li>
  <li> Deploy on digitalocean with Kubernetes, <a href="https://docs.digitalocean.com/products/kubernetes/"> digitalocean documentation</a></li>
  <li> Consider a performing testing with locust, <a href="https://docs.locust.io/en/stable/"> locust documentation</a></li>
  <li> Integrate with FreestyleLiber to generate reports directly, <a href="https://tryterra.co/integrations/freestylelibre"> here are more information</a></li>
</ul>
<br>
<h2 id="references"> 📚 References</h2>
<ul>
  <li><a href="https://docs.djangoproject.com/en/3.2/"> Django Documentation </a></li>
  <li><a href="https://www.django-rest-framework.org/"> Django REST framework Documentation </a></li>
  <li><a href="https://peps.python.org/pep-0008/"> PEP 8 – Style Guide for Python Code </a></li>
</ul>
