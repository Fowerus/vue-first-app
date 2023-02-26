<template>
	<div class="addNewTodo">
		<input type="text" placeholder="New todo" v-model="newTodosField">
		<button @click = 'addNewTodos'>+</button>
		<h5 class='error' v-if ='error.length > 0'>{{error}}</h5>
	</div>
</template>

<script>
import axios from 'axios'

export default{
	name:'addTodoItem',
	data(){
		return{
			newTodosField:'',
			error:''
		};
	},
	methods:{
		addNewTodos(){
			if (this.newTodosField.length > 3 && this.newTodosField.length < 30){
				const path = 'http://localhost:5000/addNewTodos';
				axios.post(path, JSON.stringify({todo_name:this.newTodosField, current_user:localStorage.getItem('current_user')}))
				.then(res => {
					if (typeof res.data == 'string'){
						this.error = res.data;
					}else if(res.data['new_id']){
						let newItem = {
							id:res.data['new_id'],
							name: this.newTodosField.trim(),
							successful:false
						};
						this.$emit('add-new-todo', newItem);
						this.newTodosField = '';
						this.error = '';
					}
				})
				.catch(res=>{
					console.log(res);
				})
			}else if (this.newTodosField.length >= 30){
				this.error = 'Write less text';
			}else if (this.newTodosField.length <= 3){
				this.error = 'Write more text';
			}
		}
	}
}
</script>

<style scoped>
	.addNewTodo{
		display: flex;
		flex-direction: row;
	}
	.addNewTodo button{
		padding:5px 20px 5px 20px;
		font-size: 20px;
		cursor:pointer;
	}
	.addNewTodo input{
		width:70%;
		margin:0 auto 0;
	}
	.addNewTodo .error{
		margin:5px 0 0;
	}
</style>