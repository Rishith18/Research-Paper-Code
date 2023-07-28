import csv
import numpy as np
import pandas as pd

def data_normalization(filePath):
    # Read the CSV file using pandas
    df = pd.read_csv(filePath)

    # Extract the values from the DataFrame and convert them to a numpy array
    new_arr = np.array(df).astype(float)

    maxs = [0.02144,0.22066,0.460579,33.197,1,0.78026,0.821364]
    mins = [2e-5, 0.00656, 0.000618, 3.425, 0, 0.17873, 0.55221]
    for i in range(7):
        column_array = new_arr[:, i]
        maxx = maxs[i]
        minn = mins[i]
        if minn != 0 and maxx != 1:
            normalized_column = (column_array - minn) / (maxx - minn)
            new_arr[:, i] = normalized_column
        else:
            new_arr[:, i] = column_array

    print(new_arr)
    file_path = "/Users/rishithprathi/Downloads/data_stuff/test.csv"
    np.savetxt(file_path,new_arr,delimiter=",")
    print("I did it")



file_path = "/Users/rishithprathi/Downloads/data_stuff/Copy_of_small_parkinsons_combined_data.csv"
data_normalization(file_path)