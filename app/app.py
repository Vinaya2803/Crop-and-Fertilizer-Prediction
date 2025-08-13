from flask import Flask, render_template, request
from markupsafe import Markup
import requests
import numpy as np
import pandas as pd
from utils.fertilizer import fertilizer_dic
import config
import pickle
import io
import torch
from torchvision import transforms
from PIL import Image



crop_recommendation_model_path = "models/RandomForest.pkl"
crop_recommendation_model = pickle.load(open(crop_recommendation_model_path, "rb"))


def weather_fetch(city_name):
    """
    Fetch and returns the temperature and humidity of a city
    :params: city_name
    :return: temperature, humidity
    """
    api_key = config.weather_api_key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] != "404":
        y = x["main"]

        temperature = round((y["temp"] - 273.15), 2)
        humidity = y["humidity"]
        return temperature, humidity
    else:
        return None


app = Flask(__name__)


@app.route("/")
def home():
    title = "Home"
    return render_template("index.html", title=title)


@app.route("/crop-recommend")
def crop_recommend():
    title = " Crop "
    return render_template("crop.html", title=title)


@app.route("/fertilizer")
def fertilizer_recommendation():
    title = " Fertilizer "

    return render_template("fertilizer.html", title=title)


@app.route("/crop-predict", methods=["POST"])
def crop_prediction():
    title = " Crop "

    if request.method == "POST":
        N = int(request.form["nitrogen"])
        P = int(request.form["phosphorous"])
        K = int(request.form["pottasium"])
        ph = float(request.form["ph"])
        rainfall = float(request.form["rainfall"])

        city = request.form.get("city")

        if weather_fetch(city) != None:
            temperature, humidity = weather_fetch(city)
            data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
            my_prediction = crop_recommendation_model.predict(data)
            final_prediction = my_prediction[0]

            return render_template(
                "crop-result.html", prediction=final_prediction, title=title
            )

        else:

            return render_template("try_again.html", title=title)


@app.route("/fertilizer-predict", methods=["POST"])
def fert_recommend():
    title = "Fertilizer"

    try:
        crop_name = str(request.form["cropname"])
        N = int(request.form["nitrogen"])
        P = int(request.form["phosphorous"])
        K = int(request.form["pottasium"])

        df = pd.read_csv("Data/fertilizer.csv")

        if crop_name not in df["Crop"].values:
            return render_template("fertilizer-result.html", recommendation="No fertilizer found for this crop", title=title)

        nr = df[df["Crop"] == crop_name]["N"].iloc[0]
        pr = df[df["Crop"] == crop_name]["P"].iloc[0]
        kr = df[df["Crop"] == crop_name]["K"].iloc[0]

        n = nr - N
        p = pr - P
        k = kr - K
        temp = {abs(n): "N", abs(p): "P", abs(k): "K"}
        max_value = temp[max(temp.keys())]

        if max_value == "N":
            key = "NHigh" if n < 0 else "Nlow"
        elif max_value == "P":
            key = "PHigh" if p < 0 else "Plow"
        else:
            key = "KHigh" if k < 0 else "Klow"

        response = Markup(str(fertilizer_dic[key]))

        return render_template("fertilizer-result.html", recommendation=response, title=title)

    except Exception as e:
        print(f"Error: {e}")
        return render_template("fertilizer-result.html", recommendation="An error occurred. Please try again.", title=title)



if __name__ == "__main__":
    app.run(debug=False)
