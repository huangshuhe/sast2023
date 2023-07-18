import streamlit as st
import json

st.title("Word Filling Game")
file =st.file_uploader('Choose a file:')
showtext=0
textinputnum=0
if file is not None:
    try:
        # with open(file,'r',encoding='utf-8') as f:
            st.success("Available file")
            data=json.load(file)
            articles=data["articles"]
            keys=[]
            hints=articles[0]["hints"]
            for hint in hints:
                ans=st.text_input(f"请输入{hint}：")
                keys.append(ans)
                if not ans=="":
                    textinputnum=textinputnum+1
            if textinputnum==len(keys):
                showtext=1
            text=articles[0]["article"]
            for i in range(len(keys)):
                text=text.replace(f"{{{{{i+1}}}}}", keys[i])
            if showtext==1:
                st.divider()
                st.title(articles[0]["title"])
                st.write(text)
    except FileNotFoundError:
        st.error("The file does not exist")
