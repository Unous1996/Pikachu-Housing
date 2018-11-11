import user from '../../api/user'

const state = {
  detail: {
    username: "Anonymous"
  },
  next: "",
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
}

const mutations = {
  setUserDetail(state, user) {
    state.detail = user
  },
  resetUser(state, next) {
    state.detail = {username: "Anonymous"}
    state.next = next
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
