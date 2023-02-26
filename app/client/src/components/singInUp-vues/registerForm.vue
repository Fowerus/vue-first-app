<template>
	<form class="singUpForm">
		<div class="fields">
			<input type="text" placeholder="Login" v-model = 'newLogin'>
			<input type="password" placeholder="Password" v-model = 'newPassword'>
			<input type="button" value="Sing In" @click = 'register'>
		</div>
		<h5 class='error' v-if='error.length > 0'>{{error}}</h5>
	</form>
</template>

<script>
import axios from 'axios'

export default{
	name:'singUp',
	data(){
		return{
			newLogin:'',
			newPassword:'',
			error:''
		};
	},
	methods:{
		register(){
			if (this.newLogin.length >= 4 || this.newPassword >= 4){
				let newUser = {
					'login': this.newLogin,
					'password': this.newPassword
				}
				const path = 'http://localhost:5000/sing_up';
				axios.post(path,JSON.stringify(newUser))
				.then(res => {
					this.error = res.data;
				})
				.catch(res => {
					console.log(res);
				})
			}else{
				return this.error = 'Your inputs is short';
			}
		}
	}
}
</script> 
