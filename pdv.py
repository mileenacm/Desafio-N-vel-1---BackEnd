
historico_compras = []

maquina = True

while maquina: 

    print("@--------------------------------------------@\n")
    print(" SISTEMA PARA CALCULAR DESCONTOS PROGRESSIVOS\n")
    print("@--------------------------------------------@\n")
    print("1 - Digitar a idade e o valor da compra\n")
    print("2 - Entender as regras de aplicação de desconto\n")
    print("3 - Sair e ver Resumo do dia\n")
    print("@---------------------------------------------@\n")

    choice = int(input("Insira uma opção:  \n"))


    match choice:

        case 1:

            compra = True
            while compra:    
                
                idade = int(input("Por favor, digite sua idade: \n")) 
                valor = float(input("Informe o valor da compra (ou digite 0 para finalizar): \n"))

                if valor == 0 or idade == 0:
                    print("Encerrando o loop de compras e o sistema.\n")
                    print("Obrigada por utilizar o sistema!\n")
                    break
                if valor < 0 or idade < 0:
                    print("Inválido")
                    continue

                valor_novo = valor

                if idade >= 65:
                    valor_novo = valor * 0.8
                        
                    if valor_novo > 100:
                        valor_novo = valor_novo * 0.9
                        print(f"\nValor final com desconto extra de 10%: {valor_novo:0.2f}\n")
                        
                    else:
                        print(f"\nNovo valor com desconto pela idade: {valor_novo:0.2f}\n")
                        


                elif idade < 65 and valor > 100:
                        valor_novo = valor * 0.9
                        print(f"\nValor com desconto de 10%: {valor_novo:0.2f}\n")

                else:
                    print(f"Nenhum desconto foi aplicado: {valor:0.2f}")

                    
                historico_compras.append({
                    "bruto": valor,
                    "final": valor_novo
                })

                escolha = int(input("Deseja continuar? (0/1 - Não/Sim)"))
                print("\n")
                if escolha == 0:
                    compra = False
                else:
                    compra = True
                
            

        case 2:
            print("-----------------------------------------------")
            print("                     REGRAS                    \n")
            print("Se a sua idade for maior ou igual a 65 anos\n")
            print("você tem direito a 20% de desconto.")
            print("\n")
            print("Se o valor da sua compra for maior que 100 reais\n")
            print("você tem direito a 10% de desconto.")
            print("\n")
            print("Os descontos são aplicados sucessivamente caso\n")
            print("você se aplique às duas condições.\n")
            print("-----------------------------------------------")
            print("\n")

            answer = int(input("Deseja retornar ao menu? (0/1 - Não/sim) "))
            if answer == 0:
                maquina = False
            else:
                maquina = True


        case 3:
            print("Obrigada por utilizar o sistema!\n")
        
            print("@--------------------------------------------@\n")
            print("              RESUMO DO DIA                  ")
            print("\n@--------------------------------------------@\n")

            qtd_compras = len(historico_compras)

            total_bruto = sum(compra["bruto"] for compra in historico_compras)
            total_final = sum(compra["final"] for compra in historico_compras)
            total_descontos = total_bruto - total_final

            print(f"Quantidade de compras registradas: {qtd_compras}\n")
            print(f"Total bruto (sem descontos): R$ {total_bruto:0.2f}\n")
            print(f"Total de descontos concedidos: R$ {total_descontos:0.2f}\n")
            print(f"Total arrecadado do dia: R$ {total_final:0.2f}\n")
            maquina = False

