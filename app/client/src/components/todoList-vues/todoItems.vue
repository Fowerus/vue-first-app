<template>
	<div class='todoItems'>
		<todoItem 
		v-for='(item,i) of todos'
		:todoItem = 'item'
		:key = 'item.id'
		:index='i'
		@removeitem = 'removeitem'/>
	</div>
</template>

<script>
import todoItem from './todoItem.vue'

export default{
	name:'todoItems',
	components:{
		todoItem:todoItem
	},
	props:['todos'],
	data(){
		return{

		};
	},
	methods:{
		removeitem(id){
			this.$emit('removeitem',id);
		},
	}
}
</script>
<style scoped>
	.todoItems{
		padding: 0 20px 0 20px;
		margin: 20px auto 50px;
		overflow: auto;
		max-width: inherit;
		max-height: 500px;
		border: 1px solid black;
	}
</style>