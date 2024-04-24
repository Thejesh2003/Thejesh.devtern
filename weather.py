# Import libraries
import requests
from tkinter import Tk, Label, Entry, Button

# Define API key (replace with your own)
api_key = "3997cc54cbe8d3193b75620b41560868"

# Function to get weather data
def get_weather(city):
  url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
  response = requests.get(url)
  if response.status_code == 200:
    return response.json()
  else:
    return None

# Function to display weather information
def display_weather(data):
  if data:
    city = data["name"]
    temperature = data["main"]["temp"]
    description = data["weather"][0]["description"]
    label["text"] = f"City: {city}\nTemperature: {temperature:.2f}°C\nDescription: {description}"
  else:
    label["text"] = "Error: Could not find weather data"

# Main application window
root = Tk()
root.title("Weather App")

# Entry field for city name
city_entry = Entry(root, width=30)
city_entry.pack(padx=10, pady=10)

# Button to trigger weather fetch
button = Button(root, text="Get Weather", command=lambda: display_weather(get_weather(city_entry.get())))
button.pack(padx=10, pady=10)

# Label to display weather information
label = Label(root, font=("Arial", 16))
label.pack(padx=10, pady=10)

# Run the main application loop
root.mainloop()