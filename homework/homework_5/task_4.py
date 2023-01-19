# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных

def encoding_rle(str_x:str):
    char = ''
    result = ''
    count = 1
    for el in str_x:
        if el != char:
            if char:
                result += str(count) + char
                count = 1
            char = el
        else:
            count += 1
    return result + str(count) + char

def decoding_rle(str_x:str):
    count = ''
    result = ''
    for i in str_x:
        if i.isdigit():
            count += i
        elif count:
            result += i * int(count)
            count = ''
    return result


if __name__ == '__main__':
    str_x = 'fffffe efefjfjhdfhsdkf;sfjskdjfsiisoisiksksskfjsfifjsifjijfjfjjjjjfs'
    encoding_str = encoding_rle(str_x)
    decoding_str = decoding_rle(encoding_str)
    print(encoding_str)
    print(decoding_str)
    print(decoding_str == str_x)
    