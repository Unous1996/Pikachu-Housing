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
              <v-icon x-large class="blue--text text--lighten-2" color="yellow darken-3">{{item.icon}}</v-icon>
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
          template: 'Pikachu housing is a Single Page Application for searching house in Champaign-Urbana area. Most freshmen in UIUC are hard to find their rooms, so we provide this free service.',
          icon: 'flash_on'
        },
        {
          template: 'We use authentic data from various source. Our parser ensures the prices are precise and our suggestion algorithm will provide best houses for you based on your behaviors and requests.',
          icon: 'check_circle'
        },
        {
          template: 'You are allowed to create comments and make friends with those users who might be a good future roommate for you.',
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
