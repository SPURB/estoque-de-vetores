var headercabecalho = Vue.component('headercabecalho',{
	name:'headercabecalho',
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
	},
	watch:{
		pesquisa(value){
			this.$emit('updatepesquisa', value)
		}
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
			<a href="../pictogramas">
			<img 
				src="../assets/img/BTN_01.svg" 
				class="tipoVetor" 
				alt="Pictogramas" 
				:class="ativo('Pictogramas')"
				@mouseover="evento('Pictogramas')" 
				@mouseleave="zeraEvento">
			</a>
			<a href="../infograficos">
			<img 
				src="../assets/img/BTN_02.svg" 
				class="tipoVetor" 
				:class="ativo('Infográficos')"
				alt="Infográficos" 
				@mouseover="evento('Infográficos')"
				@mouseleave="zeraEvento">
			</a>
			<a href="../blocos">
			<img 
				src="../assets/img/BTN_03.svg" 
				class="tipoVetor" 
				alt="Blocos" 
				:class="ativo('Blocos')"
				@mouseover="evento('Blocos')" 
				@mouseleave="zeraEvento">
			</a>
		</div>
	</div>
	`
})

var grid = Vue.component('grid', {
	name:'grid',
	props: ['pesquisa'],
	data: function() {
		return {
			base: base,
			emptyItems: false
		}
	},
	computed: {
			filtrados(){
				const app = this
				return this.base.filter(function(base) { 
				return base.folder.toLowerCase().indexOf(app.pesquisa.toLowerCase()) >= 0
				})
		},
	},
	watch: {
		filtrados(value){
			return value.length > 0 ? this.emptyItems = false : this.emptyItems = true
		}
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
		<p class="fail-message" v-if="emptyItems">Não itens para esta pesquisa</p>
		<div v-for="(base, index) in filtrados" class="conjunto" :key="index">
			<a :href="pastaArquivos(base.folder)">
				<img :src="caminhoDaImagem(base.folder, base.thumb.name)">
			</a>
			<h4>{{ base.folder }}</h4>
			<p v-if="ocultar(base.description)" class="descricao">{{ base.description }}</p>
			<div class="botoes">
				<ul v-for="(file, index) in base.files" :key="index">
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
	name:"App",
	el:"#app",
	data:{
		pesquisa:''
	},
	methods:{
		input(evt){
			this.pesquisa = evt
		}
	},
	components:{
		headercabecalho,
		grid
	}, 
})