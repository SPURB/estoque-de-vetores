# estoque-de-vetores
Sistema de catalogação de desenhos vetoriais produzidos pela SMUL (Secretaria de Desenvolvimento Urbano e Licenciamento) e São Paulo Urbanismo (São Paulo Urbasnimo).

O Estoque de Vetores é dividido em: Pictogramas, Infográficos e Blocos (com bases axonométricas, cortes, ilustrações e blocos para ilustrações).

### Pré-requisitos
* Servidor com PHP instalado
* Python 3 


### Inclusão de novas imagens
Criar um diretório dentro de cada seção. Dentro deste diretório incuir todos os arquivos editáveis. As extensões previstas são: 
`jpg`,`png`,`gif`,`pdf`,`svg`,`eps`,`ai,`,`psd`,`skp`,`dwg` e `dxf`. É importante criar um thumb para gerar a visualização. Para isto criar uma imagem de nome `thumb` ou terminada em `_th`. Exemplo: 
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
Arquivos terminados em `th` ou de nome `thumb` é a thumbnail.  
> Thumbnails funcionam melhor com `150x150px` para os pictogramas e 500x500 para os blocos e infográficos.

Arquivos terminados em `full` é opcional, mas caso tenha o arquivo de prévisualização grande. 

### Setup do ambiente
Basta incluir os arquivos deste repositório em pasta no servidor e abrir local da path (exemplo: http://localhost/estoque-de-vetores).

Após incluir a nova imagem fazer o update das bases pelo terminal. `cd estoque-de-vetores`

```
py update.py

```


### Licença
O conteúdo deste repositório está sob a licença [GNU General Public License](https://www.gnu.org/licenses/licenses.html#GPL).
