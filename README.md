O projeto foi desenvolvido por Gabriel Martinello, Vitória Zanella e Leticia Serpa;

# Descrição

Desenvolvemos um sistema de controle que tem como objetivo administrar a temperatura e a umidade para avícolas., estabelecendo comunicação entre o dispositivo NodeMCU via protocolo HTTP.

![Alt text](./BackEnd/static/images/nodeMCU.jpg?raw=true "ndemcuimage")

# Tecnologias utilizadas
* HTML/CSS/JS
* PlataformIO (Para desenvolver no nodeMCU)
* C++ (Para dispositivo IOT nodeMCU)
* Ajax
* Python Flask
* Postgres Database
* Google Charts (Para geração de gráficos em tela)
* Jquery
* Bibliotecas JS

# Informações da página

O frontend foi desenvolvido com HTML/CSS/JS, possue uma tela principal com 2 gráficos que são atualizados em tempo real, na qual é possível ver a média de temperatura por data, e também tem uma tabela que mostra os dados individualmente também em tempo real. A página é renderizada por uma rota da api com a funcionalidade do Flask render_template, onde é passado o nome do arquivo e renderizado no navegador

# Informações do backend
O backend foi desenvolvido utilizando VSCode com a extensão plataformIO, que possibilita desenvolver em C++ e enviar o código para o nodeMCU com facilidade. Utilizando C++, no qual é validada a temperatura através do Sensor MCU, na qual determinada temperatura liga a lâmpada se estiver muito e frio e liga o cooler caso esteja muito quente, de acordo com as validações. Também temos a api feita em Python com o framework Flask. A api contém as seguintes rotas:

# Para adicionar um registro no banco de dados

![Alt text](./BackEnd/static/images/rotaTemperatura.jpg?raw=true "post")

# Para listar todos os registros

![Alt text](./BackEnd/static/images/getAllTemp.jpg?raw=true "get")

# Para pegar a média de temperaturas agrupadas por data

![Alt text](./BackEnd/static/images/temperaturavg.jpg?raw=true "avg")

# Para listar um id específico

Para listar um id específico, é outra rota, anteriormente estávamos usando somente **/temperatura**, agora para listar pelo id é **/temperaturas/id**, e a rota delete é a mesma coisa **/temperaturas/id**

![Alt text](./BackEnd/static/images/temperaturaById.jpg?raw=true "temperaturaById")

# Página Front End
Para acessar a página é só jogar o ip e porta em que o servidor está rodando e o caminho da url, por exemplo: **http://127.0.0.1:5000/temperatura/graphs** que vai renderizar a página no navegador 
![Alt text](./BackEnd/static/images/renderizeGrapsh.jpg?raw=true "renderize")

# Passos para rodar esse projeto
* Clone o repositório.
* Altere o nome da internet e senha.
![Alt text](./BackEnd/static/images/internetSenha.jpg?raw=true "internet")
* Altere o ip caso precise no arquivo main.cpp da pasta Arduino.
* Mande o código do backend para o seu dispositivo nodeMCU.
* mude o ip da api dentro do main.cpp da pasta Arduino para o ip em que a api está rodando.
![Alt text](./BackEnd/static/images/configiparduine.jpg?raw=true "ipconfig")
* Pronto! Está tudo funcionando.

Para rodar a api em python execute esses comandos:
* Entrar dentro da pasta Backend pelo **Git Bash**
* pip install pipenv
* Caso o pipenv não funcionar: https://stackoverflow.com/questions/46041719/windows-reports-error-when-trying-to-install-package-using-pipenv
* pipenv install Flask
* Criar o banco **Temperatura** no Postgres e mudar o caminho do banco para o seu, dentro de **/BackEnd/temperatura.py**
![Alt text](./BackEnd/static/images/pgConfig.jpg?raw=true "dbConfig")
* Sempre antes de executar o projeto utilize este comando: pipenv shell
* pipenv requirements > requirements.txt

#lib para pgdb
#OBS: Instale o postgres na sua máquina pra testar o projeto
* pipenv install  psycopg2
* pipenv install python-dotenv
* pip install Flask-Mail

Para rodar: python main.py