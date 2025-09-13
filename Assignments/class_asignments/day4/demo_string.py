def no_of_words(my_str):
    char_arr = my_str.split()
    return len(char_arr)

def unique_str(my_str):
    char_arr = my_str.split()
    set_str = set(char_arr)
    return len(set_str)

def vowel_count(my_str):
    vowels = ['a','e','i','o','u']
    count = 0

    for ch in my_str:
        if ch.lower() in vowels:
            count = count + 1

    return count

def longest_word(my_str):
    str_arr = my_str.split()
    longest = ''
    for stt in str_arr:
        if len(stt)>len(longest):
            longest = stt
    return longest

def common_word(my_str):
    str_arr = my_str.split()
    common_word = ''
    count = 0
    for stt in str_arr:
        if str_arr.count(stt) > count:
            common_word = stt
    return common_word