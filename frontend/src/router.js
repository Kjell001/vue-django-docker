import { createRouter, createWebHistory } from "vue-router"
import GamesView from "@/views/GamesView.vue"
import ChatView from "@/views/ChatView.vue"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/games",
      name: "games",
      component: GamesView,
    },
    {
      path: "/chat",
      name: "chat",
      component: ChatView,
    },
  ],
})

export default router
