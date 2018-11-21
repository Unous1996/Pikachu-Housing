<template>
  <v-card dark class="white--text mt-3">
    <v-card-title primary-title>
      <div class="headline">Your House suggestion</div>
    </v-card-title>
    <v-card-text>
      <div>Based on your information, our algorithm will suggest best houses to you. Have a try!</div>
    </v-card-text>
    <v-expansion-panel dark expand>
      <v-expansion-panel-content  class="white--text" v-for="(house,i) in houses" :key="i">
        <div color="green" slot="header">{{house.name}}</div>
        <div>
          <v-card-text>
            <h3>Price: {{house.price}}</h3>
            <h4>Distance to your department(xx): xx</h4>
            <div>xx users also like this house</div>
            </v-card-text>
          <v-card-actions>
           <v-btn dark :to="'/house/'+house.id">Have a look</v-btn>
          </v-card-actions>
        </div>
      </v-expansion-panel-content>
    </v-expansion-panel>
  </v-card>
</template>

<script>
import { mapState } from 'vuex'
export default {
  name: "HouseSuggestionCard",
  props: ["houses"],
  computed: mapState({
    //houses: state => state.house.list.results, // todo get the real suggested house
  }),
  data: () => {
    return {
      activeNames: "",
      // houses: [],
    }
  },
  methods: {
     toRoute (rname, rparams = {}, query = {}) {
      this.$router.push({path: rname, params: rparams, query: query})
    },
  }
}
</script>

<style scoped>
.collapse {
  background-color: #4caf50!important;
}
.el-collapse-item {
  background-color: #4caf50!important;
}
</style>
