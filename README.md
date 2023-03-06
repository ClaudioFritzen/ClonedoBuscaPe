# esse site é inspirado no buscape
# Esse é um aplicação onde será usada webscraping, django. FastApi

# Como utilizar esse projeto apos fazer um clone

# dentro da sua maquina virtual rode o requiments.txt para instalar todas as libs utilizadas nesse projeto
pip install -r requirements.txt

# Apos isso crie um arquivo chamado .env e preencha com seus dados. Deixarei o arquivo .env_copy para saber quais
dados devem ser preenchidos para funcionar corretamente

# Estarei utilizando o banco de dados POSTGRESS, pode usar qualquer um que deseje. Mas não esqueça de muda-lo no
# setting.py 




# site para pegar imagens padrozado
https://via.placeholder.com/150


# utilizando o banco de dados Railway
# cadastrar um cartão de credito como desenvolvedor, e terá até 5 dolar gratias. Só pagará se gastar mais de 5 dolares mensais

# Criamos um novo projeto, Postgress.

# Faremos a conexão com o banco de dados.

# Utilizaremos a lib pip install psycopg2-binary para fazer a ponte
pip install psycopg2

https://pypi.org/project/psycopg2/


<!-- DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'railway',
        'USER': 'postgres',
        'PASSWORD': 'sua senha',
        'HOST': 'containers-us-west-64.railway.app'

    }

} -->

# Agora rodaremos o migrations para criar o banco na nuvem
py manage.py makemigrations
py manage.py migrate