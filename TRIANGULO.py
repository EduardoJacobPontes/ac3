def determina_tipo_triangulo(x, y, z):
    if x + y<=z or x + z<=y or y + z<=x:
        return "nao eh m triangulo"
    elif x == y == z:
        return "equilatero"
    elif x == y or y == z or x == z:
        return "isoceles"
    else:
        return "escaleno"
    

def testa_triangulo():
    print(determina_tipo_triangulo(4, 4, 4)) # Equilátero
    print(determina_tipo_triangulo(2, 4, 4)) # Isósceles
    print(determina_tipo_triangulo(3, 4, 5)) # Escaleno
    print(determina_tipo_triangulo(1, 1, 4)) # Não é um triângulo

#testa_triangulo()


def dia_semana(x):
    dias = {
        1: "domingo",
        2: "segunda-feira",
        3: "terça-feira",
        4: "quarta-feira",
        5: "quinta-feira",
        6: "sexta-feira",
        7: "sábado"
    }
    return dias.get(x, "") 
 
def testa_dia_semana():
    print(dia_semana(2)) # segunda-feira
    print(dia_semana(6)) # sexta-feira
    print(dia_semana(7)) # sábado
    print(dia_semana(9)) # string vazia
    
#testa_dia_semana()

def calculadora(op, n1, n2):
    if op == "+":
        r= n1 + n2
        print("resultado:", r)
    elif op == "-":
        r= n1 - n2
        print("resultado:", r)
    elif op == "/":
        r= n1 / n2
        print("resultado:", r)
    elif op == "*":
        r= n1 * n2
        print("resultado:", r)
    else:
        return "operacao invalida"
    
def entrada():
    n1 = float(input("primeiro numero: "))
    n2 = float(input("segundo numero: "))
    op = input("operacao: ")
    calculadora(op, n1, n2)

entrada()
