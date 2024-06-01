from flask import render_template, request, send_from_directory
import pandas as pd
from app import app
from app.global_variables import (
    DATASET_PATH,
    TRAINED_MODEL_PATH,
    WEATHER_CONDITIONS_DESCRIPTIONS,
)
from app.utils import (
    load_model_from_file,
    predict_weather,
    save_model_to_file,
    train_model,
)
import os, random


@app.route("/", methods=["POST", "GET"])
def index():
    weather_conditions = ""
    weather_conditions_descriptions = WEATHER_CONDITIONS_DESCRIPTIONS

    if request.method == "POST":
        if "train" in request.form:
            data = pd.read_csv(DATASET_PATH)
            model = train_model(data)
            save_model_to_file(model, TRAINED_MODEL_PATH)

        elif "predict" in request.form:
            model = load_model_from_file(TRAINED_MODEL_PATH)
            data = pd.read_csv(DATASET_PATH)
            new_data = pd.DataFrame(
                [
                    [
                        (
                            request.form.get("temperature-input")
                            if request.form.get("temperature-input") != ""
                            else 0
                        ),
                        (
                            request.form.get("humidity-input")
                            if request.form.get("humidity-input") != ""
                            else 0
                        ),
                        (
                            request.form.get("precipitation-input")
                            if request.form.get("precipitation-input") != ""
                            else 0
                        ),
                        (
                            request.form.get("wind-speed-input")
                            if request.form.get("wind-speed-input") != ""
                            else 0
                        ),
                    ]
                ],
                columns=[
                    "Temperature_C",
                    "Humidity_pct",
                    "Precipitation_mm",
                    "Wind_Speed_kmh",
                ],
            )

            weather_conditions = predict_weather(model, data, new_data)[0]

    return render_template(
        "index.html.jinja",
        train_button_enabled=os.path.exists(DATASET_PATH),
        predict_button_enabled=os.path.exists(TRAINED_MODEL_PATH),
        weather_conditions=weather_conditions,
        weather_conditions_description=weather_conditions_descriptions[
            weather_conditions
        ],
    )


@app.route("/sampledata")
def sampledata():
    with open(DATASET_PATH, "r", encoding="utf-8") as dataset_file:
        dataset_headers = pd.read_csv(dataset_file, nrows=0).columns.tolist()
        dataset_file.seek(0)

        # Select random rows from a percentage of the dataset (approximately 0.01 = 1%)
        dataset = pd.read_csv(
            dataset_file,
            header=0,
            skiprows=lambda i: i > 0 and random.random() > 0.00005,
        )

        dataset.columns = dataset_headers

        return render_template(
            "sampledata.html.jinja",
            rows=dataset.to_dict(orient="records"),
            headers=dataset_headers,
        )


@app.route("/about")
def about():
    return render_template("about.html.jinja")


@app.route("/static/scripts/<path:filename>")
def serve_static(filename):
    return send_from_directory(
        "static/scripts", filename, mimetype="application/javascript"
    )
