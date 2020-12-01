<template>
  <div class="row video_form">
    <div class = "col-md-6">
        <div class= "card">
          <div class="card-body">
            <form id="createForm" @submit.prevent = "createVideo" >
              <p>
                <label for="title">Title </label>
                <input type="text" name="title" id="title" v-model="title">

              </p>

              <p>
                <label for="description">Description </label>
                <input type="text" name="description" id="description" v-model="description">

              </p>

              <p>
                <label for="url">URL </label>
                <input type="text" name="url" id="url" v-model="url">

              </p>

              <p>
                <label for="category">Category </label>
                <select class="ml-2" name="category" id="category" v-model = "category">
                  <option>Web </option>
                  <option>Tech </option>
                  <option> Vlog</option>

                </select>

              </p>

              <p>
                <label for="sub_category">Sub Category </label>
                <input type="text" name="sub_category" id="sub_category" v-model="sub_category">

              </p>

              <p>
                <label for="author">Author </label>
                <input type="text" name="Author" id="author" v-model="author">

              </p>
              <p>
                <input type="submit" value="submit" @click="$emit('created')">
              </p>

            </form>

          </div>

        </div>


    </div>


  </div>




</template>


<script>

  import axios from 'axios';


  export default{
    name: 'CreateVideo',
    components: {

    },
    data(){
      return{
        title: null,
        description: null,
        url: null,
        category: null,
        sub_category: null,
        author: null,
      }
    },

    methods: {
      createVideo(){
        console.log("Here")
        axios.post("http://127.0.0.1:8000/api/videos/",
          {
            title: this.title,
            description: this.description,
            url: this.url,
            category: this.category,
            sub_category: this.sub_category,
            author: this.author,
          }
        )
        .then(res => console.log(res))
        .catch(err => console.log(err))
      }
    },
}


</script>
