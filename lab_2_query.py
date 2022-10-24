import pandas as pd
import sqlite3
con = sqlite3.connect("railway_ticket")
cursor = con.cursor()
# вывести пассажиров и их билеты, результат отсортировать по скидке по возрастанию 
df = pd.read_sql(f'''
                SELECT full_name, timetable_id, train_car_number, train_boarding_date, seat_id, discount  
                FROM ticket
                JOIN passenger USING (passenger_id)
                JOIN discount USING (discount_id)
                ORDER BY discount;
                ''', con)
print(df, '\n', '--------------------------------------------')

# вывести номера поездов их тип и рассписание результат отсортировать по номеру поезда
df = pd.read_sql(f'''
                SELECT train_number, train_type, departure_station_name, arrival_station_name, departure_date, departure_time, days_on_the_road, arrival_time  
                FROM timetable
                JOIN train USING (train_number)
                JOIN departure_station USING (departure_station_id)
                JOIN arrival_station USING (arrival_station_id)
                ORDER BY train_number;
                ''', con)
print(df, '\n', '--------------------------------------------')

# вывести количество пассажиров на каждом поезде
df = pd.read_sql(f'''
                SELECT train_number, count(passenger_id)  
                FROM ticket
                JOIN timetable USING (timetable_id)
                JOIN train USING (train_number)
                JOIN passenger USING (passenger_id)
                GROUP BY train_number;
                ''', con)
print(df, '\n', '--------------------------------------------')

# вывести среднюю цену билета для каждого поезда
df = pd.read_sql(f'''
                SELECT train_number, AVG(price)  
                FROM seat
                JOIN timetable USING (timetable_id)
                JOIN train USING (train_number)
                GROUP BY train_number;
                ''', con)
print(df, '\n', '--------------------------------------------')

# вывести все билеты средняя цена которых выше 2600
df = pd.read_sql(f'''
                SELECT train_number, full_name, timetable.timetable_id, train_car_number, train_boarding_date, seat_number, discount, mean_price  
                FROM ticket
                JOIN passenger USING (passenger_id)
                JOIN timetable USING (timetable_id)
                JOIN train USING (train_number)
                JOIN seat USING (seat_id)
                JOIN discount USING (discount_id)
                JOIN (SELECT train_number, AVG(price) as mean_price 
                    FROM seat
                    JOIN timetable USING (timetable_id)
                    JOIN train USING (train_number)
                    GROUP BY train_number) USING (train_number)
                WHERE mean_price > 2600;
                ''', con)
print(df, '\n', '--------------------------------------------')

# вывести номера поездов на которых едут 3 пассажира
df = pd.read_sql(f'''
                SELECT train_number, count_passenger
                FROM(SELECT train_number, count(passenger_id) as count_passenger  
                    FROM ticket
                    JOIN timetable USING (timetable_id)
                    JOIN train USING (train_number)
                    JOIN passenger USING (passenger_id)
                    GROUP BY train_number)
                WHERE count_passenger >= 3;
                ''', con)
print(df, '\n', '--------------------------------------------')

# удалить заранее определенного пассажира
full_name = "'Иванов Иван Иванович'"
df = pd.read_sql(f'''
                SELECT full_name
                From passenger
                WHERE full_name == {full_name}
                ''', con)
print(df, '\n', '--------------------------------------------')

cursor.executescript(f'''
                        DELETE FROM passenger
                        WHERE full_name == {full_name}
                    ''')

df = pd.read_sql(f'''
                SELECT full_name
                From passenger
                WHERE full_name == {full_name}
                ''', con)
print(df, '\n', '--------------------------------------------')

# удалить все поезда на которых ехали 3 пассажира
cursor.executescript(f'''
                        DELETE FROM train
                        WHERE train_number == (SELECT train_number 
                            FROM ticket
                            JOIN timetable USING (timetable_id)
                            JOIN train USING (train_number)
                            JOIN passenger USING (passenger_id)
                            GROUP BY train_number) 
                    ''')
