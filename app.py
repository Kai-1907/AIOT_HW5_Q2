import streamlit as st
import requests
import json

# 設定頁面資訊
st.set_page_config(page_title="n8n AI 自動化 Demo", page_icon="🤖")

st.title("🤖 仿小林 AI：n8n 自動化流程展示")
st.markdown("""
本 Demo 模擬小林 AI 的自動化邏輯，透過 **n8n** 處理後端流程：
1. 接收 Streamlit 傳送的文字
2. n8n 調用 AI 進行摘要與翻譯
3. 回傳結果至此介面
""")

# 使用者輸入區
input_text = st.text_area("請輸入想要摘要的長文章內容：", height=200)

# n8n Webhook URL (請替換成你部署的 n8n URL)
N8N_WEBHOOK_URL = "https://your-n8n-instance.com/webhook/ai-demo"

if st.button("開始自動化流程"):
    if input_text:
        with st.spinner("n8n 流程執行中..."):
            try:
                # 發送請求到 n8n
                payload = {"content": input_text}
                response = requests.post(N8N_WEBHOOK_URL, json=payload)
                
                if response.status_code == 200:
                    result = response.json()
                    st.success("✅ 流程執行成功！")
                    st.subheader("AI 處理結果：")
                    st.write(result.get("data", "無回傳內容"))
                else:
                    st.error(f"錯誤：n8n 回傳狀態碼 {response.status_code}")
            except Exception as e:
                st.error(f"連線失敗：{str(e)}")
    else:
        st.warning("請先輸入內容。")

st.info("💡 原始參考：[小林 AI Workflow](https://github.com/soluckysummer/n8n_workflows)")