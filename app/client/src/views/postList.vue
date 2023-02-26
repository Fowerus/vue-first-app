<template>
	<div class='postList' :class='{seeCurrentBlock: seeAddPostItem}'>
		<div class="searchAddBlock" v-if = '!loader && !seeAddPostItem'>
			<input class="searchBlock" type="text" placeholder='Search' v-model='filter'>
			<button @click='seeAddBlock'>+</button>
		</div>
		<postItems 
		v-if = 'filtersPosts.length > 0 && !seeAddPostItem && !loader' 
		:posts = 'filtersPosts'
		@read-this-post = 'readThisPost'/>
		<addPostItem 
		v-if='seeAddPostItem && !loader'
		@close-field = 'closeField' 
		@add-new-post = 'addNewPost'/>
		<h4 v-if='filtersPosts.length == 0 && !loader && !seeAddPostItem'>No posts!</h4>
		<loader v-if ='loader'/>
	</div>	
</template>

<script>
import axios from 'axios'

import postItems from '../components/postList-vues/postItems.vue'
import addPostItem from '../components/postList-vues/addPostItem.vue'
import loader from '../components/loader.vue'

export default{
	name:'postList',
	components:{
		postItems,
		addPostItem,
		loader
	},
	data(){
		return{
			posts:[],
			filter:'',
			error:'',
			seeAddPostItem:false,
			loader:true,
		};
	},
	methods:{
		getPosts(){
			const path = 'http://localhost:5000/getPosts';
			axios.post(path)
			.then(res => {
				setTimeout(()=>{
					if (typeof res.data == 'string'){
						this.error = res.data;
					}else{
						this.error='';
						this.posts = res.data.reverse();
					}
					this.loader = false;
				},1000);
			})
		},
		closeField(){
			this.seeAddPostItem = false;
		},
		seeAddBlock(){
			this.seeAddPostItem = true;
		},
		addNewPost(newPost){
			this.posts.unshift(newPost);
		},
		readThisPost(post){
			this.current_post = post;
		},
		closeCurrentPost(){
			this.current_post = '';
		}
	},
	computed:{
		filtersPosts(){
			return this.posts.filter(f => f.title.includes(this.filter) || f.author.includes(this.filter));
		}
	},
	created(){
		this.getPosts();
	}
}
</script>
<style scoped>
	.postList{
		max-width: 700px;
		margin:0 auto 0;
	}
	.seeCurrentBlock{
		max-width: 800px!important;
	}
	.searchAddBlock{
		max-width: 500px;
		margin:0 auto 0;
		display: flex;
		flex-direction:row;
	}
	.searchAddBlock button{
		font-size: 20px;

		padding:5px 20px 5px 20px;
		cursor:pointer;
	}
	.searchAddBlock input{
		width:70%;
		margin:0 auto 0;
		padding:0 20px 0 20px;
	}
	.postList .error{
		margin:5px 0 0;
	}
</style>