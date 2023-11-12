pip install pipenv

Caso o pipenv não funcionar: https://stackoverflow.com/questions/46041719/windows-reports-error-when-trying-to-install-package-using-pipenv

pipenv install Flask

Sempre que for executar o projeto utilize este comando
pipenv shell

pipenv requirements > requirements.txt

#lib para pgdb
#OBS: Instale o postgres na sua máquina pra testar o projeto
pipenv install  psycopg2
pipenv install python-dotenv