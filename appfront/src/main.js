// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import VueResource from 'vue-resource'
import ElementUI from '../node_modules/element-ui'
import '../node_modules/element-ui/lib/theme-chalk/index.css'

Vue.config.productionTip = false

/* eslint-disable no-new */
Vue.use(ElementUI)
Vue.use(VueResource)
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
