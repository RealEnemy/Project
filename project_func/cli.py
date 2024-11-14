import prompt
def welcome():
    print("<command> exit - выйти из программы")
    print("<command> help - справочная информация")
    name = prompt.string('Введите команду: ')
    while (name == 'help'):
        print("<command> exit - выйти из программы")
        print("<command> help - справочная информация")
        name = prompt.string('Введите команду: ')
    
