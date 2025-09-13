my_list = ["stay","GagaG","motom","haha","Tyr"]

def repeating_char(str1):
    for ch in str1:
        if str1.count(ch) >= 2:
            return False
    return True

def is_palindrome(str1):
    if str1 == str1[::-1]:
        return True
    else:
        return False

def swap_title(str1):
    if str1[0].islower():
        return str1.swapcase()
    return str1


palindrome = filter(is_palindrome,my_list)

print(list(palindrome))

my_list2 = [1,2,3,4,5]

odd_sqr = list(map(lambda x : x**2 if x%2!= 0 else x , my_list2))
print(odd_sqr)

dub_char = list(filter(repeating_char,my_list))
print(dub_char)


titled_str = list(map(swap_title ,my_list))
print(titled_str)