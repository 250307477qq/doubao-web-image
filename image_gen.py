import requests
import json

# ========== 你的豆包 API 配置 ==========
API_KEY = "B676F5EA-75AD-4EC6-8F80-79E4F30CD9ef"
API_URL = "https://ark.cn-beijing.volces.com/api/v3/text-to-image"

# 文生图请求头
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def generate_image(prompt: str):
    """调用豆包 API 生成图片"""
    
    payload = {
        "model": "doubao-image",
        "prompt": prompt,
        "size": "1024x1024",
        "num_images": 1
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        result = response.json()

        if "data" in result and len(result["data"]) > 0:
            image_url = result["data"][0]["url"]
            print("✅ 图片生成成功！")
            print("🖼️ 图片地址：", image_url)
            return image_url
        else:
            print("❌ 生成失败：", result)
            return None
            
    except Exception as e:
        print("❌ 请求出错：", str(e))
        return None

if __name__ == "__main__":
    print("=== 豆包 AI 图片生成工具 ===")
    prompt = input("请输入图片描述：")
    generate_image(prompt)