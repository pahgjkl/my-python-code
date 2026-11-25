from openai import OpenAI
from my_tools import read_pdf
client = OpenAI(
    base_url="http://localhost:1235/v1",
    api_key="lm-studio"
)
# pdf_path = r"D:\项目pdf\1.pdf"
print("---正在加载PDF知识库---")
# content = ""
# for page_text in read_pdf(pdf_path):
#     content += page_text + "\n"
# context = content[:2000]
with open(r"C:\Users\Lenovo\Desktop\1.txt", "r", encoding="utf-8") as f:
    context = f.read()
while True:
    user_input = input("问题:")
    if user_input.lower() in ["退出", "exit", "quit"]:
        print("拜拜")
        break
    if not user_input.strip():
        continue
    prompt = f"""

     你是一个王者荣耀的专家。请严格根据以下参考资料回答用户的问题。
        如果资料中没有答案，请说“根据提供的资料，无法回答该问题”。

        【参考资料】：
        {context}

        【用户问题】：
        {user_input}

    """
    print("机器正在思考...")
    response = client.chat.completions.create(
        model="qwen3.5-9b-q5_k_m",  # 确保 LM Studio 软件里加载的是这个模型
        messages = [
            {"role": "system", "content": "你是一个严谨的王者荣耀助手."},
            {"role": "user", "content": prompt}
        ],
            temperature=0.3
    )
    anseer = response.choices[0].message.content
    print(f"机器人:{anseer}\n")