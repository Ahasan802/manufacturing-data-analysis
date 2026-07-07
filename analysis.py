Python
import pandas as pd

# 1. Load the manufacturing dataset
file_name = "Manufacturing_Dataset_1000_Rows.xlsx"
df_factory = pd.read_excel(file_name)

# 2. Calculate total downtime and total defects per shift
shift_summary = df_factory.groupby('Shift')[['DowntimeMin', 'DefectQty']].sum().reset_index()

# 3. Calculate average efficiency per shift
shift_efficiency = df_factory.groupby('Shift')['Efficiency'].mean().reset_index()

# 4. Merge both summaries into a single performance report
final_summary = pd.merge(shift_summary, shift_efficiency, on='Shift')

# 5. Display the final factory performance report for the client
print("--- Factory Shift Performance Report ---")
print(final_summary.to_string(index=False))
