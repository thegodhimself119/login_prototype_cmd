from pymongo import MongoClient
import certifi
from ooptest import consts



for collist in consts.collist:
    col = consts.db[collist]
    find = col.find({})  # find existing collection
    for find in find:
        pw = find["password"]
        print("username:",collist,"// password: ",pw)