import streamlit as st

def render(data):
	st.header("Personal Diagnosis")
	st.write("Please enter the relevant information")

	st.write("#### Objective ")
	one, two, three, four = st.columns(4)
	gender = one.radio("Gender",('Male','Female'))
	age = two.slider("Age",5,100,20,1)
	height = three.slider("Height in cm",100,300,160,1)
	weight = four.slider("Weight in kg",20.0,150.0,50.0,0.1)

	st.write("#### Subjective")
	one2, two2, three2 = st.columns(3)
	smoke = one2.radio("Do you smoke?", ('Yes','No'))
	alcohol = two2.radio("Do you drink frequently?", ('Yes','No'))
	active = three2.radio("Do you exercise frequently?", ('Yes','No'))

	st.write("#### Examinable")
	if st.radio("Do you have a recent health check?", ('Yes','No'), index = 1) == 'Yes':
		one3, two3, three3 = st.columns(3)
		systolic = one3.slider("Heart Blood Pressure (Systole)",50,200,100,1)
		diastolic = one3.slider("Arteries Blood Pressure (Diastole)",50,200,100,1)
		glucose = two3.radio("Glucose Level", ("Normal","Above normal","Well above normal"))
		cholesterol = three3.radio("Cholesterol Level", ("Normal","Above normal","Well above normal"))
	else:
		pass
	
	st.subheader("Calculated Risks")
	st.write("... Blank ...")