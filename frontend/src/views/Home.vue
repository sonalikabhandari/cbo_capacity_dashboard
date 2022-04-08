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
            <h1>Welcome to the CBO Intake Portal</h1><br />
            <h4>Developed and Supported by Service Reliability Engineering</h4><br />
            Core and Backbone Operations
          </div>
        </v-flex>
        <v-spacer></v-spacer>
      </v-layout>
    </v-img>
  </v-layout>
</template>

<script>
export default {
  data: () => ({
    // add data here
  })
}
</script>

<style>
.contain {
  width: 65vw;
  height: 85vh;
  overflow: hidden;
}
</style>
