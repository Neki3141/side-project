import sys
import requests
import PyQt5

def get_weather(city_name):
    api_key = "5796abbde9106b7da4febfae8c44c232"
    #api_key = "abc36dc69136175b3de204c7fcc57eb6"
    city = city_name
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"


    try:    
        # This line sent the link into internet
        respone = requests.get(url)
        # This line try to capture HTTPError for except because default python dont have it exception
        respone.raise_for_status()
        # This line recieve the respone from the sever and extract json format
        data = respone.json()
        return data
    except requests.HTTPError:
        print("City not found")
    except requests.RequestException:
        print("Bad connection") 
    return None


def print_result(data):
    # Data have 2 levels of dictionary, first level is main and 2nd is temp
    temp = data["main"]["temp"]
    print(f"Temperature is: {temp} Celsius")




def main():
    while True:
        city = input("Enter city for cheking temp: ")
        data = get_weather(city)
        if data != None:
            break
                                        
    print_result(data)
        


if __name__ == "__main__":
    main()