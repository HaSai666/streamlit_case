# -*- coding: utf-8 -*-
# @Time : 2024/1/8 21:59
# @Author : Wang Kai
# @contact: 306178200@qq.com
# @File : streamlit_app.py
# @Software: PyCharm
import streamlit as st

name = st.text_input('请输入你的名字')
age = st.slider('请选择你的年龄', 0, 100, 25)

st.write(f'你好，{name}！你的年龄是{age}岁。')