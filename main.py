import streamlit as st
import numpy as np
import pandas as pd
import joblib


###############################
# CONFIGURATION
###############################


# Functions
def get_model():
    return joblib.load("model/calib_model.pkl")


def get_scaler():
    return joblib.load("model/scaler.joblib")


def get_imputer():
    return joblib.load("model/imputer.joblib")


# Layout
st.set_page_config(
    layout="wide",
    page_title="Delinquency Prediction",
    page_icon="https://www.ing.com.tr/documents/IngBank/assets/icons/favicon.png",
)


# Banner
custom_html = """
<div class="banner">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/ING_Group_N.V._Logo.svg/1200px-ING_Group_N.V._Logo.svg.png" alt="Banner Image">
</div>
<style>
    .banner {

        height: 300px;
        overflow: hidden;
        text-align: center;
        
    }
    .banner img {
        width: 45%;
        height: 45%;
        object-fit: contain;
        margin-left: 50px;
    }
</style>
"""

st.components.v1.html(custom_html)

# Header
st.header(":orange[Loan] Delinquency Prediction")


# Back to Top Button
scroll_to_top = """
    <script>
        function scrollToTop() {
            window.scrollTo({top: 0, behavior: 'smooth'});
        }
    </script>
"""

st.markdown(
    """<a href="#loan-delinquency-prediction" style="text-decoration:none;">
                <button style="position:fixed;bottom:60px;right:10px;padding:10px 20px;font-size:16px;">
                    Back to Top
                </button>
               </a>""",
    unsafe_allow_html=True,
)


###############################
# MODEL PREDICTION
###############################


scaler = get_scaler()
imputer = get_imputer()
model = get_model()

st.markdown(
    """
    <div class="justified-text">
    In this section, you can view the model's prediction results by entering the appropriate values in the fields below.
    <br><br>
    </div>
    """,
    unsafe_allow_html=True,
)
left_part4, right_part4 = st.columns(2)

requested_amount = left_part4.number_input(
    "Please enter the requested_amount variable:",
    min_value=2000,
    max_value=50000,
    step=1000,
    value=13000,
)


loan_term = left_part4.number_input(
    "Please enter the loan_term variable:",
    min_value=24,
    max_value=72,
    step=12,
    value=48,
)


installment = left_part4.number_input(
    "Please enter the installment variable:",
    min_value=60,
    max_value=2000,
    step=10,
    value=400,
)


number_loans_accounts = left_part4.number_input(
    "Please enter the number_loans_accounts variable:",
    min_value=0,
    max_value=3,
    step=1,
    value=0,
)


number_accounts = left_part4.number_input(
    "Please enter the number_accounts variable:",
    min_value=1,
    max_value=4,
    step=1,
    value=1,
)

# salary
salary = left_part4.text_input(
    "Please enter the salary variable (enter a number or type 'NaN' if unknown):",
    value="1800",
)

if salary.lower() == "nan":
    salary = np.nan
else:
    try:
        salary = float(salary)
        if salary < 256:
            salary = 256
        elif salary > 4292:
            salary = 4292
    except ValueError:
        left_part4.error("Invalid input. Please enter a number or 'NaN'.")
        salary = None


# current_acc_balance
current_acc_balance = left_part4.text_input(
    "Please enter the current_acc_balance variable (enter a number or type 'NaN' if unknown):",
    value="1100",
)

if current_acc_balance.lower() == "nan":
    current_acc_balance = np.nan
else:
    try:
        current_acc_balance = float(current_acc_balance)
        if current_acc_balance < -8370:
            current_acc_balance = -8370
        elif current_acc_balance > 11732:
            current_acc_balance = 11732
    except ValueError:
        left_part4.error("Invalid input. Please enter a number or 'NaN'.")
        current_acc_balance = None


# saving_acc_balance
saving_acc_balance = left_part4.text_input(
    "Please enter the saving_acc_balance variable (enter a number or type 'NaN' if unknown):",
    value="1300",
)

if saving_acc_balance.lower() == "nan":
    saving_acc_balance = np.nan
else:
    try:
        saving_acc_balance = float(saving_acc_balance)
        if current_acc_balance < 0:
            current_acc_balance = 0
        elif current_acc_balance > 14106:
            current_acc_balance = 14106
    except ValueError:
        left_part4.error("Invalid input. Please enter a number or 'NaN'.")
        saving_acc_balance = None


