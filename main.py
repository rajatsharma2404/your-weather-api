from flask import Flask, render_template
import pandas as pd

app = Flask("Website")

stations = pd.read_csv("data_small/stations.txt", skiprows=17)
stations = stations[["STAID","STANAME                                 "]]

@app.route("/")
def home():
    return render_template("home.html", data = stations.to_html())

@app.route("/api/v1/<station>/<date>")
def about(station, date):


    filename = "data_small/" + "TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows = 20, parse_dates=['    DATE'])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze()/10
    return {
        "Station" : station,
        "Date" : date,
        "temp" : temperature
    }

@app.route("/api/v1/<station>")
def all_data(station):
    filename = "data_small/" + "TG_STAID" + str(station).zfill(6) + ".txt"
    data = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    return data.to_dict(orient="records")

@app.route("/api/v1/yearly/<station>/<year>")
def yearly_data(station, year):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    data = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    data["    DATE"] = data["    DATE"].astype(str)
    yeardata = data[data["    DATE"].str.startswith(str(year))].to_dict(orient="records")
    return yeardata

if __name__ == "__main__":
    app.run(debug=True, port=1024)