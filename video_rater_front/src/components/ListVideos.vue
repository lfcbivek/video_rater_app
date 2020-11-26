<template>
  <div class="">
    <div class="row">
      <div class="col-md-12 mb-5" v-if="createNew">
        <CreateVideo />
      </div>
      <div class="col-md-5 text-center nicefont">
        <h4> Welcome to Video Rater</h4>
        <form @submit="createdNew()">
          <input type="submit" value="Create new video" class="btn-sm btn-primary mb-3 btn-center">
        </form>


        <p v-bind:key="video.id" v-for="video in videos">
          {{video.title}}
          <br />
          Average Rating: {{video.rating_average}}
          <br/>

          <br/>
          <button class="btn-sm btn-primary mt-2 mb-2 detail" v-on:click="videoDetail(video)">Details </button>


        </p>



      </div>

      <div class="col-md-6">
        <VideoDetails v-bind:videodetail="videodetail" />
      </div>





    </div>



  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios';
import VideoDetails from './VideoDetails';
import CreateVideo from './CreateVideo';

export default {
  name: 'ListVideos',
  components: {
    VideoDetails,
    CreateVideo
  },
  data(){
    return{
      videos: [],
      videodetail : Object,
      createNew: "",
    }

  },
  methods: {
    getVideos(){
      axios.get("http://127.0.0.1:8000/api/videos/")
      .then(res => (this.videos = res.data))
      .catch(err => console.log(err));


    },
    videoDetail(video){
      this.videodetail = video
      console.log(this.videodetail)
    },

    createdNew(){
      this.createNew = !this.createNew;
    }
  },
  created(){
    this.getVideos();
    this.createNew= false;
  }
}
</script>


<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Ubuntu:ital,wght@1,300&display=swap');

  .nicefont{
    font-size: 28px;
    font-family: 'Ubuntu', sans-serif;
  }

  .detail:hover{

    transform: scale(1.5);

  }


</style>