# credit_card_balance
credit_card_balance = left_part4.text_input(
    "Please enter the credit_card_balance variable (enter a number or type 'NaN' if unknown):",
    value="1500",
)

if credit_card_balance.lower() == "nan":
    credit_card_balance = np.nan
else:
    try:
        credit_card_balance = float(credit_card_balance)
        if credit_card_balance < -50:
            credit_card_balance = -50
        elif credit_card_balance > 11445:
            credit_card_balance = 11445
    except ValueError:
        left_part4.error("Invalid input. Please enter a number or 'NaN'.")
        credit_card_balance = None


# saving_acc_balance_mean
saving_acc_balance_mean = left_part4.text_input(
    "Please enter the saving_acc_balance_mean variable (enter a number or type 'NaN' if unknown):",
    value="1250",
)

if saving_acc_balance_mean.lower() == "nan":
    saving_acc_balance_mean = np.nan
else:
    try:
        saving_acc_balance_mean = float(saving_acc_balance_mean)
        if saving_acc_balance_mean < 0:
            saving_acc_balance_mean = 0
        elif saving_acc_balance_mean > 11220:
            saving_acc_balance_mean = 11220
    except ValueError:
        left_part4.error("Invalid input. Please enter a number or 'NaN'.")
        saving_acc_balance_mean = None


# credit_card_balance_mean
credit_card_balance_mean = left_part4.text_input(
    "Please enter the credit_card_balance_mean variable (enter a number or type 'NaN' if unknown):",
    value="1400",
)

if credit_card_balance_mean.lower() == "nan":
    credit_card_balance_mean = np.nan
else:
    try:
        credit_card_balance_mean = float(credit_card_balance_mean)
        if credit_card_balance_mean < -41:
            credit_card_balance_mean = -41
        elif credit_card_balance_mean > 9368:
            credit_card_balance_mean = 9368
    except ValueError:
        left_part4.error("Invalid input. Please enter a number or 'NaN'.")
        credit_card_balance_mean = None


# salary_min
salary_min = left_part4.text_input(
    "Please enter the salary_min variable (enter a number or type 'NaN' if unknown):",
    value="1700",
)

if salary_min.lower() == "nan":
    salary_min = np.nan
else:
    try:
        salary_min = float(salary_min)
        if salary_min < 112:
            salary_min = 112
        elif salary_min > 3250:
            salary_min = 3250
    except ValueError:
        left_part4.error("Invalid input. Please enter a number or 'NaN'.")
        salary_min = None


# current_acc_balance_min
current_acc_balance_min = left_part4.text_input(
    "Please enter the current_acc_balance_min variable (enter a number or type 'NaN' if unknown):",
    value="745",
)

if current_acc_balance_min.lower() == "nan":
    current_acc_balance_min = np.nan
else:
    try:
        current_acc_balance_min = float(current_acc_balance_min)
        if current_acc_balance_min < -7221:
            current_acc_balance_min = -7221
        elif current_acc_balance_min > 8678:
            current_acc_balance_min = 8678
    except ValueError:
        left_part4.error("Invalid input. Please enter a number or 'NaN'.")
        current_acc_balance_min = None


# saving_acc_balance_min
saving_acc_balance_min = left_part4.text_input(
    "Please enter the saving_acc_balance_min variable (enter a number or type 'NaN' if unknown):",
    value="950",
)

if saving_acc_balance_min.lower() == "nan":
    saving_acc_balance_min = np.nan
else:
    try:
        saving_acc_balance_min = float(saving_acc_balance_min)
        if saving_acc_balance_min < 0:
            saving_acc_balance_min = 0
        elif saving_acc_balance_min > 8462:
            saving_acc_balance_min = 8462
    except ValueError:
        left_part4.error("Invalid input. Please enter a number or 'NaN'.")
        saving_acc_balance_min = None


# credit_card_balance_min
credit_card_balance_min = left_part4.text_input(
    "Please enter the credit_card_balance_min variable (enter a number or type 'NaN' if unknown):",
    value="1100",
)

if credit_card_balance_min.lower() == "nan":
    credit_card_balance_min = np.nan
