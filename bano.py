import streamlit as st

# 🔹 Class Definition
class SavingsAccount:
    def __init__(self, name, balance, email):
        self.name = name
        self.balance = balance
        self.email = email
        self.loan = 0

    def account_type(self):
        return "Savings"

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            st.warning("⚠️ Insufficient balance!")

    def apply_loan(self, amount):
        self.loan += amount

    def repay_loan(self, amount):
        if amount <= self.loan:
            self.loan -= amount
        else:
            st.warning("⚠️ You can't repay more than your loan!")

    def get_report(self):
        return (
            f"👤 Name: {self.name}\n"
            f"💰 Balance: ₹{self.balance}\n"
            f"💸 Loan: ₹{self.loan}\n"
            f"📧 Email: {self.email}"
        )

# 🔹 Streamlit App Interface

# Add custom background color and image
st.markdown("""
    <style>
        body {
            background-color: #f0f8ff;  /* Light blue background */
            color: #333;  /* Text color */
        }
        .stButton>button {
            background-color: #4CAF50;  /* Green button */
            color: white;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
    </style>
""", unsafe_allow_html=True)

# Add an image at the top
st.image("100.jpg", width=600)

st.title("🏦 Welcome to FB Bank 🏦")
st.markdown("**Your magical savings journey starts here! ✨🧚‍♀️**")

# Input for account creation
st.header("🎀 Create Your Account")
name = st.text_input("👤 Enter your name")
email = st.text_input("📧 Enter your email")
balance = st.number_input("💵 Enter initial balance", min_value=0)

if st.button("✨ Create Account"):
    account = SavingsAccount(name, balance, email)
    st.session_state['account'] = account
    st.success("🎉 Account Created Successfully!")

# Show options only if account is created
if 'account' in st.session_state:
    account = st.session_state['account']

    st.header("🔧 Account Actions")

    deposit_amt = st.number_input("💳 Deposit Amount", min_value=0)
    if st.button("💰 Deposit"):
        account.deposit(deposit_amt)
        st.success("✅ Amount Deposited!")

    withdraw_amt = st.number_input("🏧 Withdraw Amount", min_value=0)
    if st.button("💸 Withdraw"):
        account.withdraw(withdraw_amt)
        st.success("✅ Withdrawal Successful!")

    loan_amt = st.number_input("📥 Apply for Loan", min_value=0)
    if st.button("🧾 Apply Loan"):
        account.apply_loan(loan_amt)
        st.success("💖 Loan Applied Successfully!")

    repay_amt = st.number_input("💳 Repay Loan", min_value=0)
    if st.button("🧾 Repay Loan"):
        account.repay_loan(repay_amt)
        st.success("✅ Loan Repaid!")

    if st.button("📊 Get Account Report"):
        st.info(account.get_report())
