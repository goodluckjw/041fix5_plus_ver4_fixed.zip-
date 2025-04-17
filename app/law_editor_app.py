
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from utils.xml_parser import parse_law_xml

st.title("부칙 개정 도우미")
st.write("법령 본문 중 검색어를 포함하는 조문을 찾아줍니다.")

search_term = st.text_input("🔍 찾을 단어", key="search_term")
if st.button("법률 검색"):
    st.info(f"‘{search_term}’을(를) 포함하는 조문을 검색 중입니다...")
    for file in os.listdir("./data"):
        if file.endswith(".xml"):
            file_path = os.path.join("./data", file)
            results = parse_law_xml(file_path, search_term)
            st.write(f"📄 {file}")
            for r in results:
                st.markdown(r, unsafe_allow_html=True)
