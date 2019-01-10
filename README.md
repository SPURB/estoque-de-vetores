# estoque-de-vetores
Sistema de catalogação de desenhos vetoriais produzidos pela SMUL (Secretaria de Desenvolvimento Urbano e Licenciamento) e São Paulo Urbanismo (São Paulo Urbanismo).

O Estoque de Vetores é dividido em: Pictogramas, Blocos e Infográficos.

## Setup do ambiente 

### Pré-requisitos
* Python 3

### Instruções
1. Clonar este repositório `git clone https://github.com/SPURB/estoque-de-vetores.git`

2. Incluir diretórios em cada seção no seguinte padrão abaixo:

	```
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
	##### Sempre incluir thumbnails
	Criar um thumb para gerar a pré-visualização

	Para isto crie uma imagem com o nome `thumb` ou terminada em `_th` dentro do diretório. No exemplo acima: `Indústria_th.png`.

	> Thumbnails funcionam melhor com `150x150px` para os pictogramas e `500x500px` para os blocos e infográficos.

	##### Full
	Arquivos terminados em `_full` ou `_fl` são opcionais.  Caso imagens do tipo não existam o primeiro png, jpg ou gif do diretório gerará esta pré-visualização. No exemplo acima o arquivo é `Indústria_full.png`

3. Pelo cmd do windows rodar `run-tasks`. Este comando iniciará uma de leitura dos diretórios com os arquivos vetoriais e atualização automática da aplicação.
> Caso o ambiente não seja windows pode-se rodar diretamente os arquivos python `update.py`, `clean.py` ou `watch.py`. O comando acima apenas executa estes programas periodicamente. 

#### Limpeza
Pode ser necessário limpar os diretórios para manter apenas os arquivos necessários para a renderização das páginas o comando `clean.py` irá deletar todos os arquivos diferentes das seguintes extensões: 
`jpg`, `png`, `gif`, `pdf`, `svg`, `eps`, `ai`, `psd`, `skp`, `dwg` e `dxf`. (ver `assets/py/valid_extensions.py`)


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
