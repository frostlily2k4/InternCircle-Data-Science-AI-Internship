
import streamlit as st
import pandas as pd
import joblib

# Page configuration
st.set_page_config(
    page_title="Titanic Survival Predictor",
    page_icon="🚢",
    layout="centered"
)

# Load the trained model
@st.cache_resource
def load_model():
    return joblib.load("model.joblib")

try:
    model = load_model()
except FileNotFoundError:
    st.error("Model file not found. Please keep model.joblib in the same folder as app.py.")
    st.stop()
except Exception as e:
    st.error(f"Unable to load the model: {e}")
    st.stop()

# App title
st.title("🚢 Titanic Survival Predictor")
st.write(
    "Enter passenger details below to predict whether "
    "the passenger would have survived the Titanic disaster."
)

st.caption(
    "This application uses a Decision Tree model trained on the Titanic dataset. "
    "Its test accuracy was approximately 77.65%."
)

st.divider()

# User inputs
st.subheader("Passenger Details")

pclass = st.selectbox(
    "Passenger Class",
    options=[1, 2, 3],
    format_func=lambda x: {
        1: "1st Class",
        2: "2nd Class",
        3: "3rd Class"
    }[x]
)

sex = st.radio(
    "Gender",
    options=["Male", "Female"],
    horizontal=True
)

age = st.slider(
    "Age",
    min_value=0,
    max_value=80,
    value=30
)

fare = st.number_input(
    "Ticket Fare",
    min_value=0.0,
    max_value=600.0,
    value=32.2,
    step=1.0
)

# Prediction
if st.button("Predict Survival", type="primary", use_container_width=True):

    try:
        sex_value = 0 if sex == "Male" else 1

        input_data = pd.DataFrame(
            [[pclass, sex_value, age, fare]],
            columns=["pclass", "sex", "age", "fare"]
        )

        prediction = model.predict(input_data)[0]
        probabilities = model.predict_proba(input_data)[0]

        classes = list(model.classes_)
        survival_probability = probabilities[classes.index(1)]

        st.divider()
        st.subheader("Prediction Result")

        if prediction == 1:
            st.success("🎉 The model predicts that the passenger would have survived!")
        else:
            st.error("The model predicts that the passenger would not have survived.")

        st.metric(
            "Estimated Survival Probability",
            f"{survival_probability * 100:.2f}%"
        )

        st.progress(float(survival_probability))

        st.caption(
            "This is a machine learning prediction, not a guarantee "
            "of what would have happened."
        )

    except Exception as e:
        st.error(f"Prediction failed: {e}")
