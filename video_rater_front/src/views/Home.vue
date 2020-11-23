<template>
  <div class="home">

    <ListVideos />
  </div>
</template>

<script>
// @ is an alias to /src
import ListVideos from '@/components/ListVideos.vue'

export default {
  name: 'Home',
  components: {
    ListVideos
  }
}
</script>