else:
    try:
        credit_card_balance_min = float(credit_card_balance_min)
        if credit_card_balance_min < -50:
            credit_card_balance_min = -50
        elif credit_card_balance_min > 7604:
            credit_card_balance_min = 7604
    except ValueError:
        left_part4.error("Invalid input. Please enter a number or 'NaN'.")
        credit_card_balance_min = None


# tenure
tenure = left_part4.number_input(
    "Please enter the tenure variable:", min_value=6, max_value=49, step=1, value=27
)


# salary_max
salary_max = right_part4.text_input(
    "Please enter the salary_max variable (enter a number or type 'NaN' if unknown):",
    value="2580",
)

if salary_max.lower() == "nan":
    salary_max = np.nan
else:
    try:
        salary_max = float(salary_max)
        if salary_max < 305:
            salary_max = 305
        elif salary_max > 12530:
            salary_max = 12530
    except ValueError:
        right_part4.error("Invalid input. Please enter a number or 'NaN'.")
        salary_max = None


# current_acc_balance_max
current_acc_balance_max = right_part4.text_input(
    "Please enter the current_acc_balance_max variable (enter a number or type 'NaN' if unknown):",
    value="1450",
)

if current_acc_balance_max.lower() == "nan":
    current_acc_balance_max = np.nan
else:
    try:
        current_acc_balance_max = float(current_acc_balance_max)
        if current_acc_balance_max < -6896:
            current_acc_balance_max = -6896
        elif current_acc_balance_max > 11000:
            current_acc_balance_max = 11000
    except ValueError:
        right_part4.error("Invalid input. Please enter a number or 'NaN'.")
        current_acc_balance_max = None


# saving_acc_balance_max
saving_acc_balance_max = right_part4.text_input(
    "Please enter the saving_acc_balance_max variable (enter a number or type 'NaN' if unknown):",
    value="1500",
)

if saving_acc_balance_max.lower() == "nan":
    saving_acc_balance_max = np.nan
else:
    try:
        saving_acc_balance_max = float(saving_acc_balance_max)
        if saving_acc_balance_max < 0:
            saving_acc_balance_max = 0
        elif saving_acc_balance_max > 14116:
            saving_acc_balance_max = 14116
    except ValueError:
        right_part4.error("Invalid input. Please enter a number or 'NaN'.")
        saving_acc_balance_max = None


# credit_card_balance_max
credit_card_balance_max = right_part4.text_input(
    "Please enter the credit_card_balance_max variable (enter a number or type 'NaN' if unknown):",
    value="1800",
)

if credit_card_balance_max.lower() == "nan":
    credit_card_balance_max = np.nan
else:
    try:
        credit_card_balance_max = float(credit_card_balance_max)
        if credit_card_balance_max < -41:
            credit_card_balance_max = -41
        elif credit_card_balance_max > 11487:
            credit_card_balance_max = 11487
    except ValueError:
        right_part4.error("Invalid input. Please enter a number or 'NaN'.")
        credit_card_balance_max = None


# salary_std
salary_std = right_part4.text_input(
    "Please enter the salary_std variable (enter a number or type 'NaN' if unknown):",
    value="1800",
)

if salary_std.lower() == "nan":
    salary_std = np.nan
else:
    try:
        salary_std = float(salary_std)
        if salary_std < 0:
            salary_std = 0
        elif salary_std > 3944:
            salary_std = 3944
    except ValueError:
        right_part4.error("Invalid input. Please enter a number or 'NaN'.")
        salary_std = None


# current_acc_balance_std
current_acc_balance_std = right_part4.text_input(
    "Please enter the current_acc_balance_std variable (enter a number or type 'NaN' if unknown):",
    value="200",
)

if current_acc_balance_std.lower() == "nan":
    current_acc_balance_std = np.nan
else:
    try:
        current_acc_balance_std = float(current_acc_balance_std)
        if current_acc_balance_std < 0:
            current_acc_balance_std = 0
        elif current_acc_balance_std > 1820:
            current_acc_balance_std = 1820
    except ValueError:
        right_part4.error("Invalid input. Please enter a number or 'NaN'.")
        current_acc_balance_std = None


# saving_acc_balance_std
saving_acc_balance_std = right_part4.text_input(
    "Please enter the saving_acc_balance_std variable (enter a number or type 'NaN' if unknown):",
    value="150",
)

if saving_acc_balance_std.lower() == "nan":
    saving_acc_balance_std = np.nan
