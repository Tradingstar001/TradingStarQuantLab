
import streamlit as st

st.set_page_config(
    page_title="Trading Star Quant Lab",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Trading Star Quant Lab")
st.subheader("NIFTY Market Analysis")

st.info("Welcome to your trading software!")

st.warning(
    "Sample analysis only. "
    "This app does not use live market data."
)

st.header("Support & Resistance")

support = st.number_input(
    "Enter Support Level",
    min_value=0.0,
    value=24980.0
)

resistance = st.number_input(
    "Enter Resistance Level",
    min_value=0.0,
    value=25100.0
)

price = st.number_input(
    "Enter NIFTY Price",
    min_value=0.0,
    value=25120.0
)

if st.button("Analyze Market"):
    if support >= resistance:
        st.error("Support must be lower than Resistance.")
    elif price > resistance:
        st.success("Possible Breakout — wait for confirmation.")
    elif price < support:
        st.error("Possible Breakdown — wait for confirmation.")
    else:
        st.info("Price is within the Support-Resistance range.")

st.caption("Educational prototype. Not a trading recommendation.")

