import axios, { AxiosInstance } from 'axios';
import { boot } from 'quasar/wrappers';

declare module 'vue/types/vue' {
  interface Vue {
    $axios: AxiosInstance;
  }
}

export default boot(({ Vue }) => {
  /* eslint-disable-next-line @typescript-eslint/no-unsafe-member-access */
  const api = axios.create({
    baseURL: 'http://us.artifacts.global-perspective.appspot.com',
  });
  /* eslint-disable-next-line @typescript-eslint/no-unsafe-member-access */
  Vue.prototype.$axios = api;
});
