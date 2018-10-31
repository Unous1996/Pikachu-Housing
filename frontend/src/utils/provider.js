import axios from 'axios';
import { getCookie } from './cookie.js';

function getProvider () {
  const csrf = getCookie('csrftoken')
  return axios.create({
      withCredentials: true,
      headers: {
        'X-CSRFToken': csrf,
      },
    });
}
const provider = getProvider();

export default provider;
