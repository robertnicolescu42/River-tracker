<template>
  <v-app>
  <v-card color="basil">
    <v-card-title class="text-center justify-center py-2">
      <img src="../src/icons/wave-inverted.png" alt="wave-pic">
      <h1 class="font-weight-bold display-1 basil--text">
         Rivertracker
      </h1>
    </v-card-title>

    <v-tabs
      v-model="tab"
      background-color="transparent"
      color="basil"
      grow
    >
      <v-tab
        v-for="item in items"
        :key="item"
      >
        {{ item }}
      </v-tab>
    </v-tabs>
<!-- 
    <v-tabs-items v-model="tab">
      <v-tab-item
        v-for="item in items"
        :key="item"
      >
      </v-tab-item>
    </v-tabs-items> -->
  </v-card>
    <router-view />

    <!-- footer -->
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
    <!-- footer -->
  </v-app>
</template>

<script>

export default {
  name: 'App',

  components: {

  },

  data: () => ({
    appName: process.env.VUE_APP_NAME,
    tab: null,
    items: ['Last hour', 'Last day', 'Last week', 'Last month'],
  }),
};
</script>

<style>
body::-webkit-scrollbar {
  display: none; /* this line of code hides the scrollbar */
}
</style>
