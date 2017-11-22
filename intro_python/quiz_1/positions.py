def positions(a_string, first_word, second_word, third_word):
    pos = ''
    if first_word in a_string:
        pos += str(a_string.index(first_word))
    else:
        pos += '-' #if first_word doesn't exist
    pos += ','     #add comma for next word position

    if second_word in a_string:
        pos += str(a_string.index(second_word))
    else:
        pos += '-'
    pos += ','

    if third_word in a_string:
        pos += str(a_string.index(third_word))
    else:
        pos += '-'

    return pos

#print(positions("Python is good. I like it.", 'Python', 'wise', 'like')) "0, -, 18"