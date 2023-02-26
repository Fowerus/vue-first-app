<template>
	<form class="singInForm">
		<div class="fields">
			<input type="text" placeholder="Login" v-model = 'Login'>
			<input type="password" placeholder="Password" v-model = 'Password'>
			<input type="button" value="Sing In" @click = 'login'>
		</div>
		<h5 class='error' v-if='error.length > 0'>{{error}}</h5>
	</form>
</template>

<script>
import axios from 'axios'

export default{
	name:'singIn',
	data(){
		return{
			Login:'',
			Password:'',
			error:''
		};
	},
	methods:{
		login(){
			if (this.Login.length >= 4 || this.Password >= 4){
				let User = {
					'login': this.Login,
					'password': this.Password
				}
				const path = 'http://localhost:5000/sing_in';
				axios.post(path,JSON.stringify(User))
				.then(res => {
					if (typeof res.data == 'string'){
						this.error = res.data;
					}else{
						localStorage.setItem('current_user',res.data['current_user']);
						this.error = '';
						window.location.href = '/';
					}
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
