O projeto foi desenvolvido por Gabriel Martinello, Vitória Zanella e Leticia Serpa;

Este projeto tem como objetivo administrar a temperatura e a umidade para avícolas.
Dependendo da temperatura o cooler deverá ligar se estiver muito quente e se estiver muito frio ligar a lâmpada.
O controle de temperaturas, para verificação pode ser visto em uma página web que possue 2 gráficos para
verificação, e também uma tabela para controle das temperaturas que foram feitas.

Executar esses comandos:
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
pip install Flask-Mail