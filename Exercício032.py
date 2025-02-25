
#Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
def eh_bissexto(ano):
    """
    Verifica se um ano é bissexto.

    Args:
        ano (int): O ano a ser verificado.

    Returns:
        bool: True se o ano for bissexto, False caso contrário.
    """

    # Regra 1: Anos divisíveis por 4 são bissextos
    if ano % 4 == 0:
        # Regra 2: Exceção para anos divisíveis por 100
        if ano % 100 == 0:
            # Regra 3: Anos divisíveis por 400 são bissextos
            if ano % 400 == 0:
                return True  # Ano bissexto
            else:
                return False  # Ano não bissexto
        else:
            return True  # Ano bissexto
    else:
        return False  # Ano não bissexto

# Entrada do usuário
ano = int(input("Digite um ano: "))

# Verifica se o ano é bissexto e exibe o resultado
if eh_bissexto(ano):
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano bissexto.")