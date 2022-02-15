# Bootstrap application to setup Fast API services with Azure Cosmos DB backend.

## Background
The aim is to bring together my learnings from python design patterns and setup a FastAPI service backed with cosmos DB. 
This project will help to bootstrap a backend development environment with FastAPI. 
You are encouraged to contribute to this project with your learning and pythonic best practices .

## Setup
### Create you virtual environment
- Create folder where you want to have your virtual environment hosted:    ```mkdir ~/.virtualenvs/AzureFastApiServices```
- Create virtual environment using the command :  ```virtualenv  ~/.virtualenvs/AzureFastApiServices```
- Activate your virtual environment: ```source  ~/.virtualenvs/AzureFastApiServices/bin/activate```

### Install dependencies
- Install all your project dependencies into your virtual environment . From the root of your virtual environment folder execute   ```pip install -r requirements.txt```
  
### To Start the applicaiton 
- Update your Azure credentials under ```resources>config.py```
- Set VSCode use the python interepereter of your virtual environment. 
- execute : ```python main.py```