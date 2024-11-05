biblioteca = [
  "O Primo Basílio",
  "O Casamento Da Minha Filha",
  "A Máquina De Fazer Espanhóis",
  "6",
  "O Tempo E O Vento",
  "A Revolução Dos Bichos",
  "Brida",
  "Casamento De Papel",
  "A Paixão Segundo G.H.",
  "Felicidade Roubada",
  "O Primeiro Dia",
  "Os Maias",
  "A Dama Das Camélias",
  "O Exército De Um Homem Só",
  "As Meninas",
  "O Peste",
  "Feliz Ano Novo",
  "O Nome Da Rosa",
  "O Amor Nos Tempos Do Cólera",
  "Os Irmãos Karamázov",
  "O Ensaio Sobre A Cegueira",
  "Os Sinos Da Noite",
  "A Mulher Que Escreveu A Bíblia",
  "O Casamento",
  "Casamento Em Risco",
  ]
qtd= [
    2,
    5,
    4,
    3,
    10,
    25,
    50,
    1,
    10,
    3,
    5,
    2,
    5,
    1,
    5,
    6,
    8,
    9,
    41,
    5,
    2,
    23,
    1,
    5,
    3,
]
#Função para adicionar um livro
def registrar_livro():
    livro = input("Digite o nome do livro que deseja registrar: ").strip().title()  #Remove os espaços em branco no início e no final, muda a primeira letra de cada palavra para maiúscula
# Verificar se o livro já está registrado
    if livro not in biblioteca:
        while True:
            try:
                quantidade_para_adicionar = int(input("Quantas unidades desse livro você quer adicionar? "))
                if quantidade_para_adicionar > 0:
                    biblioteca.append(livro) # Adicionar livro na lista Biblioeta
                    qtd.append(quantidade_para_adicionar) # Adiconar quantidade a lista  qtd
                    print("O livro " + livro + " foi registrado com sucesso! Quantidade de unidades: " + str(quantidade_para_adicionar) + ".")
                    break
                else:
                    print("Quantidade inválida, digite um número maior que zero!")
            except ValueError:
                print("Quantidade que você digitou está incorreta. Por favor, digite um número!")
    else:
        print("O livro:" + livro + " já está registrado na biblioteca. Se você deseja atualizar a quantidade, utilize a opção 5 para 'Alterar o Estoque")
# Função para emprestar um livro
def emprestar_livro():
    livro = input("Digite o nome do livro que deseja pegar emprestado: ").strip().title()
    if livro in biblioteca:
        posicao_do_livro = biblioteca.index(livro)
        if qtd[posicao_do_livro] > 0:
            qtd[posicao_do_livro] -= 1
            print("O livro " + livro + " foi emprestado com sucesso! Quantidade restante: " + str(qtd[posicao_do_livro]))
        else:
            print("O livro " + livro + " não está disponível!")
    else:
        print("Não encontramos o livro " + livro + " na biblioteca!")

# Função para devolver um livro
def devolver_livro():
    livro = input("Digite o nome do livro que deseja devolver: ").strip().title()
    if livro not in biblioteca:
        biblioteca.append(livro)
        qtd.append(1)
        print("Este livro foi guardado na biblioteca com 1 unidade!")
    else:
        posicao_do_livro = biblioteca.index(livro)
        qtd[posicao_do_livro] += 1
        print("O livro " + livro + " foi devolvido com sucesso! Quantidade atual: " + str(qtd[posicao_do_livro]))

# Função para consultar livros disponíveis
def consultar_livros():
    if len(biblioteca) > 0:
        print("A biblioteca possui um total de " + str(len(biblioteca)) + " livros diferentes:")
        for i in range(len(biblioteca)):
            print("\nTítulo: " + biblioteca[i] + ", quantidade: " + str(qtd[i]))
    else:
        print("A biblioteca está vazia.")

# Função para alterar estoque
def alterar_estoque():
    livro_para_alterar = input("Digite o nome do livro que deseja alterar a quantidade: ").strip().title()
    if livro_para_alterar in biblioteca:
        while True:
            try:
                nova_quantidade = int(input("Digite a nova quantidade para o livro " + livro_para_alterar + ": "))
                if nova_quantidade >= 0:
                    posicao_do_livro = biblioteca.index(livro_para_alterar)
                    qtd[posicao_do_livro] = nova_quantidade
                    print("A quantidade do livro " + livro_para_alterar + " foi alterada para " + str(nova_quantidade) + ".")

                    if nova_quantidade == 0:
                        biblioteca.pop(posicao_do_livro)
                        qtd.pop(posicao_do_livro)
                        print("O livro " + livro_para_alterar + " foi removido da biblioteca.")
                    break
                else:
                    print("Quantidade inválida. Por favor, digite um número maior ou igual a zero.")
            except ValueError:
                print("Quantidade inválida. Por favor, digite um número!")
    else:
      print("O livro '" + livro_para_alterar + "'não foi encontrado na biblioteca. Se você deseja adicioná-lo, por favor, utilize a opção 1 para 'Registrar Livro'")

# Função para buscar livros por palavra-chave
def buscar_por_palavra_chave():
    livros_encontrados = []
    palavra_chave = input("Digite a palavra-chave que deseja buscar: ").strip().lower()

    for livro in biblioteca:
        if palavra_chave in livro.lower():
            livros_encontrados.append(livro)
    if len(livros_encontrados) > 0:
        print("Livros encontrados:")
        for resultado in livros_encontrados:
            print(resultado)
    else:
        print("Nenhum livro encontrado com a palavra-chave: " + palavra_chave)



# Função principal para gerenciamento da biblioteca
def gerenciamento_biblioteca():
    while True:
        print("\nDigite a opção desejada: \n 1. Registrar livros \n 2. Emprestar livros \n 3. Devolver livros \n 4. Consultar livros disponíveis \n 5. Alterar Estoque \n 6. Busca por palavra-chave \n 0. Sair do sistema")
        opcao = input()

        if opcao == "1":
            registrar_livro()
        elif opcao == "2":
            emprestar_livro()
        elif opcao == "3":
            devolver_livro()
        elif opcao == "4":
            consultar_livros()
        elif opcao == "5":
            alterar_estoque()
        elif opcao == "6":
            buscar_por_palavra_chave()
        elif opcao == "0":
            print("Programa Finalizado")
            break
        else:
            print("Opção inválida.")
gerenciamento_biblioteca()