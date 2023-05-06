from gpt4free import you
import streamlit as st
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), os.path.pardir))


def get_answer(question: str) -> str:
    # Set cloudflare clearance cookie and get answer from GPT-4 model
    try:
        result = you.Completion.create(prompt=question)

        return result.text

    except Exception as e:
        # Return error message if an exception occurs
        return (
            f'An error occurred: {e}. Please make sure you are using a valid cloudflare clearance token and user agent.'
        )


# Set page configuration and add header
st.set_page_config(
    page_title="免费GPT4",
    initial_sidebar_state="expanded",
    page_icon="🧠",
    menu_items={
        'Get Help': 'https://github.com/xtekky/gpt4free/blob/main/README.md',
        'Report a bug': "https://github.com/xtekky/gpt4free/issues",
        'About': "### gptfree GUI",
    },
)
st.header('免费GPT4')

# Add text area for user input and button to get answer
question_text_area = st.text_area(
    '🤖 问任何问题 :', placeholder='我想让你充当一个花哨的标题生成器。我会用输入系列关键字，用逗号分隔，请回复花哨的标题。我的关键词是：年轻人，不讲武德。')
if st.button('🧠 思考'):
    answer = get_answer(question_text_area)
    escaped = answer.encode('utf-8').decode('unicode-escape')
    # Display answer
    st.caption("回答 :")
    st.markdown(escaped)

# Hide Streamlit footer
hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
