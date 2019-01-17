### Pré-requisitos:
* Python 3
* pip

## Setup 
1. Instale virtualenv 

    ```
    pip install virtualenv
    ```

2. Crie o ambiente `env` e ative-o
    ``` 
    virtualenv env
    call env/Scripts/activate # comandos para windows. no terminal -> $ source env/bin/activate
    ``` 
    > para sair o ambiente `call env/Scripts/deactivate`

3. Na raiz de `/api/` instale as dependências deste projeto
    ```
    # cd ../.. 
    pip install -r requirements.txt
    ```

4. Renomeie `host-sample.txt` para `host.txt`. No ambiente de produção altere o conteúdo incluindo o seu host.


## Inicie o servidor 
```
python server.py
```
> O servidor está no ar em `http://127.0.0.1:5000`. Veja a lista de enpoints `http://127.0.0.1:5000/endpoints`.

obs: Atalho para iniciar com debbuger (apenas em ambiente windows)
```
run-debbuger
```