#Script de calculadora com expressões lambda - Author Ricardo Euclides

opcao = int(input("Calculadora Python******\nSelecionar a operação===>> 1- Adição, 2- Subtração, 3- Multiplicação, 4- Divisão :"))

arg1 = int(input("Digite o primeiro número: "))
arg2 = int(input("Digite o segundo número: "))

if opcao == 1:
    resultado = lambda arg1, arg2: arg1+arg2
    print("O resultado é: ", resultado(arg1,arg2))
    
elif opcao == 2:
    resultado = lambda arg1, arg2: arg1-arg2
    print("O resultado é: ", resultado(arg1,arg2))
    
elif opcao == 3:
    resultado = lambda arg1, arg2: arg1*arg2
    print("O resultado é: ", resultado(arg1,arg2))
    
elif opcao == 4:
    resultado = lambda arg1, arg2: arg1/arg2
    print("O resultado é: ", resultado(arg1,arg2))
    
else:
    print("Opção Inválida! Escolher outra.")
    