<template>
  <div class="header">
    <img src="@/assets/logo.png" alt="logo" class="logo"/>
    <div class="page-title">新建聊天</div>
  </div>
</template>

<script>
export default {
  name: 'AppHeader',
};
</script>

<style scoped>
/* Flexbox 布局自适应 */
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border: 2px solid orange;
  padding: 10px;
  width: 100%;
  height: auto;
  box-sizing: border-box;
}

.logo {
  width: 50px; /* 设置一个固定的宽度或百分比，根据需要调整 */
  height: 50px;
  max-width: 100px; /* 最大宽度控制 */
  object-fit: contain; /* 保证图片保持比例，不会变形 */
}

.page-title {
  color: blue;
  font-size: 18px;
  max-font-size: 16px;
  text-align: right;
}

/* 媒体查询：在不同屏幕尺寸下调整 */
@media (max-width: 768px) {
  .header {
    flex-direction: column;
    align-items: flex-start;
  }

  .page-title {
    font-size: 5vw;
    text-align: left;
  }

  .logo {
    width: 40px;
    height: 40px;
  }
}

@media (max-width: 480px) {
  .page-title {
    font-size: 6vw;
  }

  .logo {
    width: 30vw;
    height: auto; /* 保持纵横比 */
  }
}
</style>
