import tkinter as tk
import requests
import datetime

def getCovidData():
    api = "https://disease.sh/v3/covid-19/all"
    json_data = requests.get(api).json()
    total_population = str(json_data['population'])
    active_cases = str(json_data['active'])
    total_cases = str(json_data['cases'])
    today_cases = str(json_data['todayCases'])
    total_deaths = str(json_data['deaths'])
    today_deaths = str(json_data['todayDeaths'])
    total_recovery = str(json_data['recovered'])
    today_recovery = str(json_data['todayRecovered'])
    update_at = json_data['updated']
    date = datetime.datetime.fromtimestamp(update_at/1e3)
    label.config(text = "Total Population: "+total_population
    +"\n"+"Active Cases: "+active_cases
    +"\n"+"Total Cases: "+total_cases
    +"\n"+"Cases Today: "+today_cases
    +"\n"+"Total Deaths: "+total_deaths
    +"\n"+"Deaths Today: "+today_deaths
    +"\n"+"Total Recovery: "+total_recovery
    +"\n"+"Recovered Today: "+today_recovery)

    label2.config(text = date)

canvas = tk.Tk() 
canvas.geometry("600x600")
canvas.title("Covid-19 Tracker App")

bg = tk.PhotoImage(file = 'Covid-19 Tracker\Covid-19_Virus_BG.png')
bg_label = tk.Label(canvas, image = bg)
bg_label.place(relwidth = 1, relheight = 1)

f = ("poppins", 20, "bold")

button = tk.Button(canvas, font = f, bg = 'Yellow', text = "Refresh", command = getCovidData)
button.pack(pady = 20)

label = tk.Label(canvas, font = f)
label.pack(pady = 20)

label2 = tk.Label(canvas, font = 20)
label2.pack()

canvas.mainloop()

