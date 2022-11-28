import requests
import tkinter as tk
import json

from PIL import Image
from io import BytesIO



def weatherCity():
    city = input("Enter the city name: ")
    print("\n")

    payload = {
            "q": f'{city}',
            "limit": '1', 
            "appid": '5c6819dda727a6d90f49cb484b1609cb'
            }

    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather', params=payload)
    response = response.json()

    print(f'City weather {city}: ' + "\n")
    print("Main: " + response["weather"][0]["main"])
    print("Description: " + response["weather"][0]["description"])
    print("Pressure: " + str(response["main"].get("pressure")) + " hPa")
    print("Humidity: " + str(response["main"].get("humidity")) + " %") 



def get_statistics():
    print("____________ Statistics ____________")

    dateFrom = input("Enter start date: ")
    dateTo = input("Enter the end date: ")
    # YYYY-MM-DD
    page = int(input("Enter the page number: "))
    # 0,1,2,...
    print("\n")

    url = f'https://www.cbr.ru/statistics/AllEvents/?page={page}&IsEng=true&dateFrom={dateFrom}&dateTo={dateTo}&Tid=145%2C187%2C189%2C188%2C191%2C190&phrase=&_=1669658619524'
    response = requests.get(url)
    data = response.json()

    print("____________ Found results ___________")
    print("\n")

    for new_data in data:
        print(new_data["dtupd"] + ': ' + new_data["name_doc"].strip())
    
    


def cat_image():
    def Show_img():
        url = 'https://aws.random.cat/meow'
        response = requests.get(url)
        data = response.json()
        file_url = data['file']
        
        file = requests.get(file_url)
        file_content = file.content
        
        image = Image.open(BytesIO(file_content))
        image.show()
        
    def Cancel():
        main.destroy()


    main = tk.Tk()
    main.title(" cat image ")
    main.geometry('300x300')
         
    button = tk.Button(main, text='Next', font=("Times New Roman", 15), bg="black", fg="cyan", command=Show_img)
    button.place(x=70, y=100)

    exit = tk.Button(main, text='Exit', font=("Times New Roman", 15),bg="black", fg="cyan", command=Cancel)
    exit.place(x=170, y=100)

    main.mainloop()


print("=========== REQUEST 1 ============")
weatherCity()
print("\n")
print("=========== REQUEST 2 ===========")
print("\n")
get_statistics()
print("\n")
print("========== ADDITIONAL ==========")
cat_image()