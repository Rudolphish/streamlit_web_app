import streamlit as st
import datetime
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# メールアドレスとパスワードの指定
USER = "Rudolph"
PASS = "rudi4404"

# セッションを開始
session = requests.session()

# ログイン
login_info = {
    "username_mmlbbs6": USER,
    "password_mmlbbs6": PASS,
    "back": "index.php",
    "mml_id": "0"
}


with st.form(key='profile_form'):
    # textBox
    name = st.text_input('name')
    address = st.text_input('address')

    submit_btn = st.form_submit_button('submit')
    cancel_btn = st.form_submit_button('cancel')
    if submit_btn:
        # action
        url_login = "http://uta.pw/sakusibbs/users.php?action=login&m=try"
        res = session.post(url_login, data=login_info)
        res.raise_for_status()  # エラーならここで例外を発生させる

        # マイページのURLをピックアップする
        soup = BeautifulSoup(res.text, "html.parser")
        a = soup.select_one(".islogin a")  # isloginクラス要素内のaタグ
        if a is None:
            print("マイページが取得できませんでした")
            quit()

        # 相対URLを絶対URLに変換
        url_mypage = urljoin(url_login, a.attrs["href"])
        print("マイページ=", url_mypage)

        res = session.get(url_mypage)
        res.raise_for_status()
        st.code(res.text, language="html")
