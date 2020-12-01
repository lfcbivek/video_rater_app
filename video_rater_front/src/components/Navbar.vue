<template>
  <div>

  <b-navbar type="light" variant="light">
    <b-navbar-brand href="#">Video Rater</b-navbar-brand>
    <b-navbar-nav class="ml-auto">
      <b-nav-form @submit.prevent="login" v-if="token==null">
        <b-form-input class="mr-sm-2" placeholder="Username" v-model="username"></b-form-input>
        <b-form-input class="mr-sm-2" type="password" placeholder="Password" v-model="password"></b-form-input>
        <b-button variant="outline-success" class="my-2 my-sm-0" type="submit">Log In</b-button>
      </b-nav-form>

      <b-nav-form @submit.prevent="logout" v-if="token !== null">
        <b-button variant="outline-success" class="my-2 my-sm-0" type="submit">Log Out</b-button>

      </b-nav-form>

      <b-nav-form @submit.prevent="register" v-if="token == null">
        <b-button :to="{name: 'register'}" variant="outline-success" class="my-2 my-sm-0" type="submit">Register</b-button>

      </b-nav-form>
    </b-navbar-nav>
  </b-navbar>
</div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios';

export default {
  name: 'Navbar',
  components: {

  },
  data(){
    return{
      username: '',
      password: '',
      token: localStorage.getItem('user-token') || null,
    }
  },
  methods: {
    login(){
      axios.post("http://127.0.0.1:8000/auth/", {
        username: this.username,
        password: this.password
      })
      .then(res => {
        this.token = res.data.token;
        console.log(this.token);
        localStorage.setItem('user-token',res.data.token);
      })
      .catch(err => {
        console.log(err);
        localStorage.removeItem('user-token')
      })
    },

    logout(){
      localStorage.removeItem('user-token');
      this.token = null
      
    },
    register(){
      console.log("register")
    }
  }
}
</script>
