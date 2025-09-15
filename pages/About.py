import streamlit as st

# Title with name
st.title("Elina Nordlund")

# summary in Markdowns
st.markdown("""
### About this project


During the DSHI course I built a small maternal health risk prediction model. The work had two phases: exploratory data analysis (EDA) and a simple classification model. In EDA, I loaded and cleaned the dataset, fixed datatypes, renamed features, and inspected distributions for age, blood pressure, and blood sugar. Among the visualizations was a line chart of average maternal health risk factors per age. 
In the modeling phase of the project, I prepared features, split the data, and compared logistic regression, decision trees, k-NN, and Random Forest. Random Forest performed best on recall and balanced performance across classes. This Streamlit dashboard recreates the “Risk Factors by Age” figure with synthetic data and provides a clear, minimal interface to communicate the project.
This Streamlit dashboard recreates the “Risk Factors by Age” figure with synthetic data and provides a clear, minimal interface to communicate the project.


""")
