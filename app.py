import streamlit as st
import pandas as pd

# ---------------- Page Configuration ----------------
st.set_page_config(
    page_title="HR Employee Attrition Analytics",
    page_icon="assets/logo.png",
    layout="wide"
)

# ---------------- Dashboard Header ----------------
col1, col2 = st.columns([1,5])

with col1:
    st.image("assets/logo.png", width=110)

with col2:
    st.title("HR Employee Attrition Analytics Dashboard")
    st.caption("End-to-End Data Analytics Project")

st.markdown("---")

# Load dataset
df = pd.read_csv("F:\HR Employee Attrition Analytics\HR_Employee_Attrition_Dashboard.xls")

# Show dataset
st.subheader("Dataset Preview")
st.dataframe(df.head())

total_emp = len(df)
employees_left = len(df[df["Attrition"] == "Yes"])
active_emp = len(df[df["Attrition"] == "No"])
attrition_rate = (employees_left / total_emp) * 100

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Employees", total_emp)
col2.metric("Employees Left", employees_left)
col3.metric("Active Employees", active_emp)
col4.metric("Attrition Rate", f"{attrition_rate:.2f}%")

# ---------------- Sidebar ----------------

st.sidebar.image("assets/logo.png", width=140)

st.sidebar.title("HR Analytics")

st.sidebar.markdown("---")

st.sidebar.header("🔍 Filters")

department = st.sidebar.multiselect(
    "Department",
    options=df["Department"].unique(),
    default=df["Department"].unique()
)

filtered_df = df[df["Department"].isin(department)]

import plotly.express as px

fig = px.bar(
    filtered_df,
    x="Department",
    color="Attrition",
    title="Department-wise Attrition"
)

st.plotly_chart(fig, use_container_width=True)

import streamlit as st

# KPI Calculations
total_emp = len(filtered_df)
employees_left = len(filtered_df[filtered_df["Attrition"] == "Yes"])
active_emp = len(filtered_df[filtered_df["Attrition"] == "No"])
attrition_rate = (employees_left / total_emp) * 100
avg_age = filtered_df["Age"].mean()
avg_salary = filtered_df["MonthlyIncome"].mean()
avg_experience = filtered_df["YearsAtCompany"].mean()

st.subheader("📊 Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Employees", total_emp)
col2.metric("Employees Left", employees_left)
col3.metric("Active Employees", active_emp)
col4.metric("Attrition Rate", f"{attrition_rate:.2f}%")

col5, col6, col7 = st.columns(3)

col5.metric("Average Age", f"{avg_age:.1f}")
col6.metric("Average Salary", f"${avg_salary:,.0f}")
col7.metric("Average Experience", f"{avg_experience:.1f} Years")

st.sidebar.header("🔍 Filters")

department = st.sidebar.multiselect(
    "Department",
    options=df["Department"].unique(),
    default=df["Department"].unique(),
    key="department_filter"
)

gender = st.sidebar.multiselect(
    "Gender",
    options=df["Gender"].unique(),
    default=df["Gender"].unique(),
    key="gender_filter"
)

jobrole = st.sidebar.multiselect(
    "Job Role",
    options=df["Job_Role"].unique(),
    default=df["Job_Role"].unique(),
    key="jobrole_filter"
)

education = st.sidebar.multiselect(
    "Education",
    options=df["Education"].unique(),
    default=df["Education"].unique(),
    key="education_filter"
)

age_group = st.sidebar.multiselect(
    "Age Group",
    options=df["Age Group"].unique(),
    default=df["Age Group"].unique(),
    key="age_group_filter"
)

import plotly.express as px

dept = filtered_df.groupby(
    ["Department", "Attrition"]
).size().reset_index(name="Count")

fig = px.bar(
    dept,
    x="Department",
    y="Count",
    color="Attrition",
    barmode="group",
    title="Department-wise Attrition"
)

st.plotly_chart(fig, use_container_width=True)

fig = px.histogram(
    filtered_df,
    x="MonthlyIncome",
    nbins=20,
    title="Salary Distribution"
)

st.plotly_chart(fig)

gender_count = filtered_df["Gender"].value_counts().reset_index()
gender_count.columns = ["Gender", "Count"]

fig = px.pie(
    gender_count,
    names="Gender",
    values="Count",
    title="Gender Distribution"
)

st.plotly_chart(fig)

fig = px.histogram(
    filtered_df,
    x="Age",
    nbins=20,
    title="Employee Age Distribution"
)

st.plotly_chart(fig)

st.subheader("📌 Business Insights")

highest_dept = (
    filtered_df[filtered_df["Attrition"] == "Yes"]["Department"]
    .value_counts()
    .idxmax()
)

highest_role = (
    filtered_df[filtered_df["Attrition"] == "Yes"]["Job_Role"]
    .value_counts()
    .idxmax()
)

st.success(f"Highest attrition department: **{highest_dept}**")
st.success(f"Highest attrition job role: **{highest_role}**")

if attrition_rate > 15:
    st.warning("Attrition rate is higher than the recommended threshold.")
else:
    st.info("Attrition rate is within the acceptable range.")


csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇ Download Filtered Dataset",
    data=csv,
    file_name="Filtered_HR_Employee_Data.csv",
    mime="text/csv"
) 

# ---------------- Footer ----------------

st.markdown("---")

st.markdown(
    """
    <div style='text-align: center; color: gray; font-size: 15px;'>

    <b>Designed & Developed By Hima Naga Karthikeya</b> | HR Employee Attrition Analytics Dashboard <br>
    Transforming HR Data into Actionable Business Insights

    Developed Python | Streamlit | Plotly | Power BI | SQL

    @ All Rights Reserved

    </div>
    """,
    unsafe_allow_html=True
)




