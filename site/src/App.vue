<template>
  <v-app>
    
    <router-view />


        <v-footer 
        absolute
        >
            <v-col
            class="text-right"
            cols="12"
            >
            {{ new Date().getFullYear() }} — <strong>Nicolescu Robert</strong>
            </v-col>
        </v-footer>


  </v-app>
</template>

<script>

export default {
  name: 'App',

  components: {

  },

  data: () => ({
    //
  }),
};
</script>

<style>
body::-webkit-scrollbar {
  display: none; /* this line of code hides the scrollbar */
}
</style>
