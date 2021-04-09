def weather(city):
    import requests
    import json
    api_key = "c49d5fad8d3683e31e7da6860efd3063"
    service = "https://api.openweathermap.org/data/2.5/weather"
    req = requests.get(f'{service}?q={city}&appid={api_key}&lang=ru')
    data = json.loads(req.text)
    temp = f"В городе {data['name']} {data['weather'][0]['description']}, {data['main']['temp']} градусов по Кельвину"
    return temp


print(weather(input("Type your city: ")))

