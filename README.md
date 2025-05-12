# Drive_To_Survive

## Project Objective
This project simulates the responsibilities of a GM F1 Strategy Analyst by analyzing Formula 1 qualifying and race performance trends using SQL and Python. The core objective is to understand how qualifying position impacts final race outcomes and how external sentiment (via Reddit) correlates with actual driver performance.

---

## Tech Stack
- Python  
- SQL  
- AWS RDS PostgreSQL  
- Looker Studio  
- GitHub  
- Jupyter Notebook  

---

## Project Relevance (Job Description)
This project is modeled after the GM Motorsports Strategy Analyst role, which focuses on supporting race-day decision-making through advanced modeling, data pipelines, and real-time insight delivery. The job calls for analysts who can simulate strategic scenarios, interpret driver behavior, track tire degradation, and integrate multiple data streams into actionable race insights.

In this project, I replicated that exact workflow. I extracted and modeled qualifying vs race performance using the F1 API, built SQL queries to understand position gains and losses, and layered in fan sentiment from Reddit to simulate unstructured external influences (similar to how GM teams consider media impact or broadcast pressure). I developed full ETL pipelines in Python, stored and analyzed data in PostgreSQL, and visualized findings in Looker Studio to mirror the end-to-end tools a strategy team would rely on. This project demonstrates not only the technical skillset required by the GM role, but also the race-specific thinking and data-driven storytelling that powers motorsport strategy today.
[Job Description PDF](https://github.com/apasuparthy/Drive_To_Survive/blob/main/Proposal/Job_Description.pdf)

---

## Data Sources

### 1. API Source: F1 Developer API
- [F1 API Documentation](https://f1api.dev/docs/drivers/drivers)
- Content: Driver stats, qualifying results, race outcomes, circuits  
- Use: Analyze grid-to-finish position changes, constructor performance, and circuit variability

### 2. Web Scrape Source: Reddit
- [r/formula1](https://www.reddit.com/r/formula1/)
- Content: Fan mentions, post titles, comment sentiment
- Use: Compare online popularity to race outcomes, simulate public pressure insights

---

## Data Pipelines

### ✨ Data Pipelines

#### 🚀 API ETL
F1 race data (qualifying/results) was pulled from the [Ergast F1 API](https://f1api.dev), using a Python script to fetch, normalize, and load it into PostgreSQL tables. This enabled clean, structured querying of driver performance over time.

**Pipeline:**
```
F1 API JSON → api_extract_load_raw.py → PostgreSQL Tables (qualifying_results_2022, race_results_2023, etc.)
```

**Diagram:** [API Pipeline](/Proposal/_API_Data_Pipeline.png)

---

#### 🖥️ Web Scrape ETL
Reddit comments from r/formula1 were scraped using a JSON endpoint and a Python ETL script. After cleaning and matching mentions to driver names, the data was loaded into PostgreSQL for sentiment and volume analysis.

**Pipeline:**
```
r/formula1 JSON → web_scrape_extract_load_raw.py → PostgreSQL Table (web_scrape_formula1)
```

**Diagram:** [Web Scrape Pipeline](/Proposal/_Web_Scrape_Data_Pipeline.png)

---

## Notebooks / Scripts

| Notebook/Script | Purpose |
|-----------------|---------|
| [F1API_API_Extract_Load_Raw.ipynb](https://github.com/apasuparthy/Drive_To_Survive/blob/main/Notebooks/F1API_API_Extract_Load_Raw.ipynb) | Pull and clean F1 qualifying/race data |
| [F1API_API_SQL_Analysis.ipynb](https://github.com/apasuparthy/Drive_To_Survive/blob/main/Notebooks/F1API_API_SQL_Analysis.ipynb) | SQL queries for race trends |
| [F1API_Api_Extract_Load_Raw.py](https://github.com/apasuparthy/Drive_To_Survive/blob/main/Notebooks/F1API_Api_Extract_Load_Raw.py) | Python ETL for F1 API |
| [Reddit_Web_Scrape_Extract_Load_Raw.ipynb](https://github.com/apasuparthy/Drive_To_Survive/blob/main/Notebooks/Reddit_Web_Scrape_Extract_Load_Raw.ipynb) | Extract Reddit posts/comments |
| [Reddit_Web_Scrape_Extract_Load_Raw.py](https://github.com/apasuparthy/Drive_To_Survive/blob/main/Notebooks/Reddit_Web_Scrape_Extract_Load_Raw.py) | Web scrape automation |
| [Reddit_Web_Scrape_SQL_Analysis.ipynb](https://github.com/apasuparthy/Drive_To_Survive/blob/main/Notebooks/Reddit_Web_Scrape_SQL_Analysis.ipynb) | SQL analysis: popularity vs performance |

---

## Dashboards
All insights were visualized in **Looker Studio**:
- [View Dashboard](https://lookerstudio.google.com/reporting/faf3807f-4f1b-4e61-9557-39382feabd72)

---

## 💡 Future Improvements
- Integrate historical weather data to enhance predictive accuracy  
- Add live-streaming social sentiment tracking during races
