<template>
	<div class='postItems'>
		<postItem 
		v-for = 'post of posts'
		:postItem = 'post'
		:key='post.id'/>
	</div>
</template>

<script>
import postItem from './postItem.vue'

export default{
	name:'postItems',
	components:{
		postItem,
	},
	props:['posts'],
	data(){
		return{
		};
	},
	methods:{
	}
}
</script>
<style>
	.postItems{
		padding:0;
		margin: 20px auto 50px;
		overflow: auto;
		max-width:700px!important;
		width:100%;
		max-height: 550px;
		overflow:auto;
	}
</style> 