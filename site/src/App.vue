<template>
  <v-app id="container">
    <div id="content">
      <v-card color="basil">
        <v-card-title class="text-center justify-center py-2">
          <img
            style="text-decoration: none; color: white"
            src="../src/icons/wave-inverted.png"
            alt="wave-pic"
          />
          <router-link style="text-decoration: none; color: white" to="/"
            ><h1 class="font-weight-bold display-1 basil--text">
              Rivertracker
            </h1></router-link
          >
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
  <transition name="fade" mode="out-in">
         <router-view/>
       </transition>
    </div>
    <!-- footer -->
    <v-footer id="footer">
      <router-link style="text-decoration: none; color: white" to="/settings"
        ><v-icon small class="mr-2" @click="ShowItem(item)">
          mdi-cog-outline
        </v-icon></router-link
      >
      <v-select :items="this.devices1" label="Device ID" v-model="$store.getters.getCurrentDevice" @change="setDevice($event)" style="max-width:8em; margin-left:1em">
        <template v-slot:item="{ item, attrs, on }">
          <v-list-item v-bind="attrs" v-on="on">
            <v-list-item-title
              :id="attrs['aria-labelledby']"
              v-text="item"
            ></v-list-item-title>
          </v-list-item>
        </template>
      </v-select>
      <v-spacer></v-spacer>
      <p style="margin-bottom: 0px">
        {{ new Date().getFullYear() }} — <strong>Nicolescu Robert</strong>
      </p>
    </v-footer>
    <!-- footer -->
  </v-app>
</template>

<script>
import { db } from "../src/firebase/db.js";
export default {
  name: "App",

  components: {},

  data: () => ({
    appName: process.env.VUE_APP_NAME,
    tab: null,
    items: ["Last hour", "Last day", "Last week", "Last month"],
    riverData: [],
    devices1: [],
    currentDevice: 1,
  }),
  methods: {
    setDevice(device){
      this.$store.dispatch("setCurrentDevice",device);
    }
  },
  firestore: {
    riverData: db.collection("setup_data").orderBy("device_id"),
  },
  watch: {
    riverData: function (val) {
      for (let index = 0; index < val.length; index++) {
        this.devices1.push(val[index].device_id);
      }
    },
  },
};
</script>

<style>
#footer {
  position: absolute;
  bottom: 0;
  width: 100%;
  height: 4rem;
}
#content {
  padding-bottom: 4rem; /* Footer height */
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
#router {
  width: 80%;
}
.flexing {
  display: flex;
}
.router-link-active {
  color: red;
}

.fade-enter {
  opacity: 0;
}

.fade-enter-active {
  transition: opacity 0.2s ease;
}

.fade-leave-active {
  transition: opacity 0.2s ease;
  opacity: 0;
}


</style>
