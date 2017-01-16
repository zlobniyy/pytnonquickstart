import os
import sys
#import psutil
import shutil

def work_func():
    print("Это похвально!")
    action=""
    while action !="q":
        print("Выберите действие:")
        print("[1] - Показать содержимое указанного каталога")
        print("[2] - Скопировать указанный файл *.dupl")
        print("[3] - удалить дубликаты в указанном каталоге *.dupl")
        print("[q] - выйти в меню выше")
        action=str(input())
        if action == '1':
            dirname=input("Укажите путь до каталога: ")
            i=""
            list=os.listdir(dirname)
            for i in list:
                if os.path.isfile(os.path.join(dirname,i)):
                    print(i)
        elif action == '2':
            filename=input("Укажите путь до файла: ")
            newfilename=filename+".dupl"
            shutil.copy(filename,newfilename)
            if os.path.exists(newfilename):
                print("Файл "+filename+" скопирован в "+newfilename)
            else:
                print("Возникли проблемы при копировании "+filename)
        elif action == '3':
            k=0
            dirname = input("Укажите путь до каталога: ")
            list=os.listdir(dirname)
            for i in list:
                if i.endswith(".dupl"):
                    print("файл подходит и будет удален: "+i )
                    os.remove(os.path.join(dirname,i))
                    k +=1
                else:
                    print("файл НЕподходит, пропускаем: " + i)
                print("Удалено "+str(k)+" файлов.")
        elif action=="q":
            pass
        else:
            print("Вы выбрали что-то непонятное")

print("Это первая программа.")
print("Здравствуйте, Пользователь.")
name=input("Ваше имя: ")
print(name,", добро пожаловать!")
answer=''
while answer!='q':
    answer=input("Поработаем ?(y/n/q)")
    if answer == "n":
        print("Тогда досвидания")
    elif answer == "y":
        work_func()
    elif answer == "q":
        print("До свидания, "+name)
    else:
        print("Ай донт андерстэнд!")
print("="*27)
print("Конец программы")