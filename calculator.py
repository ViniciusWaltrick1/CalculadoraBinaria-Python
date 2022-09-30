from typing import BinaryIO

print(""" Escolha sua base principal: 
[1] Binario
[2] Octal
[3] Decimal
[4] HexaDecimal""")
base = int(input("Digite a sua base: "))
if base == 1:
    operation = int(input("""operacaoes: 
    [1] Conversoes
    [2] Soma
    [3] Subtracao
    Escolha a operacao: """))
    if operation == 1:  
        choose = int(input("""Conversoes disponiveis : 
        [1] converter para Octal
        [2] converter para Decimal
        [3] converter para HexaDecimal
        [4] converter para todas as bases
        Escolha a base para a conversao: """))
        if choose == 1:
            try:
                num = int(input("Digite um numero binario: "), 2)
                print("Seu binario {} em formato octal e: {}".format(bin(num)[2:], oct(num)[2:]))
            except ValueError:
                print("Por favor, digite apenas numeros binarios!")
        elif choose == 2:
            try:
                num = int(input("Digite um numero binario: "), 2)
                print("Seu binario {} em formato decimal e: {}".format(bin(num)[2:], num))
            except ValueError:
                print("Por favor, digite apenas numeros binarios!")
        elif choose == 3:
            try:
                num = int(input("Digite um numero binario: "), 2)
                print("Seu binario {} em hexadecimal e: {} ".format(bin(num)[2:], hex(num)[2:]))
            except ValueError:
                print("Por favor, digite apenas numeros binarios!")
        elif choose == 4:
            try:
                num = int(input("Digite um numero binario: "), 2)
                print("Seu binario e: {}".format(bin(num)[2:]))
                print("Seu binario {} em formato octal e: {}".format(bin(num)[2:], oct(num)[2:]))
                print("Seu binario {} em formato decimal e: {}".format(bin(num)[2:], num))
                print("Seu binario {} em hexadecimal e: {} ".format(bin(num)[2:], hex(num)[2:]))
            except ValueError:
                print("Por favor, digite apenas numeros binarios!")
        else:
            print("Opcao invalida, fechando o programa!")
    elif operation == 2:
        try:
            num = int(input("Digite o primeiro binario: "), 2)
            num_1 = int(input("Digite o segundo binario: "), 2)
            plus = bin(num + num_1)
            print("Sua soma binaria {} + {} = {}".format(bin(num)[2:], bin(num_1)[2:], plus[2:]))
        except ValueError:
            print("Digite um Numero Binario! Fechando o Programa!")
    elif operation == 3:
        try:
            num = int(input("Digite o primeiro binario: "), 2)
            num_1 = int(input("Digite o segundo binario: "), 2)
            minus = bin(num - num_1)
            print("Sua subtracao binaria {} - {} = {}".format(bin(num)[2:], bin(num_1)[2:], minus[2:]))
        except ValueError:
            print("Digite um Numero Binario! Fechando o Programa!")
    else:
        print("Opcao invalida, fechando o programa!")
elif base == 2:
    operation = int(input("""operacaoes: 
    [1] Conversoes
    [2] Soma
    [3] Subtracao
    Escolha a operacao: """))
    if operation == 1:  
        choose = int(input("""Conversoes disponiveis : 
        [1] converter para Binario
        [2] converter para Decimal
        [3] converter para HexaDecimal
        [4] converter para todas as bases
        Escolha a base para a conversao: """))
        if choose == 1:
            try:
                num = int(input("Digite um numero octal:"), 8)
                print("Seu octal {} convertido para binario e: {}".format(oct(num)[2:], bin(num)[2:]))
            except ValueError:
                print("Por favor, digite apenas numeros octais!")
        elif choose == 2:
            try:
                num = int(input("Digite um numero octal:"), 8)
                print("Seu octal {} convertido para decimal e: {}".format(oct(num)[2:], num))
            except ValueError:
                print("Por favor, digite apenas numeros octais!")
        elif choose == 3:
            try:
                num = int(input("Digite um numero octal:"), 8)
                print("Seu octal {} convertido para hexadecimal e: {}".format(oct(num)[2:], hex(num)[2:]))
            except ValueError:
                print("Por favor, digite apenas numeros octais!")
        elif choose == 4:
            try:
                num = int(input("Digite um numero octal: "), 8)
                print("Seu octal e: {}".format(bin(num)[2:]))
                print("Seu octal {} em formato binario e: {}".format(oct(num)[2:], bin(num)[2:]))
                print("Seu octal {} em formato decimal e: {}".format(oct(num)[2:], num))
                print("Seu octal {} em hexadecimal e: {} ".format(oct(num)[2:], hex(num)[2:]))
            except ValueError:
                print("Por favor, digite apenas numeros binarios!")
        else:
            print("Opcao invalida, fechando o programa!")
    elif operation == 2:
        try:
            num = int(input("Digite o primeiro octal: "), 8)
            num_1 = int(input("Digite o segundo octal: "), 8)
            plus = oct(num + num_1)
            print("Sua soma octal {} + {} = {}".format(oct(num)[2:], oct(num_1)[2:], plus[2:]))
        except ValueError:
            print("Digite um Numero Octal! Fechando o Programa!")
    elif operation == 3:
        try:
            num = int(input("Digite o primeiro octal: "), 8)
            num_1 = int(input("Digite o segundo octal: "), 8)
            minus = oct(num - num_1)
            print("Sua subtracao octal {} - {} = {}".format(oct(num)[2:],oct(num_1)[2:],minus[2:]))
        except ValueError:
            print("Digite um Numero Octal! Fechando o Programa!")
    else:
        print("Opcao invalida, fechando o programa!")
