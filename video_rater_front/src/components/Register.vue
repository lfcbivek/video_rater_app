<template>
    <div class = "container">
        <h1> User Registration </h1>

        <form id = "Registerform" @submit.prevent="createUser">
            <p>
                <label for = "username"> Username </label>
                <input type="text" class="ml-2" name="username" id="username" v-model="username">

            </p>

            <p>
                <label for = "username"> Password </label>
                <input type="password" class="ml-2" name="password" id="password" v-model="password">

            </p>

            <input type="submit">
        </form>



    </div>




</template>
<script>
import axios from 'axios';

export default {
    name: 'register',
    components: {},
    data(){
        return{
            username: '',
            password: ''
        }
    },
    methods: {

        createUser(){
            axios.post("http://127.0.0.1:8000/api/user/",
            {
                username: this.username,
                password: this.password
            })
            .then(resp=> console.log(resp))
            .catch(err=> console.log(err))
            this.$router.push('/')
        }
        
        
    },

}
</script>

<style scoped>

</style>

