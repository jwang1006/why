import requests, datetime, time

MY_LAT = 51.5
MY_LONG = -0.1

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

def isDark():
    try:
        response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
        response.raise_for_status()  # Raise an exception for 4XX/5XX status codes
        data = response.json()
        sunsetHour = int(data["results"]["sunset"].split("T")[1].split(":")[0])
        sunriseHour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
        currentHour = datetime.now().hour
        if currentHour<sunriseHour or currentHour>sunsetHour:
            return True
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)

def isOverhead():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    position = response.json()["iss_position"]
    longitude = float(position["longitude"])
    latitude = float(position["latitude"])
    if abs(longitude-MY_LONG)<5 and abs(latitude-MY_LAT)<5:
        return True

def shouldSendEmail():
    if isOverhead() and isDark():
        print("Send email!")
        # should be replaced with email code (but i haven't learned yet)

if __name__=="__main__":
    while True:
        shouldSendEmail()
        time.sleep(60)
        