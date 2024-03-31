text='СъЕШЬ ещё этих МяГкИх французских булок'
print(len(text))
print('ещё' in text)
print(text.lower())
print(text.upper())
print(text.replace('ещё','ЕЩЁ'))


text='съешьещёэтихмягкихфранцузскихбулок' 
print(text[0]) #c 
print(text[1]) #ъ 
print(text[len(text)-1]) #к 
print(text[-5]) #б 
print(text[:]) #съешьещёэтихмягкихфранцузскихбулок 
print(text[:2]) #съ 
print(text[len(text)-2:]) #ок 
print(text[2:9]) #ешьещё print(text[6:-18]) #ещёэтихмягких 
print(text[0:len(text):6]) #сеикакл 
print(text[::6]) #сеикакл 
text=text[2:9]+text[-5]+text[:2] #...
print(text)