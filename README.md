# estoque-de-vetores
Sistema de catalogação de desenhos vetoriais produzidos pela SMUL (Secretaria de Desenvolvimento Urbano e Licenciamento) e São Paulo Urbanismo (São Paulo Urbanismo).

O Estoque de Vetores é dividido em: Pictogramas, Infográficos e Blocos.

### Pré-requisitos
* PHP
* Python 3

### Setup do ambiente
Basta incluir os arquivos deste repositório em um servidor com PHP e Python 3 instalados

### Arquivos
Incluir um diretório com o nome do conjunto de arquivos na seção adequada
```
/assets
/blocos
/infograficos
/pictogramas
	/Habitação
	/Habitação de Interesse Social
	/Indústria
		Indústria.ai
		Indústria.pdf
		Indústria_th.png
		Indústria_full.png
```
##### Thumbs
![ícone de Indústria](https://raw.githubusercontent.com/SPURB/estoque-de-vetores/master/pictogramas/Ind%C3%BAstria/Ind%C3%BAstria_th.png)  
É importante criar um thumb para gerar a pré-visualização na página de cada seção.  
Para fazer isto crie uma imagem com o nome `thumb` ou terminada em `_th` dentro do diretório. No exemplo acima: `Indústria_th.png`.


Arquivos terminados em `th` ou de nome `thumb` será a thumbnail do diretório.  
> Thumbnails funcionam melhor com `150x150px` para os pictogramas e `500x500px` para os blocos e infográficos.

##### Full
Arquivos terminados em `full` são opcionais.  Caso imagens do tipo não existam o primeiro png,jpg ou gif do diretório gerará esta pré-visualização. No exemplo acima o arquivo é `Indústria_full.png`

### Para incluir novas imagens
Criar um diretório dentro da seção adequada com os arquivos da imagem. As extensões previstas são: 
`jpg`, `png`, `gif`, `pdf`, `svg`, `eps`, `ai`, `psd`, `skp`, `dwg` e `dxf`. (ver `assets/py/valid_extensions.py`)

#### Instruções

1. Criar o diretório com todos os arquivo dentro do diretório da seção 
2. Gerar a atualização rodando `update.py` na raiz do projeto: 

```
python3 update.py nome-da-secao
```
`update.py` requer um argumento que pode um dos nomes da seção ou `all` para atualizar todas as seções.


3. Para limpar os diretórios, manter apenas os arquivos válidos 
```
python3 clean.py nome-da-secao
```
Assim como `update.py`, `clean.py` requer um argumento que pode um dos nomes da seção ou `all` para limpar todas as seções.