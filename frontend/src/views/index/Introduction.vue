<template>
  <v-flex xs12>
    <v-container grid-list-xl class="text-xs-center">
      <v-layout row>
        <v-flex xs12>
          <v-flex xs10 offset-xs1 class="pb-3">
            <div class="display-2"> {{article.title}} </div>
          </v-flex>
        </v-flex>
      </v-layout>
      <v-layout row wrap>
        <v-flex xs6 md4  v-for="(item, idx) in article.items" :key="idx" my-3>
          <v-card flat class="elevation-0 transparent">
            <v-card-text class="text-xs-center">
              <v-icon x-large class="blue--text text--lighten-2">{{item.icon}}</v-icon>
            </v-card-text>
            <v-card-text>
              {{item.template}}
            </v-card-text>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
    <slot></slot>
  </v-flex>
</template>

<script>

export default {
  name: 'Introduction',
  created () {
  },
  data: () => ({
    show: false,
    isList: false,
    article: {
      title: 'Features',
      items: [
        {
          template: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut.',
          icon: 'flash_on'
        },
        {
          template: 'Wmagna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
          icon: 'check_circle'
        },
        {
          template: 'What the fuck man, conin reprehenderit in nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
          icon: 'edit'
        }
      ]
    }
  }),
  methods: {
    toRoute (rname, rparams = {}, query = {}) {
      this.dialog = true
      this.$router.push({name: rname, params: rparams, query: query})
    }
  }
}
</script>

<style scoped>
</style>
