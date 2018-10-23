const _dummyHouse = [ {
        id: 1,
        flex: 12,
        name: 'The dog example',
        src: 'https://www.codeproject.com/KB/GDI-plus/ImageProcessing2/img.jpg',
        description: 'I\'m a thing. But, like most politicians, he promised more than he could deliver. You won\'t have time for sleeping, soldier, not with all the bed making you\'ll be doing.'
      },
      {
        id: 2,
        flex: 12,
        name: 'Listen some music!',
        src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
        description: 'I\'m a thing. But, like most politicians, he promised more than he could deliver. You won\'t have time for sleeping, soldier, not with all the bed making you\'ll be doing.'
      },
      {
        id: 3,
        flex: 12,
        name: 'Rock & Roll!',
        src: 'https://cdn.vuetifyjs.com/images/cards/foster.jpg',
        description: 'I\'m a thing. But, like most politicians, he promised more than he could deliver. You won\'t have time for sleeping, soldier, not with all the bed making you\'ll be doing.'
      }
      ]

import axios from 'axios';

export default {
  getHouseList (cb) {
    const url = "/api/house/"
    axios.get(url).then(response => {
      setTimeout(() => cb(response.data) , 100)
    })
  },
  deleteHouse (id, cb) {
    const url = `/api/house/${id}`
    axios.delete(url).then(response => {
      setTimeout(() => cb(response.data) , 100)
    })
  }
}
