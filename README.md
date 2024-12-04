<h1 align="center">Piškvorkové úlohy</h1>
<p>A project made for Tour de App. Utilizes Flask and SQLite.</p>

<h2>How to run</h2>
<p>If you have Docker, you can run it through the <code>autorun_docker.bat</code> script.</p>
<p>If you want to run the project without Docker you need:</p>
<ol>
<li>To install Python</li>
<li>install the requests package through <code>pip install requests</code></li>
<li>install the Flask package through <code>pip install flask</code></li>
<li>install the Flask-HTTPAuth package through <code>pip install Flask-HTTPAuth</code></li>
<li>then run the project with <code>python ./app/app.py</code></li>
</ol>
<p>(By default it will use the API that is hosted on "odevzdávací server". You can change that by editing the URLs in <code>app/game/game.py</code> and <code>app/gateway/gateway.py</code> to <code>http://127.0.0.1:5000/api/v1/games</code>)</p>