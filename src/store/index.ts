import { createStore } from 'vuex'

export interface State {
  something: boolean,
}

export default createStore<State>({
  state: {
    something: true,
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
  }
});
