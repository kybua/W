import sqlite3


class main:
    running = True
    while running:
        connection = sqlite3.connect('shows.db')
        cursor = connection.cursor()
        print("Здравствуйте, добро пожаловать на наш склад продуктов")
        print("1 список вкусняшек на складе")
        print("2 добавить товар на склад")
        arg = input("ваш ответ:")
        arg1 = int(arg)
        while True:
            if arg1 == 1:
                cursor.execute("SELECT * FROM shows")
                print(cursor.fetchall())
                print("Здравствуйте, добро пожаловать на наш склад продуктов")
                print("1 список вкусняшек на складе")
                print("2 добавить товар на склад")
                arg = input("ваш ответ:")
                arg1 = int(arg)
            if arg1 == 2:
                product = input('введите название товара:').split()
                cursor.execute("INSERT INTO shows (Title) VALUES (?)", product)
                connection.commit()
                print("Здравствуйте, добро пожаловать на наш склад продуктов")
                print("1 список вкусняшек на складе")
                print("2 добавить товар на склад")
                arg = input("ваш ответ:")
                arg1 = int(arg)













