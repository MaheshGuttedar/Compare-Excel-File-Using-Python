import pandas as pd
import numpy as np
import os


def compare_excel_files(file1_path, file2_path):
    """
    Compare two Excel files and highlight differences in the first file.
    """
    try:
       
        df1 = pd.read_excel(file1_path)
        df2 = pd.read_excel(file2_path)
    except Exception as e:
        print("Error reading file: ", e)
        return
    
  
    if df1.shape != df2.shape:
        print("Data frames have different shapes")
        return

    comparison_values = df1.values == df2.values
    

    rows, cols = np.where(comparison_values == False)
    

    for item in zip(rows, cols):                
        df1.iloc[item[0], item[1]] = '{} --> {}'.format(df1.iloc[item[0], item[1]], df2.iloc[item[0], item[1]])
        print(item)
  
    base_path, file1_name = os.path.split(file1_path)
    file1_modified_path = os.path.join(base_path, "modified_" + file1_name)
    df1.to_excel(file1_modified_path, index=False)
    
    print("Comparison complete. Differences highlighted in: ", file1_modified_path)
