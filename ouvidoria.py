from operacoesbd import *

def listarFeedbacks(conexao):
    sql="select * from feedbacks"
    feedbacks = listarBancoDados(conexao,sql)
    if feedbacks:
        print(f"\nLista de Feedbacks")
        for i in feedbacks:
            print(f"{i[0]} - Assunto: {i[1]} | Descrição: {i[2]} | Autor: {i[3]} | Tipo: {i[4]}")
    else:
        print("\nNão existem feedbacks registrados.")


def listarPorTipo(conexao, tipos):
    sql="select * from feedbacks where tipo=%s"

    print("\nQual tipo desejar vizualizar?")
    for p, i in enumerate(tipos):
        print(f"{p+1} - {i}")
    
    try:
        opcao=tipos[int(input("Digite o número da sua escolha: "))-1]
    except IndexError:
        print("Opção inválida. Tente novamente!")
        return
        
    dados=[opcao]

    feedbacks = listarBancoDados(conexao, sql, dados)
    if feedbacks:
        print(f"\nLista de Feedbacks ({opcao})")
        for i in feedbacks:
            print(f"{i[0]} - Assunto: {i[1]} | Descrição: {i[2]} | Autor: {i[3]} | Tipo: {i[4]}")
    else:
        print("\nNão existem feedbacks para o tipo informado.")


def criarFeedbacks(conexao, tipos):
    sql="insert into feedbacks (titulo, descricao, autor, tipo) values (%s, %s, %s, %s)"

    print("\nO que você deseja fazer?")
    for p, i in enumerate(tipos):
        print(f"{p+1} - {i}")

    try:
        tipo=tipos[int(input("Digite o número da sua escolha: "))-1]
    except IndexError:
        print("Opção inválida. Tente novamente!")
        return
    
    titulo=input("\nDigite o assunto: ").capitalize()
    descricao=input("Digite a descrição: ").capitalize()
    autor=input("Digite seu nome: ").capitalize()
    dados=[titulo, descricao, autor, tipo]

    retorno=insertNoBancoDados(conexao, sql, dados)

    if retorno!=None:
        print(f"Feedback Nº {retorno} incluído com sucesso!")


def quantidadeFeedbacks(conexao):
    sql= "select count(*) from feedbacks"
    quantidade= listarBancoDados(conexao,sql)
    print ("Total de feedbacks registrados:", quantidade[0][0])


def pesquisarPorCodigo(conexao):
    codigo = int(input("\nDigite o código do feedback para visualizar: "))
    sql = "select * from feedbacks where codigo = %s"
    dados = [codigo]
    feedback = listarBancoDados(conexao, sql, dados)

    if feedback:
        print(f"Assunto: {feedback[0][1]} | Descrição: {feedback[0][2]} | Autor: {feedback[0][3]} | Tipo: {feedback[0][4]}")
    else:
        print("Não existe feedback para o código informado.")


def excluirPorCodigo(conexao):
    codigo = int(input("\nDigite o código do feedback para excluir: "))
    sql = "delete from feedbacks where codigo = %s"
    dados = [codigo]
    rows_affecteds = excluirBancoDados(conexao, sql, dados)

    if rows_affecteds==0:
        print("Não existe feedback para o código informado.")
    else:
        print(f"Feedback Nº {codigo} excluído com sucesso!")

