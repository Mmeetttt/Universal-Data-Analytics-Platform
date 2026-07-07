# 📊 Universal Data Analytics Platform

An AI-powered analytics platform built with **Streamlit** that enables users to upload datasets, explore data interactively, generate visualizations, create automated profiling reports, and perform natural language data analysis using local Large Language Models (LLMs).

---

## 🚀 Features

- 📁 Upload CSV datasets
- 📋 Preview and inspect data
- 🔍 Filter and explore records interactively
- 📈 Generate interactive charts
- 📊 Automated data profiling reports
- 🤖 AI-powered analytics using local LLMs
- 🖥️ Completely offline AI support
- ⚡ User-friendly Streamlit interface

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Pandas
- NumPy
- Plotly
- Matplotlib
- Scikit-learn
- YData Profiling
- Llama.cpp
- Meta Llama 3
- Mistral 7B

---

## 📂 Project Structure

```
Universal-Data-Analytics-Platform
│
├── home.py
├── requirements.txt
├── .gitignore
│
├── pages
│   ├── ai_analytics.py
│   ├── chart_builder.py
│   ├── data_preview.py
│   ├── filter_explore.py
│   └── profiling_report.py
│
├── Groceries_dataset.csv
├── retail_sales_dataset.csv
│
└── README.md
```

---

## ✨ Modules

### 📋 Data Preview

- View uploaded datasets
- Display dataset dimensions
- Check column names and data types
- Handle missing values

---

### 🔍 Filter & Explore

- Filter records by selected columns
- Explore categorical and numerical features
- Dynamic filtering interface

---

### 📈 Chart Builder

Generate interactive visualizations including:

- Bar Charts
- Line Charts
- Scatter Plots
- Histograms
- Pie Charts
- Box Plots

---

### 📊 Profiling Report

Automatically generates a comprehensive dataset profile including:

- Missing values
- Correlation matrix
- Statistical summary
- Feature distributions
- Duplicate analysis

---

### 🤖 AI Analytics

Ask questions about your uploaded dataset in natural language.

Examples:

- Which product generated the highest sales?
- Summarize this dataset.
- Identify important trends.
- Detect possible anomalies.
- Which columns are most useful?

Powered by local Large Language Models.

---

## 💻 Installation

Clone the repository

```bash
git clone https://github.com/Mmeetttt/Universal-Data-Analytics-Platform.git
```

Move into the project directory

```bash
cd Universal-Data-Analytics-Platform
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run home.py
```

---

## 📦 Dataset

The repository includes sample datasets:

- Retail Sales Dataset
- Groceries Dataset

Users can also upload their own CSV datasets for analysis.

---

## 🧠 AI Models

This project supports local GGUF models such as:

- Meta-Llama-3-8B-Instruct
- Mistral-7B-Instruct

> **Note:** Model files are not included in this repository because of their large size. Download the desired GGUF model separately and place it in the project directory before using the AI Analytics module.

---

## 📸 Screenshots

Home
<img width="2876" height="1620" alt="image" src="https://github.com/user-attachments/assets/741e57b8-c1c1-4515-8a75-75b7308b243c" />
Data Preview
<img width="2878" height="1626" alt="image" src="https://github.com/user-attachments/assets/877fd50e-682c-4765-a40a-e9803d2495f7" />
Smart Filtering 
<img width="2880" height="1628" alt="image" src="https://github.com/user-attachments/assets/cef795a9-6258-4df0-8a7c-7321ea0f753a" />
Custom Charts
<img width="2880" height="1630" alt="image" src="https://github.com/user-attachments/assets/fddf35fd-0797-42ae-9f50-624c9193e84a" />
Ai Analytics Q&A 
<img width="2876" height="1634" alt="image" src="https://github.com/user-attachments/assets/fd880b40-9f69-43f3-bf8d-7b816e4d488c" />
EDA Profiling
<img width="2880" height="1630" alt="image" src="https://github.com/user-attachments/assets/597ec206-b3aa-4b9c-a8fc-91af8d47e857" />




Example:

```
screenshots/
│
├── home.png
├── preview.png
├── charts.png
├── profiling.png
└── ai_chat.png
```

---

## 🔮 Future Improvements

- Excel file support
- Multiple dataset comparison
- SQL query generation
- Automated Machine Learning (AutoML)
- Predictive Analytics
- Dashboard export
- PDF report generation
- User authentication
- Cloud deployment
- Voice-based analytics

---

## 🤝 Contributing

Contributions, suggestions, and feature requests are welcome.

Feel free to fork this repository and submit a pull request.

---

## 👨‍💻 Author

**Meet Patel**

B.Tech Data Science

GitHub: https://github.com/Mmeetttt

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
