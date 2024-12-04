# Discentes: Amanda Martins, Julio Cesar, Letícia Fonseca, Mateus Gabriel.

# ---- FILAS ----
fila = [] #Inicializa a fila como uma lista vazia.

def entrar_na_fila(cliente): #Função para adicionar um cliente à fila.
    fila.append(cliente)
    print(f"{cliente} entrou na fila.")

def atender_cliente(): #Função para atender o próximo cliente.
    if len(fila) == 0:
        print("A fila está vazia. Nenhum cliente para atender.")
    else:
        cliente = fila.pop(0)
        print(f"{cliente} foi atendido.")
        
def mostrar_fila(): #Função para exibir a fila atual.
    if len(fila) == 0:
        print("A fila está vazia.")
    else:
        print("Fila atual:", fila)

entrar_na_fila("João") #Demonstração do sistema.
entrar_na_fila("Maria")
entrar_na_fila("Carlos")

mostrar_fila()

atender_cliente()
mostrar_fila()

atender_cliente()
atender_cliente()
atender_cliente()

# ---- PILHAS ----
historico = [] #Pilha para armazenar o histórico

def adicionar_interacao(pilha, interacao): #Adiciona uma nova interação ao histórico.
    pilha.append(interacao)
    print(f"Interação adicionada: {interacao}")

def desfazer_interacao(pilha): #Remove a última interação adicionada.
    if pilha:
        interacao_desfeita = pilha.pop()
        print(f"Interação desfeita: {interacao_desfeita}")
    else:
        print("Nenhuma interação para desfazer.")

def mostrar_historico(pilha): #Exibe o histórico completo.
    
    if len(pilha) > 0:  #Verifica se a pilha não está vazia.
        print("Histórico de interações:")
        for i in range(len(pilha)): #Itera sobre a pilha.
            print(i + 1, ": ", pilha[i]) #Exibe o índice começando de 1.
    else:
        print("Histórico vazio.")


#Exemplos de uso.
adicionar_interacao(historico, "Usuário clicou no botão 'Início'")
adicionar_interacao(historico, "Usuário abriu a seção 'Configurações'")
adicionar_interacao(historico, "Usuário alterou a senha")

mostrar_historico(historico)

desfazer_interacao(historico)
desfazer_interacao(historico)

mostrar_historico(historico)
