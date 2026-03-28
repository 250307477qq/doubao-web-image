import requests

# ========== 豆包 API 配置（替换成你的真实 API_KEY） ==========
API_KEY = "B676F5EA-75AD-4EC6-8F80-79E4F30CD9ef"

def generate_image(prompt: str):
    # 正确的文生图接口地址
    url = "https://ark.cn-beijing.volces.com/api/v3/images/generations"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        # 必须和你开通的模型一致
        "model": "doubao-vision-image",
        "prompt": prompt,
        "size": "1024x1024",
        "n": 1  # 生成1张
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()

        if "data" in result and len(result["data"]) > 0:
            image_url = result["data"][0]["url"]
            print("✅ 图片生成成功！")
            print("🖼️ 图片地址：", image_url)
            return image_url
        else:
            print("❌ 接口返回异常：", result)

    except Exception as e:
        print("❌ 请求出错：", e)
        if 'response' in locals():
            print("响应内容：", response.text)

if __name__ == "__main__":
    print("=== 豆包 AI 图片生成工具 ===")
    prompt = input("请输入图片描述：")
    generate_image(prompt)