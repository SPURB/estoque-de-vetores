# estoque-de-vetores
Sistema de catalogação de desenhos vetoriais produzidos pela SMUL (Secretaria de Desenvolvimento Urbano e Licenciamento) e São Paulo Urbanismo (São Paulo Urbanismo).

## Setup do ambiente 

### Pré-requisitos
* Python 3

### Instruções
1. Clonar este repositório `git clone https://github.com/SPURB/estoque-de-vetores.git`

2. Dentro do diretório `public` incluir diretórios no padrão abaixo:

	```
	qualquer-nome-de-diretorio/
	qualquer-nome-de-diretório-1/
	pictogramas/
		imagem-para-pictogramas_home.png
		Um diretório com espaços e acetuação/
		Outro diretório/
		Indústria/
			Indústria.ai
			Indústria.pdf
			Indústria_th.png
			Indústria_full.png
	```
	##### Sempre incluir thumbnail
	Criar um thumb para gerar a pré-visualização

	Para isto crie uma imagem com o nome `thumb` ou terminada em `_th` dentro do diretório. No exemplo acima: `Indústria_th.png`.

	> Definir o padrão de thumbnails para `150x150px` ou `500x500px`.

	##### Full
	Arquivos terminados em `_full` ou `_fl` são opcionais.  Caso imagens do tipo não existam o primeiro png, jpg ou gif do diretório gerará esta pré-visualização. No exemplo acima o arquivo é `Indústria_full.png`

3. Abrir o terminal:
```
python update.py
```
veja se os arquivos foram corretamente criados em `public/_data`


4. Pode ser necessário limpar os diretórios para manter apenas os arquivos necessários para a renderização das páginas. `clean.py` irá deletar todos os arquivos diferentes das seguintes extensões utilizadas nos diretórios filhos de `public/`. São válidas as seguintes extensões: 
`jpg`, `png`, `gif`, `pdf`, `svg`, `eps`, `ai`, `psd`, `skp`, `dwg` e `dxf`. (ver `assets/py/valid_extensions.py`)

5. 

## Desenvolvimento 

### Backend
```
cd api
```
Siga as instruções do `/api/README.md`

### Frontend
```
cd app
```
Siga as instruções do `/app/README.md`
