# Copyright (c) 2021, Hyunwoong Ko. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
import pandas as pd

def page():
    st.markdown('***')
    current_page = st.radio('', ['Intent Classification', 'Add Intent', 'Intent List'])
    st.markdown('***')
    page_keys = {
        'Intent Classification': intent_classification_page,
        'Add Intent': add_intent_page,
        'Intent List': intent_list,
    }

    page_keys[current_page]()


def intent_classification_page():
    st.title('Intent Classification')
    st.markdown("<br>", unsafe_allow_html=True)
    st.write(
        "Intent classification is a feature that analyzes the intention of the user's utterance. "
        "Dialobot can predict the user's intention with just a few examples without training. "
        "You can edit by clicking name of intent, "
        "and if you want to add a new intent, click the 'Add Intent' button.")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("***")

    col1, col2, col3 = st.beta_columns(3)
    with col1:
        st.markdown(
            "<h4 style='text-align: center'>Intent Name</h4>",
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            "<h4 style='text-align: center'>Sentences</h4>",
            unsafe_allow_html=True,
        )
    with col3:
        st.markdown(
            "<h4 style='text-align: center'>Replies</h4>",
            unsafe_allow_html=True,
        )

    st.markdown("***")

    col1, col2, col3 = st.beta_columns(3)
    with col1:
        st.button("Default")
        st.button("Weather")
        st.button("Restaurant")
        st.button("Time")

    with col2:
        st.markdown(
            "<p style='text-align: center; padding: 0.25rem 0.25rem;'> N/A </p>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<p style='text-align: center; padding: 0.25rem 0.25rem;'> 12 </p>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<p style='text-align: center; padding: 0.25rem 0.25rem;'> 2 </p>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<p style='text-align: center; padding: 0.25rem 0.25rem;'> 16 </p>",
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            "<p style='text-align: center; padding: 0.25rem 0.25rem;'> 4 </p>",
            unsafe_allow_html=True)
        st.markdown(
            "<p style='text-align: center; padding: 0.25rem 0.25rem;'> 5 </p>",
            unsafe_allow_html=True)
        st.markdown(
            "<p style='text-align: center; padding: 0.25rem 0.25rem;'> 12 </p>",
            unsafe_allow_html=True)
        st.markdown(
            "<p style='text-align: center; padding: 0.25rem 0.25rem;'> 10 </p>",
            unsafe_allow_html=True)

    st.markdown("***")
    st.markdown("<br>", unsafe_allow_html=True)


def add_intent_page():
    st.markdown("<h3 style='text-align: center; color: #495057;'>Intent Name</h3>", unsafe_allow_html=True)
    tmp1, intent_input, tmp2 = st.beta_columns([1, 3, 1])
    intent_input.text_input(label='', value='', help='Here you can specify the type of intent')
    st.markdown("<br>", unsafe_allow_html=True)
    st.text_input(label="Expecting User's input: ", value='', key=1, help='Here you can specify the type of intent')
    st.text_input(label="System replies: ", value='', key=1, help='Here you can specify the type of intent')

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #495057;'>Fallback Setting</h3>", unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)

    st.markdown("***")
    st.markdown("<div style='text-align: center; color: #212529;'>Default Replies</div>", unsafe_allow_html=True)
    st.markdown("***")
    st.markdown("<p style='text-align: center; color: #868e96;'> Sorry...?</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #868e96;'> Pardon me?</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #868e96;'> i didn't get it well...</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #868e96;'> could you say that again..?</p>",
                unsafe_allow_html=True)

    st.text_input(label='', value='Add User expression')
    st.markdown("***")

    st.markdown("<p style='text-align: center; color: #495057;'>Fallback ratio</p>", unsafe_allow_html=True)
    fallback_slider = st.slider('', 0, 100, 25, help='fallback is sadfsadf')

    st.button('SAVE')


def intent_list():
    _, intent, _ = st.beta_columns([1,4,1])
    _, data, _ = st.beta_columns([1,9,1])
    intent_category = ['Default', 'Weather', 'Restaurant', 'Time']
    replies = {
        'Default': [],
        'Weather': [],
        'Restaurant': [],
        'Time': []
    }

    with intent:
        st.write()
        dropdown = st.selectbox('', intent_category)

    with data:
        st.dataframe(pd.DataFrame({
            'Sentences': ['오랜만이야','안녕','저기','잘 있었어','반가워'],
            'Replies': ['안녕!','안녕하세요!','안녕','오랜만이야!','안녕!']
        }), width=2000, height=400)
