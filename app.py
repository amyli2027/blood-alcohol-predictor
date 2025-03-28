from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///responses.db'  # SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Response model
class Response(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_1 = db.Column(db.String(200))
    question_2 = db.Column(db.String(200))
    question_3 = db.Column(db.String(200))
    question_4 = db.Column(db.String(200))
    question_5 = db.Column(db.String(200))
    question_6 = db.Column(db.String(200))
    question_7 = db.Column(db.String(200))
    question_8 = db.Column(db.String(200))
    question_9 = db.Column(db.String(200))
    question_10 = db.Column(db.String(200))


# Create the database tables
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    data = request.json
    responses = {key: f"Processed: {value}" for key, value in data.items()}

    # Save responses to the database
    new_response = Response(
        question_1=data.get("question1"),
        question_2=data.get("question2"),
        question_3=data.get("question3"),
        question_4=data.get("question4"),
        question_5=data.get("question5"),
        question_6=data.get("question6"),
        question_7=data.get("question7"),
        question_8=data.get("question8"),
        question_9=data.get("question9"),
        question_10=data.get("question10"),
    )
    db.session.add(new_response)
    db.session.commit()

    return jsonify(responses)
@app.route("/responses")
def show_responses():
    all_responses = Response.query.all()  # Get all responses from the database
    return render_template("responses.html", responses=all_responses)

if __name__ == "__main__":
    app.run(debug=True)
