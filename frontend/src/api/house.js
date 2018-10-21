const _dummyHouse = [ {
        id: 1,
        flex: 12,
        title: 'The dog example',
        src: 'https://www.codeproject.com/KB/GDI-plus/ImageProcessing2/img.jpg',
        content: 'I\'m a thing. But, like most politicians, he promised more than he could deliver. You won\'t have time for sleeping, soldier, not with all the bed making you\'ll be doing.'
      },
      {
        id: 2,
        flex: 12,
        title: 'Listen some music!',
        src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
        content: 'I\'m a thing. But, like most politicians, he promised more than he could deliver. You won\'t have time for sleeping, soldier, not with all the bed making you\'ll be doing.'
      },
      {
        id: 3,
        flex: 12,
        title: 'Rock & Roll!',
        src: 'https://cdn.vuetifyjs.com/images/cards/foster.jpg',
        content: 'I\'m a thing. But, like most politicians, he promised more than he could deliver. You won\'t have time for sleeping, soldier, not with all the bed making you\'ll be doing.'
      }
      ]

export default {
  getHouseList (cb) {
    setTimeout(() => cb(_dummyHouse), 100)
  }
}
