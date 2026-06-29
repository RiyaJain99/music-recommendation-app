# 🎵 AI Music Recommendation System

<p align="center">

![Python](https://img.shields.io/badge/Python-3.9-blue?style=for-the-badge\&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge\&logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge\&logo=scikitlearn)
![GitHub](https://img.shields.io/badge/GitHub-Repository-black?style=for-the-badge\&logo=github)

</p>

---

# 🎧 Overview

An AI-powered Music Recommendation System that recommends similar songs using Machine Learning and Content-Based Filtering.

The application analyzes audio features such as danceability, energy, tempo, valence, acousticness, and more to discover similar tracks using Cosine Similarity.

---
link:
https://music-recommendation-app-zwuhrpy43zuwkm4pexmfjb.streamlit.app/
---

## 🚀 Features

* 🎵 Smart Music Recommendation
* 🤖 Content-Based Recommendation Engine
* 📊 Audio Feature Analysis
* ⚡ Fast Similarity Search
* 🎨 Interactive Streamlit Dashboard
* 🎯 Personalized Song Suggestions
* 💾 Machine Learning Powered

---

## 📂 Dataset

**Spotify Songs Dataset**

Dataset contains over **230,000+ songs** with detailed audio characteristics.

### Important Features

* Track Name
* Artist Name
* Genre
* Danceability
* Energy
* Tempo
* Acousticness
* Instrumentalness
* Liveness
* Speechiness
* Valence

---

# 🧠 Machine Learning Workflow

```
Load Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Feature Selection
      │
      ▼
Standard Scaling
      │
      ▼
Cosine Similarity
      │
      ▼
Recommendation Engine
      │
      ▼
Streamlit Deployment
```

---

# ⚙️ Technologies Used

| Category                 | Technology        |
| ------------------------ | ----------------- |
| Programming              | Python            |
| Data Processing          | Pandas, NumPy     |
| Machine Learning         | Scikit-Learn      |
| Recommendation Algorithm | Cosine Similarity |
| Feature Scaling          | StandardScaler    |
| Dashboard                | Streamlit         |
| Version Control          | Git & GitHub      |

---

# 📊 Recommendation Logic

The recommendation engine compares songs using their audio features.

Features considered include:

* Danceability
* Energy
* Acousticness
* Instrumentalness
* Speechiness
* Liveness
* Tempo
* Valence

Songs with the highest cosine similarity score are recommended.

---

# 💼 Business Applications

This system can be used by:

* Music Streaming Platforms
* Entertainment Applications
* Smart Playlists
* Personalized User Experience
* Music Discovery Platforms
* AI Assistants

---

# 📁 Project Structure

```
music-recommendation-app/
│
├── app.py
├── SpotifyFeatures.csv
├── similarity.pkl
├── songs.pkl
├── scaler.pkl
├── requirements.txt
├── README.md
└── Music Recommendation.ipynb
```

---

# ▶️ Installation

Clone the repository

```bash
git clone https://github.com/RiyaJain99/music-recommendation-app.git
```

Go inside the folder

```bash
cd music-recommendation-app
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 🎯 Future Improvements

* 🎶 Hybrid Recommendation System
* ❤️ User Preference Learning
* 🤝 Collaborative Filtering
* 🌐 Spotify API Integration
* 🎵 Album Artwork Support
* 🎤 Artist-Based Recommendations
* ⭐ Playlist Generation
* 📈 Recommendation Analytics

---
# 👩‍💻 Author

**Riya Jain**

🎓 B.Tech CSE (IoT)
📍 Vellore Institute of Technology, Vellore

GitHub: https://github.com/RiyaJain99


---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

It helps others discover the project and motivates future improvements.

---

### Made with ❤️ using Python, Machine Learning and Streamlit.
