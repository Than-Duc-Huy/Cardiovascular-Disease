import streamlit as st
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier

tree = DecisionTreeClassifier(max_depth = 5)

st.header("EE0005 DSAI Group 8")
st.header("Cardiovascular disease risk diagnosis")

@st.cache
def loaddata():
	data = pd.read_csv('databmi.csv')
	return data

data = loaddata()

st.write("Please enter the relevant information")



st.write("#### Objective ")
one, two, three, four = st.columns(4)
gender = one.radio("Gender",('Male','Female'))
gender = 2 if gender == 'Male'else 1

one.write(gender)

age = two.slider("Age",5,100,20,1)
height = three.slider("Height in cm",100,300,160,1)
weight = four.slider("Weight in kg",20.0,150.0,50.0,0.1)

st.write("#### Subjective")
one2, two2, three2 = st.columns(3)
smoke = one2.radio("Do you smoke?", ('Yes','No'))
smoke = 1 if smoke == 'Yes' else 0
one2.write(smoke)

alcohol = two2.radio("Do you drink frequently?", ('Yes','No'))
alcohol = 1 if alcohol == 'Yes' else 0
two2.write(alcohol)

active = three2.radio("Do you exercise frequently?", ('Yes','No'))
active = 1 if active == 'Yes' else 0
three2.write(active)

st.write("#### Examinable")
exam = st.radio("Do you have a recent health check?", ('Yes','No'), index = 1)
if  exam == 'Yes':
	one3, two3, three3 = st.columns(3)
	systolic = one3.slider("Systolic Blood Pressure",40,200,120,1)
	diastolic = one3.slider("Diastolic Blood Pressure",40,200,80,1)
	if systolic < diastolic:
		st.warning("Systolic blood pressure has to be higher than Diastolic blood pressure")


	glucose = two3.radio("Glucose Level", ("Normal","Above normal","Well above normal"))
	glucose = 1 if glucose == "Normal" else (2 if glucose == "Above normal" else 3)
	two3.write(glucose)

	cholesterol = three3.radio("Cholesterol Level", ("Normal","Above normal","Well above normal"))
	cholesterol = 1 if cholesterol == "Normal" else (2 if cholesterol == "Above normal" else 3)
	three3.write(cholesterol)
else:
	systolic = 0
	diastolic = 0
	glucose = 1
	cholesterol = 1



st.subheader("Calculated Risks")
BMI = weight/(height/100)**2
if BMI < 18.5:
	obesity = "Underweight"
elif BMI < 25:
	obesity = "Healthy"
elif BMI < 30:
	obesity = "Overweight"
else:
	obesity = "Obese"
st.write("According to your BMI of ",round(BMI,1), ", you are ", obesity)
obesity = 0 if obesity == "Underweight" else (1 if obesity == "Healthy" else(2 if obesity =="Overweight" else 3))

person = pd.DataFrame({"age": [age],"gender": [gender],"height": [height],"weight": [weight],"ap_hi": [systolic],"ap_lo": [diastolic],"cholesterol": [cholesterol],"gluc": [glucose],"smoke": [smoke],"alco": [alcohol],"active": [active],"BMI": [BMI],"Obesity": [obesity]})



st.write("Your profile")
if exam == 'Yes':
	st.table(person)
	data_X = data.drop(columns = "cardio")

else :
	exam_var = ["ap_hi","ap_lo","cholesterol","gluc"]
	data = data.drop(columns = exam_var)
	person = person.drop(columns = exam_var)
	st.table(person)	

data_X = data.drop(columns = "cardio")
data_Y = data["cardio"]
tree.fit(data_X,data_Y)

cardio = tree.predict(person)
score = round(tree.score(data_X,data_Y),2)

st.write("Using Decision Tree Classifier with max depth of 5, the with training accuracy ",score)
if cardio == 0:
	st.write("You are **NOT** at risk of having cardiovascular disease")
else:
	st.write("You are **AT RISK** of having cardiovascular disease")

if exam == "No":
	st.warning("Consider providing Examinable information for better prediction!")	



