#import 
import requests
from datetime import datetime , timedelta
import os 
import matplotlib.pyplot as plt
import pandas as pd


today=datetime.today()
week_ago=today-timedelta(days=7)


start_day=week_ago.strftime("%Y-%m-%d")
end_day=today.strftime("%Y-%m-%d")


latitude=input("Enter latitude: ")
longitude=input("Enter longitude: ")

url=f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&start_date={start_day}&end_date={end_day}&daily=temperature_2m_max,temperature_2m_min"

result=requests.get(url)
data=result.json()


daily=data["daily"]
df=pd.DataFrame({
    "date" : daily["time"] , 
    "max_temp":daily["temperature_2m_max"],
    "min_temp" : daily["temperature_2m_min"]
})


plt.figure(figsize=(10,6))
plt.plot(df["date"],df["max_temp"],marker="o",label="max_temp")
plt.plot(df["date"],df["min_temp"],marker="o",label="min_temp")
plt.title("temporateur max and min in algerie oran")  
plt.legend()
plt.xlabel("days")
plt.ylabel("temporateur")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("weather.png")
plt.show()

if not os.path.exists("weatherOran") :
    os.makedirs("weatherOran")
    
df.to_csv("weatherOran/weather.csv",index=False)
        
