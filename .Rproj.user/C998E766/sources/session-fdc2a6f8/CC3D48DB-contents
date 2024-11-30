# Health Data Science Datathon 2024

## _Can you predict the next pandemic?_

<br>

### Overview

In this repository you will find the subset of the EPIWATCH data we will use for the datathon as well as some details on the dataset. 

***

<br>

### What does the data contain?

This dataset contains nine variables and over 40,000 records. Each row represents an online news article that mentions one or more infections diseases or syndromes. Below is an example of one of the online news articles contained in the dataset.

![From [sport.24tv.ua](https://sport.24tv.ua/ru/jepidemija-koronavirusa-ukrainskom-futbole-volyni-novosti-zdorovja_n1415777)](article-example.png)

Key details about each article are provided, including: 

* Dates
* Location
* Diseases
* Syndromes
* Article url

***

<br>

### Illustrating the data

Aggregating the data provides trends in diseases over time, such as the series below, which shows daily counts of articles mentioning COVID-19 in Ukraine. 

![](covid-in-ukraine.png)

***

<br>

## Dataset summary

***

### Country

![](Available_countries.png)

Data for **twelve** countries: 

  * United States
  * India 
  * China 
  * Russian Federation 
  * Ukraine 
  * United Kingdom 
  * Vietnam 
  * Indonesia 
  * Brazil 
  * Australia 
  * Argentina 
  * Nigeria

There is also:

* **location** e.g. Sydney, New South Wales
* **coordinates** e.g. [-33.873, 151.205] (points to The Scary Canary on Kent Street so may or may not be accurate) 

***

<br>

### Diseases 

Data for **seven** diseases

* Influenza (many strains)
* Covid-19
* Mpox
* Legionnaires'
* Dengue
* Measles
* Cholera

***

<br>

### Syndromes

Syndromes refer to more generalised symptoms, usually recorded when the disease is unknown. Common syndromes include 

* Acute gastroenteritis 
* Severe acute respiratory syndrome
* Febrile syndromes
* Pneumonia 
* Influenza-like illness
* See the documentation for details of related transmission types for different syndromes. 

***

<br>

### Example of syndromes preceding diseases

![](example-outbreak.gif)

<br>

Early reports like [this one](https://brazilian.report/liveblog/2022/09/01/unexplained-pneumonia-health-workers/) refer to an "unexplained type of pneumonia". 

> **Unexplained pneumonia kills two health workers in Argentina**
>
> An unexplained type of pneumonia has killed two health workers in Tucumán, a province in northwestern Argentina, with four patients undergoing intensive care 

As the week progresses, the source of the infection becomes clearer and identified as Legionnaires' Disease in articles like [this one](https://www.batimes.com.ar/news/argentina/legionnaires-outbreak-in-tucuman-claims-sixth-life.phtml)

> Legionnaires' outbreak in Tucumán claims sixth life
>
> Latest victim, who died late Sunday, was an 81-year-old patient with comorbidities who had been "in a serious condition" receiving treatment for pneumonia.

***

<br>


### Accessing the data

The latest EPIWATCH data is provided as a .csv file named `epiwatch-latest.csv`. You can download the file by navigating to the [release](./release/) folder, selecting the file and clicking download or (preferably) by reading the data directly into your statistical software package, as demonstrated in the R and Python code snippets below. 

#### Read data with R

```
# GitHub raw URL for the CSV file
url <- "https://raw.githubusercontent.com/CBDRH/hds-datathon-data/refs/heads/main/release/epiwatch-latest.csv"

# Read the CSV file from the URL
data <- read.csv(url)

# View the first few rows of the data
head(data)
```

#### Read data with Python

```
import pandas as pd

# GitHub raw URL for the CSV file
url = "https://raw.githubusercontent.com/CBDRH/hds-datathon-data/refs/heads/main/release/epiwatch-latest.csv"

# Read the CSV file from the URL into a pandas DataFrame
data = pd.read_csv(url)

# View the first few rows of the data
print(data.head())

```
