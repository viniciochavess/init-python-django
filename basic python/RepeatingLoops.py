i = 0

while i <10:
    if i == 5:
        i = i +1
        continue 
    print(f"value de : {i}")
    i = i +1

frutas = ['pera','maça','banana','laranja','limão']

for indice,fruta in enumerate(frutas,start=1):
    
    print(f'{indice}: {fruta}')


valor = 0
while  valor != 300:
    valor = int(input('Digite um valor: '))


for value in range(1,11):
    print(value)

for value in range(0,len(frutas)):
    print(value)