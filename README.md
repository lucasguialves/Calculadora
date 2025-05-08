# Calculadora
Meu primeiro codigo em python, estudo colocando codigo para rodar no linux.

## Como Executar um Arquivo .sh no Linux

-  Acesse o Diretório do Arquivo
Abra o terminal e navegue até o diretório onde o arquivo .sh está localizado.

-  Conceda Permissão de Execução ao Arquivo
Antes de executar o script, é necessário conceder permissão de execução. Isso pode ser feito com o comando:

chmod +x nome_do_arquivo.sh

isso permite que o sistema reconheça o arquivo como executável. 

-  Execute o Script
Agora, você pode executar o script de duas maneiras:

Executar Diretamente
./nome_do_arquivo.sh
Ou
./indica que o script está no diretório atual. 

-  Executar com Privilégios de Superusuário (se necessário)
Se o script requerer permissões elevadas (por exemplo, para instalar software), você pode executá-lo com o sudo:

sudo ./nome_do_arquivo.sh
O sistema solicitará sua senha para confirmar a execução com privilégios de superusuário.

## Documentação do Código da Calculadora

- Descrição Geral
Este programa é uma calculadora interativa que permite ao usuário realizar operações aritméticas básicas (soma, subtração, multiplicação e divisão) repetidamente até que escolha encerrar o programa. Utiliza um loop while para manter a interação contínua e inclui tratamento de erros para entradas inválidas.
Academia Hopper

- Estrutura do Código
Exibição do Menu de Operações

O programa apresenta um menu com as opções de operações disponíveis:


print("\nCalculadora usando while")

print("Escolha a operação:")

print("1 Soma")

print("2 Subtração")

print("3 Multiplicação")

print("4 Divisão")

print("5 Sair")

O usuário é solicitado a escolher uma operação digitando o número correspondente.


- Entrada da Operação Desejada


A operação escolhida pelo usuário é capturada com a função input():


digito = input("Digite o número da operação desejada: ")


Encerramento do Programa


Se o usuário digitar "5", o programa exibe uma mensagem de desligamento e encerra o loop com a instrução break:


if digito == "5":

    print("Calculadora desligada")
    
    break
    
Validação da Operação


Caso o usuário digite uma opção inválida (diferente de "1", "2", "3" ou "4"), o programa informa que a opção é inválida e solicita uma nova entrada:


if digito not in ["1", "2", "3", "4"]:

    print("Opção inválida. Tente novamente.")
    
    continue
    
Entrada dos Números para a Operação


O programa solicita ao usuário que digite dois números para realizar a operação desejada:


try:

    num1 = float(input("Digite o primeiro número: "))
    
    num2 = float(input("Digite o segundo número: "))
    
except ValueError:

    print("Entrada inválida. Use apenas números.")
    
    continue
    
Caso o usuário insira um valor não numérico, o programa captura a exceção ValueError e solicita novamente a entrada.


- Execução da Operação Selecionada
- 

Dependendo da escolha do usuário, o programa realiza a operação correspondente:


Soma:


if digito == "1":

    resultado = num1 + num2
    
    print(f"Resultado: {num1} + {num2} = {resultado}")
    
Subtração:


elif digito == "2":

    resultado = num1 - num2
    
    print(f"Resultado: {num1} - {num2} = {resultado}")
    
Multiplicação:


elif digito == "3":

    resultado = num1 * num2
    
    print(f"Resultado: {num1} * {num2} = {resultado}")

elif digito == "4":

    if num2 == 0:
    
        print("Erro: Divisão por zero não permitida.")
        
    else:
    
        resultado = num1 / num2
        
        print(f"Resultado: {num1} / {num2} = {resultado}")

        
Na operação de divisão, há uma verificação adicional para evitar a divisão por zero, que causaria um erro de execução.

- Considerações Finais

Uso do Loop while True: O loop while True é utilizado para criar um loop infinito que só será interrompido quando o usuário escolher a opção de encerrar o programa. É importante garantir que haja uma condição de saída para evitar que o programa fique em execução indefinida. 

