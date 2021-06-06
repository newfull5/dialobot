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
from dialobot.app.frontend.utils.css import style
from dialobot.app.frontend.pages import (
    intent,
    entity,
    qa,
    para,
    response,
)


class Frontend:

    def __init__(self):
        st.markdown(
            f'<style>{style}</style>',
            unsafe_allow_html=True,
        )

        self.pages = {
            "Intent Classification": intent,
            "Entity Recognition": entity,
            "Question Answering": qa,
            "Paraphrase Generation": para,
            "Response Generation": response,
        }
        self.build_sidebar()

    def build_sidebar(self):
        st.sidebar.image(
            "https://user-images.githubusercontent.com/38183241/118511978-5d537180-b76d-11eb-89bd-055cb9227725.png"
        )

        page_names = list(self.pages.keys())
        buttons = st.sidebar.radio('', page_names)

        # 멀티 페이지 앱을 돌리는 방법을 알아보았으나 radio버튼으로 구현하는 것이 최선이라고 한다. 디자인이 영 별로여서 나중에 회의때 부쳐봐야겠다.
        """
        current_page = "Intent Classification"
        
        for i, button in enumerate(buttons):
            if button:
                current_page = page_names[i]"""

        self.pages[buttons].page()
