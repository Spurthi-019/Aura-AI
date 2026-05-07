# ✨ Aura AI - Sentiment Analysis Dashboard

<div align="center">

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://aura-aigit.streamlit.app/)
[![GitHub](https://img.shields.io/badge/GitHub-Aura--AI-blue?logo=github)](https://github.com/Spurthi-019/Aura-AI)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

### 🚀 **[LIVE DEPLOYED APP](https://aura-aigit.streamlit.app/)** ← Click Here to Use Now!

</div>

A beautiful, modern **Streamlit web application** for real-time sentiment analysis using **TextBlob**. Analyze the emotional tone of any text with an elegant neon-styled dashboard.

---

## 🌐 Quick Links

| 🚀 Try Live | 📖 Documentation | 💻 Source Code |
|:---:|:---:|:---:|
| [![Open in Streamlit](https://img.shields.io/badge/Open%20in%20Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://aura-aigit.streamlit.app/) | [Full Docs](#-resources) | [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Spurthi-019/Aura-AI) |

---

## ✨ Key Highlights

- 🎨 **Neon Dark Theme** with glowing effects
- ⚡ **Instant Deployment** - Already live on Streamlit Cloud
- 📊 **Real-time Analysis** - See results immediately
- 🔒 **Production Ready** - Clean code, no secrets exposed
- 📱 **Responsive Design** - Works on desktop and mobile

---

## 🌐 Live Demo

**[🚀 Try Aura AI Live](https://aura-aigit.streamlit.app/)**

Visit the deployed application and start analyzing sentiment in real-time!

---

## 🎯 Features

✨ **Modern UI Design**
- Dark theme with neon cyan (#00ffcc) accents
- Glowing button effects with smooth animations
- Responsive and centered layout
- Professional AI dashboard aesthetic

📊 **Sentiment Analysis**
- Real-time text analysis using TextBlob
- Polarity score (-1 to 1)
- Subjectivity measurement (0 to 1)
- Conditional messaging based on sentiment

🎨 **Interactive Visualizations**
- Progress bars for sentiment and subjectivity
- Metrics display with neon styling
- Celebration balloons for positive sentiment
- Color-coded alerts (Success, Error, Info)

💾 **Data Management**
- Stores analysis results in session state
- Displays analyzed text and metrics
- Persistent data during session

---

## 🛠 Tech Stack

| Technology | Purpose |
|-----------|---------|
| **Streamlit** | Web framework |
| **TextBlob** | Sentiment analysis |
| **Python 3.14+** | Core language |
| **Custom CSS** | Neon styling |

---

## 📋 Requirements

```
streamlit
textblob
```

---

## 🚀 Getting Started

> **💡 TIP**: No need to install anything! [**Use the live deployed version**](https://aura-aigit.streamlit.app/) right now!

### Run Locally (Optional)

If you want to run the app locally for development or customization:

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Spurthi-019/Aura-AI.git
   cd Aura-AI
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Running the App

### Option 1: Use the Live Deployed Version (Recommended) ⭐
Simply visit: [**https://aura-aigit.streamlit.app/**](https://aura-aigit.streamlit.app/)

### Option 2: Run Locally

```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

---

## 📱 How to Use

1. **Enter Text**: Type or paste any review, comment, or sentence in the text area
2. **Click Analyze**: Press the "🔍 Analyze Sentiment" button
3. **View Results**: 
   - See sentiment classification (Positive/Negative/Neutral)
   - Check polarity score (-1 to 1)
   - View subjectivity level (0 to 1)
   - Watch the progress bars visualize the scores

### Example Inputs:
- ✅ "This product is amazing! I love it!" → **Positive Aura** 🎉
- ❌ "Terrible quality, very disappointed." → **Negative Aura**
- 🔄 "The product is average." → **Neutral Aura**

---

## 🎨 Styling Features

The app includes custom CSS with:
- **Dark background**: `#0e1117` (GitHub dark theme)
- **Neon cyan borders**: `#00ffcc` with glow effect
- **Gradient buttons**: Cyan to blue with box-shadow glow
- **Neon metrics**: Cyan-styled metric cards
- **Color-coded messages**: Success (cyan), Error (red), Info (blue)
- **Smooth animations**: Transitions and hover effects

---

## 📊 Sentiment Analysis Details

### Polarity
- **Range**: -1.0 (most negative) to 1.0 (most positive)
- **Interpretation**:
  - > 0.1: Positive
  - < -0.1: Negative
  - ≈ 0: Neutral

### Subjectivity
- **Range**: 0.0 (objective) to 1.0 (subjective)
- **Interpretation**:
  - < 0.5: More factual/objective
  - > 0.5: More opinion-based/subjective

---

## 🚀 Deployment

### Deploy to Streamlit Cloud (Recommended)

1. Push your code to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Click "New app"
4. Select your GitHub repository
5. Choose the branch and file (`app.py`)
6. Deploy!

### Other Deployment Options
- **Heroku**: Docker-based deployment
- **Railway**: Simple GitHub integration
- **Render**: Auto-deployment from GitHub
- **AWS/GCP/Azure**: Using containers

---

## 📝 Project Structure

```
Aura-AI/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .gitignore         # Git ignore file
└── README.md          # This file
```

---

## 🔧 Customization

### Change Colors
Edit the CSS in `app.py` to modify:
- Background color: `background-color: #0e1117`
- Neon color: `#00ffcc`
- Accent color: `#00ccff`

### Adjust Sentiment Thresholds
In the `analyze_sentiment()` function:
```python
if polarity > 0.1:      # Adjust this threshold
    sentiment = "Positive 😊"
elif polarity < -0.1:   # Adjust this threshold
    sentiment = "Negative 😢"
```

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| TextBlob import error | Run `pip install textblob` |
| Streamlit not found | Run `pip install streamlit` |
| Port 8501 in use | Run `streamlit run app.py --server.port=8502` |
| CSS not applying | Clear browser cache or restart Streamlit |

---

## 📖 Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [TextBlob Documentation](https://textblob.readthedocs.io/)
- [Sentiment Analysis Guide](https://en.wikipedia.org/wiki/Sentiment_analysis)

---

## 👤 Author

**Spurthi-019**  
GitHub: [@Spurthi-019](https://github.com/Spurthi-019)

---

## 📄 License

This project is open source and available under the MIT License.

---

## ⭐ Show Your Support

If you find this project helpful, please consider:
- ⭐ Starring the repository
- 🔀 Forking and contributing improvements
- 💬 Sharing feedback and suggestions

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

**Made with ❤️ and neon lights** ✨
