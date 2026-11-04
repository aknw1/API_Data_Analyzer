# API_Data_Analyzer

A Python project that retrieves, validates, analyzes, and exports API data.

## Installation

To install the required dependencies, run the following command in your terminal:

```bash
pip install -r requirements.txt
```

## Usage

To run the application, open the terminal in the project's root directory and execute the following command:

```bash
python main.py
```
## Features

- Retrieves data from an API.
- Validates and filters the retrieved data.
- Analyzes the filtered data.
- Exports the data in JSON and CSV formats.

## Technologies

- **Language:** Python.
- **External libraries:** Requests.
- **Standard library modules:** csv, json.
- **Version control:** Git and GitHub.

## Project Structure

- **main.py:** Main entry point of the application.
- **analyzer.py:** Analyzes the retrieved data
- **api.py:** Handles API requests and retrieves data
- **validation.py:** Validates and filters the data.
- **storage.py:** 	Saves data and reports in CSV and JSON formats

## Data Source

This project uses the [JSONPlaceholder API](https://jsonplaceholder.typicode.com/posts) to retrieve post data.

## Example Output

When running `python main.py`, the application produces the following output:

```text
succeeded: 200
Posts retrieved: 100
Valid posts: 100
Invalid posts: 0
Total posts: 100
User counts: {1: 10, 2: 10, 3: 10, 4: 10, 5: 10, 6: 10, 7: 10, 8: 10, 9: 10, 10: 10}
Most active user: 1
Posts saved: True
CSV saved successfully: True
Report saved successfully: True