import requests
from datetime import datetime
#Link: https://spotthestation.nasa.gov/tracking_map.cfm    
MY_LAT = 25.612677
MY_LONG = 85.158875
try:
    response = requests.get(url = "http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    now_time = datetime.now()
    now_time = str(now_time)[:-7]  #removing microsecond part
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        text = f"Time now is {now_time}, iss latitude is {iss_latitude} and iss longitude is {iss_longitude}"
    else:
        text = f"{now_time}  --------------"
except requests.exceptions.ConnectionError:
    # print("Error Caught")
    now_time = datetime.now()
    now_time = str(now_time)[:-7]  #removing microsecond part
    text = f"{now_time} Internet connection not available"
finally:
    # print("inside finally")
    with open('D:/Python files/ISS/iss_data.txt','a') as f:
        f.write(text + "\n")
