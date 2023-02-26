<template>
	<div class="mainBlock">
		<div id="nav">
			<h2 class = 'MajorMenu'>Main manu</h2>
			<div class="navElems">
				<h4 class='navElem' @click = 'changeBlock("todoList")'>Your Todo</h4>
				<h4 class='navElem' @click = 'changeBlock("postList")'>Posts</h4>
				<h4 class='navElem' @click = 'changeBlock("account")'>{{checkUser}}</h4>
			</div>
		</div>
    </div>
    <component :is='currentBlock'></component> 
</template>

<script>
import singInUp from './singInUp.vue'
import todoList from './todoList.vue'
import postList from './postList.vue'
import account from './account.vue'

export default{
	name:'main',
	data(){
		return{
			currentBlock:''
		};
	},
	components:{
		singInUp,
		todoList,
		postList,
		account
	},
	methods:{
		changeBlock(name){
			if (!localStorage.getItem('current_user')){
				return this.currentBlock = 'singInUp';
			}
			return this.currentBlock = name;
		}
	},
	computed:{
		checkUser(){
			if (localStorage.getItem('current_user')){
				return localStorage.getItem('current_user');
			}
			return 'Sing In'
		}
	},
	created(){
		this.changeBlock('todoList');
	}
}
</script>

<style scroped>
	#nav {
		padding: 30px 30px 10px 30px;
	}
	.navElems{
		max-width: 300px;
		display: flex;
		justify-content: space-between;
		margin:0 auto 0;
	}
	#nav .navElems h4.navElem {
		cursor:pointer;
		font-weight: bold;
		text-decoration: none;
		color: #2c3e50;
		-moz-user-select: none;
		-webkit-user-select: none;
		-ms-user-select: none;
		user-select: none;

	}
	#nav h2.MajorMenu{
		margin:0 auto 10px;
		padding:0;
	}
	.UserName, .UserLogout, .registerLink{
		position: absolute;
		-moz-user-select: none;
		-webkit-user-select: none;
		-ms-user-select: none;
		user-select: none;
	}
	.UserLogout:hover, .registerLink:hover{
		cursor:pointer;
		text-decoration: underline;
	}
</style>