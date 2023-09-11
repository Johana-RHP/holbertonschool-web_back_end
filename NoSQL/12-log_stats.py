#!/usr/bin/env python3
"""Log stats"""

from pymongo import MongoClient


if __name__ == "__main__":
    MONGO_URI = "mongodb://localhost"
    client = MongoClient(MONGO_URI)
    db = client['logs']
    col = db['nginx']
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print(f'{col.count:documents({})} logs')
    print('Methods:')
    for method in methods:
        count_method = db_nginx.count_documents({'method': method})
        print(f'\tmethod {method}: {count_method}')

    sc = "status check"
    print(f"{col.count_documents({'method': 'GET','path': '/status'})} {sc}")
