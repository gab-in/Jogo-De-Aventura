import random
import math
import os
import time 

#lista de itens
'''"Pocao de cura"
"Escudo"
"Bussola de escadas"
"Bussola de desafios"
"Bussola de tesouros"
"Pocao de cura maior"
"Travesseiro aconchegante"
"Coracao implantavel"
"Bussola de caminho seguro"'''


salas = []
mapa = []
player = "X"
op = 1
tamanho = 1
dificuldade = 0
desafio = 0
descanso = 0 

inventario = ["Pocao de cura"]
pontos = 0
tipo=0
#Variáveis de classe
classe = ""
vida = 0
vidamax = 0
dt = 0
espada = 0 
adaga = 0
cajado = 0
escudo = 0
esquiva = 0
modificador = 0 
dadoMaximo=8
inteligencia = 0

#Variáveis de combate
vidaInimigo = 0 
dtInimigo = 0
danoInimigo = 0
modificadorInimigo=0
esquivaInimigo=0
expbosscheck=0

#Menu

def ApagarCs():
    os.system('cls') or None

def RodarDado(lados,modificador):
    numero = random.randint(1,lados)+modificador
    return numero

def Menu():
    global tamanho
    global dificuldade
    global op
    global vida, dt, esquiva, modificador, inteligencia, vidamax, classe
    ApagarCs()
    print("\n---  SKYRIM 2: As Aventuras de NatiGhostKiller ---\n")
    op = int(input("Preparado para aventura?\n\n0 - sair  |  1 - jogar  |  2 - como jogar\n"))
    if(op==1):
        ApagarCs()
        dificuldade = int(input("\nEscolha o dificuldade inicial da dungeon:\n\n1 - facil  |  2 - medio  |  3 - dificil\n"))
        if(dificuldade==1):
            tamanho = 3
        elif(dificuldade==2):
            tamanho = 5
        elif(dificuldade==3):
            tamanho = 7
        
        ApagarCs()
        classe = int(input("\nEscolha sua classe \n\n1 - Barbaro (+DANO +VIDA)  |  2 - Ladino (+ESQUIVA +TESOUROS)  |  3 - Feiticeiro (+INTELIGENCIA +DESAFIOS)\n"))
        if(classe==1):
            vidamax=50
            vida = vidamax
            dt=12
            modificador=4
            inventario.append("Espada")
        elif(classe==2):
            vidamax=30
            vida = vidamax
            dt=16
            esquiva = 4
            inventario.append("Adaga")
            inventario.append("Bussola de tesouros")
        elif(classe==3):
            vidamax=25
            vida = vidamax
            dt=14
            inteligencia = 4
            inventario.append("Cajado")
            inventario.append("Bussola de desafios")
        
        

    elif(op==2):
        ApagarCs()
        print("O jogo consiste em se mover pela Dungeon e ganhar pontos dados pela salas andadas. As salas possuem pontos variados, normalmente salas mais dificis darão mais pontos. Para avançar para o proximo andar da Dungeon deve encontrar a sala com maior pontos.")
        aux = input("Voltar para o menu ->\n")
        Menu()

def GerarMapa(tamanho):
    global salas
    global mapa
    global player
    global descanso
    descanso = 0
    salas = []
    mapa = []
    
    for i in range(tamanho):
        linha = []
        l = []
        for j in range(tamanho):
            l.append(0)
            linha.append(random.randint(1,9))
        mapa.append(l)
        salas.append(linha)
    posicao = math.ceil((tamanho/2)-1)
    mapa[posicao][posicao] = player
    salas[posicao][posicao] = 0

    saida=0
    for i in range(tamanho):
        for j in range(tamanho):
            if(salas[i][j]==9):
                saida=1
    if(saida==0):
        GerarMapa(tamanho)
           
def ProximoAndar():
    global tamanho
    tamanho+=1
    ApagarCs()
    GerarMapa(tamanho)
    print("PARABENS!!!\nVocê desce para o proximo andar...")
    MostrarMapa()
    time.sleep(3)

def MostrarMapa():   

    print("\n----- MAP -----")
    for i in range(tamanho):
        print(mapa[i])    
    print("---------------\n")

def Mover():
    global mapa
    global salas
    global player
    global tamanho
    tamanho = len(mapa)
    for i in range(tamanho):
        for j in range(tamanho):
            if(mapa[i][j]=="X"):
                x = j
                y = i
    direcao = int(input("\nQual direção?\n\n1 - NORTE  |  2 - SUL  |  3 - LESTE  |  4 - OESTE\n"))
    PontoSala()
    if(direcao==1):
        if(y>0):
            mapa[y-1][x] = player
            mapa[y][x] = salas[y][x]
        else:
            print("\nBateu a cara na parede!\n")
            time.sleep(2)
    elif(direcao==2):
        if(y+1<tamanho):
            mapa[y+1][x] = player
            mapa[y][x] = salas[y][x]
        else:
            print("\nBateu a cara na parede!\n")
            time.sleep(2)
        
    elif(direcao==3):
        if(x+1<tamanho):
            mapa[y][x+1] = player
            mapa[y][x] = salas[y][x]
        else:
            print("\nBateu a cara na parede!\n")
            time.sleep(2)
        
        
    elif(direcao==4):
        if(x>0):
            mapa[y][x-1] = player
            mapa[y][x] = salas[y][x]
        else:
            print("\nBateu a cara na parede!\n")
            time.sleep(2)

def Descansar():
    global descanso, vida, vidamax
    ApagarCs()
    op = int(input("Deseja descansar? (apenas uma vez por andar)\n\n1 - Sim  |  2 - Deixar pra depois\n\n"))
    if(op==1):
        if(descanso<1):
            ApagarCs()
            cura = (random.randint(1,12))+4
            print("\nVocê descansa por um tempo e recupera",cura,"pontos de vida")
            vida+=cura
            if(vida>vidamax):
                vida=vidamax
            time.sleep(3)
        else:
            print("\nVocê nao pode mais descansar nesse andar")
            time.sleep(3)
    else:
        print("...")
        time.sleep(2)


#Sessao de inventario e itens
def MostrarInventario():
    global inventario
    print("\nVocê possui:",)
    for i in range(len(inventario)):
        print(i,"-",inventario[i])
    y = int(input("\n1 - sair  |  2 - Usar item\n"))
    if(y==2):
        aux = int(input("\nDigite o numero do item que deseja usar ->\n"))
        if(aux!=''):
            if(aux>len(inventario) or aux<0):
                MostrarInventario()
            else:
                UsarItem(aux)

def UsarItem(item):
    global inventario
    match inventario[item]:
        case "Pocao de cura":
            PocaoVida(item)
        case "Escudo":
            Escudo(item)
        case "Bussola de desafios":
            RevelarDes(item)
        case "Bussola de tesouros":
            RevelarTes(item)
        case "Bussola de escadas":
            RevelarEsc(item)
        case "Pocao de cura maior":
            PocaoVidaMais(item)
        case "Travesseiro aconchegante":
            Travi(item)
        case "Coracao implantavel":
            Coracao(item)
        case "Bussola de caminho seguro":
            RevelarCam(item)
        case "Espada":
            ApagarCs()
            print("Propriedades: 1d8+4 de dano")
            time.sleep(3)
        case "Cajado":
            ApagarCs()
            print("Propriedades: 1d8 de dano")
            time.sleep(3)
        case "Adaga":
            ApagarCs()
            print("Propriedades: 1d8 de dano")
            time.sleep(3)
        case "Espada da Forja Negra":
            ApagarCs()
            EspadaNegra()
            time.sleep(3)
        case "Adaga do Rei dos Ladrões":
            ApagarCs()
            AdagaRei()
            time.sleep(3)
        case "Cajado Celestial":
            ApagarCs()
            CajadoCelestial()
            time.sleep(3)
        case _:
            print("Nada a se fazer...")

