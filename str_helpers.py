def user_name_generator(text_line):
    aux = 0
    result = ""
    for x in text_line:
        if aux == 3:  ### AUX ACOUNTS NUMBER OF ' ', WHEN = 3, THE USER NAME STARTS  
            result += x
            if result[-1] == ":": ### IF RESULT = 'Gabriel Alberto:'
                result = result.strip(":") ### REMOVES THE ':'
                return result
        elif x == " ":
            aux += 1


def line_reader(f):
    number_list = list(map(str, range(10)))

    result = {}
    for line in f:
        if line[0] in number_list: #if line begins with another kind of character, dont enter to this code 
            user = user_name_generator(line)
            if user is not None:
                if user in result:
                    result[user] += 1
                else:
                    result[user] = 1

    return result


def set_max_length(text):
    length = len(text)
    
    if length > 20:
        text = text[:(length-20) * -1] + text[len(text):]
    elif length < 20:
        while len(text) < 20:
            text += '  '

    return text


def prepare_result(results):
    sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)

    result_str_format = ''
    for result in sorted_results:
        name = result[0]
        name = set_max_length(name)
        value = result[1]

        result_str_format += name + ': ' + str(value) + '\n'
        #result_str_format += '{} {:3.2f}\n'.format(name.ljust(20), value)
  
    # '{:20} {:3.2f}'.format(nombre, mensajes)
    return result_str_format

