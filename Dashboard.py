import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Page configuration
st.set_page_config(
    page_title="Maternal Health Dashboard",
    page_icon="🤰",
    layout='wide'
)
st.title("Maternal Health - Risk Factors by Age")

st.write("# Line chart of Maternal Risk Factors by Age")

# Widgets for user input
st.sidebar.header("Filters (example)")

N = st.sidebar.slider("Number of data points", min_value=50, max_value=2000, value=300, step=50)

age_range = st.sidebar.slider("Age Range", min_value=18, max_value=45, value=(18, 45), step=1)

show_diabetes_only = st.sidebar.checkbox("Show Diabetes Risk Factor Only", value=False)

# Generate synthetic data
ages = np.random.randint(18, 46, size=10)  

rng = np.random.default_rng(42)
ages = rng.integers(18, 46, size=N)
blood_sugar = rng.normal(5.3, 0.8, size=N)
risk_factors = rng.integers(0, 6, size=N)
diabetes = (blood_sugar > 6.5).astype(int)
df = pd.DataFrame({"Age": ages, "Risk Factors": risk_factors})


df = pd.DataFrame({
    "Age": ages,
    "BloodSugar": blood_sugar.round(2),
    "Diabetes": diabetes,
    "RiskFactors": risk_factors
})

# Apply filters
mask = (df["Age"] >= age_range[0]) & (df["Age"] <= age_range[1])
df_filt = df[mask].copy()
if show_diabetes_only:
    mask &= df["Diabetes"] == 1
df_filt = df[mask].copy()

# Create line chart

left, right = st.columns((1, 2), gap="large")

with left:
    st.markdown("### Generated Data Sample")
    st.dataframe(df_filt.head(10), use_container_width=True)

with right:
    st.markdown("### Average Risk Factors by Age")
    if len(df_filt) == 0:
        st.info("No data to display for the selected filters.")
    else:
        grouped = df_filt.groupby("Age", as_index=False)["RiskFactors"].mean()

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(grouped["Age"], grouped["RiskFactors"], marker='o')
        ax.set_xlabel("Age")
        ax.set_ylabel("Average Risk Factors")
        ax.set_title("Average Maternal Risk Factors by Age")
        ax.grid(True)

        st.pyplot(fig)