import Vue from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify';
import VueFriendlyIframe from 'vue-friendly-iframe';

Vue.config.productionTip = false

Vue.use(VueFriendlyIframe)
Vue.component("lastDay", require("./components/last_day.vue").default);
Vue.component("lastWeek", require("./components/last_week.vue").default);
Vue.component("lastMonth", require("./components/last_month.vue").default);
Vue.component("last3Months", require("./components/last_3months.vue").default);
new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
