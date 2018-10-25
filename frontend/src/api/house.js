import provider from '../utils/provider'

export default {
  getHouseList (cb) {
    const url = "/api/house/"
    provider.get(url).then(response => {
      setTimeout(() => cb(response.data) , 100)
    })
  },

  deleteHouse (id, cb) {
    const url = `/api/house/${id}/`
    provider.delete(url).then(response => this.getHouseList(cb))
  },

  createHouse (data, cb) {
    const url = "/api/house/"
    provider.post(url, data).then(response => this.getHouseList(cb))
  },

  editHouse (data, id, cb) {
    const url = `/api/house/${id}/`
    provider.patch(url, data).then(response => this.getHouseDetail(id, cb))
  },

  getHouseDetail (id, cb) {
    const url = `/api/house/${id}/`
    provider.get(url).then(response => {
      setTimeout(() => cb(response.data) , 100)
    })
  },
}
