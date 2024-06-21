<h1 align="center">  Glucose levels </h1>

<h2 id="table-of-contents"> 📋 Table of Contents</h2>
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#overview"> ➤ Overview</a></li>
    <li><a href="#technologies-used"> ➤ Technologies Used</a></li>
    <li><a href="#Usage"> ➤ Usage</a></li>
    <li><a href="#Unfinished_Tasks"> ➤ Unfinished Tasks </a></li>
    <li><a href="#Further_Ideas"> ➤ Further_Ideas </a></li>
    <li><a href="#references"> ➤ References</a></li>
  </ol>
</details>

<br>
<h2 id="overview"> 📖 Overview</h2>
<p align="justify"> 
  This is an API Endpoint developed to list a glucose levels records from the database.
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
<h2 id="Usage"> 🖥️ Usage</h2>

<ol>
  <li><b>Create a virtual environment<pre><code>virtualenv venv </code></pre></b></li>
  <li><b>Activate a virtual environment<pre><code>source venv//bin/activate </code></pre></b></li>
  <li><b>Clone This repository<pre><code>git clone https://github.com/wail-abbas/glucose_level.git</code></pre></b></li>
  <li><b>Go to the project Directory<pre><code> cd glucose_level</code></pre></b></li>
  <li><b>Install requirements<pre><code> pip install -r requirements.txt </code></pre></b></li>

  <li><b>Migrate<pre><code>python manage.py migrate </code></pre></b></li>
  <li><b>Makemigrations<pre><code>python manage.py makemigrations </code></pre></b></li>
  <li><b>Create super user<pre><code>python manage.py createsuperuser </code></pre></b></li>
  <li><b>Run the app <pre><code>python manage.py runserver </code></pre></b></li>
  
  <li><b>Open the admin panle in the browser, and add some data<pre><code>http://127.0.0.1:8000/admin </code></pre></b></li>

  <li><b> Run with Docker </b></li>
  <ol>
    <li><b>Run the App using Docker<pre><code>docker-compose up -d --build </code></pre></b></li>
    <li><b>Shut down the App <pre><code>docker-compose down </code></pre></b></li>
  </ol>
</ol>

<br>
<h2 id="unfinished_tasks"> ⚠️ Unfinished Tasks</h2>
<p align="justify"> 
  Due to an issue with my PostgreSQL database and bad time management, I couldn't finish everything in my implementation plan and checklist I created before coding, So Kindly find the other tasks I was planning to do:
</p>
<ul>
  <li><b>Fix the PostgreSQL issue and use it as a database engin</b></li>
  <li><b>Create Permissions to allow users to only retrieve their data.</b></li>
  <li><b>Implement a POST endpoint to fill / pre-populate the model / database via an
  API endpoint.</b></li>
  <li><b>Implement export and import features </b></li>
  <li><b>Create unit tests for both Endpoints and models.</b></li>
  <li><b>Deploy on digitalocean with kubernetes.</b></li>
</ul>

<h2 id="Further_Ideas"> 💡 To-Do</h2>
<ul>
  <li><b> Consider doing a performing testing with locust</b></li>
  <li><b> Integrat with FreestyleLiber to generate reports directoly</b></li>
</ul>
<br>
<h2 id="references"> 📚 References</h2>
<ul>
  <li><a href="https://docs.djangoproject.com/en/3.2/"> Django Documentation </a></li>
</ul>
