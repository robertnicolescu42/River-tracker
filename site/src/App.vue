<template>
  <v-app id="container">
    <div id="content">
    <v-card color="basil">
      <v-card-title class="text-center justify-center py-2">

        <img  style="text-decoration:none; color:white;" src="../src/icons/wave-inverted.png" alt="wave-pic" />
        <router-link style="text-decoration:none; color:white;" to="/"><h1 class="font-weight-bold display-1 basil--text">Rivertracker</h1></router-link>
       

      </v-card-title>

      <!-- 
    <v-tabs-items v-model="tab">
      <v-tab-item
        v-for="item in items"
        :key="item"
      >
      </v-tab-item>
    </v-tabs-items> -->
    </v-card>
    <router-view id="router"></router-view>
</div>
    <!-- footer -->
    <v-footer id="footer">
      
        <router-link style="text-decoration:none; color:white;" to="/settings"><v-icon small class="mr-2" @click="ShowItem(item)"> mdi-cog-outline </v-icon></router-link>
                 <v-spacer></v-spacer>
      <p style="margin-bottom:0px">
        {{ new Date().getFullYear() }} — <strong>Nicolescu Robert</strong>
      </p>
    </v-footer>
    <!-- footer -->
  </v-app>
</template>

<script>
export default {
  name: "App",

  components: {},

  data: () => ({
    appName: process.env.VUE_APP_NAME,
    tab: null,
    items: ["Last hour", "Last day", "Last week", "Last month"],
  }),
};
</script>

<style>
#footer{
   position: absolute;
  bottom: 0;
  width: 100%;
  height: 4rem;
}
#content {
  padding-bottom: 4rem;    /* Footer height */
}

#container {
  position: relative;
  min-height: 100vh;
}
body {
  overflow: hidden;
}
body::-webkit-scrollbar {
  display: none; /* this line of code hides the scrollbar */
}
#router{
      width:80%;
}
.flexing {
  display:flex;
}
</style>
