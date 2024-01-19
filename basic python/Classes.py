class Person:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
    def saudacao(self):
        print("Hello: " +self.name)
    def mult_idade(self,mult):
        
        print(f"sua idade é {self.age} multiplicando por {mult} = {mult * self.age}")

teste = Person("John Doe",30)
teste.saudacao()
teste.mult_idade(22)

