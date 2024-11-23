# A1Python
## Menu de Navegação
1. [Configurações](#configurando-o-ambiente-)
   - [Clonando o repositório](#clonando-o-repositório-)
   - [Instalando (e configurando) o Python](#instalando-e-configurando-o-python-)
   - [Baixando dependências](#baixando-as-dependências-)
   - [Configurando o DB](#configurando-o-banco-de-dados-)

## Configurando o ambiente &#x1F527;
A aplicação aqui presente faz extensivo uso das ferramentas do framework [Django](https://www.djangoproject.com/), escrito na linguagem de programação [Python](https://www.python.org/), portanto, para que não tenha problemas no funcionamento do sistema será necessária a presença do Python e, conjuntamente, o seu gerenciador de pacotes (pip), pelo qual será feita a instalação do pacote com os utilitários do Django e suas dependências, ambos presentes na sua máquina. A instalação do pacote Django pode ser feita tanto localmente isolada (via um ambiente virtual) como globalmente, deixamos ao seu critério essa escolha.

### Clonando o repositório &#x1F47B;
Pode começar a instalação de fato abrindo algum shell que tenha ao seu dispor para uso, caso esteja usando a plataforma Windows, indicamos fortemente o uso do **PowerShell**, caso esteja fazendo uso de uma plataforma Linux, sugerimos o **Bash** (shell padrão em muitas das distribuições) ou o **Zsh** e digitando, no diretório/pasta onde deseja ter o projeto, o seguinte comando:

```
git clone https://github.com/briansantoss/A1Python.git
```

### Instalando e configurando o Python &#x1F40D;
Não tente rodar nada ainda, não temos o Django, que, como anteriormente referido, é indispensável para o bom funcionamento da aplicação. Feito isso, estamos habilitados a partir para a instalação do Python, segue o link para download abaixo:

- <a href="https://www.python.org/downloads/" target="_blank">Instalação Python e pip</a>

### Baixando as dependências &#x1F4BE;
Após a instalação e a configuração estiver completa, faremos uso do `requirements.txt`, um arquivo de texto simples onde se encontram todas as dependências do projeto, ele vai automatizar a instalação delas, para isso, basta passarmos-o ao pip, para isso, vá ao seu terminal, acesse novamente o diretório onde o projeto foi clonado e rode o seguinte comando:

> No Windows:

```
py -m pip install -r requirements.txt
```

> No Linux:

```
python -m pip install -r requirements.txt
```

### Configurando o banco de dados &#x1F4E6;
Antes de irmos aos finalmente e poder executar o sistema na sua máquina será necessária a configuração do banco de dados, mas não se preocupe, apenas dois comandos serão requeridos, eles serão responsáveis por criar o banco de dados e as tabelas de fato:

> No Windows:
```
py manage.py makemigrations
py manage.py migrate
```

> No Linux:
```
python manage.py makemigrations
python manage.py migrate
```

Prontinho! Você está agora habilitado a rodar a aplicação, proveite!:

> No Windows:
```
py manage.py runserver
```

> No Linux:

```
python manage.py runserver
```