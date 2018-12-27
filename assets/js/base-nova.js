var headercabecalho = Vue.component('headercabecalho',{
	data: function () {
		return {
			pesquisa: '',
			vetorNome: nomePagina,
		}
	},
	methods: {
		zeraEvento(){
			this.vetorNome = nomePagina
		},
		evento(str){
			this.vetorNome = str
		},
		ativo(pagina){
			if(pagina === nomePagina){
				return 'aceso'
			}
		}
			// if (this.vetorNome == 'Blocos' || this.vetorNome == 'Pictogramas' || this.vetorNome == 'Infográficos'){
			// 	return 'aceso'
			//  	 } 
			// } 
	},
	template:`
		<div id="headercabecalho">
		<div class="pesquisar">
				<input 
				v-model="pesquisa"
				type="search" 
				name="pesquisa" 
				placeholder="Pesquise">
				<div class="buscar">
				</div>
		</div>
		<div id="icones">
			<p>{{vetorNome}}</p>
			<a href="../../pictogramas/imagens">
			<img 
				src="../../_elementos/BTN_01.svg" 
				class="tipoVetor" 
				alt="Pictogramas" 
				:class="ativo('Pictogramas')"
				@mouseover="evento('Pictogramas')" 
				@mouseleave="zeraEvento">
			</a>
			<a href="../../infograficos/imagens">
			<img 
				src="../../_elementos/BTN_02.svg" 
				class="tipoVetor" 
				:class= "ativo('Infográficos')"
				alt="Infográficos" 
				@mouseover="evento('Infográficos')"
				@mouseleave="zeraEvento">
			</a>
			<a href="../../blocos/imagens">
			<img 
				src="../../_elementos/BTN_03.svg" 
				class="tipoVetor" 
				alt="Blocos" 
				:class= "ativo('Blocos')"
				@mouseover="evento('Blocos')" 
				@mouseleave="zeraEvento">
			</a>
		</div>
	</div>
	`
})

var grid = Vue.component('grid', {
	data: function() {
		return {
			pesquisa: '', 
			// vetorNome: '',
			base: base,
		}
	},
	computed: {
			filtrados(){
			const app = this
			/* 
			.filter - fitra arrays 
			.map - transforma todos os itens  
			.forEach - para item faz alguma coisa 
			.reduce - retorna um único valor
			*/
			return this.base.filter(function(base) { 
			   return base.name.toLowerCase().indexOf(app.pesquisa.toLowerCase()) >= 0;
			})
		},
	},
	methods:{
		pastaArquivos(diretorio){
			return './' + diretorio
		},
		retornarExtensao(nomeCompletoArquivo){
			return (/[.]/.exec(nomeCompletoArquivo)) ? /[^.]+$/.exec(nomeCompletoArquivo)[0] : undefined;
		},
		caminhoDaImagem(pasta, imagem){
			return pasta + '/' + imagem
		},
		ocultar(description) {
			if (description === 'nenhuma descrição' || 'Atribua uma descrição') {
				return false
			}
			else {
				return true 
			}
		},
		urlArquivoPdf(pasta, arquivo) {
			return pasta + '/' + arquivo
		},
	},
	template: `
		<div class="grid">
		<div v-for="base in filtrados" class="conjunto">
			<a :href="pastaArquivos(base.folder)">
				<img :src="caminhoDaImagem(base.folder, base.thumb.name)">
			</a>
			<h4>{{ base.name }}</h4>
			<p v-if="ocultar(base.description)" class="descricao">{{ base.description }}</p>
			<div class="botoes">
				<ul v-for="file in base.files" >
					<li class="botao">
						<a :href="urlArquivoPdf(base.folder, file)" download> {{ retornarExtensao(file)}}</a>
					</li>
				</ul>	
			</div>
		</div>
	</div>

	`
})
var app = new Vue({
	el:"#app",
	components:{
		headercabecalho,
		grid,
	}, 

})