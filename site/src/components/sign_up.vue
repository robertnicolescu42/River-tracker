<template>
  <v-card class="mx-auto" max-width="500">
    <v-card-title class="text-h6 font-weight-regular justify-space-between">
      <span>{{ currentTitle }}</span>
      <v-avatar
        color = "white"
        class="subheading black--text"
        size="24"
        v-text="step"
      ></v-avatar>
    </v-card-title>

    <v-window v-model="step">
      <v-window-item :value="1">
        <v-card-text>
          <v-text-field v-model="email" label="Email"></v-text-field>
          <span class="text-caption grey--text text--darken-1">
            This is the email you will use to login to your Vuetify account
          </span>
        </v-card-text>
      </v-window-item>

      <v-window-item :value="2">
        <v-card-text>
          <v-text-field v-model="password" label="Password" type="password"></v-text-field>
          <v-text-field label="Confirm Password" type="password"></v-text-field>
          <span class="text-caption grey--text text--darken-1">
            Please enter a password for your account
          </span>
        </v-card-text>
      </v-window-item>

      <v-window-item :value="3">
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
          <span class="text-caption grey--text">Thanks for signing up!</span>
        </div>
      </v-window-item>
    </v-window>

    <v-divider></v-divider>

    <v-card-actions>
      <v-btn :disabled="step === 1" text @click="step--"> Back </v-btn>
      <v-spacer></v-spacer>
      <v-btn :disabled="step === 3" depressed @click="step++"> Next </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import firebase from "firebase";
export default {
  data: () => ({
    step: 1,
    password: "",
    email: "",
    error: "",
    name:""
  }),
  watch:{
    step: function (val) {
      if (val == 3) {
        firebase
          .auth()
          .createUserWithEmailAndPassword(this.email, this.password)
          .then((data) => {
            data.user
              .updateProfile({
                displayName: "admin",
              })
              .then(() => {});
          })
          .catch((err) => {
            this.error = err.message;
          });
      }}
  },
  computed: {
    currentTitle() {
      switch (this.step) {
        case 1:
          return "Sign Up";
        case 2:
          return "Create a password";
        default:
          return "Account created";
      }
    },
  },
};
</script>

<style>
</style>