def PocaoVida(id):
    global vida, vidamax,inventario
    if(vidamax==vida):
        ApagarCs()
        print("\nA vida está cheia!\n")
        time.sleep(3)
    else:
        cura=RodarDado(8,3)
        vida += cura
        if(vida>vidamax):
            vida = vidamax
        inventario.pop(id)
        ApagarCs()
        print("\nCurou", cura, "Pontos de vida!1\n")
        time.sleep(3)

def PocaoVidaMais(id):
    global vida, vidamax,inventario
    if(vidamax==vida):
        ApagarCs()
        print("\nA vida está cheia!\n")
        time.sleep(3)
    else:
        cura=RodarDado(12,8)
        vida += cura
        if(vida>vidamax):
            vida = vidamax
        inventario.pop(id)
        ApagarCs()
        print("\nCurou", cura, "Pontos de vida!1\n")
        time.sleep(3)

def Escudo(id):
    global dt, escudo
    if(escudo>0):
        ApagarCs()
        print("Escudo ja equipado!")
        time.sleep(3)
    else:
        ApagarCs()
        print("Escudo foi equipado!")
        print("\n+2 de armadura ")
        time.sleep(3)
        escudo+=1
    
def RevelarEsc(id):
    global salas, mapa, tamanho
    for i in range(tamanho):
        for j in range(tamanho):
            if(salas[i][j]==9):
                mapa[i][j]=9
    ApagarCs()
    print("A Bussula revela no seu mapa onde ficam as escadas no seu andar...")
    print("\nProcure pelos NOVES")
    time.sleep(3)

def RevelarTes(id):
    global salas, mapa, tamanho
    for i in range(tamanho):
        for j in range(tamanho):
            if(salas[i][j]==7):
                mapa[i][j]=7
    ApagarCs()
    print("A Bussula revela no seu mapa onde ficam os tesouros no seu andar...")
    print("\nProcure pelos SETES")
    time.sleep(3)

def RevelarDes(id):
    global salas, mapa, tamanho
    for i in range(tamanho):
        for j in range(tamanho):
            if(salas[i][j]==4):
                mapa[i][j]=4
    for i in range(tamanho):
        for j in range(tamanho):
            if(salas[i][j]==5):
                mapa[i][j]=5
    ApagarCs()
    print("A Bussula revela no seu mapa onde ficam os desafios no seu andar...")
    print("\nProcure pelos QUATROS e CINCOS")
    time.sleep(3)

def Travi(id):
    ApagarCs()
    global descanso, inventario
    print("\nVocê se sente confortavel com esse travesseiro, pode descansar 1 vez a mais nesse andar")
    descanso-=1
    inventario.pop(id)
    time.sleep(3)

def Coracao(id):
    ApagarCs()
    global vida, vidamax, inventario
    print("\nVocê percebe que esse Coração é um parasita vivo...")
    time.sleep(3)
    print("\nVocê aproxima ele de seu peito e ele fixa em você")
    time.sleep(3)
    print("\nMas você se sente bem!")
    time.sleep(1)
    print("\nGanha +10 de vida maxima")
    time.sleep(3)
    vida+=10
    vidamax+=10
    inventario.pop(id)
    
def RevelarCam(id):
    for i in range(tamanho):
        for j in range(tamanho):
            if(salas[i][j]==1):
                mapa[i][j]=1
    for i in range(tamanho):
        for j in range(tamanho):
            if(salas[i][j]==2):
                mapa[i][j]=2
    for i in range(tamanho):
        for j in range(tamanho):
            if(salas[i][j]==3):
                mapa[i][j]=3
    ApagarCs()
    print("A Bussula revela as salas seguras no seu andar...")
    print("\nProcure pelos UNS, DOIS, TRES")
    time.sleep(3)

def EspadaNegra():
    global vidamax, dadoMaximo, modificador, espada

    vidamax=vidamax-20
    dadoMaximo=12
    modificador=8

    if(espada>0):
        ApagarCs()
        print("Item já equipado!")
        time.sleep(3)
    else:
        ApagarCs()
        print("Equipado!\nVocê sente um peso nas costas... A vontade e força de quem empunhou essa arma agora é parte de você, assim como os seus pecados também")
        print("\nSua vida diminuiu em 20\nSeu dano máximo agora é 12\nSeu modificador agora é 8")
        time.sleep(3)
        espada+=1

def AdagaRei():
    global modificador, esquiva, vidamax, adaga

    vidamax=vidamax-10
    modificador=2
    esquiva=8

    if(adaga>0):
        ApagarCs()
        print("Item já equipado!")
        time.sleep(3)
    else:
        ApagarCs()
        print("Equipado!\nVocê sente um peso nas costas... A vontade e força de quem empunhou essa arma agora é parte de você, assim como os seus pecados também")
        print("\nSua vida diminuiu em 10\nSua esquiva agora é 8\nSeu modificador agora é 2")
        time.sleep(3)
        adaga+=1

def CajadoCelestial():
    global dadoMaximo, inteligencia, vidamax, cajado

    vidamax=vidamax-5
    dadoMaximo=10
    inteligencia=8

    if(cajado>0):
        ApagarCs()
        print("Item já equipado!")
        time.sleep(3)
    else:
        ApagarCs()
        print("Equipado!\nVocê sente um peso nas costas... A vontade e força de quem empunhou essa arma agora é parte de você, assim como os seus pecados também")
        print("\nSua vida diminuiu em 5\nSeu dano máximo agora é 10\nSua inteligência agora é 8")
        time.sleep(3)
        cajado+=1

#Estatiticas

def MostrarEstatisticas():
    global dt,vida, vidamax
    os.system('cls') or None

    print("\n--- STATUS ---")
    print("   HP =",vida,"/",vidamax)
    print("  ARMOR =",dt)    
    print("--------------\n")

    aux = input("\nEnter para retornar ->\n")

#Pontuacao

def MostrarPontos():
    global pontos
    print("  -- SCORE --")
    print("      ",pontos,"  ")
    print("  -----------")

def AddPontos(pt):
    #pt = quatidade de pontos a ser atribuido
    global pontos
    pontos += pt

def PontoSala():
    global salas
    if(salas[y][x]!=1):
        AddPontos(salas[y][x])
    

#Nova seção de funções para combate
def RolandoDados(vidaAtacado, dtAtacado, dadoMaximo, modificador, dif):
    global vida, vidaInimigo, inteligencia

    dado=random.randint(1,20)+inteligencia
    print("\nRolando dado de ataque...")
    time.sleep(1)
    print("Dado: %d!"%(dado))

    if(dado==20):
        print("\nDano crítico!")

        dado=random.randint(1,dadoMaximo)
        print("%d de dano no primeiro ataque!"%(dado))
        vidaAtacado=vidaAtacado-dado
        dado=random.randint(1,danoInimigo)
        print("%d de dano no segundo ataque!"%(dado))
        time.sleep(2)

        return vidaAtacado-dado
        
    elif(dado>=dtAtacado):
        dado=random.randint(1,dadoMaximo)+modificador
        print("Rolando dado de dano...")
        time.sleep(1)
        print("%d de dano!"%(dado))

        return vidaAtacado-dado
    
    elif(dado==1):
        print("\nDesastre!")
        dado=random.randint(1,8)+modificador
        time.sleep(1)
        print("%d de dano em si mesmo!"%(dado))
        if(dif==0):
            vida=vida-dado
        elif(dif==1):
            vidaInimigo=vidaInimigo-dado
        
        return vidaAtacado
        
    else:
        print("\nErrou o ataque.")
        time.sleep(2)
        return vidaAtacado

def AtaqueInimigo():
    global vida, dt, danoInimigo, modificadorInimigo, vidaInimigo
    ApagarCs()
