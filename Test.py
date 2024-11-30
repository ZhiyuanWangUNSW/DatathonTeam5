# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 00:35:58 2024

@author: os
"""
#%%
import requests
from bs4 import BeautifulSoup
#%%
url = "https://www.m24.ru/videos/medicina/16092020/257248"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

try:
    response = requests.get(url, headers=headers, timeout=10)
    response.encoding = response.apparent_encoding

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        print("Page fetched successfully!")
        print("Extracted content:")
        paragraphs = [p.get_text() for p in soup.find_all('p')]
        print(paragraphs if paragraphs else "No <p> tags found!")
    else:
        print(f"Failed to fetch page. Status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Error fetching page: {str(e)}")
