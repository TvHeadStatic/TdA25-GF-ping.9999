<h1 align="center">Piškvorkové úlohy</h1>
<p>A project made for Tour de App. Utilizes Flask and PostgreSQL (Which we host on Supabase).</p>

<h2>How to run on your machine</h2>
<h3>Postgres Database</h3>
<p>You can start a Postgres database easily with either <a href="https://www.postgresql.org/">PostgreSQL itself</a> or if you wanna go online you can do so for free with <a href="https://supabase.com/">Supabase</a>.
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

<h3>Preparing and running Python</h3>
<ol>
<li><a href="https://www.python.org/">Install Python</a></li>
<li>Install the requests package: <code>pip install requests</code></li>
<li>Install the Flask package: <code>pip install flask</code></li>
<li>Install the Flask-HTTPAuth package: <code>pip install Flask-HTTPAuth</code></li>
<li>Install the dotenv package: <code>pip install python-dotenv</code></li>
<li>Install the psycopg2 package: <code>pip install psycopg2</code></li>
<li>Install the flask-socketio package: <code>pip install flask-socketio</code></li>
<li>Run the project with <code>python ./app/app.py</code></li>
</ol>
<p><small>*note: It has come to our attention, that using Docker without build-args breaks environment variables. If you want to use Docker, <a href="https://stackoverflow.com/questions/34254200/how-to-pass-arguments-to-a-dockerfile#34254700">here's a comprehensive stack-overflow answer showing off how to build with build-args</a><small>.<br>(to make your life easier, the build-args are called the exact same as in the .env file)</p>