def leiaInteiro(mensagem):
    inteiro = False

    while not inteiro:
        try:
            numInt = int(input(mensagem))

        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido!\033[m')
            continue

        except (KeyboardInterrupt):
            return print('\033[33mEntrada de dados interrompida pelo usuário!\033[m')

        else:
            inteiro = True
            return numInt


def leiaFloat(mensagem):
    fração = False

    while not fração:
        try:
            numReal = float(input(mensagem))

        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número real válido.\033[m')
            continue

        except (KeyboardInterrupt):
            return print('\033[33mEntrada de dados interrompida pelo usuário.\033[m')

        else:
            fração = True
            return numReal
