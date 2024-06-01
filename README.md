***

<h1 align="center">
<sub>
<img src="app/static/assets/icons/favicon.ico" height="40" width="40">
</sub>
Weather Forecast App
</h1>

***

Weather Forecast App uses machine learning in Python to forecast weather based on passed data and display it using a user-friendly GUI written in Flask.

***

### Dataset

Dataset source: [Weather Data](https://www.kaggle.com/datasets/prasad22/weather-data/data)

Dataset columns:

- Location: The city where the weather data was simulated.
- Date_Time: The date and time when the weather data was recorded.
- Temperature_C: The temperature in Celsius.
- Humidity_pct: The humidity in percentage.
- Precipitation_mm: The precipitation in millimeters.
- Wind_Speed_kmh: The wind speed in kilometers per hour.
- Weather_Condition: The weather condition, e.g. Sunny, Rainy.

***

### Software requirements

- Python 3.11
- Modern web browser

### How to run

```
git clone https://github.com/ptakf-uek/WeatherForecastApp
cd WeatherForecastApp
python -m pip install -r requirements.txt
python -m flask run
```

This will serve the app at localhost:5000.

The dataset must be downloaded and placed in the path according to the `global_variables.py` file (default: `WeatherForecastApp/app/static/data/weather_data.csv`), otherwise the program will not run correctly.
