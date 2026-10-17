
import streamlit as st

st.set_page_config(
    page_title="Trading Star Quant Lab",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Trading Star Quant Lab")
st.subheader("NIFTY Breakout Confirmation Lab")

st.info(
    "Educational analysis tool. Enter your chart observations "
    "manually. This app does not use live market data."
)

st.divider()

# 1. Market levels
st.header("1. Market Levels")

col1, col2, col3 = st.columns(3)

with col1:
    support = st.number_input(
        "Support Level",
        min_value=0.0,
        value=24980.0,
        step=10.0
    )

with col2:
    resistance = st.number_input(
        "Resistance Level",
        min_value=0.0,
        value=25100.0,
        step=10.0
    )

with col3:
    price = st.number_input(
        "Current / Entry Price",
        min_value=0.0,
        value=25120.0,
        step=10.0
    )

st.divider()

# 2. Confirmation checklist
st.header("2. Breakout Confirmation Checklist")
st.caption(
    "Chart-ஐப் பார்த்து உண்மையான நிலைக்கு ஏற்ப check செய்யவும்."
)

candle_close = st.checkbox(
    "✅ Candle Resistance-க்கு மேலே close ஆகியுள்ளது"
)

volume_confirm = st.checkbox(
    "✅ Breakout candle-ல் volume அதிகரித்துள்ளது"
)

retest_confirm = st.checkbox(
    "✅ Retest-ல் பழைய Resistance support ஆகத் தாங்கியுள்ளது"
)

st.divider()

# 3. Risk reward calculator
st.header("3. Risk / Reward Check")

col4, col5 = st.columns(2)

with col4:
    stop_loss = st.number_input(
        "Stop-Loss Price",
        min_value=0.0,
        value=25080.0,
        step=10.0
    )

with col5:
    target = st.number_input(
        "Target Price",
        min_value=0.0,
        value=25200.0,
        step=10.0
    )

st.caption(
    "Risk/Reward கணக்கு Entry Price, Stop-Loss மற்றும் Target "
    "அடிப்படையில் செய்யப்படும். Brokerage, slippage மற்றும் "
    "Options premium மாற்றங்கள் இதில் சேர்க்கப்படவில்லை."
)

st.divider()

# 4. Analyze
if st.button("🔍 Analyze Breakout", use_container_width=True):

    if support >= resistance:
        st.error("Invalid levels: Support must be below Resistance.")

    elif price <= 0 or stop_loss <= 0 or target <= 0:
        st.error("Price, Stop-Loss and Target must be above zero.")

    elif stop_loss >= price:
        st.error(
            "For a bullish breakout calculation, Stop-Loss "
            "must be below the Entry Price."
        )

    elif target <= price:
        st.error(
            "For a bullish breakout calculation, Target "
            "must be above the Entry Price."
        )

    else:
        risk_points = price - stop_loss
        reward_points = target - price
        rr_ratio = reward_points / risk_points

        st.header("4. Analysis Result")

        # Check price and candle close
        price_above_resistance = price > resistance

        if not price_above_resistance:
            st.warning(
                "⏳ Price is not above Resistance. "
                "A bullish breakout is not confirmed by price alone."
            )

        elif not candle_close:
            st.warning(
                "⚠️ Price is above Resistance, but candle-close "
                "confirmation has not been checked."
            )

        else:
            st.success(
                "Price is above Resistance and candle-close "
                "confirmation is checked."
            )

        # Checklist progress
        checks = [
            price_above_resistance,
            candle_close,
            volume_confirm,
            retest_confirm
        ]

        completed = sum(checks)

        st.subheader("Confirmation Progress")
        st.progress(completed / len(checks))
        st.write(f"Checklist completed: {completed} / 4")

        if completed == 4:
            st.success(
                "All checklist items are marked complete. "
                "Review the chart and risk before making any decision."
            )

        elif completed >= 2:
            st.info(
                "Some confirmations are present. "
                "Wait for missing confirmations if they are part "
                "of your trading plan."
            )

        else:
            st.warning(
                "Insufficient checklist confirmation. "
                "Continue observing the chart."
            )

        # Risk reward display
        st.subheader("Risk / Reward Summary")

        r1, r2, r3 = st.columns(3)

        r1.metric("Risk", f"{risk_points:.2f} points")
        r2.metric("Potential Reward", f"{reward_points:.2f} points")
        r3.metric("Risk : Reward", f"1 : {rr_ratio:.2f}")

        if rr_ratio >= 2:
            st.success("Risk/Reward is at least 1:2.")
        else:
            st.warning(
                "Risk/Reward is below 1:2. Review your planned setup."
            )

        st.caption(
            "This is a checklist, not a buy/sell signal. "
            "A breakout can fail even when all items are checked. "
            "No profit is guaranteed."
        )

st.divider()

st.caption(
    "Trading Star Quant Lab | Educational prototype | "
    "Manual inputs only | No live data"
)
