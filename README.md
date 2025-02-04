<h1 align="center">Piškvorkové úlohy</h1>
<p>A project made for Tour de App. Utilizes Flask and PostgreSQL (Which we host on Supabase).</p>

<h2>How to run</h2>
<h3>Postgres Database</h3>
<p>Either way, you'll have to create a .env file and host a Postgres database.</p>
<p>You can start a Postrgres database easily with either <a href="https://www.postgresql.org/">PostgreSQL itself</a> or if you wanna go online you can do so for free with <a href="https://supabase.com/">Supabase</a>.
<br>
<b>No need to prepare any tables within your database, the webapp will create them for you.</b></p>
<p>create the <code>.env</code> file right next to the <code>Dockerfile</code>:</p>

```
DB_USER="your postgres username"
DB_PASS="your database password"
DB_HOST="your database host"
DB_PORT="your database port"
DB_NAME="your database name"
```

<h3>With Docker</h3>
<ol>
    <li><a href="https://www.docker.com/">Install Docker</a></li>
    <li>Run the <code>autorun_docker.bat</code> script.</li>
</ol>
<h3>Without Docker</h3>
<ol>
<li><a href="https://www.python.org/">Install Python</a></li>
<li>Install the requests package: <code>pip install requests</code></li>
<li>Install the Flask package: <code>pip install flask</code></li>
<li>Install the Flask-HTTPAuth package: <code>pip install Flask-HTTPAuth</code></li>
<li>Install the dotenv package: <code>pip install python-dotenv</code></li>
<li>Install the psycopg2 package: <code>pip install psycopg2</code></li>
<li>Run the project with <code>python ./app/app.py</code></li>
</ol>