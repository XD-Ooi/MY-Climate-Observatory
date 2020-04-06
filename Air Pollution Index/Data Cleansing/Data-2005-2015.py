"""
4 April 2020
Author: Xiandi Ooi

We'll start off by learning more about the available datasets. 
We will first download the csv file from the source. 
Then, the data is organized to ease future analysis. Specific changes are as follows:
    1. Datetime variable added;
    2. Numerical API values are extracted;
    3. Dominant pollutant type are extracted
This code is applied to the files:
    1. Malaysia API 2005 - 2013;
    2. Malaysia API 2013 - 2014;
    3. Malaysia API 2014 - 2015.
"""

import requests
import pandas as pd

def download_file(url, file_name):
    """
    url: url of the file to be downloaded
    file_name: file name to save the file.
    
    This function takes the given url and download it as the given file name.
    
    Note: the document will be saved to the current working directory, change if required.
    """
    try:
        response = requests.get(url)
    except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  
    except Exception as err:
            print(f"Other error occurred: {err}")  
    else:
        with open(file_name, "wb") as working_file:
            working_file.write(response.content)
        
def clean_data(file_name):
    """
    file_name: file to be cleaned
    
    This function converts the data types in the original dataframe into more suitable type.
    The good news is that the orginal dataframe is already in good shape so there's less to do.   
    """
    
    df_input = pd.read_csv(file_name)
    
    #Checking the basic information about the dataframe (optional)
    #print(df_input.info(), df_input.describe())
    
    #Translating the column names into English
    df_output = df_input.rename(columns = {"Tarikh":"Date", 
                                           "Waktu":"Time", 
                                           "Negeri":"State", 
                                           "Kawasan":"Area"})
    
    #Separating each API values into values and its dominant pollutant
    df_output["API"].astype(str)
    df_output["Dominant"] = df_output["API"].str.extract("(\D+)", expand = False)
    df_output["API_Values"] = df_output["API"].str.extract("(\d+)", expand = False)
    df_output["API_Values"] = pd.to_numeric(df_output["API_Values"], errors="coerce").fillna(0).astype(int)
    
    #Converting the date and time into datetime
    df_output["Datetime"] = df_output[["Date","Time"]].agg("-".join, axis = 1)
    df_output["Datetime"] = pd.to_datetime(df_output["Datetime"], format = "%d/%m/%Y-%I:%M%p")

    #Checking the basic information about the final dataframe (optional)
    #print(df_output.info())
    
    #Export output to new csv file (edit path and name as needed)
    df_output.to_csv(r"file_path\file_name.csv")
    return df_output
    
def main():
    url = "http://www.data.gov.my/data/dataset/034a727d-1eb6-4a3d-bcd1-119b059c4840/resource/e1578b5d-8bca-41ee-827d-2f8392d0c762/download/14-bacaanipu2005-2013.csv"
    file_name = "API_2005_2013.csv"
    #copy the other two links and processed similarly
    download_file(url, file_name)
    clean_data(file_name)

if __name__ == "__main__":
    main()
