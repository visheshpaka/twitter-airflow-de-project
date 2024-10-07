import tweepy
import pandas as pd 
import json
from datetime import datetime
import s3fs 

def run_twitter_etl():
    
    df = pd.read_csv('s3://airflow-before-etl/tweets.csv')              #extract data from s3 bucket
    df.drop(columns=['latitude','longitude'], inplace=True)             #basic transformation to a dataframe
    df.to_csv("s3://vishesh-airflow-etl-bucket/refined_tweets.csv")     #load processed data back to s3 bucket