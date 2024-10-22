const { defineConfig } = require('@vue/cli-service')
module.exports = {
  devServer: {
    proxy: {
      '/app_fire': {
        target: 'http://localhost:8000', // Django 后端地址
        changeOrigin: true,
      },
    },
  },
};
