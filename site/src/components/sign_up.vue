<template>
  <v-card class="mx-auto" max-width="500" elevation="0">

    <v-card-title class="text-h6 font-weight-regular justify-space-between">
      <span>{{ currentTitle }}</span>
      <v-avatar
        color="white"
        class="subheading black--text"
        size="24"
        v-text="step"
      ></v-avatar>
    </v-card-title>

    <v-window v-model="step">
      <v-window-item :value="1">
        <v-card-text>
          <v-form v-model="valid">
            <v-text-field
              v-model="email"
              :rules="emailRules"
              label="Email"
            ></v-text-field>
          </v-form>
          <span class="text-caption grey--text text--darken-1">
            This is the email that will be used to login to the Rivertracker
            account
          </span>
        </v-card-text>
      </v-window-item>

      <v-window-item :value="2">
        <v-card-text>
          <v-form v-model="valid">
            <v-text-field
              v-model="password"
              :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
              :type="show1 ? 'text' : 'password'"
              name="input-10-1"
              hint="At least 8 characters"
              @click:append="show1 = !show1"
            ></v-text-field>
          </v-form>
          <span class="text-caption grey--text text--darken-1" v-if="show == false">
            Please enter a password for the account
          </span>
          <span class="text-caption red--text text--darken-1" v-if="show == true">
            <br>
            {{ error }} Please refresh the page to try again
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
          <span class="text-caption grey--text"
            >The account is now registered!</span
          >
        </div>
      </v-window-item>
    </v-window>


    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn :disabled="step === 3" depressed @click="next()"> Next </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import firebase from "firebase";
export default {
  data: () => ({
    step: 1,
    password: "",
    passwordcheck: "",
    email: "",
    error: "",
    name: "",
    show1: false,
    show: false,
    emailRules: [
      (v) => !!v || "E-mail is required",
      (v) =>
        /^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/.test(
          v
        ) || "E-mail must be valid",
    ],
    valid: false,
  }),
  methods: {
    login() {
      firebase
        .auth()
        .createUserWithEmailAndPassword(this.email, this.password)
        .then((data) => {
          data.user
            .updateProfile({
              displayName: "admin",
            })
            .then(() => {
              this.show = false
            });
        })
        .catch((err) => {
          this.show = true
          this.error = err.message;
        });
    },
    next() {
      if (this.valid == true) {
        this.error = "";
        if (this.step == 2) {
          this.login()
            if (this.error == "") {
              this.step++;
          }
        } else {
          this.valid = false;
          this.step++;
        }
      }
    },
  },

  computed: {
    currentTitle() {
      switch (this.step) {
        case 1:
          return "Register a user";
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