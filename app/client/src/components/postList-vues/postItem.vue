<template>
	<div class='postItem'>
		<h3 class="title">{{postItem.title}}</h3>
		<h5 class="text">{{readPost}}</h5>
		<div class="postFooter">
			<h5 class='author'>by {{postItem.author}}</h5>
			<button class='readBtn' @click = 'readThisPost'>{{checkBtn}}</button>
		</div>
	</div>
</template>

<script>

export default{
	name:'postItem',
	props:{
		postItem:{
			type:Object,
			required:true
		},
	},
	data(){
		return{
			read:false
		};
	},
	methods:{
		readThisPost(){
			if (this.postItem.text.length >= 200){
				this.read = !this.read;
			}
		}

	},
	computed:{
		readPost(){
			if (this.read){
				return this.postItem.text;
			}
			else{
				if (this.postItem.text.length >= 200){
					return this.postItem.text.slice(0,198).toString()+'...';
				}else{
					return this.postItem.text
				}
			}
		},
		checkBtn(){
			if (this.read){
				return 'Close';
			}else{
				return 'Read';
			}
		}
	},
	created(){
	}
}
</script>

<style scroped>
	.postItem{
		max-width: 700px;
		padding:20px 20px 20px 20px;
		margin:0px;
		text-align: left;
		border:1px solid black;
	}
	.postItem:not(:last-child){
		margin-bottom: 20px;
	}
	.postItem .title, .author{
		margin:0;
		max-width: 500px;
	}
	.postItem .text{
		font-weight: 400;
		font-size: 14px;
		max-width: 500px;
	}
	.postFooter{
		max-width: inherit;
		display: flex;
		justify-content: space-between;
		align-items: center;
	}
	.postFooter button{
		cursor:pointer;
	}
	.postFooter .readBtn{
		padding:5px 20px 5px 20px;
	}
</style>