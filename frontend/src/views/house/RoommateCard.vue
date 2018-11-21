<template>
  <v-card color="orange" class="white--text mt-3">
    <v-layout row>
      <v-flex>
        <v-card-title primary-title>
          <div>
            <div class="headline">Your potential roommate</div>
            <div class="subheading">XXX</div>
            <div>From xx department</div>
            <div>Near ECEB | 3 houses left</div>
          </div>
        </v-card-title>
      </v-flex>
    </v-layout>
    <v-divider light></v-divider>
    <v-card-actions class="pa-3">
      <v-btn color="orange" class="white--text">
        Contact him/her via email
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
    name: "RoommateCard"
}
</script>

<style scoped>

</style>
