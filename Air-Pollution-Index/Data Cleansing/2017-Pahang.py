"""
23 May 2020
Author: Xiandi Ooi

We will first download the file from the source. 
Then, the data is organized to ease future analysis. Specific changes are as follows:
    1. Datetime variable added;
    2. Numerical API values are extracted;
    3. Dominant pollutant type are extracted

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
    
    df_input = pd.read_excel(file_name, skiprows=3)
    
    #Checking the basic information about the dataframe (optional)
    #print(df_input.info()) 
    #print(df_input.describe())

    #Selecting columns
    df_output = df_input.rename(columns = {"DATE/TIME":"Datetime"})
    df_output.drop(df_output.tail(1).index,inplace=True)
    
    #Pivoting the dataframe for its Area and State
    df_final = pd.melt(df_output, id_vars=["Datetime"], 
                        value_vars = ["Sek. Men. Keb. Seri Rompin, Rompin",
                                      " Meteorologi Temerloh, Temerloh",
                                      "SMK. Jerantut, Jerantut",
                                      "Sek. Keb. Indera Mahkota, Indera Mahkota",
                                      "Sek. Keb. Balok Baru, Balok Baru"],
                        var_name="Station", value_name="API")
    area_directory = {"Sek. Men. Keb. Seri Rompin, Rompin": ("Rompin", "Pahang"),
                      " Meteorologi Temerloh, Temerloh": ("Temerloh", "Pahang"),
                      "SMK. Jerantut, Jerantut": ("Jerantut", "Pahang"),
                      "Sek. Keb. Indera Mahkota, Indera Mahkota": ("Indera Mahkota, Kuantan","Pahang"),
                      "Sek. Keb. Balok Baru, Balok Baru": ("Balok Baru, Kuantan","Pahang")}
    #There are some new stations added, the area are displayed in a similar manner as previous datasets
    df_final["Site"] = df_final["Station"].map(area_directory)
    df_final[["Area", "State"]] = pd.DataFrame(df_final["Site"].tolist(), index= df_final.index)
    
    #Separating each API values into values and its dominant pollutant
    df_final["API"].astype(str)
    df_final["Dominant"] = df_final["API"].str.extract("(\D+)", expand = False)
    df_final["API_Values"] = df_final["API"].str.extract("(\d+)", expand = False)
    df_final["API_Values"] = pd.to_numeric(df_final["API_Values"], errors="coerce").fillna(0).astype(int)
    
    df_final = df_final.drop(columns = ["Station", "Site", "API"])  
    #Checking the basic information about the final dataframe (optional)
    #print(df_final.info())
    
    #Export output to new csv file (edit path and name as needed)
    df_output.to_csv(r"file_path\file_name.csv")
    return df_final
    
def main():
    url = "http://www.data.gov.my/data/ms_MY/dataset/ccf86990-4052-4741-a0ea-23fc544a381c/resource/59e2f89f-3fca-4d7b-8c0e-5cbda7414b54/download/pahang.xlsx"
    file_name = "API_Pahang_2017.xlsx"
    download_file(url, file_name)
    clean_data(file_name)

if __name__ == "__main__":
    main()
