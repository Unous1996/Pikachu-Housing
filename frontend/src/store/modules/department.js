import department from '../../api/department'

const state = {
  list: [],
  detail: {},
}

const getters = {
  getDepartNameById: (state) => (id) => {
    return state.department.list.find(d => d.id = id).name
  }
}

const actions = {
  getList ({ commit }, query) {
    department.getDepartmentList(departments => {
      commit('setDepartmentList', departments)
    }, query)
  },
}

const mutations = {
  setDepartmentList(state, departments) {
    state.list = departments
  },
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