else:
    try:
        saving_acc_balance_std = float(saving_acc_balance_std)
        if saving_acc_balance_std < 0:
            saving_acc_balance_std = 0
        elif saving_acc_balance_std > 1962:
            saving_acc_balance_std = 1962
    except ValueError:
        right_part4.error("Invalid input. Please enter a number or 'NaN'.")
        saving_acc_balance_std = None


# credit_card_balance_std
credit_card_balance_std = right_part4.text_input(
    "Please enter the credit_card_balance_std variable (enter a number or type 'NaN' if unknown):",
    value="220",
)

if credit_card_balance_std.lower() == "nan":
    credit_card_balance_std = np.nan
else:
    try:
        credit_card_balance_std = float(credit_card_balance_std)
        if credit_card_balance_std < 0:
            credit_card_balance_std = 0
        elif credit_card_balance_std > 1648:
            credit_card_balance_std = 1648
    except ValueError:
        right_part4.error("Invalid input. Please enter a number or 'NaN'.")
        credit_card_balance_std = None


# salary_median
salary_median = right_part4.text_input(
    "Please enter the salary_median variable (enter a number or type 'NaN' if unknown):",
    value="1800",
)

if salary_median.lower() == "nan":
    salary_median = np.nan
else:
    try:
        salary_median = float(salary_median)
        if salary_median < 213:
            salary_median = 213
        elif salary_median > 3916:
            salary_median = 3916
    except ValueError:
        right_part4.error("Invalid input. Please enter a number or 'NaN'.")
        salary_median = None


# current_acc_balance_median
current_acc_balance_median = right_part4.text_input(
    "Please enter the current_acc_balance_median variable (enter a number or type 'NaN' if unknown):",
    value="1100",
)

if current_acc_balance_median.lower() == "nan":
    current_acc_balance_median = np.nan
else:
    try:
        current_acc_balance_median = float(current_acc_balance_median)
        if current_acc_balance_median < -6904:
            current_acc_balance_median = -6904
        elif current_acc_balance_median > 9753:
            current_acc_balance_median = 9753
    except ValueError:
        right_part4.error("Invalid input. Please enter a number or 'NaN'.")
        current_acc_balance_median = None


# credit_card_balance_median
credit_card_balance_median = right_part4.text_input(
    "Please enter the credit_card_balance_median variable (enter a number or type 'NaN' if unknown):",
    value="1100",
)

if credit_card_balance_median.lower() == "nan":
    credit_card_balance_median = np.nan
else:
    try:
        credit_card_balance_median = float(credit_card_balance_median)
        if credit_card_balance_median < -41:
            credit_card_balance_median = -41
        elif credit_card_balance_median > 9371:
            credit_card_balance_median = 9371
    except ValueError:
        right_part4.error("Invalid input. Please enter a number or 'NaN'.")
        credit_card_balance_median = None


# loan_reason
loan_reason = right_part4.selectbox(
    "Please select the loan_reason variable:",
    ["Car", "Financial", "Housing", "Personal"],
)


# employment
employment = right_part4.selectbox(
    "Please select the employment variable:",
    ["Self-employed", "Private Sector", "Unemployed", "Public Sector"],
)


# postal_code
postal_code = right_part4.selectbox(
    "Please select the postal_code variable:", [10, 20, 30, 40, 50, 60, 70, 80]
)


# gender
gender = right_part4.selectbox("Please select the gender variable:", ["F", "M"])


# religion
religion = right_part4.selectbox(
    "Please select the religion variable:", ["C", "J", "M", "O", "U"]
)


# age
age = right_part4.number_input(
    "Please enter the age variable:", min_value=18, max_value=70, step=1, value=35
)


