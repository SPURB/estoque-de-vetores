import os

def get_host_url(textfilePath):
    try:
        with open(textfilePath, 'r') as host: 
            return str(host.read())
    except FileExistsError:
        print('Arquivo ' + textfilePath + ' não existe')
