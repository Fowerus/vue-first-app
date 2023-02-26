 
<template>
	<div class="account">
		<changeLogPas v-if='!loader'/>
		<loader v-if='loader'/>
	</div>
</template>

<script>
import changeLogPas from '../components/account-vues/changeLogPas.vue'
import loader from '../components/loader.vue'

export default{
	name:'account',
	components:{
		changeLogPas,
		loader
	},
	data(){
		return{
			loader:true
		};
	},
	methods:{
		loaderLoad(){
			setTimeout(()=>{
				this.loader = false;
			},1000)
		}
	},
	created(){
		this.loaderLoad();
	}
}
</script>

<style scoped>
	.account{
		max-width: 700px;
		width: 100%;
		margin:0 auto 0;
	}
</style>