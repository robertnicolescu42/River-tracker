import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    device: 1
  },
  mutations: {
    setCurrentDevice(state, payload){
      state.device = payload;
    }
  },
  actions: {
    async setCurrentDevice(state, payload){
      state.commit("setCurrentDevice", payload)
    }
  },
  modules: {
  },
  getters:{
    getCurrentDevice: state => state.device
  }
})
