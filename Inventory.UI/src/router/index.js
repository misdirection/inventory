import { createRouter, createWebHistory } from 'vue-router'
import CategoryView from '../views/CategoryView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'category',
      component: CategoryView,
    }

  ],
})

export default router
