# import streamlit as st
# import turtle
# import numpy as np
# import matplotlib.pyplot as plt


# fig, ax = plt.subplots()

# a = 2
# b = -5
# c = 3
# d = -7

# x = []
# y = []
# for i in range(-100,101):
#     x.append(i)
#     y.append(a*i**3 + b*i**2 + c*i + d)



# color = st.radio('색을 선택하시오.',('red', 'green', 'blue'))
# plt.plot(x, y, color = color)
# st.pyplot(fig)

# x = [-10, -9, -8, -7, -6]

# cc = st.radio('선의 색을 선택하시오',['red', 'green', ])

# st.image('rabbit.jpg')

import streamlit as st
import os
os.system('cls')

col1, col2 = st.columns(2)
with col1:
    st.image('rabbit.jpeg',)
with col2:
    st.write('잡으면 후회할 인재 (성승현❤️ 시급 4백원 )')
    '전화번호(📞) : 01084489323'
    '이메일(📜) : jyy9323@naver.com'
    '주소(🏡) 전라북도 익산시 궁동로 151-9 하나리움 아파트 102동 1106호'

st.link_button("naver(👎)", "https://n.news.naver.com/article/055/0001109642" )
st.image('rabbit.jpeg')

import sys
sys.exit()

import streamlit as st