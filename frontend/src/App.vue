<template>
  <div id="app">
    <v-app>
      <vsidebar :visible="sidebarVisible"></vsidebar>
      <vheader :toggle="toggle" v-if="headerVisible"></vheader>
      <vcontent>
        <router-view></router-view>
      </vcontent>
      <vfooter></vfooter>
    </v-app>
  </div>
</template>

<script>
export default {
  name: 'App',
  data () {
    return {
      sidebarVisible: false,
      headerVisible: true
    }
  },
  methods: {
    toggle () {
      this.sidebarVisible = !this.sidebarVisible
    }
  },
  components: {
    'vheader': () => import('./components/Header.vue'),
    'vsidebar': () => import('./components/Sidebar.vue'),
    'vcontent': () => import('./components/Content.vue'),
    'vfooter': () => import('./components/Footer.vue')
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
</style>
