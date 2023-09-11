#!/usr/bin/env python3
"""Where can I learn Python?"""


def schools_by_topic(mongo_collection, topic):
    """function that returns the list"""
    results = [school for school in mongo_collection.find({"topics": topic})]
    return results
