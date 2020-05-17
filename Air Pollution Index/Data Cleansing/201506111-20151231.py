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
    
    df_input = pd.read_excel(file_name)
        
    #Checking the basic information about the dataframe (optional)
    #print(df_input.info(), df_input.describe())
    #print(df_input["SiteID"].unique())
    #print(df_input["Site_Location"].unique())
    #print(df_input["Date"].unique())
    
    #Making a copy of the dataframe
    df_output = df_input.copy()
    
    #Change column name for consistency
    df_output["API_Values"] = df_output["API"]
    #Note that there is no dominant pollutant data for this dataset
    
    #Converting the date into datetime
    #Note the time are all set at 00:00 since there is no data available
    df_output["Datetime"] = pd.to_datetime(df_output["Date"], format = "%Y%m%d")
    
    #Creating new columns "Area" and "State" based on the "Site Location" for consistency
    #The area and state allocated are based on the categorization of other dataframes
    #the dictionary is organized in the following form: Site_Location: (Area, State)
    area_directory = {"Sek. Men. Pasir Gudang 2, Pasir Gudang": ("Pasir Gudang", "Johor"),
                      "SMK Bukit Rambai, Melaka": ("Bukit Rambai", "Melaka"),
                      "Sek. Keb. Tunku Ismail,Bakar Arang, Sungai Petani": ("Bakar Arang, Sg. Petani", "Kedah"),
                      "Larkin, Johor": ("Larkin Lama", "Johor"),
                      "SMK Tanjung Chat, Kota Bahru": ("SMK Tanjung Chat, Kota Bharu", "Kelantan"),
                      "Komplek Sukan Langkawi, Kedah": ("Langkawi", "Kedah"),
                      "Sek. Men. Agama Mergong, Alor Setar, Kedah": ("Alor Setar", "Kedah"),
                      "Sekolah Tinggi Melaka, Melaka": ("Bandaraya Melaka", "Melaka"),
                      "Kolej Vokasional Sg Abong, Muar, Johor": ("Muar", "Johor"),
                      "SMA, Bandar Penawar, Kota Tinggi, Johor": ("Kota Tinggi", "Johor"),
                      "SMK. Tanah Merah, Kelantan": ("Tanah Merah", "Kelantan"),
                      "Sek. Keb. Cenderawasih, Perai": ("Perai", "Pulau Pinang"),
                      "Pej. Kajicuaca Batu Embun, Jerantut": ("Jerantut", "Pahang"),
                      "Sek. Men. Jalan Tasek, Ipoh": ("Jalan Tasek, Ipoh", "Perak"),
                      "Sek. Keb. Seberang Jaya II, Perai": ("Seberang Jaya 2, Perai", "Pulau Pinang"),
                      "Tmn. Semarak (Phase II), Nilai": ("Nilai", "Negeri Sembilan"),
                      "Sek. Keb. Indera Mahkota, Kuantan": ("Indera Mahkota, Kuantan", "Pahang"),
                      "Sek. Keb. Balok Baru, Kuantan": ("Balok Baru, Kuantan", "Kuantan"),
                      "Sek. Keb. Air Puteh, Taiping": ("Kg. Air Putih, Taiping", "Perak"),
                      "Pejabat MADA, Kangar, Perlis": ("Kangar", "Perlis"),
                      "Universiti Sains Malaysia, Pulau Pinang": ("USM", "Pulau Pinang"),
                      "Pejabat Pentadbiran Daerah Manjung, Perak": ("Seri Manjung", "Perak"),
                      "Universiti Pendidikan Sultan Idris, Tanjung Malim": ("Tanjung Malim", "Perak"),
                      "Sek. Keb. Pegoh(4), Ipoh, Perak": ("S K Jalan Pegoh, Ipoh", "Perak"),
                      "Sek. Men. Teknik Tuanku Jaafar, Ampangan, Seremban": ("Seremban", "Negeri Sembilan"),
                      "Pusat Sumber Pendidikan N.S. Port Dickson": ("Port Dickson", "Negeri Sembilan"),
                      "Sek. Ren. Keb. Bukit Kuang, Teluk Kalung": ("Kemaman", "Terengganu"),
                      "Medical Store, Kuching, Sarawak": ("Kuching", "Sarawak"),
                      "Sek. Men. (P) Raja Zarina, Kelang": ("Pelabuhan Kelang", "Selangor"),
                      "Sek. Keb. Bandar Utama Damansara, Petaling Jaya": ("Petaling Jaya", "Selangor"),
                      "Kuarters TNB, Paka": ("Paka", "Terengganu"),
                      "Sek. Keb. TTDI Jaya, Shah Alam": ("Shah Alam", "Selangor"),
                      "Ibu Pejabat Polis Sibu, Sarawak": ("Sibu", "Sarawak"),
                      "Balai Polis Pusat Bintulu, Sarawak": ("Bintulu", "Sarawak"),
                      "Sek. Men. Dato Permaisuri Miri, Sarawak": ("Miri", "Sarawak"),
                      "Balai Polis Pusat Sarikei, Sarawak": ("Sarikei", "Sarawak"),
                      "Sek. Men. Keb Putatan, Tg Aru, Kota Kinabalu": ("Kota Kinabalu", "Sabah"),
                      "Dewan Suarah, Limbang, Sarawak": ("Limbang", "Sarawak"),
                      "Sek. Keb. Chabang Tiga Kuala Terengganu": ("Kuala Terengganu", "Terengganu"),
                      "Pejabat Perumahan, Kota Samarahan, Sarawak": ("Samarahan", "Sarawak"),
                      "Pejabat Perumahan, Sri Aman, Sarawak": ("Sri Aman", "Sarawak"),
                      "Pejabat Kerja Raya Tawau, Sabah": ("Tawau", "Sabah"),
                      "Jln Perumahan Majlis Perbandaran Labuan": ("Labuan", "Wilayah Persekutuan"),
                      "Sekolah Menengah Sains, Kuala Selangor": ("Kuala Selangor", "Selangor"),
                      "Sek. Men. Keb Gunsanad, Keningau. Sabah": ("Keningau", "Sabah"),
                      "Pejabat JKR, Batu 3 1/2 Sandakan. Sabah.": ("Sandakan", "Sabah"),
                      "Sek. Keb. Precint 8(2), Putrajaya": ("Putrajaya", "Wilayah Persekutuan"),
                      "Sek.Men.Keb.Seri Permaisuri, Cheras": ("Cheras,Kuala Lumpur", "Wilayah Persekutuan"),
                      "Stadium Tertutup, Kapit": ("Kapit", "Sarawak"),
                      "Batu Muda, Kuala Lumpur": ("Batu Muda,Kuala Lumpur", "Wilayah Persekutuan"),
                      "Banting, Selangor": ("Banting", "Selangor"),
                      "ILP MIRI, Sarawak": ("ILP Miri", "Sarawak")}
    
    #Create temporary column "Site"
    df_output["Site"] = df_output["Site_Location"].map(area_directory)
    df_output[["Area", "State"]] = pd.DataFrame(df_output["Site"].tolist(), index= df_output.index)
    
    #Site_location is removed since it is inconsistent with the main dataframe 
    df_output = df_output.drop(columns = ["Site_Location", "Site", "API", "Date", "SiteID"])    

    #Checking the basic information about the final dataframe (optional)
    #print(df_output.info())
    
    #This dataframe covers the time from 1 Jan to 31 Dec 2015
    #However, we already have data until 10 Jun 2015 from the dominant dataframe,
    #so we will now filter out data starting from 11 Jun - 31 Dec 2015
    df_extract = df_output[(df_output['Datetime'] > '2015-06-10')]
    #print(df_extract.info())
    
    #Export output to new csv file (edit path and name as needed)
    df_extract.to_csv(r"file_path\file_name.csv")
    return df_extract
    
def main():
    url = "http://www.data.gov.my/data/ms_MY/dataset/ed998295-82f8-497f-b2f9-e5939cd35c54/resource/8ab21ca1-85a7-4dbc-9654-1b0384b09dc5/download/ipu-2015.xlsx"
    file_name = "API_2015.xlsx"
    download_file(url, file_name)
    clean_data(file_name)

if __name__ == "__main__":
    main()
