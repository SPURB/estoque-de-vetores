### Pré-requisitos:
* Python 3
* pip

## Setup 
1. Instale virtualenv 

    ```
    pip install virtualenv
    ```

2. crie o ambiente `env` e ative-o
    ``` 
    virtualenv env
    env/Scripts/activate # comando para windows. no terminal -> $ source env/bin/activate
    ``` 

3. Instale as dependências deste projeto
    ```
    pip install -r requirements.txt
    ```

4. Renomeie `host-sample.txt` para `host.txt`. 


## Inicie o servidor 
```
python app.py
```
> O servidor em `http://127.0.0.1:5000`