from fastapi import FastAPI
from fastapi.testclient import TestClient   
from backendSortingAlgo import app
import numpy

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"massage" :"Welcome to the SeeYourAlgo place where you can see with your own eyes the most beautiful algorithms in the world, and their running efficiency."}
    
def test_sorting_page():
    response = client.get("/sorting")
    assert response.status_code == 200
    assert response.json() == {"massage":"Please select the algo that you want to see, also enter a lenght of arrayPlease select the algorithm you would like to view and analyze its runtime and the lenght of the array."}
     
#Sorting/SeeAlgo/?NameOfAlgo=BubbleSort&LenghtOfArray=9
def test_sorting_bubblesort():
    response = client.get("/Sorting/SeeAlgo/?NameOfAlgo=BubbleSort&LenghtOfArray=9")
    assert response.status_code == 200
    
#Sorting/SeeAlgo/?NameOfAlgo=HeapSort&LenghtOfArray=9
def test_sorting_heapsort():
    response = client.get("/Sorting/SeeAlgo/?NameOfAlgo=HeapSort&LenghtOfArray=9")
    assert response.status_code == 200

#Sorting/SeeAlgo/?NameOfAlgo=QuickSort&LenghtOfArray=9
def test_sorting_quicksort():
    response = client.get("/Sorting/SeeAlgo/?NameOfAlgo=QuickSort&LenghtOfArray=9")
    assert response.status_code == 200
    
#Sorting/SeeAlgo/?NameOfAlgo=SelectionSortSort&LenghtOfArray=9
def test_sorting_selectionSortsort():
    response = client.get("/Sorting/SeeAlgo/?NameOfAlgo=SelectionSort&LenghtOfArray=9")
    assert response.status_code == 200

def test_data_structur():
    response = client.get("/DataStructur")
    assert response.status_code == 200
    assert response.json() == {"massage":"When the DB implementation phase arrives, it will be possible to save results in a special place for this purpose, for future user comparison andto delete  them"}

def test_dynamic_programing():
    response = client.get("/DynamicPrograming")
    assert response.status_code == 200
    assert response.json() == {"massage":"When the DB implementation phase arrives, it will be possible to save results in a special place for this purpose, for future user comparison andto delete  them"}
