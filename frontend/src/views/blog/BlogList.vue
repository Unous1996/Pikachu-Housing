<template>
  <v-layout justify-center>

    <v-flex>
      <v-container fluid grid-list-md>

        <v-layout row wrap justify-space-between>
          <v-flex md8 xs12>
          <v-carousel style="height: 400px;">
              <v-carousel-item v-for="(item,i) in items" :key="i" :src="item.src">
                <v-layout>
                  <h1 class="white--text ml-4 carousel-title">{{item.title}}</h1>
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
            <h3>Blog list</h3>
            <v-divider></v-divider>
          </v-flex>

          <v-flex md8>
            <v-layout row wrap>
              <v-flex v-for="item in items" v-bind="{ [`xs${item.flex}`]: true }" :key="item.id">
                <v-hover>
                  <v-card class="mt-3" slot-scope="{ hover }" :class="`elevation-${hover ? 6 : 2}`" :to="'/blog/'+item.id">
                    <v-layout row>
                      <v-flex md3 v-show="$vuetify.breakpoint.mdAndUp">
                        <v-img :src="item.src" @click.stop="$router.push(item.id)"></v-img>
                      </v-flex>
                      <v-flex md9 xs12>
                        <v-card-title class="pb-2">
                          <div class="headline">{{item.title}}</div><br>
                        </v-card-title>
                          <v-card-text class="pt-2">
                            <span class="grey--text">Number 10</span><br>
                            <span>Whitehaven Beach</span><br>
                            <span>{{item.content}}</span>
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
export default {
  name: 'BlogList',
  data () {
    return {
      page: 1,
      items: [ {
        id: 1,
        flex: 12,
        title: 'The dog example',
        src: 'https://www.codeproject.com/KB/GDI-plus/ImageProcessing2/img.jpg',
        content: 'I\'m a thing. But, like most politicians, he promised more than he could deliver. You won\'t have time for sleeping, soldier, not with all the bed making you\'ll be doing.'
      },
      {
        id: 2,
        flex: 12,
        title: 'Listen some music!',
        src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
        content: 'I\'m a thing. But, like most politicians, he promised more than he could deliver. You won\'t have time for sleeping, soldier, not with all the bed making you\'ll be doing.'
      },
      {
        id: 3,
        flex: 12,
        title: 'Rock & Roll!',
        src: 'https://cdn.vuetifyjs.com/images/cards/foster.jpg',
        content: 'I\'m a thing. But, like most politicians, he promised more than he could deliver. You won\'t have time for sleeping, soldier, not with all the bed making you\'ll be doing.'
      }
      ]
    }
  }
}
</script>

<style scoped>
.carousel-title {
  position: absolute;
  bottom: 20%;
  font-size: 40px;
}
</style>
