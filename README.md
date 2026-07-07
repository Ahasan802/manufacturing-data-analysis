# manufacturing-data-analysis
Python script to analyze factory shift performance, downtime, and defects.
# Manufacturing Data Analysis Project

This project contains a Python script designed to analyze factory production data from a dataset containing 1,000 rows. It automates the process of extracting critical performance insights across different shifts for international clients and business stakeholders.

## 📊 Key Features & Analysis
The Python script utilizes the **Pandas** library to perform the following operations:
1. **Data Loading:** Efficiently reads and processes manufacturing datasets from Excel.
2. **Shift-wise Downtime & Defects:** Groups data by shifts (`Morning`, `Evening`, `Night`) to calculate the total machine loss time (`DowntimeMin`) and total rejected products (`DefectQty`).
3. **Efficiency Metrics:** Evaluates the average operational efficiency (`Efficiency`) for each factory shift.
4. **Data Aggregation:** Merges multiple summary reports into a single, clean performance matrix.

## 💻 Tech Stack Used
* **Language:** Python
* **Libraries:** Pandas, Openpyxl (for Excel integration)

## 📌 How to Run
1. Ensure you have Python and Pandas installed.
2. Place the `Manufacturing_Dataset_1000_Rows.xlsx` file in the same directory.
3. Run the script using:
   ```bash
   python analysis.py
