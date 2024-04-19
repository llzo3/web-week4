from fastapi import FastAPI

import requests

app = FastAPI()

@app.get("/")
def root():
    URL = "https://bigdata.kepco.co.kr/cmsmain.do?scode=S01&pcode=000167&pstate=L&redirect=Y"

    contents = requests.get(URL).text

    return { "message": contents }

@app.get("/home")
def home():
    return { "message": "Home!" }

