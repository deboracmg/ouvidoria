from operacoesbd import *

def listarFeedbacks(conexao):
    ...


def listaPorTipo(conexao, tipos):
    sql="select * from feedbacks where tipo=%s"

    print("\nQual tipo desejar vizualizar?")
    for p, i in enumerate(tipos):
        print(f"{p+1} - {i}")
    tipo=tipos[int(input("Digite o número da sua escolha: "))-1]
    dados=[tipo]

    feedbacks = listarBancoDados(conexao, sql, dados)
    if feedbacks:
        print(f"\nLista de Feedbacks ({tipo})")
        for i in feedbacks:
            print(f"{i[0]} - Assunto: {i[1]} | Descrição: {i[2]} | Autor: {i[3]} | Tipo: {i[4]}")
    else:
        print("\nNão existem feedbacks para o tipo informado.")


def criarFeedbacks(conexao, tipos):
    sql="insert into feedbacks (titulo, descricao, autor, tipo) values (%s, %s, %s, %s)"

    print("\nO que você deseja fazer?")
    for p, i in enumerate(tipos):
        print(f"{p+1} - {i}")
    tipo=tipos[int(input("Digite o número da sua escolha: "))-1]
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
    ...


def excluirPorCodigo(conexao):
    ...