#Outro exemplo de ASCII art super duper importante para imersão do jogador
    print("---------------------------------------------------------------------------------------------------")
    print("""                     ______
                  .-"      "-.
                 /            \
                |              |
                |,  .-.  .-.  ,|
                | )(__/  \__)( |
                |/     /\     \|
      (@_       (_     ^^     _)
 _     ) \_______\__|IIIIII|__/__________________________
(_)@8@8{}<________|-\IIIIII/-|___________________________>
       )_/        \          /
      (@           `--------`""")
    print("---------------------------------------------------------------------------------------------------")
    time.sleep(1)

    print("\nO inimigo tenta te atacar...")
    vida=RolandoDados(vida, dt, danoInimigo, modificadorInimigo, 1)

    input("\nEnter para continuar ->\n")

def Atacar():
    global vidaInimigo, dtInimigo, dadoMaximo, modificador

    vidaInimigo=RolandoDados(vidaInimigo, dtInimigo, dadoMaximo, modificador, 0)

    input("\nEnter para continuar ->\n")

def Fugir():
    global classe, esquiva, vidaInimigo, esquivaInimigo
    print("\nVocê tenta fugir...")

    destreza=random.randint(1,20)+esquiva
    print("\nVocê tirou %d!"%(destreza))

    destrezaInimigo=random.randint(1,20)+esquivaInimigo
    print("\nRolando dados do inimigo...")
    time.sleep(1)
    print("\nO inimigo tirou %d!"%(destrezaInimigo))

    if(destreza>destrezaInimigo):
        print("\nVocê escapa da batalha!")
        vidaInimigo=0
        time.sleep(2)
    else:
        print("\nParece que você não foi rápido o suficiente...")
        time.sleep(2)
        AtaqueInimigo()
    return vidaInimigo

def CriarInimigo():
    global vidaInimigo, dtInimigo, danoInimigo, modificadorInimigo, esquivaInimigo

    vidaInimigo=random.randint(4,6)*random.randint(1,3)
    dtInimigo=random.randint(7,9)+random.randint(1,3)
    danoInimigo=random.randint(1,3)+5
    modificadorInimigo=random.randint(0,1)
    esquivaInimigo=random.randint(0,2)
    
def MenuCombate():
    global vidaInimigo, dtInimigo, vida, classe
    ApagarCs()

#ASCII art super importante para a imersão do jogo
#A primeiro é uma espada
    if(classe==1):
        print("---------------------------------------------------------------------------------------------------")
        print(""" _          /~~>________________________________________
/ \////////|   \..................................~~~~~---_
\_/\\\\\\\\|   /__________________________________-----~~~
            \__>""")
#Essa segunda é uma adaga
    if(classe==2):
        print("---------------------------------------------------------------------------------------------------")
        print(""" ,-.  ,                     , ,.......____
(   ` |    @                | |               ...---...___
 `-.  |,-. , .-.-. :-..-. .-| |                           ..--..__
.   ) |  | | | | | |  | | | | |                                   .-._
 `-'  '  ' ' ' ' ' '  `-' `-` `---------------------------------------`""")
        print("---------------------------------------------------------------------------------------------------")
#E aqui a gente tem..... É meio que o simbolo dos médico, mas virou um cajado. Tem um parecido no Genshin, shhhhhh
    if(classe==3):
        print("---------------------------------------------------------------------------------------------------")
        print(""" _____  _  _____
(___  \( )/  ___)
  (___ | | ___)
   /")`| |'("\
  | |  | |  | |
   \ \_| |_/ /
    `._!' _.'
      / .'\
     | / | |
      \|/ /
       /.<
      (| |)
       | '
       | |
       `-'""")
        
    print("Vida:",vida)
    print("---------------------------------------------------------------------------------------------------")

    op=int(input("\nO que você deseja fazer?\n1 - Atacar  2 - Fugir \n"))
    if(op==1):
        Atacar()
    elif(op==2):
        vidaInimigo=Fugir()
    else:
        print(". . .")

def Combate():
    global vidaInimigo, dtInimigo, vida, expbosscheck
    print("Você entrou em uma batalha! É seu turno, se prepare\n")
    input("\nEnter para continuar ->\n")
    while True:
        MenuCombate()

        if not(vidaInimigo>0):
            break
        
        ApagarCs()
        print("É a vez do inimigo")
        time.sleep(2)
        ApagarCs()
        AtaqueInimigo()

        if not (vida>0):
            return 0
        
    print("\nVocê venceu a batalha!")
    exp=0
    if(expbosscheck==1):
        exp=exp+100
        expbosscheck=0
    elif(dtInimigo>12):
        exp=exp+35
    else:
        exp=exp+20
    
    print("Você recebeu %d pontos!"%(exp))
    AddPontos(exp)
    input("\nEnter para continuar ->\n")
    return

#Armadilhas
def Armadilha():
    global vida, dt, vidaInimigo, dtInimigo, danoInimigo, modificadorInimigo, dadoMaximo, modificador
    print("\nUm baú feito de madeira, com extremidades reforçadas a aço e uma fechadura enferrujada, aparece diante de você")
    op=int(input("\nO que deseja fazer?\n1 - Abrir o baú  |  2 - Atacar  |  3 - Sair\n"))

    if(op==1):
        print("O baú revela.... UM MÍMICO, ele te ataca de surpresa")
        vida=RolandoDados(vida, dt, danoInimigo, modificadorInimigo, 1)

        if(vida<=0):
            return 0
        
        input("\nEnter para continuar ->\n")
        op=Combate()
        return op
    
    if(op==2):
        print("Sua intuição estava correta, era um MÍMICO!")
        vidaInimigo=RolandoDados(vidaInimigo, dtInimigo, dadoMaximo, modificador, 0)
        
        if(vidaInimigo<=0):
            return
        
        input("\nEnter para continuar ->\n")
        op=Combate()
        if(op):
            RecompensaBau(0)
        return op
 #

#Desafios

def DanoDesafio():
    global vida
    dano = random.randint(2,7)
    vida -= dano
    print("\nPerde", dano, "pontos de Vida...")
    time.sleep(3)

def Desafio():
    global desafio
    desafio = 0
    ApagarCs()
    print("Você entrou numa sala de desafio!\nPrepare-se...")
    time.sleep(2)
    num = random.randint(1,4)
    match num:
        case 1:
            DesafioMat()
        case 2:
            ApagarCs()
            print("Um pequeno goblin aparece, ele parece querer jogar Pedra, Papiro e Adaga")
            DesafioPPA()
        case 3:
            DesafioQNumero()
        case 4:
            print("\nVocê se depara com um Esqueleto numa mesa de jogos de azar, ele exige que jogue uma partida com ele...")
            time.sleep(2)
            print("\nO jogo se chama VINTE E UM\nO objetivo do jogo é tirar o maximo de cartas possivel sem que a soma delas seja 21 ou maior, você pode decidir se deseja parar ou pegar outra carta, os valores são de 1 até 13")
            x = input("\nAperte ENTER se entendeu as regras ->")
            DesafioVinteUm()
    if(desafio==1):
        print("\nVocê encontra um item!")
        time.sleep(2)
        RecompensaDes()
        print("Você ganhou 25 pontos por completar o desafio com sucesso!")
        AddPontos(25)

def DesafioMat():
    global desafio
    ApagarCs()
    x = random.randint(10,20)
    y = random.randint(1,30)
    solucao = x+y
    print("Uma estatua olha em sua direção e exige que você responda corretamente:")
    resposta = int(input("\nQuanto é a soma de:\n\n"+str(x)+" + "+str(y)+" ?\n"))
    if(resposta==solucao):
        print("Resposta correta!")
        time.sleep(3)        
    else:
        print("Ouch! Você errou!\n")
        DanoDesafio()


    ApagarCs()
    x = random.randint(2,12)
    y = random.randint(1,12)
    solucao = x*y      
    print("\nA estatua persiste e pergunta:")
    resposta = int(input("\nQuanto é o produto de:\n\n"+str(x)+" x "+str(y)+" ?\n"))
    if(resposta==solucao):
        print("Resposta correta!")
        time.sleep(3)        
    else:
        print("Ouch! Você errou!\n")
        DanoDesafio()

    
    ApagarCs()
    x = random.randint(5,20)
    y = random.randint(1,10)
    z = random.randint(1,10)
    solucao = x+(y*z)      
    print("\nA estatua persiste e pergunta:")
    resposta = int(input("\nQual é o resultado da equação:\n\n"+str(x)+" + "+str(y)+" x "+str(z)+" ?\n"))
    if(resposta==solucao):
        print("Resposta correta! Você provou seu valor, siga em frente!\n")
        time.sleep(3)
        desafio=1
               
    else:
        print("Seu paspalhão! SUMA DAQUI\n")
        time.sleep(3)
        DanoDesafio()
        desafio=-1

