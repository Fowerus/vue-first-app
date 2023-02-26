<template>
	<div class="singInUpForm">
		<ul class="changeForm">
			<li id='singInBtn' :class='{select:seeSingIn}' @click = 'seeSingIn = true'>Sing In</li>
			<li id='singUpBtn' :class='{select:!seeSingIn}' @click = 'seeSingIn = false'>Sing Up</li>
		</ul>
		<div class="singForms">
			<h3 class='fieldName'>{{fieldName}}</h3>
			<loginForm v-if='seeSingIn' />
			<registerForm v-if='!seeSingIn'/>
		</div>
	</div>
</template>

<script>
import loginForm from '../components/singInUp-vues/loginForm.vue'
import registerForm from '../components/singInUp-vues/registerForm.vue'

export default{
	name:'singInUp',
	components:{
		loginForm,
		registerForm
	},
	data(){
		return{
			seeSingIn:true
		};
	},
	methods:{
	},
	computed:{
		fieldName(){
			if (this.seeSingIn){
				return 'Sing In';
			}
			return 'Sing Up';
		}
	}
}
</script>


<style>
	.singInUpForm{
		margin:0 auto 0;
		max-width: 450px;
		border-top:1px solid black;
		border-bottom:1px solid black;
		border-radius: 30px;
		padding:10px;
	}
	.singInUpForm .singForms .fields{
		max-width: 400px;
		margin:0 auto 0;
		display: flex;
		flex-direction: column;
	}
	.singInUpForm form .fields input:not(:last-child){
		width:90%;
		height:40px;
		font-size: 15px;
		padding:0 20px 0 20px;
		margin:0 auto 10px;
	}
	.singInUpForm form .fields input:last-child{
		font-size: 15px;
		padding:5px;
		width:100px;
		margin-bottom:10px;
	}
	.singInUpForm .changeForm{
		max-width: 150px;
		display: flex;
		justify-content: space-between;
		margin: 15px auto 15px;
		padding:0;
		list-style:none;
	}
	.singInUpForm .changeForm li{
		cursor:pointer;
		-moz-user-select: none;
		-webkit-user-select: none;
		-ms-user-select: none;
		user-select: none;
	}
	.singInUpForm .changeForm .select{
		text-decoration: underline;
		color:green;
	}
	.fieldName{
		margin:10px auto 10px;
	}
	.error{
		margin: 0;
	}	
</style>