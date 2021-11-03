import sqlite3

def menu(level):
    if level == 1:
        return '1. Выбор БД 2. Редактирование БД 0. Выход: '
    elif level == 2:
        return '1. SELECT 2. INSERT 3. DELETE 4. UPDATE 0. Выход в меню 1: '

menu_level = 1
connection = None
cursor = None

while True:
    if menu_level == 1:
        answer = input((menu(menu_level)))
        if answer == '2':
            menu_level = 2
        elif answer == '1':
            way = input()
            if connection:
                connection.close()
            if cursor:
                cursor.close()
            connection = sqlite3.connect(way)
            cursor = connection.cursor()
        elif answer == '0':
            break
       

    elif menu_level == 2:
        answer = input((menu(menu_level)))
        if answer == '0':
            menu_level = 1
        elif answer == '1':
            sel = input("SELECT: ")
            fr = input("FROM: ")
            where = input("WHERE: ")
            redkost_1 = "SELECT " + sel + " FROM " + fr + " WHERE " + where + ";"
            if cursor:
                cursor.execute(redkost_1)
                print(cursor.fetchall())
                connection.commit()
        elif answer == '2':
            insert = input("INSERT INTO: ")
            values = input("VALUES: ")
            name = input("NAME: ")
            redkost_2 = "INSERT INTO " + insert + " VALUES (\""+ values +"\", \""+ name +"\");"
            if cursor:
                cursor.execute(redkost_2)
                print(cursor.fetchall())
                connection.commit()
        elif answer == '3':
            delete = input("DELETE FROM: ")
            where_2 = input("WHERE: ")
            redkost_3 = "DELETE FROM " + delete + " WHERE " + where_2 + ";"
            if cursor:
                cursor.execute(redkost_3)
                print(cursor.fetchall())
                connection.commit()
        elif answer == '4':
            update = input("Table: ")
            set_ = input("SET: ")
            where_3 = input("WHERE: ")
            redkost_4 = "UPDATE " + update + " SET " + set_ +" WHERE " + where_3 + ";"
            if cursor:
                cursor.execute(redkost_4)
                print(cursor.fetchall())
                connection.commit()
        elif answer == '0':
            break