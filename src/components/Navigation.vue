<template>
  <div>
    <v-app-bar app >
      <v-app-bar-nav-icon
        class="grey--text"
        @click="drawer = !drawer"
      ></v-app-bar-nav-icon>
      <v-toolbar-title class="text-uppercase grey--text">
        <span class="font-weight-light">{{name[0].title}}</span>
        <span>{{name[0].title_sr}}</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn color="grey" text>
      {{name[0].extention}}
      </v-btn>
    </v-app-bar>
<v-navigation-drawer v-model="drawer" app style="background-color:#272727">
      <v-list>
<v-list-item v-for="i in this.links" :key="i.text" router :to="i.route">
            <v-list-item-action>
                <v-icon  >
                    {{i.icon}}
                </v-icon>
            </v-list-item-action>
          <v-list-item-content>
              <v-list-item-title >
                  {{i.text}}
              </v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
  </div>
</template>

<script>
import { db } from "../firebase/db.js";
export default {
  
  data() {
    return {
      name:[],
      drawer: false,
      links:[
          {icon: 'mdi-view-dashboard', text: 'Home', route:'/'},
          {icon: 'mdi-account-supervisor', text: 'Team', route:'/team'},
          {icon: 'mdi-silverware ', text: 'Menu', route:'/Menu'},
          {icon: 'mdi-speaker', text: 'Songs', route:'/Songs'},
          {icon: 'mdi-image-multiple', text: 'Photos', route:'/Photos'},
          {icon: 'mdi-google-keep', text: 'Notite', route:'/keep'},
      ]
    };
  },
  firestore: {
    name: db.collection("name"),
  },
};
</script>

<style>
</style>