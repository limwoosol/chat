import streamlit as st

st.title("😀임우솔에 대해서")

# 탭 생성 : 첫번째 탭의 이름은 Tab A 로, Tab B로 표시합니다.
tab1, tab2 = st.tabs(['임우솔의 탄생', '2'])

with tab1:
    # tab A 를 누르면 표시될 내용
    st.write("")
    st.subheader('1. 임우솔의 탄생')
    st.markdown("나는 2006년 10월 3일에 임씨집안 둘째 임한솔씨의 동생으로 태어났다. "
                " 이름은 세상에서 가장 큰 사람이 되어라 라는 뜻이다. ")

    st.subheader('2. 임우솔에 대해서')
    st.markdown('어릴때부터 춤추는것을 좋아해서 발레리나가 꿈이였으나 중학교 코로나시기에 그만두게 되면서 컴퓨터에 관심이 생겼다. '
                '지금 현재는 컴퓨터쪽의 직업을 갖는게 장래희망이 되었다.  ')

with tab2:
    st.write('1')