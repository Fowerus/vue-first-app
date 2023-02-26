<template>
	<div class='todoItem'>
		<input type="checkbox"
		@change="changeCondition"/>
		<strong :class="{successful:todoElem.successful}">{{todoElem.name.toUpperCase()}}</strong>
		<button @click = 'removeitem(todoElem.id)'>X</button>

	</div>
</template>

<script>
import axios from 'axios'

export default{
	name:'todoItem',
	props:{
		todoItem:{
			type:Object,
			required:true
		}
	},
	data(){
		return{

		};
	},
	methods:{
		removeitem(id){
			this.$emit('removeitem',id);
		},
		changeCondition(){
			this.todoElem.successful = !this.todoElem.successful;
			const path = 'http://localhost:5000/changeCondition';
			axios.post(path,JSON.stringify(this.todoElem.id))
			.then(res => {
				if (typeof res.data == 'string'){
					console.log(res.data)
				}
			})
			.catch(res => {
				console.log(res);
			})
		}
	},
	computed:{
		todoElem(){
			return this.todoItem;
		}
	}
}
</script>

<style scoped>
	.todoItem{
		position: relative;
		padding:0;
		margin:20px auto 0;
		text-align: left;
	}
	.todoItem:not(:last-child)::after{
		content: '';
		position: absolute;
		top:35px;
		width:70%;
		height: 1px;
		left:15%;
		background: grey;
	}
	.todoItem:last-child{
		margin-bottom:10px;
	}
	.todoItem input{
		width: 20px;
		height: 20px;
	}
	.todoItem strong{
		margin:0 0 0 35px;
	}
	.todoItem button{
		font-size:15px;
		cursor:pointer;
		background: transparent;
		outline:none;
		margin:0;
		padding:0;
		width:20px;
		height: 20px;
		border:none;
		float:right;
	}
	.successful{
		text-decoration: line-through;
	}
</style>