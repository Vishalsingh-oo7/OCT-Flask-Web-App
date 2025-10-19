from flask import Flask
app = Flask(__name__)

@app.route("/")  # maps HOME URL → this function
def home():
    return "Hello, World!"

# /aboutus route
@app.route("/aboutus", methods=['GET'])
def aboutus():
    return "<p>We are Mlops learners</p>"

# /vishal route
@app.route("/Vishal", methods=['POST'])
def hello_world():
    return "<p>Hello, World - My name is Vishal Singh Rajput and I am Learning Flask!</p>"


if __name__ == "__main__":
    app.run(debug=True)  # runs on http://127.0.0.1:5000