all_features = [
    "loan_term",
    "requested_amount",
    "installment",
    "number_loans_accounts",
    "number_accounts",
    "salary",
    "current_acc_balance",
    "saving_acc_balance",
    "credit_card_balance",
    "age",
    "tenure",
    "saving_acc_balance_mean",
    "credit_card_balance_mean",
    "salary_min",
    "current_acc_balance_min",
    "saving_acc_balance_min",
    "credit_card_balance_min",
    "salary_max",
    "current_acc_balance_max",
    "saving_acc_balance_max",
    "credit_card_balance_max",
    "salary_std",
    "current_acc_balance_std",
    "saving_acc_balance_std",
    "credit_card_balance_std",
    "salary_median",
    "current_acc_balance_median",
    "credit_card_balance_median",
    "install_salary_ratio",
    "install_salary_std",
    "install_current_acc_std",
    "install_saving_acc_std",
    "install_credit_card_balance_std",
    "request_segment",
    "loan_reason_Car",
    "loan_reason_Financial",
    "loan_reason_Housing",
    "loan_reason_Personal",
    "gender_F",
    "gender_M",
    "religion_C",
    "religion_M",
    "religion_U",
    "employment_Private Sector",
    "employment_Public Sector",
    "employment_Unemployed",
    "postal_code_10",
    "postal_code_20",
    "postal_code_30",
    "postal_code_50",
]

user = pd.DataFrame([0] * len(all_features), index=all_features).T
user.loan_term = loan_term
user.requested_amount = requested_amount
user.installment = installment
user.number_loans_accounts = number_loans_accounts
user.number_accounts = number_accounts
user.salary = salary
user.current_acc_balance = current_acc_balance
user.saving_acc_balance = saving_acc_balance
user.credit_card_balance = credit_card_balance
user.age = age
user.tenure = tenure
user.saving_acc_balance_mean = saving_acc_balance_mean
user.credit_card_balance_mean = credit_card_balance_mean
user.salary_min = salary_min
user.current_acc_balance_min = current_acc_balance_min
user.saving_acc_balance_min = saving_acc_balance_min
user.credit_card_balance_min = credit_card_balance_min
user.salary_max = salary_max
user.current_acc_balance_max = current_acc_balance_max
user.saving_acc_balance_max = saving_acc_balance_max
user.credit_card_balance_max = credit_card_balance_max
user.salary_std = salary_std
user.current_acc_balance_std = current_acc_balance_std
user.saving_acc_balance_std = saving_acc_balance_std
user.credit_card_balance_std = credit_card_balance_std
user.salary_median = salary_median
user.current_acc_balance_median = current_acc_balance_median
user.credit_card_balance_median = credit_card_balance_median
user.install_salary_ratio = installment / salary
user.install_salary_std = installment / salary_std
user.install_current_acc_std = installment / current_acc_balance_std
user.install_saving_acc_std = installment / saving_acc_balance_std
user.install_credit_card_balance_std = installment / credit_card_balance_std


# request segment
if 12000 <= requested_amount < 15000:
    user.request_segment = 1
elif 15000 <= requested_amount:
    user.request_segment = 2

# loan reason
if loan_reason == "Car":
    user.loan_reason_Car = 1
elif loan_reason == "Financial":
    user.loan_reason_Financial = 1
elif loan_reason == "Housing":
    user.loan_reason_Housing = 1
elif loan_reason == "Personal":
    user.loan_reason_Personal = 1

# gender
if gender == "F":
    user.gender_F = 1
else:
    user.gender_M = 1

# religion
if religion == "C":
    user.religion_C = 1
elif religion == "M":
    user.religion_M = 1
elif religion == "U":
    user.religion_U = 1


# employment
if employment == "Private Sector":
    user["employment_Private Sector"] = 1

elif employment == "Public Sector":
    user["employment_Public Sector"] = 1

elif employment == "Unemployed":
    user.employment_Unemployed = 1


# postal code
if postal_code == 10:
    user.postal_code_10 = 1
elif postal_code == 20:
    user.postal_code_20 = 1
elif postal_code == 30:
    user.postal_code_30 = 1
elif postal_code == 50:
    user.postal_code_50 = 1

user.replace([np.inf, -np.inf], np.nan, inplace=True)
user = pd.DataFrame(scaler.transform(user), columns=user.columns)
user = pd.DataFrame(imputer.transform(user), columns=user.columns)
user = pd.DataFrame(scaler.inverse_transform(user), columns=user.columns)
user["zero_account"] = (
    (user.credit_card_balance_min <= 0)
    | (user.saving_acc_balance_min <= 0)
    | (user.current_acc_balance_min <= 0)
    | (user.salary_min <= 0)
).astype(int)


if left_part4.button("Predict!"):
    prediction = model.predict_proba(user)[:, 1]
    prediction = round(prediction[0] * 100, 2)
    st.success(f"This customer has a {prediction}% probability of payment delinquency.")
    st.balloons()
