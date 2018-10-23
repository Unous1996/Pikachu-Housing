import house from '../../api/house'

const state = {
  list: [],
}

const getters = {}

const actions = {
  getList ({ commit }) {
    house.getHouseList(houses => {
      commit('setHouseList', houses)
    })
  },
  deleteHouseObj ({ commit }, id) {
    house.deleteHouse(id, houses => {
      commit('setHouseList', houses)
    })
  }
}


const mutations = {
  setHouseList(state, houses) {
    state.list = houses
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
