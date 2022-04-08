<template>
  <v-layout pl-3 pr-3 align-center justify-center app fill-height>
    <v-img :src="require('../assets/spectrum_background.jpg')"
           :aspect-ratio="1"
           class="contain"
    >
      <v-layout fill-height column class="lightbox white--text">
        <v-spacer></v-spacer>
        <v-flex align-center justify-center>
          <div class="subheading text-center">
            You have been logged out from the system
          </div>
          <div class="body-1 text-center">
            Thank you for spending time with us today.
          </div>
        </v-flex>
        <v-spacer></v-spacer>
      </v-layout>
    </v-img>
  </v-layout>
</template>

<script>

export default {
  components: {

  },
  beforeMount () {
    this.$store.dispatch('logout')
  }
}
</script>

<style>
.contain {
  width: 65vw;
  height: 85vh;
  overflow: hidden;
}
</style>
