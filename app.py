import streamlit as st
import random

st.title("🎯 Sayı Tahmin Oyunu")

# 1 ile 100 arasında rastgele bir sayı üret (ilk seferde)
if "target" not in st.session_state:
    st.session_state.target = random.randint(1, 100)
    st.session_state.tries = 0
    st.session_state.game_over = False

# Oyun bittiyse mesaj göster ve durdur
if st.session_state.game_over:
    st.success("🎉 Oyunu zaten kazandınız! Sayfayı yenileyerek yeniden başlayabilirsiniz.")
    st.stop()

# Kullanıcıdan tahmin al
guess = st.number_input("1 ile 100 arasında bir tahmin girin:", min_value=1, max_value=100, step=1)

# Buton ile kontrol
if st.button("Tahmin Et"):
    st.session_state.tries += 1

    if guess < st.session_state.target:
        st.warning("🔼 Daha büyük bir sayı girin.")
    elif guess > st.session_state.target:
        st.warning("🔽 Daha küçük bir sayı girin.")
    else:
        st.success(f"🎉 Tebrikler! {st.session_state.tries} denemede doğru tahmin ettiniz!")
        st.session_state.game_over = True

# Deneme sayısını göster
st.info(f"Deneme sayısı: {st.session_state.tries}")

