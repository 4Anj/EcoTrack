import pandas as pd

df=pd.read_csv("carbon_data.csv")
df.iloc[0:0].to_csv("carbon_data.csv",index=False)
print("DONE")


#for deleting rows and columns

import os # Import the os module for file system operations

file_name = "carbon_data.csv"

# Check if the file exists.
# If it doesn't, 'w' mode will create it as an empty file.
# If it does, 'w' mode will truncate (empty) it.
try:
    with open(file_name, 'w') as f:
        # The 'w' mode (write mode) automatically truncates the file to zero length
        # when opened. By immediately closing it (which 'with' statement handles),
        # the file becomes completely empty, removing both data and headers.
        pass # 'pass' means do nothing inside the block, just open and close.
    print(f"'{file_name}' has been completely cleared. It is now an empty file (no rows, no headers).")
except Exception as e:
    print(f"An error occurred while clearing the file: {e}")

print("DONE")
