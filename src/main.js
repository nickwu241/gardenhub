import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'
import BootstrapVue from 'bootstrap-vue'
import VueGoodTablePlugin from 'vue-good-table'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'vue-good-table/dist/vue-good-table.css'

import Home from "./components/Home.vue";
import FindGardens from "./components/FindGardens.vue";

Vue.use(VueRouter)
Vue.use(BootstrapVue)
Vue.use(VueGoodTablePlugin);

const routes = [{
    path: '/',
    component: Home
  },
  {
    path: '/find',
    component: FindGardens
  }
]

const router = new VueRouter({
  routes // short for `routes: routes`
})

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')