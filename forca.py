from funcoes import limpar_tela, menu_apresentacao, ganhou, perdeu
import time

limpar_tela()
menu_apresentacao()
time.sleep(1)
limpar_tela()

nome_desafiante = input("Quem vai desafiar? ")
nome_desafiado = input("Quem vai ser desafiado? ")

limpar_tela()

print("As seguintes informações devem ser completadas pelo DESAFIANTE: ")
palavra_chave = input("\nDigite a PALAVRA CHAVE: ").lower().strip()
dica1 = input("\nDigite a DICA 1: ")
dica2 = input("\nDigite a DICA 2: ")
dica3 = input("\nDigite a DICA 3: ")

letras_digitadas = []
erros = 0
letras_certas = []
limpar_tela()

palavra_escondida = ''
palavra_escondida = palavra_escondida * len(palavra_chave)
print("Bem VindoX", nome_desafiado)
print('\nA palavra escolhida por', nome_desafiante, 'é:', palavra_escondida)

while True:
    key = ''
    for letra in palavra_chave:
        key += letra if letra in letras_certas else "_ "
    print(key)       
    if key == palavra_chave:
        ganhou()
        break
    print ('''\nDigite "0" para receber dicas''')
    tentativa = input("\nDigite uma letra:").lower().strip()
    limpar_tela()
    if tentativa == '0':
        escolher_dica = input ('''
(1) Para a dica 1.
(2) Para a dica 2.
(3) Para a dica 3.

Selecione uma opção: ''' )
        if escolher_dica == "1":
            print('\nDica 1: ',dica1)
            time.sleep(3)
            limpar_tela()
        elif escolher_dica == '2':
            print('\nDica 2: ',dica2)
            time.sleep(3)
            limpar_tela()
        elif escolher_dica == '3':
            print('\nDica 3: ',dica3)
            time.sleep(3)
            limpar_tela()
        else:
            print("Opção inválida!\n")
            time.sleep(3)
            limpar_tela()
    try: 
        letras_digitadas
    except:
        print("Caracter inválido!\n")

    if tentativa in letras_digitadas:
        print("Você já tentou essa letra!\n")
    else:
         letras_digitadas += tentativa
    
    if tentativa in palavra_chave or tentativa == '0':
        letras_certas += tentativa
    else:
        erros += 1
        print ("Essa letra não está na palavra!\n")

    if erros >= 6:
        print('''Voce perdeu!!!!!
    I==:==
    I  :
    I  O
    I \|/           Enforcado Amigão!
    I / \ 
    ===========
    ''')
        break

    print("I==:==\nI  :   ") 
    print("I  O   " if erros >= 1 else "I")
    linha2 = ""
    if erros == 2:
            linha2 = "  |   "
    elif erros == 3:
            linha2 = " \|   "
    elif erros >= 4:
            linha2 = " \|/ "
    print("I%s" % linha2)
    linha3 = ""
    if erros == 5:
        linha3 = " /     "
    elif erros >= 6:
        linha3 = " / \ "
    print("I%s" % linha3)
    print("I\n===========")
    if erros == 6:
        print("Enforcado Amigão!")
        break
limpar_tela()
if key == palavra_chave:
        ganhou()
        time.sleep(3)
        limpar_tela()
else:
    perdeu()
    time.sleep(3)
    limpar_tela()
registro = open("registro.txt","w")
registro.write("A Palavra chave era: %s \n" % palavra_chave)

if key == palavra_chave:
    registro.write("O Vencedor foi...: %s \n" % nome_desafiado)
else:
    registro.write("O Vencedor foi...: %s \n" % nome_desafiante)
    
registro = open("registro.txt","r")
conteudo = registro.read()
print(conteudo)