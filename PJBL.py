import pandas
import enderecos
import matplotlib.pyplot as plt

def gerador(valor,coluna,cont,lista):
    for valor in coluna:
        cont.append(lista.count(valor))

dados = pandas.read_csv(enderecos.endereco, sep=';')

mtv =['Outro', 'Saúde', 'Visitar', 'Negócios', 'Eventos', 'Estudos', 'Lazer', 'Religião', 'Compras', 'Nao respondeu']
dias = ['segunda','terca','quarta','quinta','sexta','sabado','domingo']
cont_mtv = [0,0,0,0,0,0,0,0,0,0]
coluna1 = dados['mes']
coluna = dados['regiao']
coluna2 = dados['diasemana']
nregioes = coluna.unique()
nmes = coluna1.unique()
ndias = coluna2.unique()
lista = coluna.values.tolist()
lista1 = coluna1.values.tolist()
lista2 = coluna2.values.tolist()
cont2 = []
cont1 = []
cont = []
meses = [0,0,0]
cont_mesess = [0,0,0]
cont_mesest = [0,0,0]
cont_mesesq = [0,0,0]
cont_mesesq2 = [0,0,0]
cont_mesesse = [0,0,0]
cont_mesessa = [0,0,0]
cont_mesesdo = [0,0,0]


for i in range(len(dados)):
    linha = dados.iloc[i]
    dia = linha['diasemana']
    mes = linha['mes']
    temporada = linha['temporada']
    city = linha['cidade']
    estado = linha['UF']
    regiao = linha['regiao']
    pais = linha['pais']
    motivo = linha['motivo']
    companhia = linha["compahia"]
    if str("Outro") == motivo:
        cont_mtv[0] += 1
    elif str("Saude: tratamento  consulta medica") == motivo:
        cont_mtv[1] += 1
    elif str("Visita a amigos e parentes") == motivo:
        cont_mtv[2] += 1
    elif str("Negocios") == motivo:
        cont_mtv[3] += 1
    elif str("Congressos e Convencoes") == motivo:
        cont_mtv[4] += 1
    elif str("Estudo ou cursos") == motivo:
        cont_mtv[5] += 1
    elif str("Lazer  passeio") == motivo:
        cont_mtv[6] += 1
    elif str("Religiao  peregrinacao") == motivo:
        cont_mtv[7] += 1
    elif str("Compras") == motivo:
        cont_mtv[8] += 1
    elif str("Nao respondeu") == motivo:
        cont_mtv[9] += 1
    if str('julho') == mes and dia == str('segunda'):
        cont_mesess[0] += 1
    elif str('setembro') == mes and dia == str('segunda'):
        cont_mesess[1] += 1
    elif str('novembro') == mes and dia == str('segunda'):
        cont_mesess[2] += 1
    if str('julho') == mes and dia == str('terca'):
        cont_mesest[0] += 1
    elif str('setembro') == mes and dia == str('terca'):
        cont_mesest[1] += 1
    elif str('novembro') == mes and dia == str('terca'):
        cont_mesest[2] += 1
    if str('julho') == mes and dia == str('quarta'):
        cont_mesesq[0] += 1
    elif str('setembro') == mes and dia == str('quarta'):
        cont_mesesq[1] += 1
    elif str('novembro') == mes and dia == str('quarta'):
        cont_mesesq[2] += 1
    if str('julho') == mes and dia == str('quinta'):
        cont_mesesq2[0] += 1
    elif str('setembro') == mes and dia == str('quinta'):
        cont_mesesq2[1] += 1
    elif str('novembro') == mes and dia == str('quinta'):
        cont_mesesq2[2] += 1
    if str('julho') == mes and dia == str('sexta'):
        cont_mesess[0] += 1
    elif str('setembro') == mes and dia == str('sexta'):
        cont_mesess[1] += 1
    elif str('novembro') == mes and dia == str('sexta'):
        cont_mesess[2] += 1
    if str('julho') == mes and dia == str('sabado'):
        cont_mesessa[0] += 1
    elif str('setembro') == mes and dia == str('sabado'):
        cont_mesessa[1] += 1
    elif str('novembro') == mes and dia == str('sabado'):
        cont_mesessa[2] += 1
    if str('julho') == mes and dia == str('domingo'):
        cont_mesesdo[0] += 1
    elif str('setembro') == mes and dia == str('domingo'):
        cont_mesesdo[1] += 1
    elif str('novembro') == mes and dia == str('domingo'):
        cont_mesesdo[2] += 1



gerador(regiao,nregioes,cont1,lista)
gerador(mes,nmes,cont2,lista1)
gerador(dia,ndias,cont,lista2)


comeco = input("Quer começar? [s/n] > ")

if comeco == 'n':
    exit()