def DesafioPPA():  
    global desafio
    escolha = int(input("\n1 - Pedra  |  2 - Papiro  |  3 - Adaga\n\n"))
    goblin = random.randint(1,3)

    match escolha:
        case 1:
            print("\nVocê faz o sinal de uma Pedra\n")
        case 2:
            print("\nVocê faz o sinal de um Papiro\n")
        case 3:
            print("\nVocê faz o sinal de uma Adaga\n")
        case _:
            DesafioPPA()
    time.sleep(2)

    match goblin:
        case 1:
            print("O goblin faz o sinal de uma Pedra\n")
        case 2:
            print("O goblin faz o sinal de um Papiro\n")
        case 3:
            print("O goblin faz o sinal de uma Adaga\n")
    time.sleep(2)

    if(escolha==goblin):
        print("\nJoguem de novo!\n")
        time.sleep(2)
        ApagarCs()
        DesafioPPA()
    
    elif(escolha==1):
        if(goblin==2):
            print("\nVocê perdeu!\n\nO goblin ri de você, pega uma pedra, taca em você e sai correndo...\n")
            time.sleep(1)
            DanoDesafio()
            desafio=-1
        else:
            print("\nVocê ganhou!\n\nO goblin sai correndo...\n")
            time.sleep(2)
            desafio=1
    
    elif(escolha==2):
        if(goblin==3):
            print("\nVocê perdeu!\n\nO goblin ri de você, pega uma pedra, taca em você e sai correndo...\n")
            time.sleep(1)
            DanoDesafio()
            desafio=-1
        else:
            print("\nVocê ganhou!\n\nO goblin sai correndo...\n")
            time.sleep(2)
            desafio=1
    
    elif(escolha==3):
        if(goblin==1):
            print("\nVocê perdeu!\n\nO goblin ri de você, pega uma pedra, taca em você e sai correndo...\n")
            desafio=-1
            time.sleep(1)
            DanoDesafio()
        else:
            print("\nVocê ganhou!\n\nO goblin sai correndo...\n")
            desafio=1
            time.sleep(2)

def DesafioQNumero():
    global desafio
    print("\nUm Gato Magico Falante aparece e te fala que tem 7 chances para acertar a pergunta:\n")
    time.sleep(3)
    ratos = random.randint(1,100)    
    chance = 1
    while(chance<=7):
        ApagarCs()
        chute = int(input("--- Chance "+str(chance)+" ---\n\nQuantos ratos eu comi hoje?\n"))
        if(chute==ratos):
            chance=10
        elif(chute>ratos):
            print("\nESTA FALANDO QUE SOU GORDO??? Jamais comeria tantos ratos!\n")
            time.sleep(2)
            print("tente um numero menor... miau")
            time.sleep(3)
            chance+=1
        else:
            print("\nO QUE??? Você acha que é facil manter meu corpo magico só com isso?!\n")
            time.sleep(2)
            print("tente um numero maior... miau")
            time.sleep(3)
            chance+=1
        
    ApagarCs()
    if(chance==10):
        print("Parabens! Você acertou exatamente minhas refeições de hoje! Vou deixar você ir! miau\n")
        time.sleep(3)
        desafio=1
    else:
        print("MEOOOWW!!! Você não tem intelecto sobre as refeições de um ser mistico como eu, não merece minha atenção...\n\nO gato te arranha e vai embora.")
        time.sleep(4)
        DanoDesafio()
        desafio=-1

def DesafioVinteUm():    
    global desafio
    rodada = 1
    esqueleto = 0
    vc = 0
    escolha = 1
    escolhaesqueleto = 1
    while(rodada!=-1):
        ApagarCs()
        print("--------- VINTE UM ---------")
        print("           Round",rodada,"\n VOCÊ =",vc," |  ESQUELETO =",esqueleto)
        print("----------------------------")
        if(escolha==1):
            escolha = int(input("\nO que deseja fazer?\n\n1 - tirar uma carta  |  2 - parar de tirar\n"))
            if(escolha==1):
                carta=random.randint(1,13)
                vc+=carta
                print("\nVocê tirou",carta)
                time.sleep(2)
                if(vc>=21):
                    print("\nVocê ultrapassou 21\n")
                    time.sleep(2)
                    rodada = -1
                    
        
        if(rodada!=-1):
            rodada+=1
            if(esqueleto<=16):
                carta=random.randint(1,13)
                esqueleto+=carta
                print("\nO esqueleto tirou",carta,"\n")
                time.sleep(2)
                if(esqueleto>=21):
                    print("\nO Esqueleto ultrapassou 21\n")
                    time.sleep(2)
                    rodada = -1
            elif(esqueleto<vc):
                carta=random.randint(1,13)
                esqueleto+=carta
                print("\nO esqueleto tirou",carta,"\n")
                time.sleep(2)
                if(esqueleto>=21):
                    print("\nO Esqueleto ultrapassou 21\n")
                    time.sleep(2)
                    rodada = -1
            else:
                print("\nO esqueleto decide parar.")
                escolhaesqueleto+=1
                time.sleep(2)
            
            if(escolha!=1 and escolhaesqueleto!=1):
                rodada = -1
        
    
    print("VOCÊ =",vc," |   ESQUELETO =",esqueleto)
    if(vc>=21):
        print("\nVocê Perdeu! O esqueleto deixa você ir embora...")
        time.sleep(2)
        print("\nMas te da uma rasteira e vc cai de cara no chão.")
        time.sleep(2)
        DanoDesafio()
        desafio=-1
    elif(vc==esqueleto):
        print("\nEmpate!\nO esqueleto quer jogar de novo!")
        DesafioVinteUm()
    elif(vc>esqueleto or esqueleto>=21):
        print("\nVocê Ganhou! O esqueleto deixa você ir embora...")
        time.sleep(2)
        desafio=1
    else:
        print("\nVocê Perdeu! O esqueleto deixa você ir embora...")
        time.sleep(2)
        print("\nMas te da uma rasteira e você cai de cara no chão.")
        time.sleep(2)
        DanoDesafio()
        desafio=-1
        
#Recompensa

