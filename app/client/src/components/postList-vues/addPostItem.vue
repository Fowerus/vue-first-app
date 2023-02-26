<template>
	<div class='addPostItem'>
		<h3 class='closeField' @click = 'closeField'>X</h3>
		<form>
			<h2>Create a new post</h2>
			<input type="text" placeholder="title" v-model='title'>
			<textarea placeholder="text" maxlength='10000' v-model='text' cols = '25' wrap="soft | hard"></textarea>
			<input @click = 'addPost' type="button" value="Create">
		</form>
		<h5 class='error' v-if='error.length > 0'>{{error}}</h5>
	</div>
</template>

<script>
import axios from 'axios'	

export default{
	name:'postItem',
	data(){
		return{
			title:'',
			text:'',
			error:''
		};
	},
	methods:{
		addPost(){
			if (this.title.length > 7 && this.text.length > 20){
				const path = 'http://localhost:5000/addNewPost';
				let newPost = {
					title:this.title,
					text:this.text,
					author: localStorage.getItem('current_user')
				};
				axios.post(path, JSON.stringify(newPost))
				.then(res =>{
					if (typeof res.data == 'string'){
						this.error = res.data;
					}else{
						newPost['id'] = res.data;
						this.error = 'Post added';
						this.$emit('add-new-post', newPost);
					}
				})
			}else{
				this.error = 'Your inputs is short';
			}
		},
		closeField(){
			this.$emit('close-field');
		}
	},
	computed:{
	}
}
</script>

<style scroped>
	.addPostItem{
		max-width: 500px;
		max-height: 700px;
		width:100%;
		height:100%;
		
		border:1px solid black;
		background: white;
		padding:10px;
		margin:0px auto 50px;
	}
	.addPostItem .closeField{
		cursor:pointer;
		-moz-user-select: none;
		-webkit-user-select: none;
		-ms-user-select: none;
		user-select: none;
		margin:0;

		position: absolute;
	}
	.addPostItem form{
		max-width: inherit;
		margin:30px auto 0px;
		display: flex;
		flex-direction: column;
	}
	.addPostItem form h2{
		margin:0 0 20px 0;
	}
	.addPostItem form textarea, input:not(:last-child){
		max-width: 400px;
		width:100%;
		height:40px;
		font-size: 15px;
		padding:0 20px 0 20px;
		margin:0 auto 10px;
	}
	.addPostItem form textarea{
		resize:vertical;
		min-height: 150px;
		max-height: 400px;
		font-size: 13px;
		padding:10px 20px 10px 20px;
	}
	.addPostItem form input:last-child{
		cursor:pointer;
		font-size: 15px;
		width:100px;
		padding:5px 10px 5px 10px;
		margin:0 0 10px 32px;
	}
	.addPostItem .error{
		margin:0;
	}
</style>
