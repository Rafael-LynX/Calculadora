linha = "-----------------------------------------------"

# Função de Soma
def soma():
    try:
        resultado = num1+num2
        print(f"{num1} + {num2} = {resultado}")
        print(linha)
    except ValueError:
        print("Você não digitou número")
        print(linha)
    except Exception as error:
        print("Algum erro Inesperado ocorreu")
        print(error)

# Função de Subtração
def subtracao():
    try:
        resultado = num1-num2
        resultado2 = num2-num1
        print(f"{num1} - {num2} = {resultado}")
        print(f"{num2} - {num1} = {resultado2}")
        print(linha)
    except ValueError:
        print("Você não digitou número")
        print(linha)
    except Exception as error:
        print("Algum erro Inesperado ocorreu")
        print(error)

# Função de Divisão
def divisao():
    try:
        resultado = num1 / num2
        resultado2 = num2 / num1
        print(f"{num1} / {num2} = {resultado:.2f}")
        print(f"{num2} / {num1} = {resultado2:.2f}")
    except ValueError:
        print("Você não digitou número")
        print(linha)
    except Exception as error:
        print("Algum erro Inesperado ocorreu")
        print(error)

# Função de Multiplicação
def multiplicacao():
    try:
        resultado = num1 * num2
        print(f"{num1} x {num2} = {resultado}")
        print(linha)
    except ValueError:
        print("Você não digitou número")
        print(linha)
    except Exception as error:
        print("Algum erro Inesperado ocorreu")
        print(error)

# Função de Elevação
def exponeciacao():
    try:
        resultado = num1 ** num2
        print(f"{num1} ^ {num2} = {resultado}")
        print(linha)
    except ValueError:
        print("Você não digitou número")
        print(linha)
    except Exception as error:
        print("Algum erro Inesperado ocorreu")
        print(error)

# Função de Resto
def resto():
    try:
        resultado = num1 % num2
        print(f"{num1} % {num2} = {resultado}")
        print(linha)
    except ValueError:
        print("Você não digitou número")
        print(linha)
    except Exception as error:
        print("Algum erro Inesperado ocorreu")
        print(error)

# Função de Divisão Inteira
def divisao_inteira():
    try:
        resultado = num1 // num2
        resultado2 = num2 // num1
        print(f"{num1} // {num2} = {resultado:.2f}")
        print(f"{num2} // {num1} = {resultado2:.2f}")
    except ValueError:
        print("Você não digitou número")
        print(linha)
    except Exception as error:
        print("Algum erro Inesperado ocorreu")
        print(error)

# Função de Desconto
def descontos():
    try:
        valor = float(input("Valor Original: "))
        desconto = float(input("Valor do Desconto: "))
        valor_do_desconto = (valor*desconto) / 100
        a_pagar = valor - valor_do_desconto
        print(f"Valor = {valor}")
        print(f"Desconto = {valor_do_desconto:.2f}")
        print(f"Valor com Desconto = {a_pagar:.2f}")
        print(linha)
    except ValueError:
        print("Você não digitou número")
        print(linha)
    except Exception as error:
        print("Algum erro Inesperado ocorreu")
        print(error)

# Função de Bem vindo
def welcome():
    print("------- Welcome -------")

# Função Menu
def menu():
    welcome()
    print("1 - [+] Soma [+]")
    print("2 - [-] Subtração [-]")
    print("3 - [/] Divisão [/]")
    print("4 - [*] Multiplicação [*]")
    print("5 - [**] Exponenciação [**]")
    print("6 - [%] Resto [%]")
    print("7 - [//] Divisão Inteira [//]")
    print("8 - [*/] Desconto [*/]")
    print("0 - Sair")
    print(linha)

# Inicio do Programa
while True:
    menu()
    opcao = input("Escolha uma opção: ")
    if opcao == "0":
        print("Fechando o Programa")
        break
    if opcao == "8":
        descontos()
        continue
    print(linha)
    num1 = int(input("Digite o Primeiro Número: "))
    num2 = int(input("Digite o Segundo Número: "))
    print(linha)
    if opcao == "1":
        soma()
    elif opcao == "2":
        subtracao()
    elif opcao == "3":
        divisao()
    elif opcao == "4":
        multiplicacao()
    elif opcao == "5":
        exponeciacao()
    elif opcao == "6":
        resto()
    elif opcao == "7":
        divisao_inteira()
    else:
        print("Opção Invalida")






