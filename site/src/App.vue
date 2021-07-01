<template>
  <div>
    <v-dialog
      v-model="dialogShow"
      max-width="500"
      max-height="1000px"
      style="z-index: 1000"
    >
      <v-card>
        <v-card-title>
        </v-card-title>

<v-tabs
      v-model="tab"
      background-color="transparent"
      color="basil"
      grow
    >
      <v-tab>Log In</v-tab>
      <v-tab>Register</v-tab>
      <!-- last day -->
      <v-tab-item> 
        <v-container fluid>
              <LogIn />
        </v-container>
      </v-tab-item>
      <!-- last day -->

      <!-- last week -->
      <v-tab-item> 
        <v-container fluid>
              <SignUp />
        </v-container>
      </v-tab-item>

    </v-tabs>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="dialogShow = false">
            Exit
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-app id="container">
      <div id="content">
        <v-card color="basil">
          <v-card-title class="py-2">
            <v-spacer> </v-spacer>
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
            <v-spacer style="text-align: right">
              <v-btn v-if="user.loggedIn == false" elevation="2" @click="dialogShow=true">Log In</v-btn>
              <v-btn v-if="user.loggedIn == true" elevation="2" @click="signOut">Log Out</v-btn>
              
              </v-spacer>
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
          <router-view />
        </transition>
      </div>
      <!-- footer -->
      <v-footer id="footer">
        <router-link style="text-decoration: none; color: white" to="/settings"
          ><v-icon small class="mr-2" @click="ShowItem(item)">
            mdi-cog-outline
          </v-icon></router-link
        >
        <v-select
          :items="this.devices1"
          label="Device ID"
          v-show="$route.name=='Home'"
          v-model="$store.getters.getCurrentDevice"
          @change="setDevice($event)"
          style="max-width: 8em; margin-left: 1em"
        >
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
          <a
            href="https://github.com/robertnicolescu42/River-tracker"
            target="_blank"
            style="color: white; text-decoration: none"
            >{{ new Date().getFullYear() }} —
            <strong>Nicolescu Robert</strong></a
          >
        </p>
      </v-footer>
      <!-- footer -->
    </v-app>
  </div>
</template>

<script>
import { db } from "../src/firebase/db.js";
import { mapGetters } from "vuex";
import firebase from "firebase";
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
    dialogShow: false,
  }),
  computed: {
    // map `this.user` to `this.$store.getters.user`
    ...mapGetters({
      user: "user"
    })
  },
  methods: {
    signOut() {
      firebase
        .auth()
        .signOut()
        .then(() => {
          this.$router.replace({
            name: "Home"
          });
        });
    },
    Show() {
      this.dialogShow = true;
    },
    setDevice(device) {
      this.$store.dispatch("setCurrentDevice", device);
    },
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

.a a:hover a:visited {
  color: white;
  text-decoration: none;
}
</style>
