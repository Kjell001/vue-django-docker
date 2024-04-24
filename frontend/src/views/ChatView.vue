<template>
  <main class="p-10 flex flex-col gap-4 max-w-96">
    <h1 class="text-2xl font-medium">Chat</h1>
    <ul class="flex flex-col gap-4">
      <li
        v-for="msg in messages"
        :key="msg.timestamp"
        class="border border-black rounded-xl px-4 py-2 hover:border-dashed"
      >
        <p class="font-bold text-sm text-blue-700">{{ msg.user }}</p>
        <p>
          {{ msg.content }}
          <span class="text-xs text-gray-500">{{
            format(new Date(msg.timestamp), "HH:mm")
          }}</span>
        </p>
      </li>
    </ul>
    <!-- Input element -->
    <input
      v-model="newMessage"
      type="text"
      class="border border-black rounded-xl px-4 py-2"
      placeholder="Type your message"
      @keyup.enter="sendMessage"
    />
  </main>
</template>

<script setup>
import { ref, onUnmounted } from "vue"
import { format } from "date-fns"

// WebSocket connection
const ws = new WebSocket(`${import.meta.env.VITE_WS_URL}/chat/`)
ws.onopen = () => console.log("Connected")
ws.onmessage = (event) => {
  console.log("Reveived:", event)
  messages.value.push(JSON.parse(event.data))
}

const username = `You#${Math.floor(Math.random() * 10000)
  .toString()
  .padStart(4, "0")}`
const messages = ref([])
const newMessage = ref()

function sendMessage() {
  const payload = JSON.stringify({
    user: username,
    content: newMessage.value,
  })
  ws.send(payload)
  console.log("Sent:", payload)
  newMessage.value = ""
}

onUnmounted(() => {
  ws.close()
})
</script>
