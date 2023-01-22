# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

def delete_word(str_x:str, char:str):
    return ' '.join(filter(lambda x: char not in x.lower(), str_x.split()))

if __name__ == '__main__':
    str_x = 'Урвараро вговапроао шгморратг аБв ывоаываго мтаогвашш тмвлаоывш еотрабв'
    print(delete_word(str_x, 'абв'))