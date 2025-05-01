# %%
import os
import requests
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# %%
# Retrieve credentials from environment variables
pg_user = os.getenv('PG_USER')
pg_password = os.getenv('PG_PASSWORD')
pg_host = os.getenv('PG_HOST')
pg_db = os.getenv('PG_DB')

# Build the connection string
conn_str = f"postgresql+psycopg2://{pg_user}:{pg_password}@{pg_host}/{pg_db}"
engine = create_engine(conn_str)

# %%
# Step 1: Pull Qualifying Results from F1 API (2022)
url = "https://ergast.com/api/f1/2022/qualifying.json?limit=1000"
response = requests.get(url)
data = response.json()
# %%
# Step 2: Navigate to Race results
races = data['MRData']['RaceTable']['Races']

# %%
# Step 3: Normalize the qualifying results
qualifying_data_2022 = []
for race in races:
    for result in race['QualifyingResults']:
        qualifying_data_2022.append({
            'season': race['season'],
            'round': race['round'],
            'race_name': race['raceName'],
            'circuit': race['Circuit']['circuitName'],
            'date': race['date'],
            'driver': result['Driver']['familyName'],
            'constructor': result['Constructor']['name'],
            'position': result['position'],
            'q1': result.get('Q1', None),
            'q2': result.get('Q2', None),
            'q3': result.get('Q3', None)
        })

# %%
# Step 4: Create DataFrame
df_qualifying_2022 = pd.DataFrame(qualifying_data_2022)
df_qualifying_2022.head()

# %%
# Step 5: Save to SQL
df_qualifying_2022.to_sql(
    name="qualifying_results_2022",
    con=engine,
    schema='raw',
    if_exists='replace',
    index=False
)
print("✅ Qualifying 2022 data uploaded to PostgreSQL (raw schema) successfully.")

# %%
# Step 1: Pull Race Results from F1 API (2022)
url = "https://ergast.com/api/f1/2022/results.json?limit=1000"
response = requests.get(url)
data = response.json()

# %%
# Step 2: Navigate to Race Results
races = data['MRData']['RaceTable']['Races']

# %%
# Step 3: Normalize the Race results
race_data_2022 = []
for race in races:
    for result in race['Results']:
        race_data_2022.append({
            'season': race['season'],
            'round': race['round'],
            'race_name': race['raceName'],
            'circuit': race['Circuit']['circuitName'],
            'date': race['date'],
            'driver': result['Driver']['familyName'],
            'constructor': result['Constructor']['name'],
            'grid': result['grid'],
            'finish': result['position'],
            'status': result['status'],
            'points': result['points']
        })

# %%
# Step 4: Create DataFrame and Save to CSV
df_race_2022 = pd.DataFrame(race_data_2022)
df_race_2022.head()

# %%
# Step 5: Save 2022 Race Data to SQL
df_race_2022.to_sql(
    name="race_results_2022",
    con=engine,
    schema='raw',
    if_exists='replace',
    index=False
)
print("✅ Race 2022 data uploaded to PostgreSQL (raw schema) successfully.")

# %%
# Step 1: Pull Qualifying Results from F1 API (2023)
url = "https://ergast.com/api/f1/2023/qualifying.json?limit=1000"
response = requests.get(url)
print("Status Code:", response.status_code)
print("Sample Keys:", response.json().keys())

# %%
# Step 2: Navigate to Race Results
races = response.json()['MRData']['RaceTable']['Races']

# %%
# Step 3: Normalize the qualifying results
qualifying_data = []
for race in races:
    for result in race['QualifyingResults']:
        qualifying_data.append({
            'season': race['season'],
            'round': race['round'],
            'race_name': race['raceName'],
            'circuit': race['Circuit']['circuitName'],
            'date': race['date'],
            'driver': result['Driver']['familyName'],
            'constructor': result['Constructor']['name'],
            'position': result['position'],
            'q1': result.get('Q1', None),
            'q2': result.get('Q2', None),
            'q3': result.get('Q3', None)
        })

# %%
# Step 4: Create DataFrame
df_qualifying = pd.DataFrame(qualifying_data)
df_qualifying.head()

# %%
# Step 5: Save 2023 Qualifying Data to SQL
df_qualifying.to_sql(
    name="qualifying_results_2023",
    con=engine,
    schema='raw',
    if_exists='replace',
    index=False
)
print("✅ Qualifying 2023 data uploaded to PostgreSQL (raw schema) successfully.")

# %%
# Step 1: Pull Race Results from F1 API (2023)
url = "https://ergast.com/api/f1/2023/results.json?limit=1000"
response = requests.get(url)
data = response.json()

# %%
# Step 2: Navigate to the race results
races = data['MRData']['RaceTable']['Races']

# %%
# Step 3: Normalize the race results
race_data = []

for race in races:
    for result in race['Results']:
        race_data.append({
            'season': race['season'],
            'round': race['round'],
            'race_name': race['raceName'],
            'circuit': race['Circuit']['circuitName'],
            'date': race['date'],
            'driver': result['Driver']['familyName'],
            'constructor': result['Constructor']['name'],
            'grid': result['grid'],          # Starting position
            'finish': result['position'],    # Final result
            'status': result['status'],      # Did not finish / finished / etc.
            'points': result['points']       # Points earned
        })

# %%
# Step 4: Create DataFrame
df_race = pd.DataFrame(race_data)
df_race.head()

# %%
# Step 5: Save 2023 Race Data to SQL
df_race.to_sql(
    name="race_results_2023",
    con=engine,
    schema='raw',                  # ✅ target the 'raw' schema
    if_exists='replace',
    index=False
)
print("✅ Race 2023 data uploaded to PostgreSQL (raw schema) successfully.")


