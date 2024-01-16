text = "AULA PYCODEBR"
print(text) # AULA PYCODEBR
print(text[0]) # A
print(text[0:4]) # AULA
print(text[:4]) # AULA
print(text[5:]) # PYCODEBR
print(len(text)) # 13
print(text.count('A')) # 2
print(text.count('A',5,11)) #0
print(text.find('AULA')) # 0 ACHOU NO INDEX 0
print(text.find('PYCODEBR')) # 5 ACHOU NO INDEX 5
print(text.find('ALSD')) # -1 NAO ENCONTRADO
print(text.lower()) # aula pycodebr
print(text.capitalize()) # Aula pycodebr
print(text.title()) #Aula Pycodebr
print(text.split()) #['AULA', 'PYCODEBR']
lista_de_palavras = text.split()
print(''.join(lista_de_palavras)) # AULAPYCODEBR
print('-'.join(lista_de_palavras)) # AULA-PYCODEBR
text = "   AULA PYCODEBR    "
print(text.strip()) # remove espaço em branco semelhante 'trim'