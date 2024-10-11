import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

url_nassau = 'https://health.data.ny.gov/resource/5dtw-tffi.csv?hospital_county=Nassau&$limit=500000'
url_suffolk = 'https://health.data.ny.gov/resource/5dtw-tffi.csv?hospital_county=Suffolk&$limit=500000'

nassau_df = pd.read_csv(url_nassau)
len(nassau_df)