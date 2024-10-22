<template>
  <div class="home-page">
    <header class="header">
      <img src="../assets/logo.png" alt="Logo" class="logo" />
      <h1>欢迎使用问答系统</h1>
    </header>
    <ImageContent />
  </div>
</template>

<script>
import ImageContent from '@/components/ImageContent.vue';

export default {
  name: 'HomePage',
  components: {
    ImageContent,
  },
};
</script>

<style scoped>
.home-page {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh; /* 使页面填满整个视口高度 */
  background-color: #f9f9f9; /* 设置背景颜色 */
  transition: all 0.5s ease; /* 添加平滑过渡 */
}

.header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  padding: 20px;
  background-color: white; /* 头部背景颜色 */
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); /* 添加阴影效果 */
}

.logo {
  max-width: 100px; /* 控制 logo 大小 */
}
</style>