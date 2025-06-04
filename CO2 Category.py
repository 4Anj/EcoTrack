import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import joblib

#load the dataset
df= pd.read_csv("carbon_data.csv")

#The input(x) and output(y) features for the model
x=df[["Travel (km/day)", "electricity (kWh/month)", "meat meals/week", "Online orders"]]
y=df["CO2 Category"]

#encode the output into numbers(0,1,2) in order for the model to understand
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

#split the training and testing data
x_train, x_test, y_train, y_test= train_test_split(x, y_encoded, test_size=0.2, random_state=42)

#training model
model=DecisionTreeClassifier()
model.fit(x_train, y_train)

#testing
y_pred= model.predict(x_test)
accuracy=accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy*100:.2f}%")

# Save the trained model
joblib.dump(model, "carbon_footprint_classifier.pkl")

# Save the label encoder too
joblib.dump(label_encoder, "label_encoder.pkl")
