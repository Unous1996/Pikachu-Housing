import user from '../../api/user'

const state = {
  detail: {
    username: "Anonymous"
  },
  next: "",
  status: false,
}

const getters = {}

const actions = {
  getUser({commit}) {
    user.getUser(user => {
      commit('setUserDetail', user)
    })
  },
  logout({commit}) {
    user.logout((data) => {
      commit('resetUser',data.next)
    })
  },
  login({ commit }, data) {
    user.login(data, user => {
      commit('setUserDetail', user)
    }, e => {state.status = false})
  }
}

const mutations = {
  setUserDetail(state, user) {
    state.detail = user
    state.status = true
  },
  resetUser(state, next) {
    state.detail = {username: "Anonymous"}
    state.next = next
  },
  setStatusFailure(state, user) {
    state.status = false
  },
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}