import json
import os


file_txt = 'homework\homework_7\phone.txt'
file_json = 'homework\homework_7\phone.json'

def GetInfo(message):
    return input(message)

def InfoContact():
    firstname = GetInfo('Enter firstname: ')
    lastname = GetInfo('Enter lastname: ')
    phone = GetInfo('Enter phone: ')
    return (firstname, lastname, phone)

def WriteJson(tuple_contact:tuple):
    list_x = ReadJson()
    list_x.append(tuple_contact)
    with open(file_json, 'w', encoding='utf-8') as f:
        json.dump(list_x, f)

def ReadJson():
    with open(file_json, encoding='utf-8') as f:
        return json.load(f)

def WriteTxt(tuple_contact:tuple):
    with open(file_txt, 'a', encoding='utf-8') as f:
        for i in tuple_contact:
            f.write(i + '\n')
        f.write('***\n')

def ReadTxt():
    with open(file_txt, encoding='utf-8') as f:
        str_x = f.read()
        return [i.split('\n')[:-1] for i in str_x.split('***\n')][:-1] if str_x else []


def AddNewContact(contact:tuple, file_json:bool):
    WriteJson(contact) if file_json else WriteTxt(contact)


def List_Contacts(file_json:bool):
    return ReadJson() if file_json else ReadTxt()

if __name__ == '__main__':
    if not os.path.isfile(file_json):
        with open(file_json, 'w', encoding='utf-8') as f:
            json.dump(list(), f)
    if not os.path.isfile(file_txt):
        with open(file_txt, 'w', encoding='utf-8') as f:
            pass
    x = int(GetInfo('Enter 1 if read contacts, enter 2 if add contact or 0 for exit: '))
    if x:
        file = int(GetInfo('Enter 1 if format .json or 0 if format .txt: '))
        if x == 2:
            AddNewContact(InfoContact(), file==1)
            print('Contact added.')
        elif x == 1:
            print(List_Contacts(file==1))