def AtribuirItem(id):
    global inventario
    contador = 0
    match id:
        case 0:
            print("")
        case 1:
            print("\nAdquiriu uma Pocao de cura")
            inventario.append("Pocao de vida")
        case 2:
            print("\nAdquiriu um Escudo")
            for i in range(len(inventario)):
                if(inventario[i]=="Escudo"):
                    contador+=1
            if(contador==0):
                inventario.append("Escudo")
        case 3:
            print("\nAdquiriu um Bussola de tesouros")
            for i in range(len(inventario)):
                if(inventario[i]=="Bussola de tesouros"):
                    contador+=1
            if(contador==0):
                inventario.append("Bussola de tesouros")
        case 4:
            print("\nAdquiriu um Bussola de escadas")
            for i in range(len(inventario)):
                if(inventario[i]=="Bussola de escadas"):
                    contador+=1
            if(contador==0):
                inventario.append("Bussola de escadas")
        case 5:
            print("\nAdquiriu um Bussola de desafios")
            for i in range(len(inventario)):
                if(inventario[i]=="Bussola de desafios"):
                    contador+=1
            if(contador==0):
                inventario.append("Bussola de desafios")
        case 6:
            print("\nAdquiriu um Pocao de vida maior")            
            inventario.append("Pocao de vida maior")
        case 7:
            print("\nAdquiriu um Bussola de caminho seguro")
            for i in range(len(inventario)):
                if(inventario[i]=="Bussola de caminho seguro"):
                    contador+=1
            if(contador==0):
                inventario.append("Bussola de caminho seguro")
        case 8:
            print("\nAdquiriu um Travesseiro aconchegante")
            inventario.append("Travesseiro aconchegante")
        case 9:
            print("\nConseguiu um Coracao implantavel")
            inventario.append("Coracao implantavel")
        case 10:
            for i in range(len(inventario)):
                if(inventario[i]=="Espada da Forja Negra"):
                    contador+=1
                    RecompensaBau(0)
            if(contador==0):
                print("\nAdquiriu Espada da Forja Negra")
                inventario.append("Espada da Forja Negra")
        case 11:
            for i in range(len(inventario)):
                if(inventario[i]=="Adaga do Rei dos Ladrões"):
                    contador+=1
                    RecompensaBau(0)
            if(contador==0):
                print("\nAdquiriu Adaga do Rei dos Ladrões")
                inventario.append("Adaga do Rei dos Ladrões")
        case 12:
            for i in range(len(inventario)):
                if(inventario[i]=="Cajado Celestial"):
                    contador+=1
                    RecompensaBau(0)
            if(contador==0):
                print("\nAdquiriu Cajado Celestial")
                inventario.append("Cajado Celestial")

    time.sleep(3)
    if(contador!=0):
        print("\nJá possui esse item no inventario...")
        time.sleep(2)

def RecompensaDes():
    x = random.randint(1,10)
    if(x<=4):
        AtribuirItem(1)
    elif(x==5):
        AtribuirItem(6)
    elif(x==6):
        AtribuirItem(6)
    elif(x==7):
        AtribuirItem(8)
    elif(x==8):        
        AtribuirItem(7)
    elif(x==9):
        AtribuirItem(4)
    else:
        AtribuirItem(5)

def Quebrar(retornoItem):
    quebrar=random.randint(0,1)
    if(quebrar==1):
        print("\nVocê ouve o som de vidro se estilhaçando dentro do baú, parece que você quebrou sua recompensa...")
        return 0
    else:
        return retornoItem
    
def RecompensaBau(tentouAtacar): #0=não, 1=sim
    x=random.randint(1,10)
    if(x==1) and (tentouAtacar==1):
        AtribuirItem(Quebrar(1))
    elif(x==1) and (tentouAtacar==0):
        AtribuirItem(1)
    elif(x<=2):
        AtribuirItem(2)
    elif(x==3) and (tentouAtacar==1):        
        AtribuirItem(Quebrar(6))
    elif(x==3) and (tentouAtacar==0):
        AtribuirItem(6)
    elif(x==4):
        AtribuirItem(4)
    elif(x==5):
        AtribuirItem(5)
    elif(x==6):
        AtribuirItem(7)
    elif(x==7):
        AtribuirItem(9)
    
    #Itens amaldiçoados------------
    elif(x==8):
        AtribuirItem(10)
    elif(x==9):
        AtribuirItem(11)
    elif(x==10):
        AtribuirItem(12)
    #--------------------------
    else:
        AtribuirItem(3)
    
#Bau, simples, rápido e direto
def Bau():
    print("\nUm baú feito de madeira, com extremidades reforçadas a aço e uma fechadura enferrujada, aparece diante de você")
    op=int(input("\nO que deseja fazer?\n1 - Abrir o baú  |  2 - Atacar  |  3 - Sair\n"))

    if(op==1):
        print("\nO cheiro de mofo contamina o ambiente... Você encontra um item!")     
        RecompensaBau(0)
    elif(op==2):
        RecompensaBau(1)
    elif(op==3):
        return

#BOSS!!!!!!
def TesteInteligencia():
    global inteligencia

    ApagarCs()
    dado=random.randint(1,20)+inteligencia

    if(dado>16):
        print("\nEm meio à lama fedida, você nota um cristal... Talvez acertá-lo acabe com a aberração")
        return 1
    else:
        print("\nA lama torna sua visão turva... Você não consegue enxergar direito.")
        return 0
    
