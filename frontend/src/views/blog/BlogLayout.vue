<template>
  <router-view :key="key"></router-view>
</template>

<script>
export default {
  name: 'BlogLayout',
  computed: {
    key () {
      return this.$route.fullPath
    }
  }
}
</script>

<style scoped>

</style>
