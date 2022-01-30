import json
import random
import pymongo
from pymongo import MongoClient
import os

mongoconnectionstring = os.environ['MONGO']
print("connecting...")
client = pymongo.MongoClient(mongoconnectionstring)

#<- this was supposed to be named bread-api
#lets hv the db be bread-api,only the cluster is named cluster 0
# we used the wrong link, it was supposed to be mongodb+srv://replit:{mongopass}@bread-api.cwf7d.mongodb.net/breads?retryWrites=true&w=majority

# bruh mononnnononnnn shitbase is impossible <-----------


# note: db name is breadapi | collection name is breads | breadapi.breads
# nothing
#💀
#💀
#AYo WAit 
#i pressed connect and it asked ip adreses toallow
#we had no ips
#but then theres an option toallow all ips
#and u need to put ip as 0.0.0.0 for all ips
# done. its pending
#huh wuts pending.
# 0.0.0.0/0
#it wasnt added?
#nope, just added it
#:O
#still pending, take forever
# ok done
#pls wrk <---
#:OOOOOOOOOOOOOOOOOOOOOOOOOOO
#ayyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
#TES TES TES TS ET YR SY SEY SL GDHGKFGKdhg'dfhgjl
#dam finaly
# ezzz, (not really)
# lets go!
#go to breowse collections
#all breads tehre
# im there, I cant type for shti <=== see
#lol
#now we gotta intergrate it. pull data from db then write that data to a json so the dev can use it
#ye

# sacred chat of troubleshooting and debugging ^^^
#lol

#####################################
# NOTES:                            #
# Clust. Name:      Cluster0        #
# Database Name:    breadapi        #
# Collection Name:  breads          #
# DB and Col. Name: breadapi.breads #
#####################################


db = client["breadapi"]
breads = db["breads"]



def putBread(name,desc,image,id=None):  # I added baguette, oui oui, nice 
  last_doc = breads.find_one(sort=[("_id", pymongo.DESCENDING)])
  post = {
    "_id":int(last_doc["_id"]) + 1,
    "name":name,
    "desc":desc,
    "image":image,
    "rating":0
    }
  if breads.find_one({"name":post["name"]}) is not None:
    failed = {"success":False,"error":"bread already exists"}
    return failed
  if len(desc.split(" ")) < 5:
    return {"success":False,"error":"description too small"}
  breads.insert_one(post)
  post["success"]=True
  return post

def get(name=None):
  if name is None:
    cursor = breads.aggregate([{"$sample": {"size": 1}}])
    bread = list(cursor)
    return bread[0]
    #ayyyyy
    #les go, ima test bread cmd
    #nice
  else:
    bread = breads.find_one({"name":name})
    if bread is not None:
      return bread
    return {"name": "not found :o"}
    #it works :o

def vote(name):
  breadtovote = get(name=name)
  if "name" in breadtovote:
    breadtovote["rating"] += 1.0
    breads.replace_one({"name":name},breadtovote)
    breadtovote["success"]= True
    return breadtovote
  else:
    return breadtovote

def leaderboard(order="1"):
  if order == "-1":
    bread = breads.find().sort("rating",pymongo.DESCENDING)   
  elif order == "1":
    bread =breads.find().sort("rating",pymongo.ASCENDING)
  return list(bread)


