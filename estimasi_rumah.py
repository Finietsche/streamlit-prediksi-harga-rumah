import pickle
import streamlit as st

# Load model
model = pickle.load(open('estimasi_rumah.sav', 'rb'))

# Set up page
st.set_page_config(page_title="Estimasi Harga Rumah", page_icon="🏠", layout="centered")

# Add background
def add_bg_from_url():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://img.pikbest.com/wp/202342/living-room-background-wall-contemporary-comfort-3d-render-of-minimalist-with-blue-pattern_9863141.jpg!bw700");
            background-attachment: fixed;
            background-size: cover;
        }}
        .card {{
            background-color: rgba(255, 255, 255, 0.9);
            border-radius: 10px;
            padding: 20px;
            margin: 20px 0;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }}
        .header {{
            text-align: center;
            font-family: 'Arial', sans-serif;
            color: #4CAF50; /* Tetap hijau untuk judul */
        }}
        p, label, .stMarkdown {{
            color: black; /* Warna hitam untuk teks lainnya */
            font-family: 'Arial', sans-serif;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_url()

# Title
st.markdown("<h1 class='header'>🏠 Estimasi Harga Rumah</h1>", unsafe_allow_html=True)
st.subheader('Masukkan detail rumah untuk mendapatkan estimasi harga.')

# Input fields in two columns
col1, col2 = st.columns(2)

with col1:
    bedrooms = st.number_input('🛏️ Jumlah Kamar Tidur', min_value=0, max_value=10, step=1, value=3, help="Jumlah kamar tidur dalam rumah.")
    bathrooms = st.number_input('🛁 Jumlah Kamar Mandi', min_value=0, max_value=10, step=1, value=2, help="Jumlah kamar mandi dalam rumah.")
    sqft_living = st.number_input('📐 Luas Rumah (sqft)', min_value=100, max_value=10000, step=100, value=1500, help="Luas total rumah dalam satuan persegi.")
    floors = st.slider('🏢 Jumlah Lantai', min_value=1, max_value=5, value=1, help="Jumlah lantai dalam rumah.")

with col2:
    condition = st.slider('🔧 Kondisi Rumah (1: Buruk - 5: Bagus)', min_value=1, max_value=5, value=3, help="Kondisi keseluruhan rumah.")
    grade = st.slider('⭐ Grade Rumah (1: Rendah - 13: Tinggi)', min_value=1, max_value=13, value=7, help="Grade rumah berdasarkan evaluasi.")
    yr_built = st.number_input('📅 Tahun Dibangun', min_value=1800, max_value=2025, step=1, value=2000, help="Tahun rumah selesai dibangun.")

# Button to estimate price
if st.button('📊 Hitung Estimasi Harga'):
    # Prediction
    predict = model.predict([[bedrooms, bathrooms, sqft_living, condition, grade, floors, yr_built]])
    usd_price = predict[0]
    idr_price = usd_price * 16282

    # Display results in a card-style layout
    st.markdown(
        f"""
        <div class="card">
            <h3 class="header">💰 Hasil Estimasi:</h3>
            <p><b>Harga dalam USD:</b> <span style="color:#4CAF50; font-size: 20px;">${usd_price:,.2f}</span></p>
            <p><b>Harga dalam IDR:</b> <span style="color:#4CAF50; font-size: 20px;">Rp {idr_price:,.0f}</span></p>
        </div>
        """,
        unsafe_allow_html=True,
    )
else:
    st.info("Silakan masukkan detail rumah dan tekan tombol **Hitung Estimasi Harga**.")

# Add an image
st.image('rumah3.png', use_column_width=False, width=400, caption="Contoh Rumah Modern")

# Footer
st.markdown(
    """
    ---
    <p style="text-align:center; font-size:14px;">
    Dibuat Oleh Kelompok Kami.
    </p>
    """,
    unsafe_allow_html=True,
)
