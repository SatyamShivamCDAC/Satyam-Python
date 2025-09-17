#Ceaser Cipher(Assignment1)
cipher_key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y',
'm':'z', 'n':'a','o':'b',
'p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m', 'A':'N', 'B':'O',
'C':'P', 'D':'Q','E':'R',
'F':'S', 'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 'O':'B', 'P':'C', 'Q':'D', 'R':'E',
'S':'F', 'T':'G', 'U':'H', 'V':'I', 'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}

original_text =  input('Write text message: ')
text_encoded = ""

for char in original_text:
    if not char.isalpha():
        text_encoded = text_encoded + char
    else:
        text_encoded = text_encoded + cipher_key[char]
print("Cipher endcode code- ",text_encoded)

text_decoded = ""

for char in text_encoded:
    if not char.isalpha():
        text_decoded = text_decoded + char
    else:
        text_decoded = text_decoded + cipher_key[char]

print("Cipher dedcode code- ",text_decoded)