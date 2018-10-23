<template>
  <v-layout justify-center>

    <v-flex>
      <v-container fluid grid-list-md>

        <v-layout row wrap justify-space-between>
          <v-flex md8 xs12>
          <v-carousel style="height: 400px;">
              <v-carousel-item v-for="(item,i) in houses" :key="i" :src="item.imgs_url">
                <v-layout>
                  <h1 class="white--text ml-4 carousel-title">{{item.name}}</h1>
                </v-layout>
              </v-carousel-item>
            </v-carousel>
          </v-flex>

          <v-flex md3 v-show="$vuetify.breakpoint.mdAndUp">
            <div class="mr-3" style="position:fixed;">
            <v-card color="blue-grey darken-2" class="white--text mt-3">
                  <v-card-title primary-title>
                    <div class="headline">Unlimited music now</div>
                  </v-card-title>
                  <v-card-text>
                    <div>Listen to your favorite artists and albums whenever and wherever, online and offline.</div>
                  </v-card-text>
                  <v-card-actions>
                    <v-btn flat dark>Listen now</v-btn>
                  </v-card-actions>
              </v-card>

              <v-card color="purple" class="white--text mt-3">
                <v-layout row>
                  <v-flex xs7>
                    <v-card-title primary-title>
                      <div>
                        <div class="headline">Halycon Days</div>
                        <div>Ellie Goulding</div>
                        <div>(2013)</div>
                      </div>
                    </v-card-title>
                  </v-flex>
                  <v-flex xs5>
                    <v-img
                      src="https://cdn.vuetifyjs.com/images/cards/halcyon.png"
                      height="125px"
                      contain
                    ></v-img>
                  </v-flex>
                </v-layout>
                <v-divider light></v-divider>
                <v-card-actions class="pa-3">
                  Rate this album
                </v-card-actions>
            </v-card>
            </div>
          </v-flex>

          <v-flex md8>
            <h3>House list</h3>
            <v-divider></v-divider>
          </v-flex>

          <v-flex md8>
            <v-layout row wrap>
              <v-flex v-for="item in houses" v-bind="{ [`xs${item.flex}`]: true }" :key="item.id">
                <v-hover>
                  <v-card class="mt-3" slot-scope="{ hover }" :class="`elevation-${hover ? 6 : 2}`" :to="'/house/'+item.id">
                    <v-layout row>
                      <v-flex md3 v-show="$vuetify.breakpoint.mdAndUp">
                        <v-img :src="item.imgs_url" @click.stop="$router.push(item.id)"></v-img>
                      </v-flex>
                      <v-flex md9 xs12>
                        <v-card-title class="pb-2">
                          <div class="headline">{{item.name}}</div><br>
                        </v-card-title>
                          <v-card-text class="pt-2">
                            <span class="grey--text">Location: {{item.location}}</span><br>
                            <span>Price: ${{item.price}}</span><br>
                            <span class="grey--text">{{item.description}}</span>
                          </v-card-text>
                        <v-card-actions>
                          <v-btn flat color="orange">Share</v-btn>
                          <v-btn flat color="orange">Explore</v-btn>
                        </v-card-actions>
                      </v-flex>
                    </v-layout>
                  </v-card>
                </v-hover>
              </v-flex>
            </v-layout>
          </v-flex>

        </v-layout>
        <v-flex md12 class="mt-3">
          <div class="text-xs-center">
            <v-pagination
              v-model="page"
              :length="6"
            ></v-pagination>
          </div>
        </v-flex>

      </v-container>
    </v-flex>
  </v-layout>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'HouseList',
  created() {
    this.$store.dispatch('house/getList')
  },
  computed: mapState({
    houses: state => state.house.list.results
  }),
}
</script>

<style scoped>
.carousel-title {
  position: absolute;
  bottom: 20%;
  font-size: 40px;
}
</style>
