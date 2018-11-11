import provider from '../utils/provider'

export default {
  getUser (cb) {
    let url = '/api/user/profile'
    provider.get(url).then(response => {
      setTimeout(() => cb(response.data) , 100)
    })
  },
  logout (cb) {
    let url = '/api/user/logout'
    provider.get(url).then(response => {
      setTimeout(() => cb(response.data) , 100)
    })
  }
}
