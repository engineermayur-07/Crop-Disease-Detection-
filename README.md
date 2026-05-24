<div align="center">

# 🌿 Crop Suraksha — AI-Powered Crop Disease Detection

**Automated plant disease analysis for Indian farmers**

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Plant.id API](https://img.shields.io/badge/Plant.id-API%20v2-3ea94b?style=flat)](https://plant.id)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat)](LICENSE)

*Dedicated to **Shetkari Raja** — By Team Bug Hunters*

</div>

---

## 🎯 About The Project

**Crop Suraksha** (meaning "Crop Protection" in Hindi) is a web application that empowers farmers and agronomists to detect plant diseases instantly using AI. Upload a photo of any crop leaf, and the app identifies the plant species, assesses its health, and provides a complete treatment guide — all in seconds.

The app is built with Python + Streamlit and powered by the **Plant.id API**, which uses machine learning trained on millions of plant images to detect diseases with high confidence.

---

## ✨ Features

- **Instant plant identification** — detects species from a single leaf photo
- **Disease detection** — identifies diseases with confidence percentage
- **Treatment guide** — provides cause analysis and biological action plan
- **Confidence-based reporting** — flags low-confidence results and recommends expert consultation
- **Clean, responsive UI** — two-column layout with real-time status feedback
- **Healthy plant validation** — explicitly confirms when no disease is found
- **Invalid image handling** — gracefully rejects non-plant images

---

## 🖥️ Live Demo

> **Try the interactive UI demo** embedded below (click any specimen card and hit "Begin Analysis"):

An interactive walkthrough demo is available in the repository's README on GitHub. To run the live application locally, follow the setup steps below.

---

## 📸 How It Works

```
1. User uploads a crop leaf image (JPG / PNG)
         ↓
2. Image is base64-encoded and sent to Plant.id API v2
         ↓
3. API returns: plant identification + health assessment + disease details
         ↓
4. App parses the response and displays:
   ├── Plant name & scientific name
   ├── Health status (Healthy / Diseased)
   ├── Disease name + confidence %
   └── Cause analysis + biological treatment plan
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend & App Framework | [Streamlit](https://streamlit.io) |
| AI / Plant Disease Detection | [Plant.id API v2](https://plant.id) |
| HTTP Client | `requests` |
| Image Encoding | `base64` (Python standard library) |
| Styling | Custom CSS (`style.css`) |

---

## 📁 Project Structure

```
Crop-Disease-Detection-/
│
├── app.py              # Main Streamlit application
├── style.css           # Custom UI styling
├── requirements.txt    # Python dependencies
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- A [Plant.id API key](https://web.plant.id) (free tier available)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/engineermayur-07/Crop-Disease-Detection-.git
cd Crop-Disease-Detection-

# 2. Install dependencies
pip install -r requirements.txt

# 3. Add your Plant.id API key
# Open app.py and replace the value on line 6:
PLANT_ID_API_KEY = "your_api_key_here"

# 4. Run the app
streamlit run app.py
```

The app will open automatically at `http://localhost:8501`

---

## 🌐 Deploying to Streamlit Cloud

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Set `app.py` as the entry point
5. Add your `PLANT_ID_API_KEY` as a **secret** in the Streamlit Cloud dashboard (Settings → Secrets), instead of hardcoding it

```toml
# .streamlit/secrets.toml (for Streamlit Cloud deployment)
PLANT_ID_API_KEY = "your_key_here"
```

Then update `app.py` to read it as:
```python
PLANT_ID_API_KEY = st.secrets["PLANT_ID_API_KEY"]
```

---

## 🔒 Security Notice

> ⚠️ **Important:** The current version has the API key hardcoded in `app.py`. Before pushing to a public repository or deploying, move it to environment variables or Streamlit secrets as shown above. Never commit live API keys to GitHub.

---

## 🌾 Supported Crops

The app can identify and diagnose diseases for virtually any crop species supported by Plant.id, including but not limited to:

Tomato · Rice · Wheat · Maize · Cotton · Sugarcane · Soybean · Potato · Bell Pepper · Mango · Banana · Grape

---

## 📊 Confidence Thresholds

| Confidence | App Behaviour |
|---|---|
| < 1% plant probability | Shows "Invalid Specimen" warning |
| < 5% disease probability | Shows "Low Confidence" advisory |
| ≥ 5% disease probability | Shows full disease + treatment report |
| Healthy | Shows "Healthy Plant" confirmation |

---

## 🤝 Contributing

Contributions are welcome — especially for localisation into Indian regional languages and adding offline disease detection models.

1. Fork the repository
2. Create a branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add feature"`
4. Push: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 👥 Developers

Built with ❤️ by **Team Bug Hunters** — FY B.Tech Computer Science Engineering

| Name | Role |
|---|---|
| **Mayur B Gund** | FY B.Tech Computer Engineering |
| **Rohit J Khokale** | FY B.Tech Computer Engineering |
| Prathamesh Hon | FY B.Tech CSE |
| Abhishek A Shinde | FY B.Tech CSE |
| Danish A Shaikh | FY B.Tech CSE |

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

<div align="center">
  <i>🌾 Crop Suraksha — Protecting crops, empowering farmers. 🌾</i>
</div>
