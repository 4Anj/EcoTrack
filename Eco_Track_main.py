import pandas as pd
import numpy as np
import joblib
import csv
from datetime import datetime

def welcome():
    print("hello tracker")
    print("This app lets you monitor and track your carbon footprint")
    print("Cause just knowing makes a lot of difference :)")
    print("Rise to live the best life")
    print("Lets begin...\n")

def get_user_inputs():
    print("Please answer the following questions:")
    
    travel_km = float(input("1. How many kilometers do you travel by vehicle daily?"))
    electricity_kwh = float(input("2. How many kWh of electricity do you use per month?"))
    meat_meals = int(input("3. How many meat-based meals do you eat per week?"))
    online_orders = int(input("4. How many online purchases do you make per month?"))

    return travel_km, electricity_kwh, meat_meals, online_orders

# Estimate factors:
# Travel: 0.21kg CO2/km
# Electricity: 0.92 kg CO2/kWh
# Meat Meals: 2.5 kg CO₂ / meal
# Online Orders: 1.1 kg CO₂ / order

def calculate_carbon_footprint(travel_km, electricity_kwh, meat_meals, online_orders):
    travel_emission= travel_km * 30 * 0.21
    electricity_emission= electricity_kwh * 0.92
    food_emission= meat_meals * 4 * 2.5
    shopping_emission= online_orders * 1.1

    total_emission= travel_emission+electricity_emission+food_emission+shopping_emission
    return round(total_emission,2)


def save_to_csv(date, travel_km, electricity_kwh, meat_meals, online_orders, total_emission, category):
    filename= "carbon_data.csv"
    file_exists= False

    try:
        with open(filename,"r"):
            file_exists=True
    except FileNotFoundError:
        pass

    with open(filename, "a", newline="") as csvfile:
        fieldnames = ["Date","Travel (km/day)", "electricity (kWh/month)", "meat meals/week", "Online orders", "Total CO2 (kg)", "CO2 Category"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow({
            "Date": date, "Travel (km/day)": travel_km, "electricity (kWh/month)": electricity_kwh, "meat meals/week": meat_meals,
            "Online orders": online_orders, "Total CO2 (kg)": round(total_emission,2),
            "CO2 Category":category
            })

        
welcome()
travel_km, electricity_kwh, meat_meals, online_orders = get_user_inputs()
total_emission = calculate_carbon_footprint(travel_km, electricity_kwh, meat_meals, online_orders)

if total_emission < 500:
    category = "Low"
elif total_emission < 1000:
    category = "Medium"
else:
    category = "High"

print("\n Thank you! summary of your monthly inputs:")
print(f"-> Daily travel: {travel_km} km")
print(f"-> monthly use of electricity: {electricity_kwh} kwh")
print(f"-> weekly meat based meals: {meat_meals}")
print(f"-> monthly online purchases: {online_orders}")

print(f"Estimated monthly carbon footprint:{total_emission:.2f} kg CO2")

if total_emission < 500:
    print("Your lifestyle has a low carbon impact. Great job!")
elif total_emission < 1000:
    print("Moderate carbon footprint. Some improvements possible!")
else:
    print("High carbon footprint. Consider more sustainable habits.")

model=joblib.load("carbon_footprint_classifier.pkl")
label_encoder = joblib.load("label_encoder.pkl")

# Prepare input for model
input_data = pd.DataFrame([[travel_km, electricity_kwh, meat_meals, online_orders]],
                          columns=["Travel (km/day)", "electricity (kWh/month)",
                                   "meat meals/week", "Online orders"])

prediction = model.predict(input_data)
predicted_category = label_encoder.inverse_transform(prediction)[0]

# Print predicted category
print(f"\nPredicted Carbon Category (via ML model): {predicted_category}")

# Give personalized suggestion
if predicted_category == "Low":
    print("Great job! Keep up your eco-friendly habits.")
elif predicted_category == "Medium":
    print("Tip: Reduce meat meals by 1/week to cut ~10kg CO₂.")
elif predicted_category == "High":
    print("Consider limiting vehicle travel or switching to greener transport.")

today = datetime.now().strftime("%Y-%m-%d")
save_to_csv(today, travel_km, electricity_kwh, meat_meals, online_orders, total_emission, category)
print("\n Your data has been saved to carbon_data.csv!")
