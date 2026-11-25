# Oran Weather Report

A Python script that retrieves the last 7 days of daily temperatures for Oran, Algeria, organizes them in a table, and generates a line chart.

## Features

- Fetches daily maximum and minimum temperatures from a public weather API
- Builds a structured table with pandas
- Plots a clear line chart (max vs. min temperature)
- Exports results to `CSV` and `PNG` files

## Tech Stack

- Python 3
- `requests` (API calls)
- `pandas` (data handling)
- `matplotlib` (visualization)

## Installation

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPO.git
cd YOUR-REPO
pip install -r requirements.txt
```

## Usage

```bash
python weather.py
```

The script displays the chart and saves two files:

| File | Description |
|------|-------------|
| `weather.png` | Line chart of daily max and min temperatures |
| `weatherOran/weather.csv` | Daily temperature data in CSV format |

## Example Output

![Weather chart](weather.png)

## Data Source

Weather data provided by [Open-Meteo](https://open-meteo.com/) under the [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) license. No API key is required.

## Possible Improvements

- Choose the city from a list of Algerian cities
- Add precipitation and wind speed
- Handle network errors (timeout and retries)
- Organize the code into reusable functions

## Author

Nacer Akram Boumous