elif base == 3:
    operation = int(input(""" Operacoes:
    [1] Conversoes
    [2] Soma
    [3] Subtracao
    Escolha a operacao: """))
    if operation == 1:
        choose = int(input("""Conversoes disponiveis : 
        [1] converter para Binario 
        [2] converter para octal
        [3] converter para hexadecimal
        [4] converter para todas as bases
        Escolha a base para a conversao: """))
        if choose == 1:
            try:
                num = int(input("Digite um numero decimal: "))
                print(" Seu decimal {} convertido para binario e igual a {}".format(num, bin(num)[2:]))
            except ValueError:
                print("Digite um valor decimal! fechando o programa!")
        elif choose == 2:
            try:
                num = int(input("Digite um numero decimal: "))
                print("Seu decimal {} convertido para octal e igual a {}".format(num, oct(num)[2:]))
            except ValueError:
                print("Digite um valor decimal! fechando o programa!")
        elif choose == 3:
            try:
                num = int(input("Digite um numero decimal: "))
                print("Seu decimal {} convertido para hexadecimal e igual a {}".format(num, hex(num)[2:]))
            except ValueError:
                print("Digite um valor decimal! fechando o programa!")
        elif choose == 4:
            try:
                num = int(input("Digite um numero decimal: "))
                print("Seu decimal e {}".format(num))
                print("Seu decimal {} convertido para binario e igual a {}".format(num, bin(num)[2:]))
                print("Seu decimal {} convertido para octal e igual a {}".format(num, oct(num)[2:]))
                print("Seu decimal {} convertido para hexadecimal e igual a {}".format(num, hex(num)[2:]))
            except ValueError:
                print("Digite um valor decimal! fechando o programa!")
        else:
            print("Opcao invalida, selecione uma opcao valida!")
    elif operation == 2:
        num = int(input("Digite o primeiro valor: "))
        num_1 = int(input("Digite o segundo valor: "))
        plus = num + num_1
        print("Sua soma em decimal e: ", plus)
    elif operation == 3:
        num = int(input("Digite o primeiro valor: "))
        num_1 = int(input("Digite o segundo valor: "))
        minus = num - num_1
        print("Sua subtracao em decimal e: ", minus)
    else:
        print("Opcao invalida, fechando o programa!")
elif base == 4:
    operation = int(input(""" Operacoes:
    [1] Conversoes
    [2] Soma
    [3] Subtracao
    Escolha a operacao: """))
    if operation == 1:
        choose = int(input("""Conversoes disponiveis : 
        [1] converter para Binario 
        [2] converter para octal
        [3] converter para decimal
        [4] converter para todas as bases
        Escolha a base para a conversao: """))
        if choose == 1:
            try:
                num = int(input("Digite um numero hexadecimal: ") ,16)
                print("Seu hexadecimal {} convertido em binario e: {}".format(hex(num)[2:], bin(num)[2:]))
            except ValueError:
                print("Por favor, digite apenas numeros HexaDecimais!")
        elif choose == 2:
            try:
                num = int(input("Digite um numero hexadecimal: ") ,16)
                print("Seu hexadecimal {} convertido para octal e: {}".format(hex(num)[2:],oct(num)[2:]))
            except ValueError:
                print("Por favor, digite apenas numeros octais!")
        elif choose == 3:
            try:
                num = int(input("Digite um numero hexadecimal: ") ,16)
                print("Seu hexadecimal {} convertido para decimal e: {}".format(hex(num)[2:],num))
            except ValueError:
                print("Por favor, digite apenas numeros octais!")
        elif choose == 4:
            try:
                num = int(input("Digite um numero hexadecimal: "), 16)
                print("Seu hexadecimal e: {}".format(hex(num)[2:]))
                print("Seu hexadecimal {} em formato binario e: {}".format(hex(num)[2:], bin(num)[2:]))
                print("Seu hexadecimal {} em formato octal e: {}".format(hex(num)[2:], oct(num)[2:]))
                print("Seu hexadecimal {} em decimal e: {} ".format(hex(num)[2:], num))
            except ValueError:
                print("Por favor, digite apenas numeros binarios!")
        else:
            print("Opcao invalida, fechando o programa!")
    elif operation == 2:
        try:
            num = int(input("Digite o primeiro hexadecimal: "), 16)
            num_1 = int(input("Digite o segundo hexadecimal: "), 16)
            plus = hex(num + num_1)
            print("Sua soma hexadecimal {} + {} = {}".format(hex(num)[2:], hex(num_1)[2:], plus[2:]))
        except ValueError:
            print("Digite um Numero hexadecimal! Fechando o Programa!")
    elif operation == 3:
        try:
            num = int(input("Digite o primeiro hexadecimal: "), 16)
            num_1 = int(input("Digite o segundo hexadecimal: "), 16)
            minus = hex(num - num_1)
            print("Sua subtracao hexadecimal {} - {} = {}".format(hex(num)[2:],hex(num_1)[2:],minus[2:]))
        except ValueError:
            print("Digite um Numero hexadecimal! Fechando o Programa!")
    else:
        print("Opcao invalida, fechando o programa!")
else:
    print("Opcao invalida, fechando o programa!")