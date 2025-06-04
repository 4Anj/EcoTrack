import pandas as pd
import matplotlib.pyplot as plt

#visualise through line, bar, pie and category-wise graphs.

def load_data(filename = "carbon_data.csv"):
    df= pd.read_csv(filename)
    df["Date"]= pd.to_datetime(df["Date"])
    
    df["Travel_CO2"]= df["Travel (km/day)"] * 30 * 0.21
    df["Electricity_CO2"]= df["electricity (kWh/month)"] * 0.92
    df["Meat_CO2"]= df["meat meals/week"] * 4 * 2.5
    df["Online_CO2"]= df["Online orders"] * 1.1
    return df

def plot_total_emission(df):
    plt.figure(figsize=(10,6))
    plt.plot(df["Date"], df["Total CO2 (kg)"], marker="o", linestyle="-", color="green")
    plt.title("Carbon footprint over time")
    plt.xlabel("Date")
    plt.ylabel("Total CO2 (kg)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_category_wise(df):
    plt.figure(figsize=(10,6))
    plt.plot(df["Date"], df["Travel_CO2"], label="Travel", marker="o")
    plt.plot(df['Date'], df['Electricity_CO2'], label='Electricity', marker='o')
    plt.plot(df['Date'], df['Meat_CO2'], label='Meat', marker='o')
    plt.plot(df['Date'], df['Online_CO2'], label='Online Orders', marker='o')
    plt.title("Category-wise Carbon Emissions Over Time")
    plt.xlabel("Date")
    plt.ylabel("CO2 (kg)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_pie(df):
    latest=df.iloc[-1]
    labels = ['Travel', 'Electricity', 'Meat', 'Online Orders']
    values = [latest['Travel_CO2'], latest['Electricity_CO2'], latest['Meat_CO2'], latest['Online_CO2']]

    plt.figure(figsize=(6, 6))
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=["skyblue", "lightgreen", "salmon", "orange"])
    plt.title("Latest Carbon Footprint Breakdown")
    plt.tight_layout()
    plt.show()
    
#Bar graph
def plot_bar_comparison(df):
    latest= df.iloc[-1]
    emissions = {"Travel":latest["Travel_CO2"],
           "Electricity":latest["Electricity_CO2"],
           "Meat":latest["Meat_CO2"],
           "Online Orders":latest["Online_CO2"]}
    
    plt.figure(figsize=(8,5))
    plt.bar(emissions.keys(), emissions.values(), color=['skyblue', 'lightgreen', 'salmon', 'orange'])
    plt.title("Carbon Emission Breakdown (Latest Entry)")
    plt.ylabel("CO2 (kg)")
    plt.xlabel("Activity")
    plt.tight_layout()
    plt.show()

df = load_data()
plot_total_emission(df)
plot_category_wise(df)
plot_pie(df)
plot_bar_comparison(df)


#insights on these data
#monthly Average Carbon Footprint
def plot_monthly_average(df):
    df["Month"]= df["Date"].dt.to_period("M")
    monthly_avg=df.groupby("Month")["Total CO2 (kg)"].mean()
    plt.figure(figsize=(10,6))
    monthly_avg.plot(kind="bar", color="teal")
    plt.title("Average Monthly Carbon Footprint")
    plt.ylabel("Average CO₂ (kg)")
    plt.xlabel("Month")
    plt.xticks(rotation=0)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

def plot_CO2_change(df):
    df["Date"]=pd.to_datetime(df["Date"])
    df= df.sort_values("Date")
    df["CO2 change"]= df["Total CO2 (kg)"].diff()
    plt.figure(figsize=(10,6))
    colors=df["CO2 change"].apply(lambda x: "green" if x<0 else "red")
    plt.bar(df["Date"], df["CO2 change"], color=colors)
    plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
    plt.title("Daily Change in Carbon Footprint")
    plt.xlabel("Date")
    plt.ylabel("CO2 change (kg)")
    plt.grid(axis="y")
    plt.tight_layout()
    plt.show()
    
plot_monthly_average(df)
plot_CO2_change(df)
