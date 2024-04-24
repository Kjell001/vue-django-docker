<template>
  <main class="p-10 flex flex-col gap-4 max-w-96">
    <p class="text-gray-500 italic">API endpoint: {{ endpoint }}</p>
    <div>
      <h1 class="text-2xl font-medium mb-2">Games</h1>
      <ul class="flex flex-col gap-4">
        <li
          v-for="game in games"
          :key="game.id"
          class="border border-black rounded-xl p-4 hover:border-dashed"
        >
          <p class="font-medium">{{ game.title }} ({{ game.year }})</p>
          <p class="text-sm">Available on {{ game.platform.name }}</p>
        </li>
      </ul>
    </div>
  </main>
</template>

<script setup>
import { ref } from "vue"

const endpoint = import.meta.env.VITE_API_URL
const games = ref([])

fetch(`${endpoint}/games/`)
  .then((response) => {
    if (response.status === 200) {
      return response.json()
    } else {
      throw new Error("Failed to fetch games")
    }
  })
  .then((data) => (games.value = data))
  .catch((error) => console.error(error))
</script>
