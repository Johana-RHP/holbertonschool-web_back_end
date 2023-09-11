#!/usr/bin/env python3
"""Insert a document in Python"""


def insert_school(mongo_collection, **kwargs):
    """inserts a new document in a collection"""
    insert_id = mongo_collection.insert_one(kwargs)
    return (insert_id.inserted_id)
