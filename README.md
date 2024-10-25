# Gestão de vendas de Carros

## Descrição do Projeto

Este projeto é uma aplicação Django para gerenciar o cadastro de carros e suas marcas. Ele permite adicionar, visualizar e gerenciar carros com informações detalhadas, incluindo a marca, modelo, ano de fabricação, valor, e outras especificações. O projeto também inclui validações de formulário para garantir que certos requisitos sejam atendidos, como valores mínimos e anos de fabricação.

## Funcionalidades
- Cadastro e gerenciamento de carros
- Vinculação dos carros a suas marcas
- Validações personalizadas para o valor e ano dos carros
- Upload de fotos dos carros
- Visualização do inventário com contagem e valor total dos carros

## Tecnologias Usadas
- **Python**: Linguagem de programação usada para construir o backend.
- **Django**: Framework web usado para construir o servidor e o gerenciamento de dados.
- **Bootstrap**: Framework de front-end usado para criar uma interface de usuário responsiva e estilizada.
- **HTML/CSS**: Linguagens de marcação e estilo usadas para construir e estilizar a interface do usuário.

## Como Configurar o Projeto

Para executar este projeto localmente, siga os passos abaixo:

1. **Clone o Repositório**
- Usando HTTPS:
```bash
git clone https://github.com/htadmg/carros_django.git
```
- Usando SSH:
```bash
git clone git@github.com:htadmg/carros_django.git
```
- Navegue até o diretório do projeto:
```bash
cd .\carros_django
```

2. **Crie e Ative um Ambiente Virtual (opcional, mas recomendado)**
- **Para Linux/MacOS:**
```bash
python -m .venv venv
source .venv/bin/activate
```

- **Para Windows:**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

## Configuração do Banco de Dados

Aplique as migrações para configurar o banco de dados:

```bash
python manage.py migrate
```
   
