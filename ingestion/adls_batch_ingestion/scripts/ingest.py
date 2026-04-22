import pandas as pd
df=pd.read_csv("data/yellow_tripdata_2019-01.csv")
#print(df.head())
print(df.columns)
df['tpep_pickup_datetime']=pd.to_datetime(df['tpep_pickup_datetime'])
df['tpep_dropoff_datetime']=pd.to_datetime(df['tpep_dropoff_datetime'])

df['pickup_date']=df['tpep_pickup_datetime'].dt.floor('D')
df['dropoff_date']=df['tpep_dropoff_datetime'].dt.floor('D')

print(df.head())
print(df.dtypes)

df.to_parquet('data/yellow_tripdata.parquet', engine='pyarrow',index='False')

