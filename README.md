# 🎓 Academic Performance Analytics System

An interactive Streamlit dashboard for monitoring student academic performance, teacher effectiveness, attendance trends, and risk detection.

This project demonstrates end-to-end dashboard development including data generation, KPI design, visualization, and risk classification logic.

---

# 📌 Project Overview

The Academic Performance Analytics System helps analyze:

- 📊 Student Performance
- 👩‍🏫 Teacher Effectiveness
- 📈 Monthly Academic Trends
- ⚠ High-Risk Student Identification
- 📉 Attrition Monitoring
- 🕒 Late Submission Analysis

The application includes authentication, interactive filtering, and dynamic visualizations.

---

# 🛠 Tech Stack

- Python
- Streamlit
- Pandas
- NumPy
- Plotly

---

# 📁 Project Structure

Academic_Performance_Analytics/

│── Dashboard.py  
│── data_generator.py  
│── requirements.txt  
│── README.md  
│  
└── data/  
  ├── advanced_academic_performance_dataset.csv  

---

# 📊 Dataset Information

File: `advanced_academic_performance_dataset.csv`

This dataset simulates academic records across teachers, subjects, and sections.

## Dataset Columns

| Column Name | Description |
|-------------|------------|
| student_id | Unique student identifier |
| teacher | Assigned teacher name |
| section | Class section (A, B, C) |
| subject | Subject name |
| score | Student exam score (35–100) |
| attendance_percent | Attendance percentage (60–100) |
| late_count | Number of late submissions |
| status | Student status (Active / Dropped) |
| month | Academic month |
| performance_percent | Performance percentage |
| risk_level | Risk classification (Normal / High Risk) |

---

# ⚠ Risk Classification Logic

A student is marked as **High Risk** if:

- Performance < 50  
OR  
- Attendance < 70  
OR  
- Late Count > 3  

Otherwise → Normal

---

# 🚀 Installation & Setup

## 1️⃣ Clone Repository

git clone https://github.com/yourusername/academic-performance-analytics.git  
cd academic-performance-analytics  

---

## 2️⃣ Install Dependencies

pip install -r requirements.txt  

---

## 3️⃣ Generate Dataset (If Needed)

python data_generator.py  

---

## 4️⃣ Run Dashboard

streamlit run Dashboard.py  

---

# 🔐 Login Credentials

Username: admin  
Password: admin123  

---

# 📈 Dashboard Modules

### 1️⃣ Executive Dashboard
- Total Students
- Average Score
- Attendance %
- Attrition Rate
- Monthly Performance Trend
- Risk Distribution

### 2️⃣ Teacher Performance Analysis
- Teacher-wise KPIs
- Subject Performance Breakdown
- Detailed Student Data

### 3️⃣ Risk & Attrition Monitoring
- Late Count by Section
- Attrition by Teacher
- High-Risk Student Table

---

# 🎯 Project Purpose

This project demonstrates:

- Data Analytics
- KPI Development
- Dashboard Engineering
- Risk Modeling Logic
- Interactive Data Visualization
- Clean Project Structuring

Suitable for:

- Portfolio Projects
- Data Analyst Interviews
- Academic Demonstrations
- Educational Analytics Use Cases

---

# 🔮 Future Improvements

- Role-Based Authentication
- Database Integration (PostgreSQL/MySQL)
- Machine Learning Risk Prediction
- Cloud Deployment
- Real-Time Data Streaming

---

# 📌 Author

Rahul Thakre  
Data Analytics & Dashboard Developer  

---

# 📄 License

MIT License