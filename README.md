# Data Analytics & Log Processing Pipeline

This project is a Lightweight Data Analytics and Log Processing Automation Pipeline written in Python. It reads access log data from a CSV file, filters security events, and calculates performance metrics.

## Project Structure

```text
capstone_project/
├── data/
│   └── sample_data.csv
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── utils.py
│   └── logic.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Features
- **Data Ingestion**: Parses structured log records from standard CSV files using native Python modules.
- **Data Filtering**: Filters for specific log event types (e.g., failed login attempts).
- **Metric Aggregation**: Computes metrics like average HTTP response times.

## How to Run

1. Clone or download the repository.
2. Navigate into the `src/` folder:
   ```bash
   cd src
   ```
3. Run the main execution script:
   ```bash
   python main.py
   ```