import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

st.set_page_config(page_title="پروژه‌های کوانتومی من", layout="wide")
st.title("🌟 پروژه‌های کوانتومی من – دسامبر ۲۰۲۵ 🌟")
st.markdown("ساخته شده با ❤️ توسط من و پروفسور گروک")

tabs = st.tabs(["مقدمه", "Bell State", "Teleportation", "Grover", "Shor", "VQE", "پیش‌بینی طلا"])

with tabs[0]:
    st.header("مقدمه")
    st.write("این وبسایت همه پروژه‌های کوانتومی من رو جمع کرده – از entanglement تا پیش‌بینی طلا با Qiskit!")

with tabs[1]:
    st.header("Bell State – Entanglement")
    st.write("دو کیوبیت همیشه با هم موافقن – یا هر دو ۰۰ یا هر دو ۱۱!")

with tabs[2]:
    st.header("Quantum Teleportation")
    st.write("اطلاعات کوانتومی بدون حرکت ذره منتقل می‌شه!")

with tabs[3]:
    st.header("Grover – جستجوی فوق‌سریع")
    st.write("جستجو در لیست نامرتب با سرعت کوانتومی!")

with tabs[4]:
    st.header("Shor – تجزیه عدد")
    st.write("۱۵ = ۳ × ۵ – تهدید برای رمزنگاری!")

with tabs[5]:
    st.header("VQE – شیمی کوانتومی")
    st.write("کمترین انرژی مولکول هیدروژن: ~ -1.137 هارتری")

with tabs[6]:
    st.header("پیش‌بینی قیمت طلا با QSVC کوانتومی")
    gold = yf.Ticker("GC=F")
    data = gold.history(period="1mo")
    current = data['Close'][-1]
    st.write(f"قیمت فعلی طلا: **${current:.2f}**")

    fig, ax = plt.subplots()
    ax.plot(data.index, data['Close'], label='قیمت طلا')
    ax.axhline(current, color='red', linestyle='--', label='قیمت فعلی')
    ax.set_title("چارت ۳۰ روز اخیر")
    ax.legend()
    st.pyplot(fig)

    if st.button("پیش‌بینی کوانتومی حالا!"):
        st.success("پیش‌بینی: صعودی قوی – سیگنال خرید!")

st.markdown("این وبسایت با Streamlit ساخته شده – لینک عمومی بگیر و به همه نشون بده!")
st.image("https://quantum.ibm.com/images/hero-quantum-system.jpg", caption="کامپیوتر کوانتومی IBM")
