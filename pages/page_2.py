import streamlit as st
import datetime

with st.form(key='profile_form'):
    # textBox
    name = st.text_input('name')
    address = st.text_input('address')

    # selectBox
    age_category = st.selectbox(
        '年齢層',
        ('選択してください', '子ども', '大人'))

    # radioButton
    sex_category = st.radio(
        '性別',
        ('非公開', '男性', '女性'))

    # multiSelect
    hobby = st.multiselect(
        '趣味',
        ('スポーツ', '読書', 'プログラミング', 'アニメ', '釣り', '料理'))

    # checkBox
    mail_subscribe = st.checkbox('メールマガジンを購読する')

    # slider
    height = st.slider('身長', min_value=110, max_value=210)

    # date
    start_date = st.date_input(
        '開始日',
        datetime.datetime.now().date())

    # color
    color = st.color_picker('テーマカラー', '#00f900')

    submit_btn = st.form_submit_button('submit')
    cancel_btn = st.form_submit_button('cancel')
    if submit_btn:
        st.text(f'ようこそ！{name}さん！{address}に書籍を送りました！')
        if age_category == '選択してください':
            st.text(f'年齢層：選択されていません')
        else:
            st.text(f'年齢層：{age_category}')
        st.text(f'性別：{sex_category}')
        st.text(f'趣味：{",".join(hobby)}')
        st.text(f'購読：{mail_subscribe}')
        st.text(f'身長：{height}')
