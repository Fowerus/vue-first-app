<template>
	<div class="todoList">
		<addTodoItem @add-new-todo = 'addNewTodo' v-if = '!loader'/>
		<h5 class='error' v-if ='error.length > 0'>{{error}}</h5>
		<select v-if ='!loader && todos.length > 0' class='optionsTodos' v-model = 'filters'>
			<option value="all">All</option>
			<option value="successful">Successful</option>
			<option value="no-successful">No-successful</option>
		</select>
		<todoItems
		v-if='filterTodos.length > 0'
		:todos = 'filterTodos'
		@removeitem = "removeitem"/>
		<loader v-if ='loader'/>
		<h4 v-else-if='!loader && filterTodos.length == 0'>No todos!</h4>
	</div>
</template>

<script>
import axios from 'axios'

import addTodoItem from '../components/todoList-vues/addTodoItem.vue'
import todoItems from '../components/todoList-vues/todoItems.vue'
import loader from '../components/loader.vue'

export default{
	name:'todoList',
	components:{
		addTodoItem,
		todoItems,
		loader
	},
	data(){
		return{
			todos:[],
			loader:true,
			filters:'all',
			error:''
		};
	},
	methods:{
		getTodos(){
			const path = 'http://localhost:5000/getTodos';
			axios.post(path,JSON.stringify(localStorage.getItem('current_user')))
			.then(res => {
				setTimeout(()=>{
					if (typeof res.data == 'string'){
						this.error = res.data;
					}else{
						this.error='';
						this.todos = res.data.reverse();
					}
					this.loader=false;
				},1000);
			})
			.catch(res => {
				console.log(res);
			})
		},
		addNewTodo(newTodo){
			this.todos.unshift(newTodo);
		},
		removeitem(id){
			const path = 'http://localhost:5000/removeItem';
			axios.post(path,JSON.stringify(id))
			.then(res => {
				if (typeof res.data == 'string'){
					console.log(res.data);
				}else{
					this.todos = this.todos.filter(t => t.id !== id);
				}
			})
			.catch(res => {
				console.log(res);
			})
		}
	},
	computed:{
		filterTodos(){
			if (this.filters === 'all'){
				return this.todos;
			}else if (this.filters === 'successful'){
				return this.todos.filter(t=> t.successful);
			}else if (this.filters === 'no-successful'){
				return this.todos.filter(t=> !t.successful);
			}
			return ''
		}
	},
	created(){
		this.getTodos();
	}
}
</script>

<style>
	.todoList{
		max-width: 500px;
		margin:0 auto 0;
	}
	.optionsTodos{
		margin:5px 0 0;
		font-size: 10px;
		height:20px;
	}
	.todoList .error{
		margin:5px 0 0;
	}
</style>