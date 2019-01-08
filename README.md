# estoque-de-vetores
Sistema de catalogação de desenhos vetoriais produzidos pela SMUL (Secretaria de Desenvolvimento Urbano e Licenciamento) e São Paulo Urbanismo (São Paulo Urbanismo).

O Estoque de Vetores é dividido em: Pictogramas, Blocos e Infográficos.

### Pré-requisitos
* Python 3 (instalado e configurada na PATH) e pip

### Setup do ambiente
Incluir os arquivos deste repositório em um servidor http

1. Instalar watchdog:
```
pip install watchdog
```
2. Observar alterações nos diretórios `/pictogramas`, `/blocos` e `/infograficos`
```
python3 watch.py
```

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
![ícone de Indústria](https://raw.githubusercontent.com/SPURB/estoque-de-vetores/master/pictogramas/Ind%C3%BAstria/Ind%C3%BAstria_th.png)
É importante criar um thumb para gerar a pré-visualização. 

Para fazer isto crie uma imagem com o nome `thumb` ou terminada em `_th` dentro do diretório. No exemplo acima: `Indústria_th.png`.


> Thumbnails funcionam melhor com `150x150px` para os pictogramas e `500x500px` para os blocos e infográficos.

##### Full
Arquivos terminados em `full` são opcionais.  Caso imagens do tipo não existam o primeiro png, jpg ou gif do diretório gerará esta pré-visualização. No exemplo acima o arquivo é `Indústria_full.png`

#### Limpeza
Pode ser necessário limpar os diretórios para manter apenas os arquivos necessários para a renderização das páginas. As extensões previstas são: 
`jpg`, `png`, `gif`, `pdf`, `svg`, `eps`, `ai`, `psd`, `skp`, `dwg` e `dxf`. (ver `assets/py/valid_extensions.py`)

Para limpar as pastas e manter apenas arquivos com estas extensões executar o comando: 

1. Para limpeza em seção específica:
```
python3 clean.py nome-da-secao
```
2. Limpar os três diretórios: 
```
python3 clean.py all
```
