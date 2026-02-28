import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="Academic Performance Analytics",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# LOAD DATA FROM CSV
# --------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv(r"C:/Users/Admin/Desktop/Rahul_Thakre9422486423/academic_performance_dataset.csv")
    return df


# --------------------------------------------------
# AUTHENTICATION
# --------------------------------------------------
def authenticate():
    st.title("🔐 Academic Analytics Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "admin123":
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Invalid credentials")


# --------------------------------------------------
# SIDEBAR FILTERS
# --------------------------------------------------
def apply_filters(df):
    st.sidebar.header("Filter Panel")

    teacher_filter = st.sidebar.multiselect(
        "Teacher",
        df["teacher"].unique(),
        default=df["teacher"].unique()
    )

    section_filter = st.sidebar.multiselect(
        "Section",
        df["section"].unique(),
        default=df["section"].unique()
    )

    month_filter = st.sidebar.multiselect(
        "Month",
        df["month"].unique(),
        default=df["month"].unique()
    )

    filtered_df = df[
        (df["teacher"].isin(teacher_filter)) &
        (df["section"].isin(section_filter)) &
        (df["month"].isin(month_filter))
    ]

    return filtered_df


# --------------------------------------------------
# DASHBOARD VIEW
# --------------------------------------------------
def render_dashboard(df):
    st.title("📊 Executive Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Students", df["student_id"].nunique())
    col2.metric("Average Score", round(df["score"].mean(), 2))
    col3.metric("Avg Attendance %",
                round(df["attendance_percent"].mean(), 2))
    col4.metric("Attrition Rate",
                f"{round((df['status'] == 'Dropped').mean() * 100, 2)}%")

    st.markdown("---")

    colA, colB = st.columns(2)

    with colA:
        monthly_perf = df.groupby("month")["performance_percent"].mean().reset_index()

        fig_line = px.line(
            monthly_perf,
            x="month",
            y="performance_percent",
            markers=True,
            title="Monthly Performance Trend"
        )

        st.plotly_chart(fig_line, use_container_width=True)

    with colB:
        risk_dist = df["risk_level"].value_counts().reset_index()
        risk_dist.columns = ["Risk Level", "Count"]

        fig_pie = px.pie(
            risk_dist,
            names="Risk Level",
            values="Count",
            title="Risk Distribution"
        )

        st.plotly_chart(fig_pie, use_container_width=True)


# --------------------------------------------------
# TEACHER ANALYSIS
# --------------------------------------------------
def render_teacher_analysis(df):
    st.title("👩‍🏫 Teacher Performance Analysis")

    teacher = st.selectbox("Select Teacher", df["teacher"].unique())
    teacher_df = df[df["teacher"] == teacher]

    col1, col2 = st.columns(2)
    col1.metric("Average Score", round(teacher_df["score"].mean(), 2))
    col2.metric("Avg Attendance %",
                round(teacher_df["attendance_percent"].mean(), 2))

    subject_perf = teacher_df.groupby("subject")["performance_percent"].mean().reset_index()

    fig_bar = px.bar(
        subject_perf,
        x="subject",
        y="performance_percent",
        title="Subject-wise Performance"
    )

    st.plotly_chart(fig_bar, use_container_width=True)
    st.dataframe(teacher_df)


# --------------------------------------------------
# RISK & ATTRITION VIEW
# --------------------------------------------------
def render_risk_analysis(df):
    st.title("⚠ Risk & Attrition Monitoring")

    col1, col2 = st.columns(2)

    with col1:
        late_summary = df.groupby("section")["late_count"].sum().reset_index()

        fig_late = px.bar(
            late_summary,
            x="section",
            y="late_count",
            title="Late Count by Section"
        )

        st.plotly_chart(fig_late, use_container_width=True)

    with col2:
        attrition_summary = df.groupby("teacher")["status"] \
            .apply(lambda x: (x == "Dropped").sum()) \
            .reset_index(name="Attrition Count")

        fig_attr = px.bar(
            attrition_summary,
            x="teacher",
            y="Attrition Count",
            title="Attrition by Teacher"
        )

        st.plotly_chart(fig_attr, use_container_width=True)

    st.markdown("### High Risk Students")

    high_risk = df[df["risk_level"] == "High Risk"]

    st.dataframe(high_risk)


# --------------------------------------------------
# MAIN CONTROLLER
# --------------------------------------------------
def main():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
        authenticate()
    else:
        df = load_data()
        filtered_df = apply_filters(df)

        menu = st.sidebar.radio(
            "Navigation",
            ["Dashboard", "Teacher Analysis", "Risk & Attrition"]
        )

        if menu == "Dashboard":
            render_dashboard(filtered_df)
        elif menu == "Teacher Analysis":
            render_teacher_analysis(filtered_df)
        else:
            render_risk_analysis(filtered_df)


if __name__ == "__main__":
    main()