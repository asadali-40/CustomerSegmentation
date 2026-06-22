import streamlit as st
from predict import predict_segment

# Page Configuration

st.set_page_config(
page_title="Customer Segmentation",
page_icon="📊",
layout="centered"
)

# Custom CSS

st.markdown("""

<style>
.main {
    background-color: #f8fafc;
}

.title {
    text-align: center;
    color: #1e3a8a;
    font-size: 42px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: gray;
    margin-bottom: 30px;
}

.result-box {
    padding: 20px;
    border-radius: 15px;
    background-color: #eef2ff;
    border: 2px solid #4f46e5;
    text-align: center;
}

.metric {
    font-size: 22px;
    font-weight: bold;
    color: #1e3a8a;
}
</style>

""", unsafe_allow_html=True)

# Header

st.markdown(
"<div class='title'>📊 Customer Segmentation App</div>",
unsafe_allow_html=True
)

st.markdown(
"<div class='subtitle'>Predict customer groups using Machine Learning</div>",
unsafe_allow_html=True
)

# Input Section

st.subheader("Customer Information")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input(
        "Age",
    min_value=18,
    max_value=100,
    value=25
    )

with col2:
    income = st.number_input(
    "Annual Income (k$)",
    min_value=0,
    value=50
    )

spending = st.slider(
"Spending Score",
min_value=1,
max_value=100,
value=50
)

st.write("")

# Predict Button

if st.button("Predict Segment"):

    cluster, segment = predict_segment(
        age,
        income,
        spending
    )

    st.success(f"Cluster: {cluster}")
    st.success(f"Segment: {segment}")

# Footer

st.write("")
st.divider()

st.caption(
"Built with Streamlit, Scikit-Learn, KMeans Clustering & Python"
)