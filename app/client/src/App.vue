<template>
  <div id="app">
    <h2 class='UserName' v-if='checkUser !== ""'>{{checkUser}}</h2><br>
    <h5 class='UserLogout' v-if="checkUser !==''" @click='Logout'>Logout</h5>  
    <router-view/>
  </div>
</template>
<script>
export default{
  name:'app',
  data(){
    return{
    };
  },
  methods:{
    Logout(){
      localStorage.removeItem('current_user');
      return window.location.href = '/';
    },
  },
  computed:{
    checkUser(){
      if (localStorage.getItem('current_user')){
        return localStorage.getItem("current_user");
      }else{
        return '';
      }
    }
  },
  created(){
    this.checkUser;
  }
}
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
