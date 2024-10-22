<template>
  <div class="qa-container">
    <!-- 标题部分 -->
    <h1 class="title">有什么可以帮忙的?</h1>

    <!-- 聊天记录展示 -->
    <div class="chat-history">
      <div v-for="(message, index) in chatHistory" :key="index" :class="['chat-message', message.role]">
        <div class="message-content">{{ message.content }}</div>
      </div>
    </div>

    <!-- 输入框和发送按钮部分 -->
    <div class="input-section">
      <div class="input-wrapper">
        <!-- 上传附件按钮 -->
        <label class="upload-button">
          <input type="file" @change="handleFileUpload" hidden multiple />
          <i class="icon">&#128206;</i> <!-- 附件图标 -->
        </label>

        <!-- 输入框 -->
        <input
          type="text"
          v-model="inputValue"
          placeholder="给 'ChatGPT' 发送消息"
          class="styled-input"
          @paste="handlePaste"
        />

        <!-- 发送按钮 -->
        <button @click="sendMessageToQwen" class="send-button">
          <i class="arrow-icon">&#9650;</i> <!-- 向上箭头图标 -->
        </button>
      </div>

      <!-- 上传的文件信息展示 -->
      <div v-if="uploadedFiles.length" class="file-display">
        <div v-for="(file, index) in uploadedFiles" :key="index" class="file-item">
          <div class="file-icon"> <!-- 图标样式 -->
            <img :src="getFileIcon(file)" alt="File Icon" />
          </div>
          <div class="file-info">
            <p class="file-name">{{ file.name }}</p>
            <p class="file-size">{{ formatFileSize(file.size) }}</p>
          </div>
          <div @click="removeFile(index)" class="remove-file">✖</div> <!-- 移除文件按钮 -->
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      inputValue: '', // 保存输入框的内容
      chatHistory: [], // 用于保存聊天记录
      uploadedFiles: [], // 保存上传的文件信息
      isSending: false, // 用于标识消息是否正在发送
    };
  },
  methods: {
    // 发送消息到后端并处理响应
    async sendMessageToQwen() {
      // 确保输入框不为空
      if (this.inputValue.trim() === '') return;

      // 禁用输入框，避免重复提交
      this.isSending = true;

      // 将用户消息添加到聊天记录
      this.chatHistory.push({ role: 'user', content: this.inputValue });

      try {
        console.log('Sending message to backend:', this.inputValue);
        // 发送请求到后端
        const response = await fetch('/api/chat/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ message: this.inputValue }),
        });

        if (response.ok) {
          const data = await response.json();
          console.log('Received response from backend:', data);

          // 确保后端返回了有效的回复
          if (data.reply) {
            // 添加 Qwen 的回复到聊天记录
            this.chatHistory.push({ role: 'qwen', content: data.reply });
          } else {
            console.error('No reply received from backend');
            this.chatHistory.push({ role: 'error', content: 'No reply received from Qwen.' });
          }
        } else {
          console.error('Failed to get response from server:', response.status);
          this.chatHistory.push({ role: 'error', content: 'Error: Server did not respond successfully.' });
        }
      } catch (error) {
        console.error('Error while communicating with backend:', error);
        this.chatHistory.push({ role: 'error', content: 'Error: Failed to communicate with the backend.' });
      }

      // 清空输入框
      this.inputValue = '';
      this.isSending = false; // 恢复输入框可用状态
    },

    // 处理文件上传
    handleFileUpload(event) {
      const files = Array.from(event.target.files);
      this.uploadedFiles.push(...files); // 添加上传的文件到数组中
      console.log('Uploaded files:', this.uploadedFiles);
    },

    // 处理粘贴图片
    handlePaste(event) {
      const items = event.clipboardData.items;
      for (let i = 0; i < items.length; i++) {
        const item = items[i];
        if (item.kind === 'file') {
          const file = item.getAsFile();
          this.uploadedFiles.push(file); // 添加粘贴的文件到数组中
          console.log('Pasted file:', file);
        }
      }
    },

    // 移除文件
    removeFile(index) {
      this.uploadedFiles.splice(index, 1);
      console.log('File removed. Updated file list:', this.uploadedFiles);
    },

    // 根据文件类型返回对应的图标
    getFileIcon(file) {
      if (file.type.startsWith('image/')) {
        return URL.createObjectURL(file);
      }
      return '/path/to/default-file-icon.png'; // 默认文件图标路径
    },

    // 格式化文件大小
    formatFileSize(size) {
      const kb = size / 1024;
      if (kb < 1024) return `${kb.toFixed(1)} KB`;
      return `${(kb / 1024).toFixed(1)} MB`;
    },
  },
};
</script>


<style scoped>
/* 主容器 */
.qa-container {
  max-width: 1000px;
  margin: 40px auto;
  padding: 20px;
  text-align: center;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

/* 标题 */
.title {
  font-size: 32px;
  color: #333;
  margin-bottom: 20px;
  font-weight: 700;
}

/* 聊天记录 */
.chat-history {
  max-width: 80%;
  margin: 20px auto;
  padding: 10px;
  background-color: #f9f9f9;
  border-radius: 10px;
  height: 300px;
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

/* 输入区域外部包裹 */
.input-section {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-bottom: 30px;
}

.input-wrapper {
  position: relative;
  width: 80%;
  display: flex;
  align-items: center;
  border: 1px solid #ddd;
  border-radius: 10px;
  padding-right: 5px;
  background-color: #f9f9f9;
  transition: box-shadow 0.3s ease;
}

.input-wrapper:hover {
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
}

/* 输入框 */
.styled-input {
  flex: 1;
  padding: 12px 15px;
  font-size: 16px;
  border: none;
  border-radius: 10px 0 0 10px;
  outline: none;
  background-color: transparent;
}

/* 上传按钮 */
.upload-button {
  cursor: pointer;
  margin-right: 10px;
  color: #555;
}

.upload-button .icon {
  font-size: 20px;
  color: #555;
}

/* 发送按钮 */
.send-button {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  border: none;
  background-color: #e0e0e0;
  cursor: pointer;
  transition: background-color 0.3s ease, box-shadow 0.3s ease;
}

.send-button:hover {
  background-color: #ccc;
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.2);
}

/* 向上箭头图标 */
.arrow-icon {
  font-size: 14px;
  color: #555;
}

/* 文件展示区域 */
.file-display {
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-start;
  margin-top: 15px;
  width: 80%;
}

/* 文件块样式 */
.file-item {
  display: flex;
  align-items: center;
  width: 150px;
  height: 50px;
  background-color: #f1f1f1;
  border-radius: 8px;
  margin-right: 10px;
  margin-bottom: 10px;
  padding: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: box-shadow 0.3s ease;
}

.file-item:hover {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

/* 文件图标 */
.file-icon {
  width: 32px;
  height: 32px;
  margin-right: 10px;
}

.file-icon img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* 文件信息 */
.file-info {
  flex: 1;
}

.file-name {
  font-size: 14px;
  color: #333;
}

.file-size {
  font-size: 12px;
  color: #999;
}

/* 移除文件按钮 */
.remove-file {
  cursor: pointer;
  color: #e74c3c;
  font-size: 18px;
  margin-left: 10px;
}
</style>
