from openai import OpenAI

# 创建客户端
client = OpenAI(
    base_url="http://localhost:1235/v1",
    api_key="lm-studio"
)

# 发送请求
response = client.chat.completions.create(
    model="qwen3.5-9b-q5_k_m",  # 确保 LM Studio 软件里加载的是这个模型
    messages = [
        {"role": "system", "content": "你是一个智能建造领域的专家"},
        {"role": "user", "content": "请用一句话解释一下BIM是什么?"}
    ],
    temperature=0.7
)

# 打印 AI 返回的内容
print(response.choices[0].message.content)