from weather_classes_and_functions import *


def menu():
    while True:
        print("1. Get current weather conditions")
        print("2. Get a 10-day forecast")
        print("3. Get sunrise and sunset times")
        print("4. Get weather alerts")
        print("5. Get all hurricanes")
        print("6. quit")
        choice = int(input())
        if 1 <= choice <= 6:
            return choice


def main():
    cont = True
    while cont:
        choice = menu()
        if choice == 1:
            print_current_conditions(CurrentConditions, response)
        elif choice == 2:
            print_10_day_forecast(ForecastDay, Forecast10Day, response)
        elif choice == 3:
            print_sunrise_sunset(SunriseSunset, response)
        elif choice == 4:
            print_alert(Alert, response)
        elif choice == 5:
            print_hurricanes(Hurricane, response)
        else:
            cont = False


main()
