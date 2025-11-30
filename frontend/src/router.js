import { createRouter, createWebHistory } from "vue-router"
import PickerView from "@/views/PickerView.vue"
import GamesView from "@/views/GamesView.vue"
import ChatView from "@/views/ChatView.vue"

export default createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "picker",
      component: PickerView,
    },
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
