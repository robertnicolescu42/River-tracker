import firebase from 'firebase';
import 'firebase/firestore';
import {firestorePlugin} from 'vuefire';
import Vue from 'vue';
Vue.use(firestorePlugin);

// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
    apiKey: "AIzaSyBy8L07RxjRsPKyTq7AC0geJUpAh6T8T4I",
    authDomain: "river-tracker-295612.firebaseapp.com",
    databaseURL: "https://river-tracker-295612.firebaseio.com",
    projectId: "river-tracker-295612",
    storageBucket: "river-tracker-295612.appspot.com",
    messagingSenderId: "344075096194",
    appId: "1:344075096194:web:4d6c5793da25221faba49b",
    measurementId: "G-P7THV24Y7M"
  };

  export const db = firebase.initializeApp(firebaseConfig).firestore();
