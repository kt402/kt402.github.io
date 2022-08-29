import { createApp } from 'vue';
import App from './App.vue';
import store from './store';
import router from './router';
// import { firestorePlugin } from 'vuefire'


import '@/app.scss';

const app = createApp(App);
app.use(store);
app.use(router);
// app.use(firestorePlugin);
app.mount('#app');


