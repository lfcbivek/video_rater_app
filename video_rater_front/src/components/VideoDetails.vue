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

  </div>
</template>

<script>
// @ is an alias to /src
export default {
  name: 'VideoDetails',
  components: {},
  props:{
    videodetail: {},
  },

}

</script>


<style scoped>



</style>
