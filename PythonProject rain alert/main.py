api_key = "b6e4727e9c59bb2d5f00641d5dd5ed77"
import requests,os

parameters = {

    "q"    : "Thoothukudi",
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
    elif will_rain==False:
        print("it's cloudy today 🌥️ !")
        break