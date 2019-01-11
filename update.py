import sys
from assets.py import joiner

if __name__ == "__main__":
    try: 
        folder = str(sys.argv[1])
        if(folder == 'all'):
            joiner.create_base('./pictogramas/')
            joiner.create_base('./blocos/')
            joiner.create_base('./infograficos/')
        else:
            joiner.create_base('./' + folder + '/')
    except:
        print("ERRO: Inclua um parâmetro. Exemplo: 'python uplate.py all' ou 'python upldate.py blocos'")
