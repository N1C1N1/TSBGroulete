import streamlit as st
from random import *

characters = {
    'The Strongest Hero': 'https://static.wikia.nocookie.net/the-strongest-battlegrounds-rblx/images/3/3c/Baldclick2.gif/revision/latest?cb=20230516013351',
    'Hero Hunter': 'https://static.wikia.nocookie.net/the-strongest-battlegrounds-rblx/images/1/18/Garou_m1.gif/revision/latest?cb=20230516151835',
    'Destructive Cyborg': 'https://static.wikia.nocookie.net/the-strongest-battlegrounds-rblx/images/3/35/M1cyborg2.gif/revision/latest?cb=20230515122730',
    'Deadly Ninja': 'https://static.wikia.nocookie.net/the-strongest-battlegrounds-rblx/images/d/d1/F_-_SD_480p_AdobeExpress.gif/revision/latest?cb=20230603125018',
    'Brutal Demon': 'https://static.wikia.nocookie.net/the-strongest-battlegrounds-rblx/images/e/e9/AdrenalineDemonM1.gif/revision/latest?cb=20230716100358'
}

challenges = [
    f'Сделать {randint(1, 11)} аппер кодов',
    f'Сделать {randint(1, 11)} впечатываней',
    f'Не юзать {choice(["блок", "прыжок", "аппер код", "впечатывание"])}',
    f'Не юзать {randint(1, 4)} скилл'
]

def create(pvp: bool):
    if pvp:
        with st.container(border=True):
            st.header(choice(list(characters.keys())), divider='rainbow')
            st.subheader(choice(challenges))
    else:
        with st.container(border=True):
            st.title('1 Игрок')
            p1 = choice(list(characters.keys()))
            st.header(p1, divider='rainbow')
            st.subheader(choice(challenges))
            st.title('2 Игрок')
            while True:
                p2 = choice(list(characters.keys()))
                if p2 != p1:
                    st.header(p2, divider='rainbow')
                    st.subheader(choice(challenges))
                    break
with st.container():
    st.button('1v1', on_click=lambda: create(True), use_container_width=True)
    st.button('2v2', on_click=lambda: create(False), use_container_width=True)
