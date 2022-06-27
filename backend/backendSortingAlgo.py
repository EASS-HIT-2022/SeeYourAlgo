import errno
from urllib import request
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
import numpy
from numpy import random
import uvicorn 
import pytest
from fastapi.testclient import TestClient
import requests
from fastapi.middleware.cors import CORSMiddleware
import json


app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Result(BaseModel):
    Name_Of_Algo:str
    Number_Of_Actions:str
    Array_Befor_Sort:str
    Array_After_Sort:str

from database import (
    CreateResult,
    ClearAllResults,
    GetAllDataFromSavedResults
)

# function and global counter for quick sort algo 
counterOfQuickSort = 0
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot_idx = len(arr) // 2
    smaller, larger = [], []
    for idx, num in enumerate(arr):
        if idx != pivot_idx:
            global counterOfQuickSort
            counterOfQuickSort += 1
            (larger, smaller)[num < arr[pivot_idx]].append(num)
    return quicksort(smaller) + [arr[pivot_idx]] + quicksort(larger)


def QuickSort(LenghtOfArray):
    arrQ = random.randint(100, size=(LenghtOfArray))
    copyarrQ = arrQ.copy()
    quicksort(arrQ)
    global counterOfQuickSort
    counterQ = counterOfQuickSort
    counterOfQuickSort = 0
    return counterQ, arrQ, copyarrQ

def BubbleSort(LenghtOfArray):
    arrB = random.randint(100, size=(LenghtOfArray))
    copyarrB = arrB.copy()
    counterB = 0
    for i in range(LenghtOfArray-1):
        for j in range(0, LenghtOfArray-i-1):
            counterB += 1
            if arrB[j] > arrB[j + 1] :
                counterB += 1       
                arrB[j], arrB[j + 1] = arrB[j + 1], arrB[j]
    return counterB, arrB, copyarrB

def SelectionSort(LenghtOfArray):
    arrS = random.randint(100, size=(LenghtOfArray))
    copyarrS = arrS.copy()
    counters = 0
    for step in range(LenghtOfArray):
        min_idx = step
        for i in range(step + 1, LenghtOfArray):
            counters += 1
            if arrS[i] < arrS[min_idx]:
                min_idx = i
                counters += 1
        (arrS[step], arrS[min_idx]) = (arrS[min_idx], arrS[step])
    return counters, arrS,copyarrS

def HeapSort(LenghtOfArray):
    arrH = random.randint(100, size=(LenghtOfArray))
    copyarrH = arrH.copy()
    countH = 0
    for i in range(LenghtOfArray, -1, -1):
        heapify(arrH, LenghtOfArray, i)  
        countH += heapify(arrH, i, 0)
    for i in range(LenghtOfArray-1, 0, -1):
        arrH[i], arrH[0] = arrH[0], arrH[i] 
        countH += heapify(arrH, i, 0)
    return countH, arrH, copyarrH

# heapify function for the heap sort algo
def heapify(arr, n, i):
    count = 0
    largest = i  
    l = 2 * i + 1     
    r = 2 * i + 2     
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        count += 1
        arr[i],arr[largest] = arr[largest],arr[i]
        count += heapify(arr, n, largest)
    return count

@app.get("/")
def HomePage():
    return {"massage" :"Welcome to the SeeYourAlgo place where you can see with your own eyes the most beautiful algorithms in the world, and their running efficiency."}


@app.get("/sorting")
def SortingPage():
    return {"massage":"Please select the algo that you want to see, also enter a lenght of arrayPlease select the algorithm you would like to view and analyze its runtime and the lenght of the array."}

@app.get("/Sorting/SeeAlgo/")
#Here we get the name of the algo and the lenght of the array from the cilent 
def SeeAlgoByNameAndLenghtFromClient(NameOfAlgo:str, LenghtOfArray:int):
    if NameOfAlgo == "HeapSort":
        r1h, r2h,r3h =  HeapSort(LenghtOfArray)
        print({"Number of actions performed" : r1h, "The array befor the sorting":r3h.tolist(), "The array after the sorting":r2h.tolist() })
        return {"Number of actions performed" : r1h, "The array befor the sorting":r3h.tolist(), "The array after the sorting":r2h.tolist() }
        
    if NameOfAlgo == "QuickSort":
        r1q, r2q,r3q =  QuickSort(LenghtOfArray)
        return {"Number of actions performed" : r1q, "The array befor the sorting":r3q.tolist(), "The array after the sorting":r2q.tolist() }
        
    if NameOfAlgo == "BubbleSort":
        r1b, r2b,r3b =  BubbleSort(LenghtOfArray)
        return {"Number of actions performed" : r1b, "The array befor the sorting":r3b.tolist(), "The array after the sorting":r2b.tolist() }
    
    if NameOfAlgo == "SelectionSort":
        r1s, r2s,r3s =  SelectionSort(LenghtOfArray)
        return {"Number of actions performed" : r1s, "The array befor the sorting":r3s.tolist(), "The array after the sorting":r2s.tolist() }

    if NameOfAlgo != ("HeapSort", "QuickSort", "BubbleSort", "SelectionSort"):
        raise HTTPException(status_code=404, detail="Sorry, currently supported algorithms are: HeapSort / QuickSort / BubbleSort / SelectionSort ")
        return "Sorry, currently supported algorithms are: HeapSort / QuickSort / BubbleSort / SelectionSort "

@app.get("/DataStructur")
def DataStructurPage():
    return {"massage":"When the DB implementation phase arrives, it will be possible to save results in a special place for this purpose, for future user comparison andto delete  them"}

@app.get("/DynamicPrograming")
def DynamicProgramingPage():
    return {"massage":"When the DB implementation phase arrives, it will be possible to save results in a special place for this purpose, for future user comparison andto delete  them"}

@app.delete("/ClearSavedResults")
async def ClearSavedResults():
    await ClearAllResults()
    return {"massage": "The results deleted"}

@app.post("/SaveResult")
async def SaveResult(request: Result):
    await CreateResult(request.dict())
    return ({"messege": "The result saved succesfully" , "data" : request.dict()})


@app.get("/GetAllSavedResults")
async def GetAllResults ():
    response = await GetAllDataFromSavedResults()
    return response