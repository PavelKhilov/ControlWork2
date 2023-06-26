# Реализовать консольное приложение заметки, с сохранением, чтением, добавлением, редактированием и удалением заметок.
# Заметка должна содержать идентификатор, заголовок, тело заметки и дату/время создания или последнего изменения 
# заметки. Сохранение заметок необходимо сделать в формате json или csv формат (разделение полей рекомендуется 
# делать через точку с запятой). Реализацию пользовательского интерфейса студент может делать как ему удобнее, 
# можно делать как параметры запуска программы (команда, данные), можно делать как запрос команды с консоли 
# и последующим вводом данных, как-то ещё, на усмотрение студента.

import os
import json
import time

dir_tasks = os.getcwd() + "/Tasks"

def chk_dir_for_tasks():
    l = os.listdir(dir_tasks)
    lt = [x.split('.')[0] for x in l]
    if len(lt) == 0:
        print("Заметки еще не созданы!")
        return False
    else:
        print("Список имеющихся заметок:", *lt, sep="\n")

def view_tasks():
    if not chk_dir_for_tasks():
        fn = input("Введите номер заметки, которую хотите просмотреть: ")

        with open(dir_tasks + "/" + fn + ".json", "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
            for p in data['task']:
                print('ID: ' + p['id'])
                print('Title: ' + p['title'])
                print('Body: ' + p['body'])
                print('Date: ' + p['date'])
                print('Time: ' + p['time'])

def add_task():
    data = {}
    fn = time.strftime("%d%m%y%H%M%S")
    data["task"] = []
    data["task"].append({
        "id": fn,
        "title": input("Введите заголовок заметки: "),
        "body": input("Введите содержание заметки: "),
        "date": time.strftime("%d/%m/%y"),
        "time": time.strftime("%H:%M:%S")
    })

    if not os.path.exists(dir_tasks):
        os.mkdir(dir_tasks)

    with open(dir_tasks + "/" + fn + ".json", 'w') as outfile:
        json.dump(data, outfile)
    print(f"Заметка {fn} успешно сохранена.")
    chk_dir_for_tasks()        

def edit_task():
    if not chk_dir_for_tasks():
        fn = input("Введите номер заметки, которую хотите просмотреть: ")
        with open(dir_tasks + "/" + fn + ".json", "r",
                  encoding="utf-8") as json_file:
            data = json.load(json_file)
        json_file.close()

        for p in data['task']:
            p["title"] = input("Введите заголовок заметки: ")
            p["body"] = input("Введите тело заметки: ")
            p["date"] = time.strftime("%d/%m/%y")
            p["time"] = time.strftime("%H:%M:%S")

        with open(dir_tasks + "/" + fn + ".json", 'w') as outfile:
            json.dump(data, outfile)
        print(f"Заметка {fn} успешно узменена.")

def delete_task():
    if not chk_dir_for_tasks():
        fn = input("Введите номер заметки, которую хотите удалить: ") + ".json"
        os.remove(dir_tasks + "/" + fn)
        print(f"Заметка {fn} успешно удалена.")

def main():
    state = True
    while state:
        command = input("Введите команду:\n"
                        "1. view\n"
                        "2. add\n"
                        "3. edit\n"
                        "4. delete\n"
                        "5. exit\n")
        match command:
            case "1":  # view
                view_tasks()
            case "2":  # add
                add_task()
            case "3":  # edit
                edit_task()
            case "4":  # delete
                delete_task()
            case "5":  # exit
                state = False
            case _:
                print(f"Извините, но такой команды {command!r} у меня нет.\n")


if __name__ == '__main__':
    main()