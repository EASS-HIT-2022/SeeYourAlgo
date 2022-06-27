# RonOfir-EX1-SeeYourAlgo
Welcome to **SeeYourAlgo**

# Some background:
During my degree studies in computer science I began to really like the analysis of algorithms and their logic, even the mathematical side.
During my studies I realized that there is nothing better to learn an algorithm, than to see it run, visually, at the speed I choose, with an explanation of the steps, then when we look at the code it will be much much simpler!
Another thing, over time, with today's technology, I began to ask myself, is it really possible to analyze the running time analysis that we are taught (even in the worst case)?
For that matter, we are all familiar with the bubble sort sorting algorithm, we also know in its worst case the runtime is o (n ^ 2), but given a random array, **does it really happen**?
From what I've been able to check out so far, no!
I ran the algorithm hundreds of times on different random inputs and never got close to n ^ 2, ever!
I really do not disagree with math, nor can I. I just want to show you that with technology, processors, and statistics, what we have learned may not necessarily come true, so, maybe we should treat the term runtime a little differently?
**I am not going to answer this question because it is subject to complex analysis, but please, think about it**.


The system **SeeYourAlgo**
Please provide us with two main things:
The ability to visually observe the algorithm during its run.
2. Running Run Time Analysis **(When I say run time analysis I mean the number of comparisons performed and the number of swaps performed - as befits comparative sorting algorithms)**.



**important information:**

In the future, the system (WBA) will support three issues:
1. Sorting algorithms
2. Data structures
3. Dynamic programming

## Currently, for the project in the course "Advanced Software Solutions Engineering" only the subject of sorting algorithms will be available, both front and back.


# Using the system:

**Server side:**
In the first part of the task, only the server side is implemented (with DB).
This is how we will use it.
Once we've run all the files, we can go into fastapi's swagger and there see the bids of the requests before us.


![image](https://user-images.githubusercontent.com/48864890/164219573-b0228faa-f6f3-4aea-8ba6-d9e1fe24d5e7.png)


where what's relevant to us is the request to:

![image](https://user-images.githubusercontent.com/48864890/164219766-bc280aef-59fc-4cdc-892d-0db4fe243ae0.png)

The rest of the requests are for the client side and for saving and deleting the results (which as I have already written this will be implemented in the part of the DB).

The request is structured in such a way that we need to provide it with two query parameters:
1. Sorting algorithm name - must be a string
When at the current stage the options are:

    1. HeapSort
    2. QuickSort
    3. BubbleSort
    4. SelectionSort
2. Array size - must be int
**Please note: Other names of algorithms will not be accepted into the program - the names of the algorithms should be written exactly as I wrote here.
**

## It is important to note - in terms of visualization - the system can currently only deal with arrays.


After the run, the correct answer we will get will consist of 3 parts:
1. Run time (comparison operations + replacement operations)
2. The array before sorting
3. The array after sorting


![image](https://user-images.githubusercontent.com/48864890/164220999-f11c233c-9087-4f06-a584-930d1e3d65c2.png)
![image](https://user-images.githubusercontent.com/48864890/164221067-c5d99cfe-359e-4a33-83d9-24a79598133e.png)



As I have already written, in this project only the part of the sort will be available, the data structures and dynamic programming will be added in the future.

![image](https://user-images.githubusercontent.com/48864890/164221748-85543c14-686c-432b-b8b7-2d07fbf4a00b.png)



## Please pay attention!!!
## If you typed the name of an incorrect algorithm, do not make a "paste copy" of the message you received in swagger, but write the name of the  ## algorithm yourself in the text box.
![image](https://user-images.githubusercontent.com/48864890/164223599-129ed55f-3636-4946-bc34-84069dd76701.png)




# Examples of running algorithms:
Heap sort : 

![image](https://user-images.githubusercontent.com/48864890/164225252-39050585-379f-4ebb-9f11-dcc04df5e1f6.png)

![image](https://user-images.githubusercontent.com/48864890/164225862-56232326-41fe-466d-a88e-21183b0276c9.png)


Selection sort :

![image](https://user-images.githubusercontent.com/48864890/164226006-5a0b9897-4121-423f-b336-c9544bb7fde7.png)

![image](https://user-images.githubusercontent.com/48864890/164226045-b04d1553-e835-4a77-a9ee-4075f06f7250.png)


Bubble sort : 

![image](https://user-images.githubusercontent.com/48864890/164226121-51e3dee5-9cc6-49fd-baa2-857daedc4e9f.png)

![image](https://user-images.githubusercontent.com/48864890/164226160-14b0fffd-ee6f-4139-99ea-17720c31e20a.png)


Quick  sort : 

![image](https://user-images.githubusercontent.com/48864890/164226221-40e86cda-ab84-4af7-bb93-2bd7865fb1e0.png)

![image](https://user-images.githubusercontent.com/48864890/164226260-e382356f-a9ab-47af-80f7-5a41ad51b64e.png)


## DB - MongoDB
This project uses DB in several ways:
1. Save a specific result
2. Get all the results (on the designated screen)
3. Delete all saved results

I use MONGODB, as you can see.
Using MONGO is very convenient, very JSON! :)

![image](https://user-images.githubusercontent.com/48864890/165379026-baf86251-8294-4656-a4b2-55783bac32ae.png)


You can add a record to the result as follows:
![image](https://user-images.githubusercontent.com/48864890/165379569-c728df56-572c-4880-88e4-3b21604a588b.png)

It is very simple and very convenient, especially with the relevant luxuries that Python offers (motor.motor_asyncio \ pymongo)



## To make it easier for the user I opened with my user (with the user and password) the access to all the IP addresses so all you need is MONGO installed on the computer so you can use the program, so, do not change anything for running the project

In the future (if you want it locally, and in your DB)
--
For the DB connection, note that you are setting up your own connection, and actually changing this line before you run the project.
You need to install Mongodb on your computer, log in to the site and make a connection accordingly.
--
---- connction string to ypur db ---- 




For the testing i use 'pytest' and 'testclient' platform 
this is the results for the tests i wrote:

![image](https://user-images.githubusercontent.com/48864890/164978664-161da985-7ccd-43be-b6a1-9a8a84e1dc8b.png)




So, to run the project you need to have Docker on your computer; toy to build the container and run it.
after that ypu download the docker:
1. 'docker build . -t ron-ex1'
2. 'docker run -p8080:8080 ron-ex1'
3. To see the swagger on ypur browser:
'localhost:8080/docs'

# important comments:
* Play with the system, you will see for example that in the quick sort algorithm (for example) even though its maximum runtime is n ^ 2, no matter how many times you run the algorithm you will never know n ^ 2.


* It is important for me to note, if you encounter a problem, difficulty understanding how the system works, difficulty understanding the result or anything else, please write to me in the personal email: ronofir97@gmail.com



