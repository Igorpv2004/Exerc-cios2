class Model:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0



    def exercicio1(self, a, b, c):
        self.a = 10
        self.b = 20
        self.c = self.a
        self.a = self.b
        self.b = self.c
        print("O valor do A agora é: {} \n O valor do B agora é: {}".format(self.a, self.b))



    def exercicio2(self, valor):
       print("o antecessor do valor digitado é: ", valor - 1)

    def exercicio3(self, base, altura):
        print("A área do retângulo é: ", base * altura)

    def exercicio4(self, ano, mes, dia):
        return ano * 365 + mes * 30 + dia

    def exercicio8(self, n1, n2, n3):
        return (n1 + n2 + n3) / 3

    def exercicio9(self, quantidade):
        return quantidade * 1.30

    def exercicio9b(self, quantidade):
        return quantidade * 1.00

    # votot * votob / 100
    def exercicio5(self,votot, votob, voton, votov):
        print("Digite a quantidade de votos totais: ")
        votot = float(input())
        print("Digite a quantidade de votos brancos: ")
        votob = float(input())
        print("Digite a quantidade de votos nulos: ")
        voton = float(input())
        print("Digite a quantidade de votos válidos: ")
        votov = float(input())
        print("O percentual de votos brancos é: ", votob * 100 / votot)
        print("O percentual de votos nulos é: ", voton * 100 / votot)
        print("O percentual de votos válidos é: ", votov * 100 / votot)

    def exercicio6(self, salario, percentual,):
        print("Digite o salário atual do funcionário: ")
        salario = int(input())
        print("Digite o percentual do salário: ")
        percentual = int(input())
        print("O novo sálario do funcionário: ", salario * percentual / 100 + salario)

    def exercicio11(self, salario, vendas,):
        print("Digite o sálario fixo: ")
        salario = float(input())
        print("Digite a quantidade de vendas efetuadas: ")
        vendas = float(input())
        if vendas <= 1500:
            print("O sálario com a comissão agora é: ", vendas * 3 / 100 + salario)
        elif vendas > 1500:
            print("O salário com a comissão agora é: ", vendas * 5 / 100 + salario)

    def exercicio7(self, valor, distribuidor, impostos):
        print("Digite o valor de custo de fábrica do carro: ")
        valor = int(input())
        distribuidor = valor * 28 / 100
        impostos = valor * 45 / 100
        print("O valor do carro com a soma do distribuidor e os impostos agora é:", valor + distribuidor + impostos)

    def exercicio15(self, n1, n2, n3, n4, n5, n6, n7, n8, n9, n10,):
        print("Digite 10 números: ")
        n1 = int(input())
        n2 = int(input())
        n3 = int(input())
        n4 = int(input())
        n5 = int(input())
        n6 = int(input())
        n7 = int(input())
        n8 = int(input())
        n9 = int(input())
        n10 = int(input())

        if n1 < 0:
            print("O valor {} é negativo".format(n1))
        if n2 < 0:
            print("O valor {} é negativo".format(n2))
        if n3 < 0:
            print("O valor {} é negativo".format(n3))
        if n4 < 0:
            print("O valor {} é negativo".format(n4))
        if n5 < 0:
            print("O valor {} é negativo".format(n5))
        if n6 < 0:
            print("O valor {} é negativo".format(n6))
        if n7 < 0:
            print("O valor {} é negativo".format(n7))
        if n8 < 0:
            print("O valor {} é negativo".format(n8))
        if n9 < 0:
            print("O valor {} é negativo".format(n9))
        if n10 < 0:
            print("O valor {} é negativo".format(n10))

    def exercicio19(self, n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15, n16, n17, n18, n19, n20, media, contador):
        contador = 0
        print("Digite a nota dos 20 alunos: ")
        n1 = int(input())
        n2 = int(input())
        n3 = int(input())
        n4 = int(input())
        n5 = int(input())
        n6 = int(input())
        n7 = int(input())
        n8 = int(input())
        n9 = int(input())
        n10 = int(input())
        n11 = int(input())
        n12 = int(input())
        n13 = int(input())
        n14 = int(input())
        n15 = int(input())
        n16 = int(input())
        n17 = int(input())
        n18 = int(input())
        n19 = int(input())
        n20 = int(input())
        media =  (n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10 + n11 + n12 + n13 + n14 + n15 + n16 + n17 + n18 + n19 + n20) / 20
        print("A média de nota da turma é: ", media)
        if n1 > media:
            contador = contador + 1
        if n2 > media:
            contador = contador + 1
        if n3 > media:
            contador = contador + 1
        if n4 > media:
            contador = contador + 1
        if n5 > media:
            contador = contador + 1
        if n6 > media:
            contador = contador + 1
        if n7 > media:
            contador = contador + 1
        if n8 > media:
            contador = contador + 1
        if n9 > media:
            contador = contador + 1
        if n10 > media:
            contador = contador + 1
        if n11 > media:
            contador = contador + 1
        if n12 > media:
            contador = contador + 1
        if n13 > media:
            contador = contador + 1
        if n14 > media:
            contador = contador + 1
        if n15 > media:
            contador = contador + 1
        if n16 > media:
            contador = contador + 1
        if n17 > media:
            contador = contador + 1
        if n18 > media:
            contador = contador + 1
        if n19 > media:
            contador = contador + 1
        if n20 > media:
            contador = contador + 1

        print("Quantidade de alunos aprovados: ", contador)

    def exercicio16(self, n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, contador):
        contador = 0
        print("Digite 10 valores: ")
        n1 = int(input())
        n2 = int(input())
        n3 = int(input())
        n4 = int(input())
        n5 = int(input())
        n6 = int(input())
        n7 = int(input())
        n8 = int(input())
        n9 = int(input())
        n10 = int(input())
        if n1 < 40:
            contador = contador + n1
        if n2 < 40:
            contador = contador + n2
        if n3 < 40:
            contador = contador + n3
        if n4 < 40:
            contador = contador + n4
        if n5 < 40:
            contador = contador + n5
        if n6 < 40:
            contador = contador + n6
        if n7 < 40:
            contador = contador + n7
        if n8 < 40:
            contador = contador + n8
        if n9 < 40:
            contador = contador + n9
        if n10 < 40:
            contador = contador + n10

        print("A soma dos valores inferiores a 40 é: ", contador)





