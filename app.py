import streamlit as st
def suggest_investment(salary, time_horizon, age, risk_appetite):
    investments = {
        'low': {'Bonds': 50, 'Fixed Deposits': 30, 'Real Estate': 20},
        'medium': {'Index Funds': 40, 'Mutual Funds': 40, 'Real Estate': 20},
        'high': {'Stocks': 50, 'Cryptocurrency': 30, 'Startups': 20}
    }

    allocation = investments.get(risk_appetite, {})

    monthly_investment = {}
    for investment, percentage in allocation.items():
        monthly_investment[investment] = salary * (percentage / 100)

    return allocation, monthly_investment

## Streamlit App
def run_app():
    st.title("Investment Planning Guidelines")

    st.text("This app is just giving a guidance as to how to start investing. THis is not recommending any investment. Please consult your investment advisor and do due diligence before investing ")

    # Input Fields
    salary = st.number_input("Enter your monthly salary (in $)", min_value=0)
    time_horizon = st.number_input("Enter your investment time horizon (in years)", min_value=0)
    age = st.number_input("Enter your age", min_value=0)
    risk_appetite = st.selectbox("Select your risk appetite", ['low','medium', 'high'])

    if st.button("Get Investment Suggestions"):
        allocation, monthly_investment = suggest_investment(salary,time_horizon, age, risk_appetite)
        st.write("Based on your inputs, here are some investment suggestions for you:")

        st.write("**Investment Allocation (%):**")
        for investment, percentage in allocation.items():
            st.write(f"- {investment}: {percentage}%")

        st.write("**Monthly Investment Amount ($):**")
        for investment, amount in monthly_investment.items():
            st.write(f"- {investment}: ${amount:.2f}")

## Run Streamlit App
if __name__ == "__main__":
    run_app()
