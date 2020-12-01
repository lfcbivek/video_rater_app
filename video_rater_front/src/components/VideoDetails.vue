<template>
  <div class="">
    <div class = "row">
      <div class="col-md-10">
        <p>Title : {{videodetail.title}}</p>
        <p>Description : {{videodetail.description}}</p>
        <p>Rating : {{videodetail.rating_average}}</p>
        <p>Comments : {{videodetail.comments_list}}</p>
        <p>URL : {{videodetail.url}}</p>
      </div>


    </div>

    <form id= "formvideo" @submit.prevent = "giveRating1(videodetail)" @submit="$emit('updated',videodetail)"> 

      <p>
        <label for = "stars"> Give a Rating </label>
        <input class = "ml-2" type= "text" name="stars" id="stars" v-model="stars">
      </p>

      <p>
        <label for = "comments"> Give a Comment </label>
        <input class = "ml-2" type= "text" name="comments" id="comments" v-model="comments">

      </p>
      <input type="submit" class = "btn-sm btn-primary mt-3 mb-3">

    </form>
    <button class = "btn-sm btn-danger mt-3 mb-3" v-on:click = "videoDelete(videodetail)" @click="$emit('deleted',videodetail)">Delete Video</button>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios';
import {TokenService} from '../storage/service.js';

export default {
  name: 'VideoDetails',
  components: {},
  data(){
    return {
      token: null,
      comments: '',
      stars: '',
    }
  },
  props:{
    videodetail: {},
  },
  methods: {
    videoDelete(videodetail){
      

      let axiosConfig = {
        headers: {
          "Authorization" : "Token "+this.token,
        }
      };
      axios.delete(`http://127.0.0.1:8000/api/videos/${videodetail.id}/`,axiosConfig)
      .then(resp => console.log(resp))
      .catch(err => console.log(err))
      

    },

    giveRating1(videodetail){
      console.log(videodetail.id);
      this.token = TokenService.getToken()
      console.log(this.stars)
      console.log(this.comments)
      let postData = {
        stars: this.stars,
        comments: this.comments
      }

      let axiosConfig = {
        headers: {
          'Authorization': 'Token '+this.token
        }
      }

      axios.post(`http://127.0.0.1:8000/api/videos/${videodetail.id}/rate_video/`,postData,axiosConfig)
      .then(res => console.log(res.data))
      .catch(err => console.log(err))

    }
  },
  created() {
    
    this.token = TokenService.getToken();
  },
}

</script>


<style scoped>



</style>
