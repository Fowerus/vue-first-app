<template>
	<div class="changeLogPas">
		<form>
			<h5>New login</h5>
			<input type="text" placeholder="New Login" v-model ='newLogin'>

			<h5 class='n'>New password</h5>
			<input type="password" placeholder="New password" v-model ='newPassword'>
			<input type="password" placeholder="Repeat new password" v-model = 'repeatPassword'>

			<h5 class='n'>Current password</h5>
			<input type="password" placeholder="Current password" v-model ='curPassword'>
			<button type='button' @click='changeAccInf'>Save</button>
			<h5 class='error' v-if ='error.length > 0'>{{error}}</h5>
		</form>
	</div>
</template>

<script>
import axios from 'axios'	

export default{
	name:'changeLogPas',
	components:{
	},
	data(){
		return{
			newInf:{},
			newLogin:'',
			newPassword:'',
			repeatPassword:'',
			curPassword:'',
			error:'',
		};
	},
	methods:{
		changeAccInf(){
			if (this.curPassword.length > 4){
				if (this.newLogin.length > 4 || this.newPassword.length > 4){

					this.newInf['currentUser'] = localStorage.getItem('current_user');
					this.newInf['newLogin'] = this.newLogin;
					this.newInf['newPassword'] = this.newPassword;
					this.newInf['newRepPassword'] = this.repeatPassword;
					this.newInf['curPassword'] = this.curPassword;

					const path = 'http://localhost:5000/changeLogPas';
					axios.post(path,JSON.stringify(this.newInf))
					.then(res=>{
						if (res.data['Error']){
							this.error = res.data['Error'];
						}else{
							this.newLogin = '',
							this.newPassword = '',
							this.repeatPassword = '',
							this.curPassword = '',
							this.newInf = {};

							if (res.data['current_user']){
								localStorage.setItem('current_user',res.data['current_user']);
							}
							this.error = 'Save successful';
							window.location.href = '/';
						}
					})
				}else{
					this.error = 'Your input is short';
				}
			}else{
				this.error = 'Current password is short';
			}
		}
	},
}
</script>

<style scoped>
	.changeLogPas{
		max-width: 700px!important;
	}
	.changeLogPas form .error{
		max-width: 200px;
		margin:10px auto 0;
	}
	.changeLogPas h5{
		text-align: left;
		margin:0 0 5px 100px ;
	}
	.changeLogPas form{
		max-width: inherit;
		display:flex;
		flex-direction:column;
		border:1px solid black;
		padding:20px 0 20px 0;
	}
	.changeLogPas form input{
		padding:10px 20px 10px 20px;
		margin-bottom:10px;
		width:100%;
		height: 20px;
	}
	.changeLogPas form .n{
		margin-top:20px;
	}
	.changeLogPas form button{
		cursor:pointer;
		width:100px;
		height: 30px;
		margin:10px 0 0 100px;
	}
</style>