FROM python
RUN pip install fastapi
RUN pip install pymongo
RUN pip install uvicorn
RUN pip install pydantic
RUN pip install numpy
RUN pip install requests
RUN pip install motor
RUN pip install "pymongo[srv]"
RUN pip install  pytest==7.1.0
RUN pip install --upgrade pytest
COPY ./backendSortingAlgo.py .
COPY ./test_sorting_algo.py .
COPY ./database.py .


CMD ["uvicorn", "backendSortingAlgo:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]



