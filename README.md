# estoque-de-vetores
Sistema de catalogação de desenhos vetoriais produzidos pela SMUL (Secretaria de Desenvolvimento Urbano e Licenciamento) e São Paulo Urbanismo (São Paulo Urbanismo).

## Características
Cria, a partir de qualquer conjunto de diretórios com arquivos de imagens em uma api e aplicação web. 
Não há banco de dados. Os dados são compilados em arquivos `.json` (por cron job) e disponibilizados pela api. A api foi escrita em [flask](http://flask.pocoo.org/) e a aplicação em [vue](https://vuejs.org/).

## Setup do ambiente 

### Pré-requisitos
* Python 3

### Instruções
1. Clonar este repositório `git clone https://github.com/SPURB/estoque-de-vetores.git`

2. Dentro do diretório `public` incluir diretórios no padrão abaixo:

	```
	public/
		diretorio-1/
		diretório-2/
		diretorio-n/
			diretorio-n.png
			subdiretorio-1/
			subdiretorio-2/
				arquivo.ai
				arquivo.pdf
				arquivo_th.png
				arquivo_full.png
	```
	### Alguns cuidados:
	* Incluir thumbnail em todos os diretórios. No exemplo acima o thumbnail do diretório é  `diretorio-n.png`.

	* Incluir thumbnail no subdiretório. Criar uma imagem com o nome `thumb` ou terminada em `_th` dentro do subdiretório. No exemplo acima: `arquivo_th.png`. Os padrões de tamanho previstos são `150x150px` e `500x500px`.

	* Incluir arquivos `_full` ou `_fl` (opcional). Caso imagens com este padrão não existam o primeiro `png`, `jpg` ou `gif` do diretório gerará esta pré-visualização. No exemplo o arquivo equivalente é o `arquivo_full.png`

4. Renomeie `host-public-folders-sample.txt` para `host-public-folders.txt` e altere o texto incluindo a url pública da aplicação. (caso seja para desenvolvimento local pode manter `http://127.0.0.1/estoque-de-vetores/public`)

5. Abra o terminal:
	```
	py update.py # ~ py3 ~ caso tenha as duas versões do python
	```
veja se os arquivos `.json` foram corretamente criados em `public/_data`

6. Faça o setup do backend (se já fez pule para etapa 7) seguindo as instruções do `api/README.md`

7. Inicie a API (backend)
	```
	cd api
	py app.py
	```

8. Faça o setup do app (frontend) (se já fez pule para etapa 9) seguindo as instruções do `app/README.md`


9. Inicie o app
	```
	cd app
	npm run serve
	```
10. O app estará rodando em [localhost:8080](http:localhost:8080)

## Limpeza de subdiretórios (`/public/diretorios/subdiretorio`)
Pode ser necessário limpar os subdiretórios para manter apenas os arquivos necessários. Execute `py clean.py` para deletar todos os arquivos das extensões válidas definidas em `assets/py/valid_extensions.py`. São elas: 
 * `jpg`
 * `png`
 * `gif`
 * `pdf`
 * `svg`
 * `eps`
 * `ai`
 * `psd`
 * `skp`
 * `dwg`
 * `dxf`

## Desenvolvimento 

### Backend
Siga as instruções do `/api/README.md`

### Frontend
Siga as instruções do `/app/README.md`
