import motor.motor_asyncio
import pymongo
from fastapi import FastAPI
from backendSortingAlgo import Result

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://user:pass@database:27017')
database = client.SavedResults
collection = database.SeeYourAlgo

async def CreateResult(request):
    await collection.insert_one(request)
    return request

async def ClearAllResults():
    collection.drop()

async def GetAllDataFromSavedResults():
    allResults = []
    all = collection.find({})
    async for doc in all:
        allResults.append(Result(**doc))
    return allResults
