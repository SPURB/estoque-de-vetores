import sys
from assets.py import joiner

if __name__ == "__main__":
    folder = str(sys.argv[1])
    if(folder == 'all'):
        joiner.create_base('./pictogramas/')
        joiner.create_base('./blocos/')
        joiner.create_base('./infograficos/')
        
    else:
        joiner.create_base('./' + folder + '/')