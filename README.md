# 🌱 EcoTrack: Personal Carbon Footprint Tracker

EcoTrack is a beginner-friendly Python project that helps users calculate and track their monthly carbon footprint based on their daily habits. It also uses data visualization and machine learning to analyze and classify environmental impact. 

> 💡 Built as part of my learning journey in Python and Data Science — this is my first complete end-to-end project, from logic to ML!

---

## What It Does

 **User Input & Calculation**  
It asks the user for inputs on:
- Daily travel distance
- Monthly electricity usage
- Weekly meat consumption
- Monthly online orders  

These are used to calculate an estimated **monthly CO₂ emission (in kg)**.

 **Visual Insights**
- Monthly average carbon footprint
- Emission increases or decreases over time

 **Machine Learning**
- A Decision Tree Classifier that labels the user as:
  - **Low**
  - **Medium**
  - **High**
  carbon emitter based on their input.
  
 **Suggestions Engine**  
After classification, the program gives small actionable advice to lower emissions.

---

## What I Learned

- How to collect and store data using CSV
- How to use `pandas` and `matplotlib` for data analysis and visualization
- How to build a simple ML model using `scikit-learn`
- How to use `LabelEncoder` and `joblib` for predictions
- How to work with real-world logic and user interaction

---

## Tech Stack

- Python 3
- Pandas
- Matplotlib
- Scikit-learn
- Joblib (for model persistence)

---

## Machine Learning
- Model: DecisionTreeClassifier
- Input Features: Daily travel, monthly electricity, weekly meat meals, monthly online orders
- Target: Carbon footprint category (Low, Medium, High)
- Accuracy: ~80% on a small dataset

---

## Installations

1. Requirements (packages used)
   ```bash
   pip install -r requirements.txt

---

## How to Run It

1. Clone the repo:
   ```bash
   git clone https://github.com/4Anj/EcoTrack.git
   cd EcoTrack
2. Install the libraries
   ```bash
   pip install pandas matplotlib scikit-learn joblib
3. Run the main tracker
   ```bash
   python Eco_Track_main.py
   
---

## Future Enhancements

- Mobile/web-based interface (Flask/Streamlit)
- Export results as PDF or shareable report
- Improve ML accuracy with more data

---
