from flask import Flask

app = Flask(__name__)

def add(a, b):
    return a + b

@app.route("/")
def home():
    return "Hello DevOps"

@app.route("/add/<int:a>/<int:b>")
def addition(a, b):
    return str(add(a, b))

# IMPORTANT 👇
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
