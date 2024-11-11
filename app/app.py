from flask import Flask

app = Flask(__name__)


@app.route("/")
def main():
    return "Hello TdA", 200

@app.route("/api")
def api():
    return "{\"organization\": \"Student Cyber Games\"}", 200

if __name__ == '__main__':
    app.run(debug=True)
