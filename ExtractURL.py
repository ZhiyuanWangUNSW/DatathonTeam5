#%%
import pandas as pd
import requests
from bs4 import BeautifulSoup
from googletrans import Translator
from concurrent.futures import ThreadPoolExecutor
import unicodedata
import os
import time
#%%
# Translator initialization
translator = Translator()
#%%
# Load the CSV file
csv_file = r"I:\UNSW\DatathonTeam5\release\epiwatch-latest.csv"
df = pd.read_csv(csv_file)
#%%
# Function to clean text
def clean_content(content):
    content = unicodedata.normalize('NFKD', content)
    content = content.replace('“', '"').replace('”', '"')
    content = content.replace("‘", "'").replace("’", "'")
    content = content.replace("\n", " ").strip()
    return content

# Function to fetch content with retries, timeout, and skip hanging URLs
def fetch_full_content_with_retry(url, retries=3):
    for attempt in range(retries):
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            response = requests.get(url, headers=headers, timeout=10)  # Set timeout to 10 seconds
            response.encoding = response.apparent_encoding
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                paragraphs = [p.get_text() for p in soup.find_all('p')]
                return ' '.join(paragraphs).strip() if paragraphs else "No content found"
            elif response.status_code == 404:
                return "Error 404: Page not found"
            elif response.status_code == 401:
                return "Error 401: Unauthorized"
        except requests.exceptions.Timeout:
            print(f"Timeout occurred for URL: {url}. Retrying... (Attempt {attempt + 1}/{retries})")
        except requests.exceptions.RequestException as e:
            print(f"Request failed for URL: {url} - {str(e)}. Retrying... (Attempt {attempt + 1}/{retries})")
        time.sleep(2 ** attempt)  # Exponential backoff (1s, 2s, 4s, etc.)

    # If all retries fail, skip the URL
    print(f"Skipping URL after {retries} failed attempts: {url}")
    return "Error: Skipped due to repeated failures"


#%% No other changes in the code

# Function to translate content dynamically
def translate_content(content):
    try:
        if not content or content.startswith("Error"):
            return content

        content = clean_content(content)
        detected_lang = translator.detect(content).lang
        if detected_lang != 'en':
            translated = translator.translate(content, src=detected_lang, dest='en')
            return translated.text
        return content
    except Exception as e:
        return f"Translation Error: {str(e)}"

# Combined function to process each row
def process_row(row):
    url = row['url']
    try:
        print(f"Processing URL: {url}")
        full_content = fetch_full_content_with_retry(url)
        translated_content = translate_content(full_content)
        return translated_content
    except Exception as e:
        print(f"Error processing URL: {url} - {str(e)}")
        return f"Error: {str(e)}"

#%% Process URLs in Batches and Skip Specific Countries
batch_size = 100  # Number of rows in each batch
output_folder = r"I:\UNSW\DatathonTeam5\processed_batches"  # Folder to save individual batch files
os.makedirs(output_folder, exist_ok=True)  # Ensure the folder exists

total_records = len(df)
total_batches = (total_records // batch_size) + (1 if total_records % batch_size != 0 else 0)

print(f"Total records: {total_records}, Batch size: {batch_size}, Total batches: {total_batches}")

for i in range(0, total_records, batch_size):
    try:
        # Extract the current batch
        batch = df.iloc[i:i + batch_size].copy()

        # Patch where country is china
        batch = batch[batch['country'] == 'China']
        if batch.empty:
            print(f"Batch {i // batch_size + 1}/{total_batches} has no valid URLs to process. Skipping...")
            continue

        # Process rows in the batch using multithreading
        with ThreadPoolExecutor(max_workers=5) as executor:
            batch['Translated_Content'] = list(executor.map(process_row, [row for _, row in batch.iterrows()]))

        # Save the processed batch to an individual CSV file
        batch_file = os.path.join(output_folder, f"batch_{i // batch_size + 1}.csv")
        batch.to_csv(batch_file, index=False)
        
        print(f"Batch {i // batch_size + 1}/{total_batches} processed and saved to {batch_file}.")
    except Exception as e:
        print(f"Error processing batch {i // batch_size + 1}/{total_batches}: {str(e)}")


