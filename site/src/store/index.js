import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    device: 1,
    user: {
      loggedIn: false,
      data: null
    }
  },
  mutations: {
    setCurrentDevice(state, payload){
      state.device = payload;
    },
    SET_LOGGED_IN(state, value) {
      state.user.loggedIn = value;
    },
    SET_USER(state, data) {
      state.user.data = data;
    }
  },
  actions: {
    async setCurrentDevice(state, payload){
      state.commit("setCurrentDevice", payload)
    },
    fetchUser({ commit }, user) {
      commit("SET_LOGGED_IN", user !== null);
      if (user) {
        commit("SET_USER", {
          displayName: user.displayName,
          email: user.email
        });
      } else {
        commit("SET_USER", null);
      }
    }
  },
  modules: {
  },
  getters:{
    getCurrentDevice: state => state.device,
    user(state){
      return state.user
    }
  }
})
