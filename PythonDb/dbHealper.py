import sqlite3 as db
# Проверка наличия в базе информации о нужном населенном пункте

from datetime import date
from WeatherApi import request_current_weather, get_city_id

def print_from_data(data):
    format = input("Введите в каком виде вывести температура: \n"
                   "Фаренгейт напишите - F\n"
                   "Кельвин напишите - K\n"
                   "Цельсий напишите - что угодно или ничего\n")
    try:
       if format == 'K':
            for iterator in data:
                print(f"Id: {iterator[0]}, Город: {iterator[1]}, Температура: {iterator[2] + 273.15} K, Температура мин: {iterator[3] + 273.15} K, Температура макс: {iterator[4] + 273.15} K, Ощущается как: {iterator[7] + 273.15} K,"
                f"Давление: {iterator[5]} мм рт.ст, Влажность: {iterator[6]} %, Сила ветра: {iterator[8]} м/с, Дата запроса: {iterator[9]}, Описание: {iterator[10]}")
       elif format == 'F':
            for iterator in data:
                print(
                    f"Id: {iterator[0]}, Город: {iterator[1]}, Температура: {iterator[2] * 1.8 + 32} F, Температура мин: {iterator[3] * 1.8 + 32} F, Температура макс: {iterator[4] * 1.8 + 32} F, Ощущается как: {iterator[7]* 1.8 + 32} F,"
                    f"Давление: {iterator[5]} мм рт.ст, Влажность: {iterator[6]} %, Сила ветра: {iterator[8]} м/с, Дата запроса: {iterator[9]}, Описание: {iterator[10]}")
       else:
            for iterator in data:
                print(
                    f"Id: {iterator[0]}, Город: {iterator[1]}, Температура: {iterator[2]} °C, Температура мин: {iterator[3]} °C, Температура макс: {iterator[4]} °С, Ощущается как: {iterator[7]} °С,"
                    f"Давление: {iterator[5]} мм рт.ст, Влажность: {iterator[6]} %, Сила ветра: {iterator[8]} м/с, Дата запроса: {iterator[9]}, Описание: {iterator[10]}")

    except Exception as e:
        print("Exception:", e)
        pass

def create_table(cu, conn):
    try:

        cu.execute("""
            CREATE TABLE weather (
                id INTEGER primary key,
                city VARCHAR(50),
                temp FLOAT,
                temp_min INTEGER,
                temp_max INTEGER,
                pressure INTEGER,
                humidity INTEGER,
                feels_like FLOAT,
                wind_speed INTEGER,
                creation_date DATE, 
                condition VARCHAR(100)
              );
              """)
    except db.DatabaseError:
        print('Ошибка')


def add_weather(cu, conn):
    today = date.today()

    cityName = input(
        "Введите имя города коректно на английском языке: ")  ## Сюда название города London, Nur-Sultan, Moscow, Karagandy
    city_id = get_city_id(cityName)

    data = request_current_weather(city_id)
    cu.execute(f"""
    INSERT INTO weather (city, temp, temp_min, temp_max, pressure, humidity, feels_like, wind_speed, creation_date, condition)
    VALUES ('{cityName}', {data['main']['temp']}, {data['main']['temp_min']}, {data['main']['temp_max']}, {data['main']['pressure']}, {data['main']['humidity']}, {data['main']['feels_like']},
    {data['wind']['speed']}, {today}, '{data['weather'][0]['description']}')
    """)
    conn.commit()


