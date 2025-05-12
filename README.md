# Drive_To_Survive

## 📌 Project Objective
This project simulates the responsibilities of a GM F1 Strategy Analyst by analyzing Formula 1 qualifying and race performance trends using SQL and Python. The core objective is to understand how qualifying position impacts final race outcomes and how external sentiment (via Reddit) correlates with actual driver performance.

---

## 🛠 Tech Stack
- Python  
- SQL  
- AWS RDS PostgreSQL  
- Looker Studio  
- GitHub  
- Jupyter Notebook  

---

## 🧩 Project Relevance (Job Description)
This project is modeled after the **GM Motorsports Strategy Analyst** role, which involves building race strategy tools, modeling performance, and applying AI/ML techniques during live race events. The job requires strong data engineering and analysis skills using Python, SQL, and simulation logic — all core components of this project.  
🔗 [Job Description PDF](https://github.com/apasuparthy/Drive_To_Survive/blob/main/Proposal/Job_Description.pdf)

---

## 📊 Data Sources

### 1. API Source: F1 Developer API
- 🔗 [F1 API Documentation](https://f1api.dev/docs/drivers/drivers)
- Content: Driver stats, qualifying results, race outcomes, circuits  
- Use: Analyze grid-to-finish position changes, constructor performance, and circuit variability

### 2. Web Scrape Source: Reddit
- 🔗 [r/formula1](https://www.reddit.com/r/formula1/)
- Content: Fan mentions, post titles, comment sentiment
- Use: Compare online popularity to race outcomes, simulate public pressure insights

---

## 🔄 Data Pipelines

### 🔹 API ETL
![API Pipeline](/Proposal/_API_Data_Pipeline.png)

### 🔹 Web Scrape ETL
![Web Scrape Pipeline](/Proposal/_Web_Scrape_Data_Pipeline.png)

---

## 📓 Notebooks / Scripts

| Notebook/Script | Purpose |
|-----------------|---------|
| [F1API_API_Extract_Load_Raw.ipynb](https://github.com/apasuparthy/Drive_To_Survive/blob/main/Notebooks/F1API_API_Extract_Load_Raw.ipynb) | Pull and clean F1 qualifying/race data |
| [F1API_API_SQL_Analysis.ipynb](https://github.com/apasuparthy/Drive_To_Survive/blob/main/Notebooks/F1API_API_SQL_Analysis.ipynb) | SQL queries for race trends |
| [F1API_Api_Extract_Load_Raw.py](https://github.com/apasuparthy/Drive_To_Survive/blob/main/Notebooks/F1API_Api_Extract_Load_Raw.py) | Python ETL for F1 API |
| [Reddit_Web_Scrape_Extract_Load_Raw.ipynb](https://github.com/apasuparthy/Drive_To_Survive/blob/main/Notebooks/Reddit_Web_Scrape_Extract_Load_Raw.ipynb) | Extract Reddit posts/comments |
| [Reddit_Web_Scrape_Extract_Load_Raw.py](https://github.com/apasuparthy/Drive_To_Survive/blob/main/Notebooks/Reddit_Web_Scrape_Extract_Load_Raw.py) | Web scrape automation |
| [Reddit_Web_Scrape_SQL_Analysis.ipynb](https://github.com/apasuparthy/Drive_To_Survive/blob/main/Notebooks/Reddit_Web_Scrape_SQL_Analysis.ipynb) | SQL analysis: popularity vs performance |

---

## 📈 Dashboards
All insights were visualized in **Looker Studio**:
- [View Dashboard](https://lookerstudio.google.com/reporting/faf3807f-4f1b-4e61-9557-39382feabd72)

---

## 💡 Future Improvements
- Integrate historical weather data to enhance predictive accuracy  
- Add live-streaming social sentiment tracking during races
