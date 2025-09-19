import random  # Biblioteca para escolher aleatoriamente uma palavra

def jogar():
    imprime_mensagem_abertura()

    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:
        chute = pede_chute()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        print('Você ganhou!')
    else:
        print('Você perdeu!')
    print('Fim do jogo')

def pede_chute():
    chute = input('Qual a letra? ')
    chute = chute.strip().lower()
    return chute

def imprime_mensagem_abertura():
    print('*****************************************************')
    print('****************** Bem-vindo ao jogo de forca *******')
    print('*****************************************************')

def carrega_palavra_secreta(nome_do_arquivo='palavras_forca.txt'):
    try:
        with open(nome_do_arquivo, 'r') as arquivo:
            palavras = [linha.strip().lower() for linha in arquivo]
    except FileNotFoundError:
        print(f"Arquivo {nome_do_arquivo} não encontrado.")
        exit()
    
    palavra_secreta = random.choice(palavras)
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ['_' for letra in palavra]

# Inicia o jogo
jogar()