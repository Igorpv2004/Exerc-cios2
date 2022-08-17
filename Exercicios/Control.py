from Model import Model

class Control:
    def __init__(self):
        self.opcao = -1
        self.modelo = Model() #conectando com a class model
        self.altura = 0
        self.base = 0
        self.ano = 0
        self.mes = 0
        self. dia = 0
        self.n1 = 0
        self.n2 = 0
        self.n3 = 0
        self.n4 = 0
        self.n5 = 0
        self.n6 = 0
        self.n7 = 0
        self.n8 = 0
        self.n9 = 0
        self.n10 = 0
        self.n11 = 0
        self.n12 = 0
        self.n13 = 0
        self.n14 = 0
        self.n15 = 0
        self.n16 = 0
        self.n17 = 0
        self.n18 = 0
        self.n19 = 0
        self.n20 = 0
        self.quantidade = 0
        self.votot = 0
        self.votob = 0
        self.voton = 0
        self.votov = 0
        self.media = 0
        self.contador = 0

    def getContador(self):
        return self.contador
    def setContador(self, contador):
        self.contador = contador

    def getMedia(self):
        return self.media
    def setMedia(self, media):
        self.media = media

    def getVotot(self):
        return self.votot

    def getVotob(self):
        return self.votob

    def getVoton(self):
        return self.voton

    def getVotov(self):
        return self.votov

    def setVotot(self, voto):
        self.votot = voto

    def setVotob(self, voto):
        self.votob = voto

    def setVoton(self, voto):
        self.voton = voto

    def setVotov(self, voto):
        self.votov = voto

    def getQuantidade(self):
        return self.quantidade

    def setQuantidade(self, quantidade):
        self.quantidade = quantidade

    def getN4(self):
        return  self.n4
    def getN5(self):
        return  self.n5
    def getN6(self):
        return  self.n6
    def getN7(self):
        return  self.n7
    def getN8(self):
        return  self.n8
    def getN9(self):
        return  self.n9
    def getN10(self):
        return  self.n10
    def getN11(self):
        return  self.n11
    def getN12(self):
        return  self.n12
    def getN13(self):
        return  self.n13
    def getN14(self):
        return  self.n14
    def getN15(self):
        return  self.n15
    def getN16(self):
        return  self.n16
    def getN17(self):
        return  self.n17
    def getN18(self):
        return  self.n18
    def getN19(self):
        return  self.n19
    def getN20(self):
        return  self.n20

    def setN4(self, n4):
        self.n4 = n4

    def setN5(self, n5):
        self.n5 = n5

    def setN6(self, n6):
        self.n6 = n6

    def setN7(self, n7):
        self.n7 = n7

    def setN8(self, n8):
        self.n8 = n8

    def setN9(self, n9):
        self.n9 = n9

    def setN10(self, n10):
        self.n10 = n10

    def setN10(self, n11):
        self.n11 = n11

    def setN10(self, n12):
        self.n12 = n12

    def setN10(self, n13):
        self.n13 = n13

    def setN10(self, n14):
        self.n14 = n14

    def setN10(self, n15):
        self.n15 = n15

    def setN10(self, n16):
        self.n16 = n16

    def setN10(self, n17):
        self.n17 = n17

    def setN10(self, n18):
        self.n18 = n18

    def setN10(self, n19):
        self.n19 = n19

    def setN20(self, n20):
        self.n20 = n20
    def getN1(self):
        return  self.n1

    def getN2(self):
        return  self.n2

    def getN3(self):
        return  self.n3

    def setN1(self, n1):
        self.n1 = n1

    def setN2(self, n2):
        self.n2 = n2

    def setN3(self, n3):
        self.n3 = n3

    def getAno(self):
        return self.ano

    def getMes(self):
        return self.mes

    def getDia(self):
        return self.dia

    def setAno(self, ano):
        self.ano = ano

    def setMes(self, mes):
        self.mes = mes

    def setDia(self, dia):
        self.dia = dia


    def getAltura(self):
        return self.altura

    def getBase(self):
        return self.base

    def setAltura(self, altura):
        self.altura = altura

    def setBase(self, base):
        self.base = base


    def getOpcao(self):
        return self.opcao

    def setOpcao(self, opcao):
        self.opcao = opcao

    def Menu(self):
        print("\nEscolha o exercício abaixo" +
              "\n0. Sair"                    +
              "\n1. Exercício"               +
              "\n2. Exercício"               +
              "\n3. Exercício"               +
              "\n4. Exercício"               +
              "\n5. Exercicio"               +
              "\n6. Exercício"               +
              "\n7. Exercício"               +
              "\n8. Exercício"               +
              "\n9. Exercicio"               +
              "\n11.Exercício"               +
              "\n15.Exercício"               +
              "\n16.Exercício"               +
              "\n19.Exercício")

        self.setOpcao(int(input()))

    def operacao(self):
        self.Menu()
        if self.getOpcao() == 0:
            print("Obrigado!")


        elif self.getOpcao() == 1:
            print(self.modelo.exercicio1(self.getN1(), self.getN2(), self.getN3()))


        elif self.getOpcao() == 2:
            print("Digite uma valor para saber seu antecessor: ")
            print(self.modelo.exercicio2(float(input())))

        elif self.getOpcao() == 3:
            print("Digite a base do retângulo: ")
            self.setAltura(int(input()))
            print("Digite a altura do retângulo: ")
            self.setBase(int(input()))
            print(self.modelo.exercicio3(self.getBase(), self.getAltura()))

        elif self.getOpcao() == 4:
            print("Digite sua idade em anos: ")
            self.setAno(int(input()))
            print("Digite sua idade em meses: ")
            self.setMes(int(input()))
            print("Digite sua idade em dias: ")
            self.setDia(int(input()))
            print("A idade em dias é: {}".format(self.modelo.exercicio4(self.getAno(), self.getMes(), self.getDia())))

        elif self.getOpcao() == 5:
            print(self.modelo.exercicio5(self.getVotot(), self.getVotob(), self.getVoton(), self.getVotov()))

        elif self.getOpcao() == 6:
            print(self.modelo.exercicio6(self.getN1(), self.getN2()))





        elif self.getOpcao() == 8:
            print("Digite o valor da primeira nota: ")
            self.setN1(int(input()))
            print("Digite o valor da segunda nota: ")
            self.setN2(int(input()))
            print("Digite o valor da terceira nota: ")
            self.setN3(int(input()))
            print("A média final do aluno é {}".format(self.modelo.exercicio8(self.getN1(), self.getN2(), self.getN3())))

        elif self.getOpcao() == 9:
            print("Digite a quantidade de maçãs desejadas: ")
            self.setQuantidade(int(input()))

            if self.getQuantidade() < 12:
                print("As maçãs custaram: {}".format(self.modelo.exercicio9(self.getQuantidade())))
            else:
                print("As maçãs custaram: {}".format(self.modelo.exercicio9b(self.getQuantidade())))

        elif self.getOpcao() == 11:
            print(self.modelo.exercicio11(self.getN1(), self.getN2()))

        elif self.getOpcao() == 7:
            print(self.modelo.exercicio7(self.getN1(), self.getN2(), self.getN3()))

        elif self.getOpcao() == 15:
            print(self.modelo.exercicio15(self.getN1(), self.getN2(), self.getN3(), self.getN4(), self.getN5(), self.getN6(), self.getN7(), self.getN8(), self.getN9(), self.getN10()))

        elif self.getOpcao() == 16:
            print(self.modelo.exercicio16(self.getN1(), self.getN2(), self.getN3(), self.getN4(), self.getN5(), self.getN6(), self.getN7(), self.getN8(), self.getN9(), self.getN10(), self.getContador()))

        elif self.getOpcao() == 19:
            print(self.modelo.exercicio19(self.getN1(), self.getN2(), self.getN3(), self.getN4(), self.getN5(), self.getN6(), self.getN7(), self.getN8(), self.getN9(), self.getN10(), self.getN11(), self.getN12(), self.getN13(), self.getN14(), self.getN15(), self.getN16(), self.getN17(), self.getN18(), self.getN19(), self.getN20(), self.getMedia(), self.getContador()))















