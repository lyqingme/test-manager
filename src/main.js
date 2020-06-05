import Vue from 'vue'
import App from '@/App.vue'

import store from '@/store' 
import router from '@/router'

import './plugin/jquery-3.3.1.min.js'
import './plugin/bootstrap-3.3.7-dist/js/bootstrap.min.js'

Vue.config.productionTip = false

// Vue.use(VueRouter)

const vue = new Vue({
  router,
  store,
  render: h => h(App)
})

vue.$mount('#app')
