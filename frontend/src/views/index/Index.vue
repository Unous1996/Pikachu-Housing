<template lang="html">
  <v-layout fill-height column class="text-xs-center">
    <section>
      <v-parallax src="https://images8.alphacoders.com/779/779982.jpg" height=800>
        <v-layout
          align-center
          justify-center
          class="white--text"
        >
          <v-flex>
            <img src="../../assets/logo.png" alt="Vuetify.js" height="200">
            <h1 class="white--text mb-2 display-3 text-xs-center">BLOGME</h1>
            <div class="subheading mb-3 text-xs-center">Want to start a blog, huh?</div>
            <movedown>
              <v-btn class="transparent" flat dark large @click.stop="scrollToNext('features')">
                <v-icon>
                  keyboard_arrow_down
                </v-icon>
              </v-btn>
            </movedown>
          </v-flex>
        </v-layout>
      </v-parallax>
    </section>
    <section id="features">
      <vintro></vintro>
      <movedown>
          <v-btn class="transparent" flat large @click.stop="scrollToEnd">
            <v-icon blue>
              keyboard_arrow_down
            </v-icon>
          </v-btn>
        </movedown>
    </section>
    <section id="create">
      <v-parallax src="https://images.wallpaperscraft.com/image/book_glasses_coffee_flowers_118088_1350x2400.jpg" height=800>
        <v-layout
          align-center
          justify-center
          class="white--text"
        >
          <v-flex>
            <h1 class="white--text mb-2 display-3 text-s-center">BLOGME</h1>
            <div class="subheading mb-3 text-xs-center">Let's start now!</div>
            <v-btn dark large class="info" to="/blog" >Get Started</v-btn>
          </v-flex>
        </v-layout>
      </v-parallax>
    </section>
  </v-layout>
</template>

<script>
export default {
  name: 'index',
  components: {
    'movedown': () => import('../../components/shared/MoveDown'),
    'vintro': () => import('./Introduction.vue')
  },
  methods: {
    scrollToNext (e) {
      const element = document.getElementById(e)
      const offset = element.getBoundingClientRect().y
      window.scrollTo({'behavior': 'smooth', 'top': offset})
    },
    scrollToEnd () {
      window.scrollTo({'behavior': 'smooth', 'top': document.body.scrollHeight})
    }
  }
}
</script>

<style scoped>

</style>
