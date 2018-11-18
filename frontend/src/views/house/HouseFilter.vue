<template>
<v-dialog v-model="dialog" max-width="800px">
  <v-list three-line subheader>
    <v-subheader>Properties</v-subheader>
    <v-list-tile avatar>
      <v-list-tile-content>
        <v-list-tile-title>Department</v-list-tile-title>
        <v-list-tile-sub-title>Set the department property to get the houses nearest to this department</v-list-tile-sub-title>
      </v-list-tile-content>
    </v-list-tile>
    <v-list-tile avatar>
      <v-list-tile-content>
        <v-list-tile-title>Password</v-list-tile-title>
        <v-list-tile-sub-title>Require password for purchase or use password to restrict purchase</v-list-tile-sub-title>
      </v-list-tile-content>
    </v-list-tile>

    <v-divider></v-divider>

    <v-list three-line subheader>
      <v-subheader>General</v-subheader>
      <v-list-tile avatar>
        <v-list-tile-action>
          <v-checkbox v-model="notifications"></v-checkbox>
        </v-list-tile-action>
        <v-list-tile-content>
          <v-list-tile-title>Notifications</v-list-tile-title>
          <v-list-tile-sub-title>Notify me about updates to apps or games that I downloaded</v-list-tile-sub-title>
        </v-list-tile-content>
      </v-list-tile>
      <v-list-tile avatar>
        <v-list-tile-action>
          <v-checkbox v-model="sound"></v-checkbox>
        </v-list-tile-action>
        <v-list-tile-content>
          <v-list-tile-title>Sound</v-list-tile-title>
          <v-list-tile-sub-title>Auto-update apps at any time. Data charges may apply</v-list-tile-sub-title>
        </v-list-tile-content>
      </v-list-tile>
      <v-list-tile avatar>
        <v-list-tile-action>
          <v-checkbox v-model="widgets"></v-checkbox>
        </v-list-tile-action>
        <v-list-tile-content>
          <v-list-tile-title>Auto-add widgets</v-list-tile-title>
          <v-list-tile-sub-title>Automatically add home screen widgets</v-list-tile-sub-title>
        </v-list-tile-content>
      </v-list-tile>
    </v-list>
  </v-list>

  <v-divider></v-divider>
  <v-list three-line subheader>
  <v-subheader>Price</v-subheader>
    <v-layout row wrap>
      <v-flex xs1>
        <v-text-field v-model="price[0]"  class="price-textfield mr-0" type="number" color="yellow darken-1"></v-text-field>
      </v-flex>

      <v-flex xs10>
        <v-range-slider v-model="price" :max="6000" :min="0" :step="10" color="yellow darken-1"></v-range-slider>
      </v-flex>

      <v-flex xs1>
        <v-text-field class="price-textfield ml-0" v-model="price[1]" type="number" color="yellow darken-1"></v-text-field>
      </v-flex>
    </v-layout>
  </v-list>


  <v-btn flat slot="activator"><v-icon>filter</v-icon>Filter</v-btn>
</v-dialog>
</template>

<script>
export default {
  name: "HouseFilter",
  data: () => {
    return {
      price: [0,6000]
    }
  }
}
</script>

<style scoped>
.price-textfield {
  padding-top: 0px;
  text-align: center;
}
</style>
