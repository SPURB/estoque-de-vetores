# estoque-de-vetores
Sistema de catalogação de desenhos vetoriais produzidos pela SMUL (Secretaria de Desenvolvimento Urbano e Licenciamento) e São Paulo Urbanismo (São Paulo Urbanismo).

O Estoque de Vetores é dividido em: Pictogramas, Blocos e Infográficos.

### Pré-requisitos
* Python 3 e pip (e configueradas na PATH)

### Setup do ambiente
1. Incluir os arquivos deste repositório em um servidor 

2.  Instalar watchdog :
```
pip install watchdog
```
3. Pelo cmd do windows 
```
run-tasks
```
> Caso o ambiente não seja windows pode-se rodar diretamente os arquivos python `watch.py`, `update.py` ou `clean.py`. O comando acima apenas executa estes programas periodicamente. 

### Arquivos
Incluir diretórios em cada seção no seguinte padrão:

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

#### Limpeza
Pode ser necessário limpar os diretórios para manter apenas os arquivos necessários para a renderização das páginas. As extensões previstas são: 
`jpg`, `png`, `gif`, `pdf`, `svg`, `eps`, `ai`, `psd`, `skp`, `dwg` e `dxf`. (ver `assets/py/valid_extensions.py`)