def GerarBoss():
    global vidaInimigo, dtInimigo, danoInimigo, modificadorInimigo, esquivaInimigo, inteligencia, expbosscheck

    ApagarCs()
    tipo=random.randint(1,3)
    if(tipo==1):
        #Boss de dano
        print("\nUm círculo se incendeia à sua volta. Você NÂO tem saída.")
        time.sleep(2)
        print("\nO espírito do fogo se ergue em sua frente, o bater de suas asas faz você estremesser\n")
        time.sleep(3)
        print("""              ▓▓██▓▓▒▒▒▒▒▒████████████████▓▓████▓▓▒▒▒▒▓▓▓▓██  ▒▒▓▓░░░░    ▓▓████▓▓░░▓▓▓▓░░▒▒██████████▓▓██████▓▓▒▒▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓                
                                  ░░▓▓██████▓▓▓▓████▓▓▒▒▓▓▓▓▓▓░░▒▒▓▓    ▓▓░░████▓▓▓▓▒▒▒▒  ▒▒▒▒▒▒████▓▓▒▒▓▓▓▓████▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒  ░░░░▒▒▒▒▓▓██▓▓▓▓████████▓▓              
                              ▓▓▓▓▓▓▓▓▓▓██████▓▓██▓▓████▒▒██▓▓▒▒▓▓██  ▓▓██▓▓▓▓▓▓▓▓▒▒▒▒▓▓▒▒    ██▓▓▓▓██████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒                        ░░▒▒██▓▓▓▓▓▓            
                            ██▓▓▓▓▓▓▓▓▓▓▓▓████▓▓▒▒▓▓████▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓██▒▒▓▓████▓▓▓▓    ██▒▒  ▒▒▓▓▓▓▓▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                              ▓▓▓▓▒▒          
                          ▓▓▓▓▓▓██████████▓▓▓▓██████▓▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓██▒▒▓▓  ▒▒██▒▒  ▒▒██▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▒▒▒▒▓▓░░                              ▓▓          
                        ░░▓▓▓▓████████████████▓▓▓▓████▓▓██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓▓▓▒▒▓▓░░▓▓▒▒  ▒▒██▓▓▓▓▓▓▓▓██████▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▒▒▓▓                                ░░        
                        ▓▓▓▓██████████████████████▓▓▓▓██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓██▓▓▓▓▒▒░░▓▓▓▓▓▓▓▓▓▓██▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓▓▓▓▓▓▓                                        
                        ▓▓████████▒▒░░        ░░▓▓██████▓▓██▒▒▓▓▓▓▓▓▒▒▓▓▓▓██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▒▒▒▒░░      ▒▒▓▓██▓▓████▓▓▓▓▓▓                                      
                      ░░▓▓▓▓▓▓▓▓                    ▒▒▓▓██▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▒▒▒▒  ▒▒                ▒▒▓▓▓▓▓▓▓▓▓▓░░                                    
                      ░░██▓▓▒▒                        ░░████▓▓▓▓▓▓██████▓▓▓▓▓▓████▓▓████▓▓▓▓▓▓██████▓▓▒▒░░▒▒▓▓                      ▒▒▓▓▓▓██▓▓                                    
                      ░░▓▓▓▓                          ▓▓▓▓██▓▓▓▓██████████████▓▓▓▓▓▓▓▓████████▓▓▓▓▒▒▓▓▓▓▓▓▒▒                            ▓▓▓▓▓▓▓▓                                  
                      ░░▓▓░░                          ▓▓▓▓██▓▓▓▓██▓▓██████████▓▓▒▒▓▓▓▓▓▓████▓▓██▓▓▓▓▓▓▒▒                                  ▒▒▓▓██▒▒                                
                        ▓▓                            ██▓▓██▓▓▓▓▒▒  ████▓▓████▒▒▓▓▒▒▓▓▓▓██▓▓████▓▓▓▓▓▓▓▓    ▒▒                                ▓▓▓▓                                
                        ▓▓                            ▓▓▓▓▓▓▓▓▓▓    ░░▓▓██▓▓▓▓▓▓▓▓▓▓▓▓██████▓▓████▓▓▓▓██    ██                                  ▒▒░░                              
                        ░░                            ▓▓██▓▓▓▓▓▓░░    ▓▓▓▓▓▓▓▓██▓▓▓▓██▓▓▓▓██████▓▓▒▒▓▓▓▓░░░░▓▓                                    ▓▓                              
                                              ░░      ▓▓██▓▓██▓▓▓▓    ░░██▓▓▓▓▓▓▓▓▓▓██▓▓██▓▓████▓▓▒▒▒▒▓▓▒▒▓▓▒▒                                      ░░                            
                                              ░░░░    ▒▒██▓▓▓▓▓▓██░░▒▒  ██▓▓▓▓░░▓▓██▓▓██▓▓██▓▓▓▓▓▓▓▓▒▒▒▒████                                                                      
                                                ▒▒▒▒    ▓▓██▓▓▓▓▒▒▓▓▓▓  ▓▓▓▓░░      ▓▓▒▒▓▓▓▓▓▓██▓▓▓▓▒▒▒▒▓▓▓▓                                                                      
                                                  ▓▓▓▓▒▒▓▓██▓▓▓▓▓▓▓▓▓▓  ░░▒▒          ▓▓██▓▓██▓▓▓▓▓▓▒▒▓▓▓▓▓▓                                                                      
                                                    ▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▒▒              ░░▓▓▓▓████▓▓██▓▓▓▓▓▓▓▓▓▓                                                                      
                                                        ▓▓████▒▒▓▓▓▓▒▒              ▒▒▓▓██████▓▓████▓▓▓▓▓▓▓▓                                                                      
                                                          ████▓▓▓▓▓▓▓▓              ▓▓▓▓██████  ████▓▓▓▓▒▒▓▓░░                                                                    
                                                          ▓▓▓▓▒▒▓▓▓▓▓▓▓▓          ▒▒▓▓██████  ▒▒  ▓▓▓▓▒▒▒▒▓▓▓▓                                                                    
                                                          ▓▓▓▓▓▓██▓▓████▒▒        ▓▓▒▒██▓▓▓▓████░░██████▓▓██▓▓                                                                    
                                                            ▓▓▓▓▓▓  ▒▒▓▓▓▓        ▓▓████▓▓████▓▓  ▓▓██▓▓▓▓▓▓▓▓▒▒                                                                  
                                                            ░░▓▓██    ▒▒▓▓        ▓▓██▓▓░░████    ██▓▓██▓▓▓▓▓▓▓▓▓▓                                                                
                                                              ▓▓▓▓      ░░        ▒▒██░░░░▓▓▓▓    ██▓▓██  ▓▓▒▒██▓▓██                                                              
                                                              ▓▓▓▓                ░░    ▓▓██▒▒  ░░▓▓▓▓██      ██▓▓▓▓                                                              
                                                                ▓▓                    ▒▒▓▓▓▓▒▒  ░░▓▓▓▓▒▒      ▓▓▓▓▓▓                                                              
                                                                                  ░░██▓▓▓▓██    ██▓▓▓▓        ▒▒▓▓▓▓▒▒                                                            
                                                                      ░░        ████▓▓▓▓██      ██▓▓▓▓        ▒▒▓▓▓▓▓▓                                                            
""")
        vidaInimigo=40
        dtInimigo=15
        danoInimigo=12
        modificadorInimigo=4
        esquivaInimigo=20
        expbosscheck=1
        input("\n\nPressione enter para continuar ->\n")
    if(tipo==2):
        #Boss de inteligencia
        print("\nUm cheiro pútrido preenche o ar a sua volta, um lamaçal cobre todo o chão da sala")
        time.sleep(2)
        print("\nO lamaçal no chão começa a se levantar e tomar forma de vários humanóides...")
        time.sleep(3)
        print("""░░▒▒░░▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓██▒▒░░░░░░▒▒░░░░▒▒▓▓░░░░▒▒▒▒▒▒▒▒▒▒██▒▒▒▒░░▓▓▓▓▒▒░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░▒▒▒▒▒▒██▓▓▓▓▒▒▒▒▓▓░░▓▓▓▓██▓▓▒▒░░▒▒▓▓▓▓▓▓▓▓██████████▓▓▒▒▒▒░░▓▓░░░░░░░░░░▒▒▒▒▓▓▓▓████
░░░░  ▒▒██▓▓██▓▓▓▓▓▓▒▒▓▓▓▓░░░░░░▒▒░░░░░░▒▒▒▒▓▓░░░░░░▒▒▒▒▒▒▓▓▒▒░░▒▒▒▒░░▓▓▒▒░░░░▓▓▒▒░░░░░░▒▒▓▓▒▒░░░░░░▓▓██▓▓░░░░░░░░░░▓▓██▓▓██▓▓▒▒░░▒▒▓▓▓▓▓▓▓▓██████████▓▓▒▒░░░░░░▓▓░░░░░░▒▒▒▒▒▒████████
░░▓▓▒▒▒▒██████▓▓▓▓▓▓▓▓██░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒░░▒▒▒▒░░░░▒▒░░░░▓▓▒▒▒▒▓▓░░░░░░░░░░▒▒▒▒░░░░░░░░██▒▒░░░░░░░░░░▓▓▓▓▓▓▓▓██▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▒▒░░░░░░▓▓██▒▒▒▒▒▒▓▓▓▓████████
░░▓▓▒▒░░▓▓▒▒████▓▓▓▓▓▓▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒░░░░▓▓░░▓▓▒▒▒▒▒▒▓▓▓▓▓▓░░▒▒░░░░░░░░░░▒▒░░░░▒▒░░▓▓▒▒░░░░░░░░▒▒▒▒▓▓▓▓▓▓██▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░▒▒░░▓▓██▒▒██▓▓▓▓██████████
░░▓▓▓▓▓▓██████▒▒▒▒▓▓▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓▒▒░░░░▒▒▓▓▓▓▒▒▒▒▒▒▒▒░░▒▒██▓▓▓▓▓▓██░░░░▒▒░░░░░░░░░░░░▒▒░░░░░░░░░░▓▓▒▒▒▒░░░░░░░░▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▓▓██▓▓▓▓▓▓████▓▓▒▒▒▒░░░░▓▓▓▓▓▓▓▓████▓▓████████████
▒▒██▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓██▓▓▒▒▒▒▓▓▒▒░░░░░░░░░░▒▒▓▓▒▒▒▒░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░▓▓░░░░░░░░░░▒▒▒▒░░▒▒░░░░░░░░▒▒██▓▓▓▓▒▒▒▒▒▒██▓▓██▓▓▓▓████▓▓▓▓▒▒░░▓▓▒▒▒▒░░▓▓████▓▓▓▓██████████
▓▓▓▓▒▒▓▓▒▒▓▓▒▒░░▒▒▒▒▒▒▓▓██▒▒▓▓▒▒▒▒▓▓░░░░    ░░░░▒▒▒▒░░░░░░██▓▓▒▒░░░░░░░░░░░░  ░░░░░░░░░░░░▒▒  ░░  ░░  ░░▒▒░░░░░░░░░░░░▒▒██▓▓▓▓▒▒░░▒▒██▓▓██▓▓▓▓████▓▓▓▓▒▒░░▒▒▒▒░░▓▓▓▓████▓▓▓▓██████████
████▒▒░░▒▒▒▒▓▓▒▒▒▒▒▒▒▒▓▓▓▓▒▒▓▓▒▒▒▒▓▓░░░░░░  ░░░░▒▒▒▒░░░░░░▓▓▒▒░░░░░░░░░░▒▒░░  ░░░░░░░░░░▒▒▒▒        ░░░░░░▒▒░░░░░░░░░░▒▒██▓▓▓▓▒▒░░░░░░▓▓██▓▓▓▓████▓▓▓▓░░░░▒▒▒▒░░░░▒▒██████▓▓▓▓██████▓▓
████▒▒▒▒░░░░▓▓▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░▒▒▓▓░░░░░░▓▓▒▒░░░░░░░░░░▒▒░░  ░░░░░░░░░░▒▒            ░░▓▓▒▒░░░░░░░░▒▒▓▓▓▓▓▓▓▓░░░░  ░░░░▓▓▓▓▓▓████▓▓▓▓▓▓▓▓░░░░░░░░░░████████▓▓██████▒▒
██████▓▓░░░░▓▓▓▓▒▒▒▒░░▒▒▓▓▓▓▒▒▒▒▒▒▒▒░░░░░░░░░░░░▒▒▓▓░░░░░░▒▒▒▒░░░░░░░░▒▒░░░░  ░░░░░░░░▒▒▓▓  ░░        ░░░░▒▒▒▒░░░░▒▒▒▒▒▒▒▒▓▓▒▒░░    ░░▓▓▓▓▓▓▓▓██▓▓██▓▓██▒▒░░▒▒░░░░░░▒▒██████▓▓▓▓██▒▒▒▒
████████▒▒░░▓▓▓▓▒▒▒▒░░░░▓▓▓▓▓▓▒▒▒▒░░░░░░░░░░░░░░░░▓▓▒▒░░░░░░▒▒░░░░░░░░░░░░▓▓  ░░░░░░░░▒▒▓▓▓▓░░      ░░░░▒▒▒▒░░▒▒░░░░▒▒░░░░▒▒░░    ▒▒██████▓▓▓▓▓▓████████▓▓░░▒▒░░░░░░████████▓▓▓▓▓▓░░▓▓
▓▓██████▓▓░░▓▓▓▓▓▓▓▓░░▒▒▓▓▓▓▒▒▒▒▒▒▓▓░░░░░░░░░░░░▓▓▓▓▒▒░░▒▒░░░░░░░░░░░░░░░░▓▓░░░░░░░░▒▒▓▓▓▓▓▓  ░░    ░░░░░░░░░░░░░░░░▒▒▒▒▒▒░░    ▒▒████████████▓▓████▓▓▒▒██▒▒▒▒▒▒░░░░████████▓▓▓▓▓▓▒▒██
▓▓██████▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▒▒░░░░░░░░░░▒▒▓▓▓▓██████▒▒░░░░░░░░░░░░░░▓▓░░  ░░▓▓▓▓▓▓▓▓░░  ░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░  ▓▓██▒▒▓▓▓▓▒▒▓▓████▓▓██▓▓▒▒▓▓██▓▓▒▒░░▒▒████▓▓▒▒▓▓▓▓▓▓▓▓██
▓▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▒▒▒▒▓▓▒▒▒▒░░░░░░░░░░░░▓▓▓▓▒▒████████░░░░░░░░░░░░▒▒▓▓░░  ▓▓▓▓▓▓▓▓▓▓      ░░░░░░░░░░░░░░░░▒▒░░░░░░░░  ░░▓▓▓▓  ▓▓▒▒▓▓▓▓▓▓████████▒▒▒▒▓▓██▒▒░░▓▓██▓▓▒▒▓▓▓▓▓▓▓▓████
▓▓██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▒▒░░  ░░░░░░░░░░░░▒▒██▓▓▓▓▒▒▓▓██▓▓▒▒░░░░░░░░░░░░▓▓▒▒░░░░▓▓▓▓▓▓▓▓▒▒        ░░░░░░░░░░░░░░░░▒▒▒▒      ░░░░    ▓▓▓▓▒▒░░░░░░▒▒████▓▓▒▒▒▒▓▓░░░░████▓▓▓▓▓▓██████████
▒▒▓▓██████▓▓▓▓▒▒▒▒▒▒▒▒░░░░░░░░  ░░░░░░░░░░▓▓██▓▓▓▓▒▒▓▓▓▓██▓▓░░░░░░░░░░░░░░▒▒  ░░▓▓▓▓▓▓▓▓▓▓        ▒▒░░░░░░░░░░░░░░░░░░░░  ░░▓▓▒▒  ░░▓▓██░░░░░░░░░░▒▒██▓▓██▒▒▒▒░░░░▒▒▓▓▓▓████████▓▓████
▒▒▓▓██████▓▓▓▓▒▒▒▒▒▒░░  ░░░░░░░░  ░░░░░░░░░░▓▓▓▓▓▓▒▒▓▓██▓▓▓▓▓▓░░░░▒▒░░▓▓▒▒░░  ▒▒▒▒▓▓▓▓▓▓▓▓░░    ░░▓▓░░░░░░░░░░░░░░░░░░  ░░▒▒▒▒▒▒  ░░▓▓▓▓▒▒░░░░░░░░░░▓▓██▓▓▓▓▓▓░░░░▓▓▓▓▓▓▓▓██████▒▒▓▓██
░░▒▒██▓▓▓▓▓▓▓▓▒▒▒▒░░░░  ░░░░░░░░  ░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▒▒▓▓▒▒▒▒░░░░░░▓▓▓▓▓▓▓▓▒▒▓▓░░░░░░▒▒░░░░  ░░░░░░░░░░░░  ░░▓▓▒▒▒▒▒▒░░▓▓▓▓░░░░░░░░░░░░░░▓▓▓▓▓▓▒▒░░░░▒▒▒▒▒▒▓▓▓▓████▒▒▒▒██
░░▓▓▓▓▓▓▓▓▓▓▒▒▒▒░░░░░░  ░░▒▒░░░░  ░░░░░░░░  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓░░▒▒░░░░    ▓▓▓▓▓▓▓▓▓▓░░░░▒▒░░░░▒▒░░░░░░░░▒▒▒▒░░░░░░  ░░▒▒▒▒▒▒▒▒▒▒██▓▓▒▒░░░░░░░░░░░░░░▓▓██▒▒░░░░▒▒▒▒░░░░▒▒▓▓██▓▓░░▒▒
░░▓▓▓▓▓▓▓▓▓▓▓▓░░  ░░░░▒▒░░░░░░░░    ░░▒▒░░  ▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░  ░░▒▒▓▓▓▓▓▓▓▓▒▒░░░░    ░░░░░░░░▒▒▒▒░░░░░░░░░░▒▒▒▒▒▒▒▒░░▒▒▓▓██░░▒▒░░░░░░░░░░░░░░▓▓░░░░░░▒▒▓▓▒▒░░░░▒▒██▓▓░░▓▓
░░████▓▓▓▓▓▓      ▒▒░░░░░░░░░░░░      ░░    ▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒    ░░▓▓▓▓▓▓▓▓▓▓▓▓░░░░    ░░░░░░░░▒▒▒▒░░░░░░░░░░▓▓▒▒▒▒▒▒░░░░▒▒▓▓██▓▓▓▓▒▒░░░░░░░░░░▒▒░░░░░░▒▒▒▒▒▒░░░░░░▓▓▓▓░░▓▓
░░▓▓▓▓▓▓▓▓▒▒░░  ░░  ░░░░░░░░░░              ▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓░░    ▒▒▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░▒▒▒▒▒▒▒▒░░░░░░░░░░▓▓▒▒░░▒▒░░░░▒▒▒▒▓▓██▓▓▓▓▒▒░░░░░░░░░░░░░░░░▒▒▒▒▒▒░░░░░░▒▒▒▒████""")
        input("Pressione enter para continuar ->")

        vidaInimigo=1
        dtInimigo=12
        danoInimigo=8
        modificadorInimigo=2
        esquivaInimigo=20
        expbosscheck=1

        while True:
            op=int(input("\n1 - Atacar  2 - Olhar em volta\n"))

            if(op==1):
                dado=random.randint(1,20)+inteligencia
                print("\nRolando dado de ataque...")
                time.sleep(1)
                print("Dado: %d!"%(dado))
                print("\nErrou o ataque.")
                print("\nSua espada atravessa a lama, porem e a figura humanoide se reconstrói")
                time.sleep(2)
                input("Pressione enter para continuar ->")

                print()
                AtaqueInimigo()
                ApagarCs()
            elif(op==2):
                ApagarCs()
                pontoFracoCheck=TesteInteligencia()
            else:
                print("...")

            if(pontoFracoCheck==1):
                break
            else:
                AtaqueInimigo()

    if(tipo==3):
        #Boss de Destreza
        print("\nA sala está estranhamente arrumada, a decoração parece a de um castelo")
        time.sleep(2)
        print("\nUm cavaleiro gigante, talvez do tamanho de um dragão você diria, se levanta bravamente.")
        time.sleep(3)
        print("""                                                                                                                                                                                                                                                                                                                                                                  
                                                                                      ▒▒                                                                                              
                                                                                      ░░▒▒                                                                                            
                                                                                      ▒▒▒▒▒▒░░                                                                                        
                                                                                    ▒▒▒▒▒▒▒▒▒▒                                                                                        
                                                                                    ▒▒░░▒▒▒▒▓▓▒▒                                                                                      
                                                                                    ▒▒▒▒▒▒▓▓▓▓▒▒                                                                                      
                                                                                    ▒▒░░▒▒▓▓▓▓▒▒                                                                                      
                                                                                    ░░▒▒▓▓▓▓▓▓▓▓▒▒░░                                                                                  
                                                                                  ░░▒▒▒▒▒▒▒▒▓▓▓▓░░░░░░░░                                                                              
                                                                              ░░░░░░▒▒▓▓▒▒▒▒▓▓░░░░░░░░░░░░░░                                                                          
                                                                              ░░░░░░▓▓▒▒▓▓██▓▓░░░░░░▒▒██▒▒▒▒░░                                                                        
                                                                            ░░░░░░▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒░░                  ░░                                                    
                                                                            ░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▓▓▓▓▓▓▒▒          ░░▒▒▒▒▓▓                                                    
                                                                            ░░░░▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▓▓▒▒▒▒▒▒▓▓▓▓▓▓▓▓      ▒▒▒▒▓▓▓▓▓▓▒▒                                                    
                                                                            ░░░░▒▒▒▒▒▒░░▒▒░░░░▒▒██▒▒▒▒▓▓▓▓▓▓████░░▒▒▓▓▓▓▓▓▒▒▓▓▓▓▒▒                                                    
                                                                            ▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒████▓▓▒▒▓▓██▓▓▒▒▒▒▓▓▓▓▓▓▒▒▓▓▓▓▓▓░░                                                    
                                                                            ▒▒▓▓▓▓▒▒░░▒▒▒▒▒▒▒▒▓▓████▓▓░░▒▒▒▒▒▒▓▓▒▒▒▒▓▓▓▓▒▒▓▓▓▓▒▒░░                                                    
                                                                              ▓▓▓▓▓▓▒▒▒▒▒▒▓▓▓▓▓▓██████▒▒▒▒▓▓▒▒▒▒▒▒▓▓▒▒▒▒▓▓▓▓▓▓▒▒                                                      
                                                                              ▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████▒▒▒▒▓▓▒▒▒▒▒▒▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓                                                      
                                                                            ░░▓▓▓▓██▓▓▒▒▓▓▓▓▓▓▓▓▓▓▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▓▓▓▓▓▓▓▓▓▓                                                      
                                                                            ▒▒▓▓▓▓██▒▒▒▒░░▒▒▓▓▓▓▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▓▓▓▓▒▒▒▒                                                      
                                                                            ▒▒▒▒▓▓▓▓▒▒▒▒░░▒▒▒▒░░▓▓▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒░░                                                      
                                                                            ░░▒▒▓▓▓▓▒▒▒▒▒▒▓▓▒▒▓▓▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓                                                        
                                                                            ░░▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓                                                        
                                                                          ░░▒▒██▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒                                                        
                                                                      ░░  ▒▒▓▓▒▒▓▓██▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒                                                          
                                                                      ░░░░▓▓▓▓▓▓▒▒▓▓▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▓▓▓▓▓▓▓▓                                                          
                                                                        ▓▓▓▓▓▓██▓▓▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓▒▒▓▓▓▓▓▓▓▓▓▓▒▒░░                                                          
                                                                    ▒▒▓▓▓▓▓▓▒▒░░▓▓▒▒▒▒▓▓▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒▓▓▓▓▓▓                                                            
                                                                ░░▓▓▓▓▓▓▓▓▒▒  ▓▓▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓▒▒▓▓▒▒▓▓▓▓▓▓▒▒░░                                                            
                                                              ▒▒▓▓▓▓▒▒    ▒▒  ▓▓▒▒▓▓▓▓▒▒▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒▓▓▒▒▓▓▓▓▓▓▓▓                                                              
                                                          ▒▒▓▓▓▓▒▒        ░░▓▓▒▒▒▒▒▒████▒▒▓▓▒▒▓▓▒▒▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓                                                                
                                                      ░░▓▓▓▓▓▓              ▓▓▒▒▓▓██▓▓██▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░                                                                
                                                  ░░▓▓▓▓▓▓                ▒▒▒▒▒▒▓▓▓▓▓▓████▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒▓▓                                                                                                                                                                                                                                                                                  
""")
        vidaInimigo=100
        dtInimigo=19
        danoInimigo=10
        modificadorInimigo=2
        esquivaInimigo=-5
        expbosscheck=1

        print("Ele parece mais lento, mas mais resistente que você.")
        input("Pressione enter para continuar ->")

