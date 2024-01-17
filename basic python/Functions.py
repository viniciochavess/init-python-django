def soma(a,b):
    print(f"resultado da soma {a} + {b} = {a+b}")
soma(2,10)


def quadrado(a):
    return a**2

two = quadrado(2)
print(two)

four = quadrado(4)
print(four)


def enviar_email(nome,email):
    nome_dest=nome
    email_dest=email
    print(f"Email enviado para {nome_dest} email: {email_dest}")

listPessoa = [{"name":"fulano","email":"johndoe@gmail.com"},{"name":"seu madruga","email":"madruguinha@gmail.com"},{"name":"haz","email":"haz@gmail.com"}]

for pessoa in listPessoa:
    enviar_email(pessoa["name"],pessoa["email"])