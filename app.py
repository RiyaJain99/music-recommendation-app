import streamlit as st
import pickle
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(
    page_title="AI Music Recommendation",
    page_icon="🎵",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
* { font-family: 'Inter', sans-serif; }
.stApp { background: #0d0d0d; color: white; }
.stSelectbox > div > div {
    background: #1f1f1f !important;
    border: 1px solid #333 !important;
    color: white !important;
    border-radius: 10px !important;
}
.big {
    font-size: 42px; font-weight: 700; text-align: center;
    background: linear-gradient(135deg, #1DB954, #17a047);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    margin-bottom: 0px;
}
.subtitle { text-align: center; color: #888; font-size: 16px; margin-top: 4px; margin-bottom: 30px; }
.selected-song {
    background: linear-gradient(135deg, #1DB954 0%, #158a3e 100%);
    padding: 16px 24px; border-radius: 12px; margin-bottom: 24px;
    display: flex; align-items: center; gap: 12px;
}
.card {
    background: #1a1a1a; padding: 18px 22px; border-radius: 12px;
    border: 1px solid #2a2a2a; margin-bottom: 12px;
    display: flex; align-items: center; justify-content: space-between;
}
.card:hover { border-color: #1DB954; }
.rank { font-size: 28px; font-weight: 700; color: #1DB954; min-width: 45px; }
.song-info { flex: 1; }
.song-title { font-size: 17px; font-weight: 600; color: #ffffff; margin: 0; }
.artist-name { font-size: 14px; color: #aaa; margin-top: 4px; }
.score-badge {
    background: #1DB954; color: black; font-weight: 700;
    font-size: 13px; padding: 4px 12px; border-radius: 20px;
}
.stButton > button {
    background: linear-gradient(135deg, #1DB954, #17a047) !important;
    color: black !important; font-weight: 700 !important; font-size: 16px !important;
    border: none !important; border-radius: 30px !important;
    padding: 12px 40px !important; width: 100%;
}
.stButton > button:hover { opacity: 0.85 !important; }
</style>
""", unsafe_allow_html=True)

# ── Load data (cached so it only runs once) ────────────────
@st.cache_resource
def load_data():
    songs = pickle.load(open("songs.pkl", "rb"))
    scaler = pickle.load(open("scaler.pkl", "rb"))

    features = ['acousticness', 'danceability', 'energy', 'instrumentalness',
                'liveness', 'speechiness', 'tempo', 'valence']

    X = songs[features].values
    X_scaled = scaler.transform(X)
    return songs, X_scaled

songs, X_scaled = load_data()

# ── Header ─────────────────────────────────────────────────
st.markdown("<p class='big'>🎵 AI Music Recommendation</p>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Select a song and discover your next favourite tracks</p>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    song = st.selectbox("🎼 Choose a Song", songs["track_name"].values, label_visibility="collapsed")
    st.write("")
    clicked = st.button("🎧 Get Recommendations")

# ── Recommend function ──────────────────────────────────────
def recommend(song):
    index = songs[songs["track_name"] == song].index[0]

    # compute similarity only for the selected song (fast!)
    song_vector = X_scaled[index].reshape(1, -1)
    distances = cosine_similarity(song_vector, X_scaled)[0]

    song_list = sorted(enumerate(distances), reverse=True, key=lambda x: x[1])[1:6]

    recommendations = []
    for i in song_list:
        recommendations.append({
            "title":  songs.iloc[i[0]]["track_name"],
            "artist": songs.iloc[i[0]]["artist_name"],
            "score":  round(i[1] * 100, 1)
        })
    return recommendations

# ── Results ────────────────────────────────────────────────
if clicked:
    recs = recommend(song)

    st.write("")
    st.markdown(f"""
    <div class='selected-song'>
        <span style='font-size:24px'>🎵</span>
        <div>
            <div style='font-weight:700;font-size:16px'>Now playing: {song}</div>
            <div style='font-size:13px;opacity:0.85'>Finding similar tracks...</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🔥 Top 5 Recommendations")
    st.write("")

    medals = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣"]

    for idx, rec in enumerate(recs):
        st.markdown(f"""
        <div class='card'>
            <div class='rank'>{medals[idx]}</div>
            <div class='song-info'>
                <p class='song-title'>{rec['title']}</p>
                <p class='artist-name'>👤 {rec['artist']}</p>
            </div>
            <span class='score-badge'>{rec['score']}% match</span>
        </div>
        """, unsafe_allow_html=True)