from dotenv import load_dotenv
import requests,os
load_dotenv()
api_key =os.getenv("API_KEY")

parameters = {

    "q"    : "Chennai",
    "appid": api_key,
    "cnt"  : 4
}
response = requests.get("https://api.openweathermap.org/data/2.5/forecast",params=parameters)
data = response.json()
will_rain=None
id_list = []
for x in range(0,4):
    id_num = data['list'][x]["weather"][0]["id"]
    id_list.append(id_num)
for i in id_list:
    if i<700:
        will_rain = True
    elif i>800:
        will_rain = False
    if will_rain==True:
        print("Rain alert⚠️! Bring an umbrella☔!")
        break
    elif will_rain==False:
        print("it's cloudy today 🌥️ !")
        break