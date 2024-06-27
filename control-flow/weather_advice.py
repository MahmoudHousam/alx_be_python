def detect_weather():
    weather_dict = {
        "sunny": "Wear a t-shirt and sunglasses.",
        "rainy": "Don't forget your umbrella and a raincoat.",
        "cold": "Make sure to wear a warm coat and a scarf.",
    }

    weather_input = input("What's the weather like today? (sunny/rainy/cold): ")
    if weather_input == "sunny":
        print(weather_dict["sunny"])
    elif weather_input == "rainy":
        print(weather_dict["rainy"])
    if weather_input == "cold":
        print(weather_dict["cold"])
    else:
        print("Sorry, I don't have recommendations for this weather.")


if __name__ == "__main__":
    detect_weather()
