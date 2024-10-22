<template>
  <div class="homePage">
    <AppHeader />
    <ChatHistory :chatHistory="chatHistory" />
    <InputSection @sendMessage="handleSendMessage" />
  </div>
</template>

<script>
import AppHeader from '../components/AppHeader.vue';
import ChatHistory from '../components/ChatHistory.vue';
import InputSection from '../components/InputSection.vue';

export default {
  name: 'HomePage',
  components: {
    AppHeader,
    ChatHistory,
    InputSection
  },
  data() {
    return {
      chatHistory: [] // 用于存储聊天记录
    };
  },
  methods: {
    // 处理发送消息的逻辑
    async handleSendMessage(message) {
      // 将用户的消息添加到聊天记录
      this.chatHistory.push({ role: 'user', content: message });

      try {
        // 模拟发送消息到后端获取千问的回复
        const response = await fetch('/api/chat/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ message })
        });

        const data = await response.json();
        if (data.reply) {
          // 将千问的回复添加到聊天记录
          this.chatHistory.push({ role: 'qwen', content: data.reply });
        } else {
          this.chatHistory.push({ role: 'error', content: 'No reply from Qwen.' });
        }
      } catch (error) {
        this.chatHistory.push({ role: 'error', content: 'Error connecting to Qwen.' });
      }
    }
  }
};
</script>

<style>
.homePage {
  width: 70%;
  margin: 0 auto;
  border: 1px solid #000;
  padding: 20px;
}
</style>