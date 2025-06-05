from ouvidoria import *
from operacoesbd import *

menu=["Listar tudo", "Listar por tipo", "Criar feedback", "Ver quantidade", "Pesquisar por código", "Excluir por código", "Sair"]
tipos=["Reclamação", "Sugestão", "Elogio"]

opcao=0

conexao=criarConexao("localhost", "root", "root", "ouvidoria")

print("Bem vindo(a) a nossa Central de Atendimento!")

while opcao!=7:  
    print("\nEscolha uma opção abaixo:")
    for p, i in enumerate(menu):
        print(f"{p+1} - {i}")

    opcao=int(input("Digite o número da sua escolha: "))

    if opcao==1:
        listarFeedbacks(conexao)

    elif opcao==2:
        listaPorTipo(conexao, tipos)
    
    elif opcao==3:
        criarFeedbacks(conexao, tipos)
    
    elif opcao==4:
        quantidadeFeedbacks(conexao)

    elif opcao==5:
        pesquisarPorCodigo(conexao)

    elif opcao==6:
        excluirPorCodigo(conexao)

    elif opcao!=7:
        print("\nOpção inválida. Tente novamente!")

encerrarConexao(conexao)
print("\nObrigado por utilizar nossos serviços!")

