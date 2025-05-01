# %%
!pip install praw pandas
!pip install pandas requests
!pip install -q praw
import os
import time
import requests
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine


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
import requests
import csv
import time

def fetch_all_threads(subreddit, max_pages=10, delay=2):
    headers = {'User-Agent': 'RedditScraper/1.0'}
    base_url = f'https://www.reddit.com/r/formula1/.json'
    after = None
    all_posts = []

    for _ in range(max_pages):
        url = base_url + (f'?after={after}' if after else '')
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print(f"Failed to fetch data: {response.status_code}")
            break

        data = response.json()
        posts = data['data']['children']
        all_posts.extend([post['data'] for post in posts])

        after = data['data'].get('after')
        if not after:
            break

        time.sleep(delay)

    return all_posts

def write_to_csv(posts, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=['title', 'selftext'])
        writer.writeheader()

        for post in posts:
            writer.writerow({
                'title': post.get('title', '').replace('\n', ' ').strip(),
                'selftext': post.get('selftext', '').replace('\n', ' ').strip()
            })

# Usage
subreddit = 'formula1'
threads = fetch_all_threads(subreddit, max_pages=5)
csv_filename = f'{subreddit}_threads.csv'

write_to_csv(threads, csv_filename)
print(f"Wrote {len(threads)} threads to {csv_filename}")

# %%
# Convert threads (list of dicts) into a DataFrame
df_web_scraped = pd.DataFrame(threads)

# %%
df_web_scrape = pd.read_csv('formula1_threads.csv')
print(df_web_scrape.shape)
print(df_web_scrape.head())

# %%
import pandas as pd

# Read CSV into DataFrame (this file was created earlier by your Reddit script)
df_web_scrape = pd.read_csv('formula1_threads.csv')

# Write to PostgreSQL in 'raw' schema
df_web_scrape.to_sql(
    name='web_scrape_formula1',
    con=engine,
    schema='raw',
    if_exists='replace',
    index=False
)

print("Web scrape CSV uploaded to PostgreSQL successfully.")


