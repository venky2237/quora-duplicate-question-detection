from flask import Flask, render_template, request

import pickle

from utils import query_point_creator


app = Flask(__name__)


# ---------------------------------------------------------
# LOAD TRAINED MODEL
# ---------------------------------------------------------

with open("model.pkl", "rb") as file:
    model = pickle.load(file)


# ---------------------------------------------------------
# LOAD BAG OF WORDS VECTORIZER
# ---------------------------------------------------------

with open("cv.pkl", "rb") as file:
    cv = pickle.load(file)


# ---------------------------------------------------------
# HOME PAGE
# ---------------------------------------------------------

@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    probability = None

    question1 = ""
    question2 = ""

    if request.method == "POST":

        question1 = request.form.get(
            "question1", ""
        ).strip()

        question2 = request.form.get(
            "question2", ""
        ).strip()

        if question1 and question2:

            # Create features
            query_features = query_point_creator(
                question1,
                question2,
                cv
            )

            # Prediction
            prediction = model.predict(
                query_features
            )[0]

            # Probability
            if hasattr(model, "predict_proba"):

                probability = model.predict_proba(
                    query_features
                )[0][1]

    return render_template(
        "index.html",
        prediction=prediction,
        probability=probability,
        question1=question1,
        question2=question2
    )


# ---------------------------------------------------------
# RUN FLASK
# ---------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)