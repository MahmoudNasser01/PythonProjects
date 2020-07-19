import requests
import json
import pyttsx3
import speech_recognition as sr
import re
from gtts import gTTS
import os
API_KEY = "tPKXx7YFT7ay"
PROJECT_TOKEN = "t0c_9hfQjsKY"
RUN_TOKEN = "taVrrDTiwts9"





class Data:
    def __init__(self,api_key , project_token):
        self.api_key = api_key
        self.project_token = project_token
        self.params = {
            "api_key":self.api_key
        }
        self.get_data()

    def get_data(self):
        response = requests.get(f'https://www.parsehub.com/api/v2/projects/{PROJECT_TOKEN}/last_ready_run/data',
                                params={"api_key": API_KEY})
        self.data = json.loads(response.text)

    def get_total_cases(self):
        data = self.data['total']
        for content in data:
            if content['name'] == "Coronavirus Cases:":
                return content['value']
    def get_total_deaths(self):
        data = self.data['total']
        for content in data:
            if content['name'] == "Deaths:":
                return content['value']
    def get_total_recovers(self):
        data = self.data['total']
        for content in data:
            if content['name'] == "Recovered:":
                return content['value']
    def get_country_data(self , country):
        data = self.data['country']
        for content in data:
            if content['name'].lower() == country.lower():
                return content
        return "0"

data = Data(API_KEY ,PROJECT_TOKEN )
country_name = input('Enter Your Country Name: ')
dic = data.get_country_data(country_name)
cases = dic.get('total_cases')
deaths = dic.get('total_deaths')
speech = f"the total cases in {country_name} is {cases} and the total deaths is {deaths}"
output = gTTS(text=speech, lang='en', slow=False)
output.save('output.mp3')
os.system('start output.mp3')



########Speeach recognizer








