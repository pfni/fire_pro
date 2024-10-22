<template>
  <div class="input-section">
    <input type="text" v-model="inputValue" placeholder="请输入你的问题" />
    <button @click="sendMessage" :disabled="isSending">发送</button>
<!--    <input type="text" v-model="inputText" placeholder="请输入文字" />-->
<!--    <button @click="sendMessage">发送</button>-->
  </div>
</template>

<script>
export default {
  name: 'InputSection',
  data() {
    return {
      inputValue: '',  // 初始化为空字符串
      chatHistory: [],
      isSending: false
    };
  },
  methods: {
    async sendMessage() {
      if (!this.inputValue || this.inputValue.trim() === '') return;  // 防止 undefined 和空字符串的情况

      this.isSending = true;

      this.chatHistory.push({ role: 'user', content: this.inputValue });

      try {
        const response = await fetch('/api/chat/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ message: this.inputValue }),
        });

        if (response.ok) {
          const data = await response.json();
          if (data.reply) {
            this.chatHistory.push({ role: 'qwen', content: data.reply });
          } else {
            this.chatHistory.push({ role: 'error', content: '千问没有回复' });
          }
        } else {
          this.chatHistory.push({ role: 'error', content: '服务器错误' });
        }
      } catch (error) {
        this.chatHistory.push({ role: 'error', content: '通信错误' });
      }

      this.inputValue = ''; // 重置输入框
      this.isSending = false;
    }
  }
};
</script>

<style>
.input-section {
  display: flex;
  align-items: center;
  justify-content: space-between;
  border: 2px solid blue;
  padding: 10px;
}

input[type="text"] {
  flex: 1;
  margin-right: 10px;
  padding: 5px;
  border: 1px solid #ccc;
}

button {
  padding: 5px 10px;
  background-color: blue;
  color: white;
  border: none;
  cursor: pointer;
}
</style>