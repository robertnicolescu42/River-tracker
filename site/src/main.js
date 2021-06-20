import Vue from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify';
import VueFriendlyIframe from 'vue-friendly-iframe';
import { LMap, LTileLayer, LMarker } from 'vue2-leaflet';
import 'leaflet/dist/leaflet.css';
// import * as firebase from "firebase";

// const firebaseConfig = {
//   apiKey: "AIzaSyBy8L07RxjRsPKyTq7AC0geJUpAh6T8T4I",
//   authDomain: "river-tracker-295612.firebaseapp.com",
//   databaseURL: "https://river-tracker-295612.firebaseio.com",
//   projectId: "river-tracker-295612",
//   storageBucket: "river-tracker-295612.appspot.com",
//   messagingSenderId: "344075096194",
//   appId: "1:344075096194:web:4d6c5793da25221faba49b",
//   measurementId: "G-P7THV24Y7M"
// };
// firebase.initializeApp(firebaseConfig);
Vue.config.productionTip = false

Vue.use(VueFriendlyIframe)
Vue.component("lastDay", require("./components/last_day.vue").default);
Vue.component("lastWeek", require("./components/last_week.vue").default);
Vue.component("lastMonth", require("./components/last_month.vue").default);
Vue.component("last3Months", require("./components/last_3months.vue").default);
Vue.component("edit_setup_map", require("./components/edit_setup_map.vue").default);
Vue.component('l-map', LMap);
Vue.component('l-tile-layer', LTileLayer);
Vue.component('l-marker', LMarker);
new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
