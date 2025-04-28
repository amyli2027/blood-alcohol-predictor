from flask import Flask, render_template, request, redirect, url_for, session
import pandas as pd
import pickle

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Load your trained BAC model
with open('ohio_ethanol_model.pkl', 'rb') as f:
    bac_model = pickle.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    weight = float(request.form.get("weight"))
    desired_bac = float(request.form.get("desired_bac"))

    if desired_bac > 0.25:
        session["desired_bac"] = desired_bac
        return redirect(url_for('warning'))

    # Convert weight from pounds to grams
    weight_in_grams = weight * 453.592

    input_features = [[weight_in_grams, desired_bac]]
    grams_alcohol_needed = bac_model.predict(input_features)[0]  # MODEL OUTPUTS GRAMS

    num_drinks = grams_alcohol_needed / 14
    num_drinks = round(num_drinks, 2)

    # BAC over time: rising then falling
    bac_over_time = []

    # Rising phase
    time_to_peak = 1
    bac_increase_rate = desired_bac / time_to_peak

    time_step = 0.1
    time = 0.0
    bac = 0.0

    while bac < desired_bac:
        bac = min(bac + bac_increase_rate * time_step, desired_bac)
        bac_over_time.append((round(time, 2), round(bac, 4)))
        time += time_step

    # Falling phase
    bac_fall_rate = 0.015

    while bac > 0:
        bac = max(bac - bac_fall_rate * time_step, 0)
        bac_over_time.append((round(time, 2), round(bac, 4)))
        time += time_step

    # Save session values
    session["grams_alcohol_needed"] = grams_alcohol_needed
    session["num_drinks"] = num_drinks
    session["bac_over_time"] = bac_over_time

    return render_template(
        "results.html",
        num_drinks=num_drinks,
        bac_over_time=bac_over_time
    )


@app.route("/results")
def results():
    num_drinks = session.get("num_drinks", 0)
    bac_over_time = session.get("bac_over_time", [])

    return render_template(
        "results.html",
        num_drinks=num_drinks,
        bac_over_time=bac_over_time
    )

@app.route("/amounts")
def amounts():
    grams_alcohol_needed = session.get("grams_alcohol_needed", 0)
    num_drinks = session.get("num_drinks", 0)

    alcohol_contents = {
        "Wine": 0.12,   # 12% alcohol by volume
        "Beer": 0.05,   # 5% alcohol
        "Seltzer": 0.07,
        "Hard liquor": 0.40
    }

    amounts = {}

    # Ethanol density = 0.789 g/mL
    pure_ethanol_volume_ml = grams_alcohol_needed / 0.789

    for drink_type, alc_percent in alcohol_contents.items():
        volume_ml = pure_ethanol_volume_ml / alc_percent
        volume_oz = volume_ml * 0.033814

        # Standard drinks = (total grams of alcohol in this drink) / 14
        # grams_alcohol_in_total_drink = (alc_percent * volume_ml) * 0.789
        total_grams_alcohol = alc_percent * volume_ml * 0.789
        standard_drinks = total_grams_alcohol / 14

        amounts[drink_type] = {
            "ml": round(volume_ml, 1),
            "oz": round(volume_oz, 1),
            "standard_drinks": round(standard_drinks, 2)
        }

    return render_template("amounts.html", amounts=amounts, num_drinks=num_drinks)

@app.route("/warning")
def warning():
    desired_bac = session.get("desired_bac", 0)
    return render_template("warning.html", desired_bac=desired_bac)




if __name__ == "__main__":
    app.run(debug=True)
