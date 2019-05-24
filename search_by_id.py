import csv
from elasticsearch import Elasticsearch
import pandas as pd


def main():
    filename = "/home/ubuntu/Downloads/sample.csv"
    df = pd.read_csv(filename, sep=",")
    es = Elasticsearch()
    i = 1
    for index,row in df.iterrows():
        # print(row['User Id'])
        es.index(index='my-index', doc_type='twitter', id=i, body={
            "user_id": row['User Id'],
            "Tweet URL": row['Tweet URL'],
            "user_name": row['Username'],
            "Tweet_content": row['Tweet Content']
        })
        i = i+1

    res = es.get(index='my-index', doc_type='twitter', id=15)
    print(res['_source'])


if __name__ == '__main__':
    main()