while comeco == 's':
    print("\n1 - Gráfico do número de vezes que cada motivo foi escolhido")
    print("2 - Gráfico do número de vezes que cada região foi escolhida")
    print("3 - Gráfico do número de vezes que cada mês foi escolhido")
    print('4 - Quantidade de vezes que dois dias escolhidos foram escolhidas nos meses')
    print("5 - Sair")

    escolha = int(input("\nDigite o número da ação que deseja fazer: "))

    while escolha > 5 or escolha < 1:
        print("Opção inexistente!!!!")
        print("\n1 - Gráfico do número de vezes que cada motivo foi escolhido")
        print("2 - Gráfico do número de vezes que cada região foi escolhida")
        print("3 - Gráfico do número de vezes que cada mês foi escolhido")
        print('4 - Quantidade de vezes que dois dias escolhidos foram escolhidas nos meses')
        print("5 - Sair")
        escolha = int(input("\nDigite o número da ação que deseja fazer: "))

    if escolha == 1:

        plt.rcParams.update({'font.size': 6})
        plt.plot(mtv, cont_mtv,marker='o', markerfacecolor='r')
        plt.title("Quantidade de vezes de cada motivo")
        plt.ylabel("Número de vezes")
        plt.xlabel("Motivos")
        plt.show()

    elif escolha == 2:

        print('\nCores: red, green, blue, cyan, magenta, yellow, black(k) , white')
        cor1 = input('\nDigite a primeira letra do cor que você deseja: ')
        plt.title("Quantidade de vezes de cada região")
        plt.bar(nregioes, cont1, color= cor1 ,width=0.5)
        plt.xticks(nregioes, fontsize = 9)
        plt.show()

    elif escolha == 3:

        print('\nCores: red, green, blue, cyan, magenta, yellow, black(k) , white')
        cor2 = input('\nDigite a primeira letra do cor que você deseja: ')
        plt.title("Quantidade de vezes que cada mês foi escolhido")
        plt.bar(nmes, cont2, color=cor2,width=0.5)
        plt.xticks(nmes, fontsize = 9)
        plt.show()

    elif escolha == 4:
        print("Dias: Segunda, Terca(sem o ç), Quarta, Quinta, Sexta, Sábado, Domingo")
        dia1 = input("Digite o primeiro dia a ser comparado (sem acentos): ")
        dia2 = input('Digite o segundo dia a ser comparado (sem acentos): ')
        dia1 = dia1.lower()
        dia2 = dia2.lower()
        cont_meses_input1 = 0
        cont_meses_input2 = 0

        while dia1.lower() not in dias or dia2.lower() not in dias:
            print("\nNão existe um dia com um desses nomes!")
            print("\nDias: Segunda, Terca(sem o ç), Quarta, Quinta, Sexta, Sábado, Domingo")
            dia1 = input("Digite o primeiro dia a ser comparado (sem acentos): ")
            dia2 = input('Digite o segundo dia a ser comparado (sem acentos): ')
            dia1 = dia1.lower()
            dia2 = dia2.lower()
            cont_meses_input1 = 0
            cont_meses_input2 = 0


        if dia1 == str('segunda'):
            cont_meses_input1 = cont_mesess
        elif dia1 == str('terca'):
            cont_meses_input1 = cont_mesest
        elif dia1 == str('quarta'):
            cont_meses_input1 = cont_mesesq
        elif dia1 == str('quinta'):
            cont_meses_input1 = cont_mesesq2
        elif dia1 == str('sexta'):
            cont_meses_input1 = cont_mesesse
        elif dia1 == str('sabado'):
            cont_meses_input1 = cont_mesessa
        elif dia1 == str('domingo'):
            cont_meses_input1 = cont_mesesdo
        if dia2 == str('segunda'):
            cont_meses_input2 = cont_mesess
        elif dia2 == str('terca'):
            cont_meses_input2 = cont_mesest
        elif dia2 == str('quarta'):
            cont_meses_input2 = cont_mesesq
        elif dia2 == str('quinta'):
            cont_meses_input2 = cont_mesesq2
        elif dia2 == str('sexta'):
            cont_meses_input2 = cont_mesesse
        elif dia2 == str('sabado'):
            cont_meses_input2 = cont_mesessa
        elif dia2 == str('domingo'):
            cont_meses_input2 = cont_mesesdo

        x = ['Julho', 'Setembro', 'Novembro']
        plt.rcParams.update({'font.size': 10})
        plt.title("Quantidade de vezes que os dois dias digitados foram escolhidas nos meses")
        plt.plot(x, cont_meses_input1, label=dia1)
        plt.plot(x, cont_meses_input2, label=dia2)
        plt.legend()
        plt.show()

    elif escolha == 5:
        exit()
