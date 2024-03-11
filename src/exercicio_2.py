def verifica_fibonacci(numero):
    ## Inicializa os dois primeiros números da sequência ##
    fibonacci_atual = 0
    fibonacci_proximo = 1
    
    ## Loop para gerar a sequência de Fibonacci até ultrapassar o número informado ##
    while fibonacci_atual <= numero:
        ## Verifica se o número atual é igual ao número informado ##
        if fibonacci_atual == numero:
            return True  
            
        ## Atualiza os valores para o próximo número da sequência ##
        fibonacci_atual, fibonacci_proximo = fibonacci_proximo, fibonacci_atual + fibonacci_proximo
    
    # Se o número informado não estiver na sequência, retorna False
    return False

## Solicita ao usuário um número para verificar se pertence à sequência de Fibonacci ##
numero = int(input("Informe um número: "))

## Chama a função para verificar se o número pertence à sequência de Fibonacci e printa a mensagem ##
if verifica_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
