# Este repositório contém: 





1. Um modelo básico de arquitetura MVC para orientação de desenvolvimento projetos de aplicações Flask



# Os diretórios e arquivos em uma arquitetura MVC aplicada em Flask podem ser organizados da seguinte forma:



O diretório principal contém:

1. 1 diretório **ambientev** onde foi instalado o ambiente virtual com as instalações necessárias para a aplicação

2. 1 arquivo **run.py** que é responsável por rodar a aplicação

3. 1 arquivo **requirements.txt** que contém todos os pacotes e suas versões instaladas e usadas na aplicação. Este arquivo pode ser gerado utilizando no comando **pip3 freeze > requirements.txt**

   

4. 1 diretório **app_dir** que guarda dentro a aplicacão, que está organziada dentro de diretórios que compões o MVC

   O diretório app_dir contém:

   1. 1 arquivo **____init____.py**  que é responsável inicializar o diretório app_dir como um módulo Python

   2. 1 diretório **models** que contém os modelos de dados da aplicação

      Dentro de models existem:

      1. 1 arquivo **____init____.py**  que é responsável inicializar o diretório models como um módulo Python

   3. 1 diretório **controller** que contém a lógica da aplicação e suas rotas @app.route

      Dentro de controller existem:

      1. 1 arquivo **____init____.py**  que é responsável inicializar o diretório controller como um módulo Python
      2. 1 arquivo **default.py**

   4. 1 diretório **static** que contém os arquivos visuais estáticos da aplicação, como arquivos CSS e imagens

   5. 1 diretório **templates** que contém os arquivos das páginas HTML da aplicação.



```
diretório_principal/

​			run.py

​			ambientev/

​			app_dir/

​						models/

​						controller/

​						static/

​						templates/
```



​			

​		

