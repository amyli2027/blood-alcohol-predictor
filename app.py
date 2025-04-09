from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///responses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Response(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sex = db.Column(db.String(10))
    age = db.Column(db.Integer)
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    strength_training = db.Column(db.String(50))
    desired_drunkenness = db.Column(db.String(50))
    wine_percentage = db.Column(db.Float)
    beer_percentage = db.Column(db.Float)
    other_percentage = db.Column(db.Float)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    data = request.json

    new_response = Response(
        sex=data.get("sex"),
        age=data.get("age"),
        height=data.get("height"),
        weight=data.get("weight"),
        strength_training=data.get("strength_training"),
        desired_drunkenness=data.get("desired_drunkenness"),
        wine_percentage=data.get("wine_percentage"),
        beer_percentage=data.get("beer_percentage"),
        other_percentage=data.get("other_percentage"),
    )

    db.session.add(new_response)
    db.session.commit()

    return jsonify({"message": "Data saved successfully!"})

@app.route("/responses")
def show_responses():
    all_responses = Response.query.all()
    return render_template("responses.html", responses=all_responses)

if __name__ == "__main__":
    app.run(debug=True)
