<template>
	<div class="home">
		<h2 v-if='!loader'>Versions</h2>
		<div class="versionBlock" v-if='!loader'>
			<h5>13.08.2020 | Version 1.0</h5>
			<h5>14.08.2020 | Version 2.0</h5>
			<h5>15.08.2020 | Version 3.0</h5>
			<h5>21.08.2020 | Version 4.0</h5>
			<h5>21.08.2020 | Version 5.0</h5>
		</div>
		<loader v-if='loader'/>
	</div>
</template>

<script>
import loader from '../components/loader.vue'

export default{
	name:'Home',
	components:{
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
	.home .versionBlock{
		max-width: 200px;
		margin:0 auto 0;
		padding:5px;
		border: 2px solid black;
	}
	.home h2{
		margin:0;
	}
	.home .versionBlock h5{
		margin:10px 0 0;
	}
	.home .versionBlock h5:last-child{
		margin-bottom:7px;
	}
</style>