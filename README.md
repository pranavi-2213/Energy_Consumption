# ⚡ Energy Consumption Analytics Dashboard

### 📊 Real-Time Energy Data Analysis using Streamlit & Plotly

This project provides an **interactive dashboard** for analyzing **hourly energy consumption data** from the PJM Interconnection (a regional electricity transmission organization).
The goal of this phase is to explore, visualize, and analyze energy consumption patterns — **without using any machine learning**.

---

## 🚀 Features

* 📈 Real-time interactive dashboard built with **Streamlit**
* ⚙️ Simulated real-time data streaming
* 📅 Detailed time-based breakdowns:

  * Hourly, daily, monthly, and yearly trends
  * Day-of-week analysis
* 🔺 Highlights maximum and minimum consumption points with timestamps
* 📉 Zoomed-in visualization around minimum consumption
* 🌐 Clean and modern UI with dark/light charts using **Plotly**

---

## 🧠 Insights Provided

* Identify when energy usage peaks and drops
* Analyze how consumption changes over time (hourly, daily, monthly)
* Understand operational trends for power management and load balancing

---

## 🗂️ Dataset

**Source:** [PJM Hourly Energy Consumption Dataset (Kaggle)](https://www.kaggle.com/datasets/robikscube/hourly-energy-consumption)

You can use any of the 14 regional CSV files provided in the dataset.
Example used in this project: `PJM_hourly.csv`

**Columns:**

| Column   | Description                     |
| -------- | ------------------------------- |
| Datetime | Timestamp (Hourly)              |
| MW       | Energy consumption in Megawatts |

---

## 🧩 Tech Stack

| Tool               | Purpose                             |
| ------------------ | ----------------------------------- |
| **Python**         | Core programming language           |
| **Streamlit**      | Interactive web dashboard framework |
| **Pandas / NumPy** | Data manipulation & analysis        |
| **Plotly Express** | Data visualization                  |
| **Datetime**       | Date-time parsing & transformations |

---

## 🧮 Dashboard Structure

```
├── energy_consumption_analytics.py   # Main dashboard code
├── PJM_hourly.csv                    # Dataset file
└── README.md                         # Documentation
```

---

## ▶️ How to Run the Project

### 1️⃣ Install dependencies

```bash
pip install streamlit pandas numpy plotly
```

### 2️⃣ Run the app

```bash
streamlit run energy_consumption_analytics.py
```

### 3️⃣ Open in your browser

Go to `http://localhost:8501` to explore the dashboard.

---

## 📸 Sample Dashboard Views

* **Overall Energy Consumption Trend**
* **Hourly Average Consumption**
* **Monthly Trend**
* **Minimum Consumption Details**
* **Energy Usage Around Minimum Point**

---

## 👩‍💻 Author

**Pranavi Karnam**
📧 [karnampranavi23@gmail.com](mailto:karnampranavi23@gmail.com)
💼 *"Practice. Improve. Get Hired — with UdyogAI."*

---

## 🏁 License

This project is licensed under the **MIT License** — feel free to use and modify with credit.
