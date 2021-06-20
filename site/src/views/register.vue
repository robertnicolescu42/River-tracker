<template>
  <div>
  <v-container>
  <v-form v-model="valid">
    <v-container>
      <v-row>
        <v-col
          cols="12"
          md="4"
        >
          <v-text-field
            v-model="firstname"
            :rules="nameRules"
            label="First name"
            required
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          md="4"
        >
          <v-text-field
            type="password"
            v-model="lastname"
            :rules="passwordrules"
            label="Password"
            required
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          md="4"
        >
          <v-text-field
            v-model="email"
            :rules="emailRules"
            label="E-mail"
            required
          ></v-text-field>
        </v-col>
        <v-col>
          <v-btn
      :disabled="!valid"
      color="success"
      class="mr-4"
      @click="submit"
    >
      Submit
    </v-btn>
        </v-col>
      </v-row>
    </v-container>
  </v-form>

  
  </v-container>
  </div>
</template>


<script>
import firebase from "firebase";

export default {
  data() {
    return {
      
      name: "",
      error: null,
      valid: false,
      firstname: '',
      lastname: '',
      passwordrules:[
        v => (v && v.length >= 6) || "Min 6 characters"
      ],
      nameRules: [
        v => !!v || 'Name is required',
      ],
      email: '',
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+/.test(v) || 'E-mail must be valid',
      ],
    };
  },
  methods: {
    submit() {
      firebase
        .auth()
        .createUserWithEmailAndPassword(this.email, this.lastname)
        .then(data => {
          data.user
            .updateProfile({
              displayName: this.name
            })
            .then(() => {});
        })
        .catch(err => {
          this.error = err.message;
        });
    }
  }
};
</script>