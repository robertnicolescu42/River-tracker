<template>
  <v-card class="mx-auto" max-width="500">
    <v-card-title class="text-h6 font-weight-regular justify-space-between">
      <span>{{ currentTitle }}</span>
    </v-card-title>

    <v-window v-model="step">
      <v-window-item :value="1">
        <v-card-text>
          <v-text-field
            v-model="email"
            label="Email"
            type="email"
          ></v-text-field>
          <v-text-field
            v-model="password"
            label="Password"
            type="password"
          ></v-text-field>
          <span class="text-caption grey--text text--darken-1">
            {{ error }}
          </span>
        </v-card-text>
      </v-window-item>

      <v-window-item :value="2">
        <div class="pa-4 text-center">
          <v-img
            class="mb-4"
            contain
            height="40"
            src="../icons/wave-inverted.png"
          ></v-img>
          <h3 class="text-h6 font-weight-light mb-2">
            Welcome to Rivertracker
          </h3>
          <span class="text-caption grey--text">You are now logged in.</span>
        </div>
      </v-window-item>
    </v-window>

    <v-divider></v-divider>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn :disabled="step === 2" depressed @click="login()"> Log In </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import firebase from "firebase";
export default {
  data: () => ({
    step: 1,
    error: "Enter your credentials.",
    email: "",
    password:""
  }),

  computed: {
    currentTitle() {
      switch (this.step) {
        case 1:
          return "Log In";
        case 2:
          return "";
        default:
          return "Account created";
      }
    },
  },
    methods: {
      login() {
        firebase
          .auth()
          .signInWithEmailAndPassword(this.email, this.password)
          .then(() => {
            this.step++
          })
          .catch((err) => {
            this.error = err.message;
          });
      },
    },
};
</script>

<style>
</style>