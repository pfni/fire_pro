import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def chat_with_qwen(request):
    if request.method == 'POST':
        # 获取前端发送的用户消息
        data = json.loads(request.body)
        user_message = data.get('message')

        # 千问API的URL和Headers
        qwen_api_url = 'https://dashscope.aliyuncs.com/compatible-mode/v1'  # 替换成千问API的实际URL
        headers = {
            'Authorization': 'sk-CUPyz5jlFA',  # 替换成你的千问API密钥
            'Content-Type': 'application/json',
        }

        # 向千问发送请求
        payload = {'message': user_message}
        try:
            response = requests.post(qwen_api_url, headers=headers, json=payload)
            response_data = response.json()

            # 获取千问的回复
            qwen_reply = response_data.get('reply', '千问没有回复')

            # 返回千问的回复给前端
            return JsonResponse({'reply': qwen_reply})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
