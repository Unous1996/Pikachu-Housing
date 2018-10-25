import house from '../../api/house'

const state = {
  list: [],
  detail: {},
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
  },
  createHouseObj ({ commit }, data) {
    house.createHouse(data, houses => {
      commit('setHouseList', houses)
    })
  },

  editHouseObj ({ commit }, payload) {
    house.editHouse(payload.data, payload.id, houses => {
      commit('setHouseDetail', houses)
    })
  },

  getHouseDetailObj({ commit }, id) {
    house.getHouseDetail(id, house => {
      commit('setHouseDetail', house)
    })
  },

}


const mutations = {
  setHouseList(state, houses) {
    state.list = houses
  },
  setHouseDetail(state, house) {
    state.detail = house
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