def Boss():
    ApagarCs()
    print("Uma sala ampla se encontra a sua frente, e uma figura está a sua espera.")
    time.sleep(1)
    print("\nEle bloqueia o seu caminho.")
    time.sleep(1)
    print("\n...")
    time.sleep(1)
    input("\nPressione enter para continuar ->\n")

    GerarBoss()
    Combate()


        

Menu()
GerarMapa(tamanho)

while(op!=0 and vida>0):
    for i in range(tamanho):
        for j in range(tamanho):
            if(mapa[i][j]=="X"):
                x = j
                y = i
    ApagarCs()
    MostrarPontos()
    MostrarMapa()

    if(salas[y][x]==9):
        PontoSala()
        Boss()
        ProximoAndar()
        

    elif(salas[y][x]==8):
        PontoSala()
        CriarInimigo()
        op=Combate()
        salas[y][x]=1

    elif(salas[y][x]==7):
        PontoSala()
        CriarInimigo()
        op=Armadilha()
        salas[y][x]=1

    elif(salas[y][x]==6):
        PontoSala()
        Bau()
        salas[y][x]=1

    elif(salas[y][x]==4 or salas[y][x]==5):
        PontoSala()
        Desafio()
        salas[y][x]=1

    else:    
        op = int(input("O que quer fazer?\n\n0 - Encerrar  |  1 - Mover  |  2 - Inventario  |  3 - Status  |  4 - Descansar\n"))
        if(op==1):    
            Mover()
        if(op==2):    
            MostrarInventario()
        if(op==3):    
            MostrarEstatisticas()
        if(op==4):
            Descansar()
        else:
            print("...")
            time.sleep(1)

ApagarCs()
print("\nGAME OVER\n")
time.sleep(1)
print("Jogo criado por Daniel Dwulatka e Gabriel Covalski\n")
print("TOTAL SCORE:", pontos,"\n")