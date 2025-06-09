# 🗣️ Sistema de Ouvidoria

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## 📄 Descrição

**Sistema de Ouvidoria** é um módulo em Python desenvolvido para gerenciar registros de feedbacks em um banco de dados MySQL. Ele permite registrar, listar, pesquisar e excluir feedbacks com segurança e simplicidade, utilizando **prepared statements** e **tratamento de exceções**.

Este sistema é ideal para aplicações que necessitam coletar e organizar sugestões, críticas ou elogios de usuários.

## 🚀 Funcionalidades

- **Criar Feedbacks**: Registra novos feedbacks com título, descrição, autor e tipo.
- **Listar Feedbacks**: Exibe todos os feedbacks armazenados.
- **Listar por Tipo**: Mostra feedbacks filtrando por tipo (ex: Elogio, Sugestão, Crítica).
- **Contar Feedbacks**: Informa o número total de feedbacks cadastrados.
- **Pesquisar por Código**: Busca um feedback específico pelo ID.
- **Excluir por Código**: Remove feedbacks com base no código informado.

## 📦 Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/ouvidoria.git
    ```
2. Instale as dependências:
    ```bash
    pip install mysql-connector-python
    ```

## 🛠 Uso

### 1. Criar uma Conexão com o Banco de Dados

```python
from operacoesbd import criarConexao
conexao = criarConexao('localhost', 'root', 'senha', 'meubancodedados')
```

### 2. Criar Feedback

```python
from ouvidoria import criarFeedbacks
tipos = ["Elogio", "Sugestão", "Crítica"]
criarFeedbacks(conexao, tipos)
```

### 3. Listar Todos os Feedbacks

```python
from ouvidoria import listarFeedbacks
listarFeedbacks(conexao)
```

### 4. Listar Feedbacks por Tipo

```python
from ouvidoria import listaPorTipo
listaPorTipo(conexao, tipos)
```

### 5. Contar Feedbacks

```python
from ouvidoria import quantidadeFeedbacks
quantidadeFeedbacks(conexao)
```

### 6. Pesquisar Feedback por Código

```python
from ouvidoria import pesquisarPorCodigo
pesquisarPorCodigo(conexao)
```

### 7. Excluir Feedback

```python
from ouvidoria import excluirPorCodigo
excluirPorCodigo(conexao)
```

## 🛡️ Segurança

Este sistema usa **prepared statements** em todas as consultas para proteger contra **SQL Injection**. Também implementa **tratamento de exceções** para maior confiabilidade.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para enviar **pull requests** ou reportar **issues**.

## 📄 Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais informações.

