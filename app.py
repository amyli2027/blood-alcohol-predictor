from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    data = request.json  
    user_input = data.get("user_input", "No input provided")
    result = {"output": f"Processed: {user_input}"}
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)