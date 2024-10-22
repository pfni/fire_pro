<template>
  <div class="qa-container">
    <!-- 标题部分 -->
<!--    <h1 class="title">有什么可以帮忙的?</h1>-->

    <!-- 聊天记录展示 -->
    <div class="chat-history">
      <div v-for="(message, index) in chatHistory" :key="index" :class="['chat-message', message.role]">
        <div class="message-content">{{ message.content }}</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ChatHistory',
  props: {
    chatHistory: {
      type: Array,
      required: true
    }
  }
};
</script>

<style scoped>
.chat-history {
  max-width: 100%;
  margin: 20px auto;
  padding: 10px;
  background-color: #f9f9f9;
  border-radius: 10px;
  height: 500px;
  overflow-y: scroll;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
}

.chat-message {
  margin-bottom: 15px;
}

.chat-message.user {
  text-align: right;
  color: #007bff;
}

.chat-message.qwen {
  text-align: left;
  color: #555;
}

.message-content {
  display: inline-block;
  padding: 8px 12px;
  border-radius: 10px;
  background-color: #e0e0e0;
  color: #333;
  font-size: 14px;
}
</style>
