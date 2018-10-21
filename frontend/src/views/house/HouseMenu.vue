<template>
  <v-container>
    <v-card class="mr-5" style="position: fixed;">
      {{content}}
    </v-card>
  </v-container>
</template>

<script>
export default {
  name: 'HouseMenu',
  props: ['content'],
  data () {
    return {

    }
  }
}
</script>

<style scoped>

</style>
