from flask import Flask

app = Flask(__name__)


@app.route("/")
def main():
    return "Hello TdA"

@app.route("/api")
def api():
    return {"organization": "Student Cyber Games"}

if __name__ == '__main__':
    app.run(debug=True)
