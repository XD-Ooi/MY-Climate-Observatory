"""
17 May 2020
Author: Xiandi Ooi

We'll start off by learning more about the available datasets. 
We will first download the csv file from the source. 
Then, the data is organized to ease future analysis. Specific changes are as follows:
    1. Column names changed to match the dominant dataframes;
    2. Site location modified to match the dominant dataframes.

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
    
    df_input = pd.read_excel(file_name,sheet_name = "IPU2016")
        
    #Checking the basic information about the dataframe (optional)
    #print(df_input.info(), df_input.describe())
    #print(df_input["Lokasi"].unique())
    
    #Making a copy of the dataframe
    df_output = df_input.copy()
    
    #Change column name for consistency
    df_output = df_input.rename(columns = {"Tarikh":"Date",
                                           "API":"API_Values",
                                           "Masa":"Time"})
    #Note that there is no dominant pollutant data for this dataset
    
    #Converting the date into datetime
    df_output["Date"] = df_output["Date"].astype(str)
    df_output["Time"] = df_output["Time"].astype(str)
    df_output["Datetime"] = df_output[["Date","Time"]].agg("-".join, axis = 1)
    df_output["Datetime"] = pd.to_datetime(df_output["Datetime"], format = "%Y%m%d-%I:%M:%S")
    
    #Creating new columns "Area" based on "Lokasi" for consistency
    #The area and state allocated are based on the categorization of other dataframes
    #the dictionary is organized in the following form: Lokasi: Area
    #Note that there are subtle differences in the input Lokasi values so the directory from previous data cleaning python doc is not applicable
    df_output["Lokasi"] = df_output["Lokasi"].astype(str)
    df_output["Lokasi"] = df_output["Lokasi"].str.rstrip()
    area_directory = {"Sek. Men. Pasir Gudang 2, Pasir Gudang": "Pasir Gudang",
                      "Institut Perguruan Malaysia, Temenggong Ibrahim, Larkin, Johor Bharu": "Lakrin Lama",
                      "Sek. Men. Teknik Muar, Muar, Johor": "Muar",
                      "SMA, Bandar Penawar, Kota Tinggi": "Kota Tinggi",
                      "Sek. Keb. Bakar Arang, Sungai Petani": "Bakar Arang, Sg. Petani",
                      "Komplek Sukan Langkawi, Kedah": "Langkawi",
                      "Sek. Men. Agama Mergong, Alor Setar": "Alor Setar",
                      "Sek. Men. Keb. Tanjung Chat, Kota Bahru": "SMK Tanjung Chat, Kota Bharu",
                      "SMK. Tanah Merah": "Tanah Merah",
                      "Sek. Men. Keb. Bukit Rambai": "Bukit Rambai",
                      "Sek. Men. Tinggi Melaka, Melaka": "Bandaraya Melaka",
                      "Tmn. Semarak (Phase II), Nilai": "Nilai",
                      "Sek. Men. Teknik Tuanku Jaafar, Ampangan, Seremban": "Seremban",
                      "Pusat Sumber Pendidikan N.S. Port Dickson": "Port Dickson",
                      "Pej. Kajicuaca Batu Embun, Jerantut": "Jerantut",
                      "Sek. Keb. Indera Mahkota, Kuantan": "Indera Mahkota, Kuantan",
                      "Sek. Keb. Balok Baru, Kuantan": "Balok Baru, Kuantan",
                      "Sek. Men. Jalan Tasek, Ipoh": "Jalan Tasek, Ipoh",
                      "Sek. Men. Keb. Air Puteh, Taiping": "Kg. Air Putih, Taiping",
                      "Pejabat Pentadbiran Daerah Manjung, Perak": "Seri Manjung",
                      "Universiti Pendidikan Sultan Idris, Tanjung Malim": "Tanjung Malim",
                      "Sek. Men. Pegoh, Ipoh, Perak": "S K Jalan Pegoh, Ipoh",
                      "Institut Latihan Perindustrian (ILP) Kangar": "Kangar",
                      "Sek. Keb. Cederawasih, Taman Inderawasih, Perai": "Perai",
                      "Sek. Keb. Seberang Jaya II, Perai": "Seberang Jaya 2, Perai",
                      "Universiti Sains Malaysia, Pulau Pinang": "USM",
                      "Sek. Men. Keb Putatan, Tg Aru, Kota Kinabalu": "Kota Kinabalu",
                      "Pejabat JKR Tawau, Sabah": "Tawau",
                      "Sek. Men. Keb Gunsanad, Keningau": "Keningau",
                      "Pejabat JKR Sandakan, Sandakan": "Sandakan",
                      "Medical Store, Kuching": "Kuching",
                      "Ibu Pejabat Polis Sibu, Sibu": "Sibu",
                      "Balai Polis Pusat Bintulu": "Bintulu",
                      "Sek. Men. Dato Permaisuri Miri": "Miri",
                      "Balai Polis Pusat Sarikei": "Sarikei",
                      "Dewan Suarah, Limbang": "Limbang",
                      "Pejabat Daerah Samarahan, Kota Samarahan": "Samarahan",
                      "Kompleks Sukan, Sri Aman": "Sri Aman",
                      "Stadium Tertutup, Kapit": "Kapit",
                      "ILP MIRI": "ILP Miri",
                      "Sek. Men. (P) Raja Zarina, Kelang": "Pelabuhan Kelang",
                      "Sek. Keb. Bandar Utama, Petaling Jaya": "Petaling Jaya",
                      "Sek. Keb. TTDI Jaya, Shah Alam": "Shah Alam",
                      "Sekolah Menengah Sains, Kuala Selangor": "Kuala Selangor",
                      "Kolej MARA, Banting": "Banting", 
                      "Sek. Ren. Keb. Bukit Kuang, Teluk Kalung, Kemaman": "Kemaman",
                      "Kuarters TNB, Paka-Kertih": "Paka",
                      "Sek. Keb. Chabang Tiga, Kuala Terengganu": "Kuala Terengganu",
                      "Taman Perumahan Majlis Perbandaran Labuan": "Labuan",
                      "Sek. Keb. Putrajaya 8(2), Jln P8/E2, Presint 8, Putrajaya": "Putrajaya",
                      "Sek.Men.Keb.Seri Permaisuri, Cheras": "Cheras,Kuala Lumpur",
                      "Sek. Keb. Batu Muda, Batu Muda, Kuala Lumpur": "Batu Muda,Kuala Lumpur"}
    
    #Create column "Area"
    df_output["Area"] = df_output["Lokasi"].map(area_directory)
    
    #Create column "State"
    #Since there is very little tokens, mapping a dictionary will be faster
    state_directory = {"JOHOR": "Johor",
                       "KEDAH": "Kedah",
                       "KELANTAN": "Kelantan",
                       "MELAKA": "Melaka",
                       "N.SEMBILAN": "Negeri Sembilan",
                       "PAHANG": "Pahang",
                       "PERAK": "Perak",
                       "PERLIS": "Perlis",
                       "PULAU PINANG": "Pulau Pinang",
                       "SABAH": "Sabah",
                       "SARAWAK": "Sarawak",
                       "SELANGOR": "Selangor",
                       "TERENGGANU": "Terengganu",
                       "WILAYAH PERSEKUTUAN": "Wilayah Persekutuan"}
    df_output["State"] = df_output["Negeri"].map(state_directory)

    df_output = df_output.drop(columns = ["Lokasi", "Negeri"])    

    #Checking the basic information about the final dataframe (optional)
    #print(df_output.info())

    #Export output to new csv file (edit path and name as needed)
    df_extract.to_csv(r"file_path\file_name.csv")
    return df_output
    
def main():
    url = "http://www.data.gov.my/data/ms_MY/dataset/1b22566f-38bf-4b5d-95e7-655fbd9fa36a/resource/fd187e4d-a623-46e4-910b-bd2016a1c5c0/download/jasipu2016.xlsx"
    file_name = "API_2016.xlsx"
    download_file(url, file_name)
    clean_data(file_name)

if __name__ == "__main__":
    main()
