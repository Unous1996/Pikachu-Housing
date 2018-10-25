<template>
  <v-toolbar app dense fixed dark clipped-left class="info darken-2">
    <v-btn dark flat @click.stop="onToggle" class="info">
      <v-icon>menu</v-icon>
    </v-btn>
    <v-avatar tile="tile" style="cursor: pointer">
      <img class="ml-3" src="../assets/logo.png" style="height: 30px;width: 30px" @click.stop="toRoute('index')">
    </v-avatar>
    <v-toolbar-title class="mr-5 align-center">
      <div> Pikachu! </div>
    </v-toolbar-title>
    <v-layout row justify-center>
      <v-flex xs12 sm10 style="max-width: 750px">
        <v-text-field
          placeholder="Search..."
          single-line
          append-icon="search"
          :append-icon-cb="() => {}"
          dark
        ></v-text-field>
      </v-flex>
    </v-layout>
      <v-menu transition="slide-y-transition" bottom>
        <v-btn dark icon slot="activator">
          <v-icon>more_vert</v-icon>
        </v-btn>
        <v-list>
          <v-list-tile
            v-for="(item, i) in items"
            :key="i"
            @click=""
          >
            <v-list-tile-title><v-icon>{{ item.icon }}</v-icon> {{ item.title }}</v-list-tile-title>
          </v-list-tile>
        </v-list>
      </v-menu>

</v-toolbar>
</template>
<script>
export default {
  name: 'Header',
  props: ['toggle'],
  data () {
    return {
      isList: true,
      items: [{
        title: "Create new house",
        to: "/house/create",
        icon: "create",
      }]
    }
  },
  methods: {
    onToggle () {
      this.toggle()
    },
    toRoute (rname, rparams = {}, query = {}) {
      this.dialog = true
      this.$router.push({name: rname, params: rparams, query: query})
    }
  }
}
</script>

<style scoped>

</style>
