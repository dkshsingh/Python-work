import tkinter as tk 
import requests
import datetime

def getCovidData():
    api = " https://disease.sh/v3/covid-19/all"
    json_data = requests.get(api).json()
    total_cases = str(json_data['cases'])
    total_deaths = str(json_data['deaths'])
    today_cases = str(json_data['todayCases'])
    today_deaths = str(json_data['todaysDeaths'])
    today_recovered = str(json_data['todaysRcovered'])
    updated_at = json_data['updated']
    date = datetime.datetime._fromtimestamp(updated_at/le3)
    label.config(text = "total Cases: "+ total_cases
                 +"total Deaths: "+ total_deaths
                 +"total Cases: "+ today_cases
                 +"todays Deaths: "+ today_deaths
                 +"today recovered: "+ today_recovered)
    
    label2.config( text = date )
canvas = tk.Tk()
canvas.geometry("400x400")
canvas.title("corona tracker app")

f = ("poppins", 15, "bold")

button = tk.Button(canvas, font = f, text = "load", command = getCovidData)
button.pack(pady = 20)

label = tk.Label(canvas, font= f)
label.pack(pady= 20)

label2 = tk.Label(canvas, font = 8)
label2.pack()
getCovidData()

canvas.mainloop()