from flask import Flask

app = Flask(__name__)

def add(a, b):
    return a + b

@app.route("/")
def home():
    return f"Result: {add(8,2)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
