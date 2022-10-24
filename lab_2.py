import sqlite3
con = sqlite3.connect("railway_ticket")
cursor = con.cursor()
cursor.executescript('''
                    CREATE TABLE IF NOT EXISTS arrival_station(
                        arrival_station_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        arrival_station_name VARCHAR(30)
                    );

                    INSERT INTO arrival_station (arrival_station_name)
                    VALUES
                    ('Бира'),
                    ('Биракан'),
                    ('Биробиджан'),
                    ('Хабаровск'),
                    ('Завитая'),
                    ('Владивосток'),
                    ('Уссурийск'),
                    ('Белогорск'),
                    ('Благовещенск'),
                    ('Чита'),
                    ('Омск'),
                    ('Новосибирск'),
                    ('Красноярск'),
                    ('Тверь'),
                    ('Москва');
                    
                    
                    CREATE TABLE IF NOT EXISTS train(
                        train_number INTEGER PRIMARY KEY,
                        train_type VARCHAR(20)
                    );

                    INSERT INTO train (train_number, train_type)
                    VALUES
                    (15, 'Скоростной'),
                    (10, 'Скорый'),
                    (1, 'Пассажирский'),
                    (16, 'Скоростной'),
                    (14, 'Скорый'),
                    (13, 'Скоростной'),
                    (12, 'Пассажирский'),
                    (11, 'Скоростной'),
                    (9, 'Скорый'),
                    (8, 'Пассажирский'),
                    (7, 'Скорый'),
                    (6, 'Скоростной'),
                    (5, 'Скорый'),
                    (4, 'Скоростной'),
                    (3, 'Пассажирский'),
                    (2, 'Скорый');

                    CREATE TABLE IF NOT EXISTS departure_station(
                        departure_station_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        departure_station_name VARCHAR(30)
                    );

                    INSERT INTO departure_station (departure_station_name)
                    VALUES
                    ('Хор'),
                    ('Бира'),
                    ('Биракан'),
                    ('Биробиджан'),
                    ('Хабаровск'),
                    ('Завитая'),
                    ('Владивосток'),
                    ('Уссурийск'),
                    ('Белогорск'),
                    ('Благовещенск'),
                    ('Чита'),
                    ('Омск'),
                    ('Новосибирск'),
                    ('Красноярск'),
                    ('Тверь'),
                    ('Москва');

                    CREATE TABLE IF NOT EXISTS passenger(
                        passenger_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        full_name VARCHAR(50),
                        passport_series VARCHAR(4),
                        passport_number VARCHAR(6)
                    );

                    INSERT INTO passenger (full_name, passport_series, passport_number)
                    VALUES
                    ('Иванов Иван Иванович', '0000', '000000'),
                    ('Иванов Иван Петрович', '0001', '000001'),
                    ('Иванов Иван Сергеевич', '0002', '000002'),
                    ('Иванов Иван Олегович', '0003', '000003'),
                    ('Иванов Иван Васильевич', '0004', '000004'),
                    ('Иванов Петр Иванович', '0005', '000005'),
                    ('Иванов Петр Петрович', '0006', '000006'),
                    ('Иванов Петр Сергеевич', '0007', '000007'),
                    ('Иванов Петр Олегович', '0008', '000008'),
                    ('Иванов Петр Васильевич', '0009', '000009'),
                    ('Иванов Сергей Иванович', '0010', '000010'),
                    ('Иванов Сергей Петрович', '0011', '000011'),
                    ('Иванов Сергей Сергеевич', '0012', '000012'),
                    ('Иванов Сергей Олегович', '0013', '000013'),
                    ('Иванов Сергей Васильевич', '0014', '000014'),
                    ('Иванов Олег Иванович', '0015', '000015'),
                    ('Иванов Олег Петрович', '0016', '000016'),
                    ('Иванов Олег Сергеевич', '0017', '000017'),
                    ('Иванов Олег Олегович', '0018', '000018'),
                    ('Иванов Олег Васильевич', '0019', '000019'),
                    ('Иванов Василий Петрович', '0020', '000020'),
                    ('Иванов Василий Иванович', '0030', '000021'),
                    ('Иванов Василий Сергеевич', '0040', '000022'),
                    ('Иванов Василий Олегович', '0050', '000023'),
                    ('Иванов Василий Васильевич', '0060', '000024'),
                    ('Петров Иван Иванович', '0070', '000025'),
                    ('Петров Иван Петрович', '0080', '000026'),
                    ('Петров Иван Сергеевич', '0090', '000027'),
                    ('Петров Иван Олегович', '0100', '000028');

                    CREATE TABLE iF NOT EXISTS discount(
                        discount_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        discount INTEGER
                    );

                    INSERT INTO discount (discount)
                    VALUES
                    (5),
                    (15),
                    (6),
                    (10),
                    (9),
                    (7),
                    (20),
                    (3),
                    (1),
                    (6),
                    (18),
                    (15),
                    (10),
                    (20);

                    CREATE TABLE IF NOT EXISTS train_car(
                        train_car_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        train_number INTEGER,
                        train_car_number INTEGER,
                        train_car_type VARCHAR(20),
                        amount_of_seats INTEGER,
                        FOREIGN KEY (train_number) REFERENCES train(train_number) ON DELETE CASCADE
                    );

                    INSERT INTO train_car (train_number, train_car_number, train_car_type, amount_of_seats)
                    VALUES
                    (1, 1, 'купе', 40),
                    (1, 2, 'плацкарт', 38),
                    (1, 3, 'плацкарт', 30),
                    (1, 4, 'купе', 20),
                    (1, 5, 'плацкарт', 10),
                    (1, 6, 'купе', 18),
                    (2, 1, 'купе', 40),
                    (2, 14, 'плацкарт', 17),
                    (2, 15, 'купе', 28),
                    (2, 16, 'плацкарт', 34),
                    (2, 17, 'люкс', 14),
                    (2, 18, 'купе', 4),
                    (2, 19, 'купе', 9),
                    (3, 1, 'купе', 19),
                    (3, 2, 'купе', 23),
                    (3, 3, 'купе', 34),
                    (10, 5, 'люкс', 7),
                    (10, 6, 'купе', 23),
                    (10, 7, 'купе', 34);

                    CREATE TABLE IF NOT EXISTS timetable(
                        timetable_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        departure_station_id INTEGER,
                        train_number INTEGER,
                        arrival_station_id INTEGER,
                        departure_date VARCHAR(20),
                        departure_time VARCHAR(20),
                        days_on_the_road INTEGER,
                        arrival_time VARCHAR(20),
                        FOREIGN KEY (departure_station_id) REFERENCES departure_station(departure_station_id) ON DELETE CASCADE,
                        FOREIGN KEY (train_number) REFERENCES train(train_number) ON DELETE CASCADE,
                        FOREIGN KEY (arrival_station_id) REFERENCES arrival_station(arrival_station_id) ON DELETE CASCADE
                    );

                    INSERT INTO timetable (departure_station_id, train_number, arrival_station_id, departure_date, departure_time, days_on_the_road, arrival_time)
                    VALUES
                    (1, 1, 1, '07.08.2022', '10:31', 3, '9:31'),
                    (2, 3, 15, '16.09.2022', '11:38', 1, '1:31'),
                    (2, 10, 14, '12.05.2022', '12:38', 2, '3:31'),
                    (2, 5, 15, '17.08.2022', '11:00', 2, '12:30'),
                    (3, 7, 10, '07.06.2022', '14:10', 2, '14:31'),
                    (4, 8, 9, '12.03.2022', '11:55', 3, '10:15');
                    
                    CREATE TABLE IF NOT EXISTS seat(
                        seat_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        timetable_id INTEGER,
                        seat_number INTEGER,
                        type_seat VARCHAR(20),
                        price REAL,
                        FOREIGN KEY (timetable_id) REFERENCES timetable(timetable_id) ON DELETE CASCADE
                    );

                    INSERT INTO seat (timetable_id, seat_number, type_seat, price)
                    VALUES
                    (1, 15, 'нижнее', 2500.00),
                    (1, 16, 'нижнее', 2500.00),
                    (2, 5, 'нижнее', 2450.00),
                    (2, 6, 'нижнее', 2450.00),
                    (2, 7, 'верхнее', 2340.50),
                    (2, 8, 'верхнее', 2340.50),
                    (2, 9, 'нижнее', 3500.00),
                    (2, 10, 'нижнее', 3500.00),
                    (2, 16, 'нижнее', 2450.00),
                    (2, 17, 'верхнее', 2450.00),
                    (2, 18, 'верхнее', 2340.50),
                    (2, 19, 'нижнее', 2340.50),
                    (2, 20, 'нижнее', 3500.00),
                    (2, 21, 'верхнее', 3200.50);

                    CREATE TABLE IF NOT EXISTS ticket(
                        ticket_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        passenger_id INTEGER,
                        timetable_id INTEGER,
                        seat_id INTEGER,
                        discount_id INTEGER,
                        train_car_number INTEGER,
                        train_boarding_date VARCHAR(20),
                        FOREIGN KEY (passenger_id) REFERENCES passenger(passenger_id) ON DELETE CASCADE,
                        FOREIGN KEY (timetable_id) REFERENCES timetable(timetable_id) ON DELETE CASCADE,
                        FOREIGN KEY (seat_id) REFERENCES seat(seat_id) ON DELETE CASCADE,
                        FOREIGN KEY (discount_id) REFERENCES discount(discount_id) ON DELETE CASCADE
                    );

                    INSERT INTO ticket(passenger_id, timetable_id, seat_id, discount_id, train_car_number, train_boarding_date)
                    VALUES
                    (1, 1, 1, 1,  2, '07.08.2022'),
                    (2, 1, 2, 2, 6, '07.08.2022'),
                    (3, 2, 3, 3, 1, '16.09.2022'),
                    (4, 2, 4, 3, 2, '16.09.2022'),
                    (5, 2, 5, 6, 3, '16.09.2022'),
                    (6, 3, 6, 10, 5, '12.05.2022'),
                    (7, 3, 7, 9, 6, '12.05.2022'),
                    (8, 3, 8, 10, 7, '12.05.2022');
                    ''')
