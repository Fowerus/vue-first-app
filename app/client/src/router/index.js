import { createRouter, createWebHistory } from 'vue-router'
import mainBLock from '../views/mainBlock.vue'

const routes = [
  {
    path: '/',
    name: 'mainBLock',
    component: mainBLock
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router