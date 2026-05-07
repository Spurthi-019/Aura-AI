import streamlit as st
from textblob import TextBlob

# Page configuration
st.set_page_config(
    page_title="Aura AI",
    page_icon="✨",
    layout="centered"
)

# Custom CSS for dark theme with neon effects
custom_css = """
<style>
    /* Dark theme background */
    .stApp {
        background-color: #0e1117;
    }
    
    /* Main container */
    [data-testid="stAppViewContainer"] {
        background-color: #0e1117;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #010409;
    }
    
    /* Text color for light text on dark background */
    p, span, div {
        color: #e6edf3 !important;
    }
    
    /* Text area with neon cyan border */
    .stTextArea textarea {
        background-color: #010409 !important;
        border: 2px solid #00ffcc !important;
        border-radius: 8px !important;
        color: #e6edf3 !important;
        padding: 12px !important;
        font-size: 14px !important;
        box-shadow: 0 0 10px rgba(0, 255, 204, 0.3) !important;
        transition: box-shadow 0.3s ease !important;
    }
    
    /* Text area hover effect */
    .stTextArea textarea:focus {
        border-color: #00ffcc !important;
        box-shadow: 0 0 20px rgba(0, 255, 204, 0.6) inset, 0 0 20px rgba(0, 255, 204, 0.3) !important;
        outline: none !important;
    }
    
    /* Button with neon glow effect */
    .stButton button {
        background: linear-gradient(135deg, #00ffcc, #00ccff) !important;
        color: #0e1117 !important;
        border: 2px solid #00ffcc !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        padding: 12px 24px !important;
        font-size: 16px !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 0 15px rgba(0, 255, 204, 0.5), 0 0 30px rgba(0, 204, 255, 0.3) !important;
        cursor: pointer !important;
    }
    
    /* Button hover effect - enhanced glow */
    .stButton button:hover {
        box-shadow: 0 0 25px rgba(0, 255, 204, 0.8), 0 0 50px rgba(0, 204, 255, 0.6), inset 0 0 20px rgba(0, 255, 204, 0.2) !important;
        transform: translateY(-2px) !important;
    }
    
    /* Button active state */
    .stButton button:active {
        box-shadow: 0 0 30px rgba(0, 255, 204, 0.9), 0 0 60px rgba(0, 204, 255, 0.7), inset 0 0 30px rgba(0, 255, 204, 0.4) !important;
        transform: translateY(0) !important;
    }
    
    /* Success message styling */
    .stSuccess {
        background-color: rgba(0, 255, 204, 0.1) !important;
        border: 2px solid #00ffcc !important;
        border-radius: 8px !important;
        color: #00ffcc !important;
        padding: 16px !important;
        box-shadow: 0 0 15px rgba(0, 255, 204, 0.3) !important;
    }
    
    /* Error message styling */
    .stError {
        background-color: rgba(255, 0, 102, 0.1) !important;
        border: 2px solid #ff0066 !important;
        border-radius: 8px !important;
        color: #ff0066 !important;
        padding: 16px !important;
        box-shadow: 0 0 15px rgba(255, 0, 102, 0.3) !important;
    }
    
    /* Info message styling */
    .stInfo {
        background-color: rgba(0, 204, 255, 0.1) !important;
        border: 2px solid #00ccff !important;
        border-radius: 8px !important;
        color: #00ccff !important;
        padding: 16px !important;
        box-shadow: 0 0 15px rgba(0, 204, 255, 0.3) !important;
    }
    
    /* Warning message styling */
    .stWarning {
        background-color: rgba(255, 153, 0, 0.1) !important;
        border: 2px solid #ff9900 !important;
        border-radius: 8px !important;
        color: #ff9900 !important;
        padding: 16px !important;
        box-shadow: 0 0 15px rgba(255, 153, 0, 0.3) !important;
    }
    
    /* Metrics styling */
    .stMetric {
        background-color: rgba(0, 255, 204, 0.05) !important;
        border: 1px solid rgba(0, 255, 204, 0.3) !important;
        border-radius: 8px !important;
        padding: 16px !important;
        box-shadow: 0 0 10px rgba(0, 255, 204, 0.2) !important;
    }
    
    /* Title styling */
    h1, h2, h3 {
        color: #00ffcc !important;
        text-shadow: 0 0 10px rgba(0, 255, 204, 0.5) !important;
    }
    
    /* Progress bar styling */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #00ffcc, #00ccff) !important;
        box-shadow: 0 0 10px rgba(0, 255, 204, 0.5) !important;
    }
    
    /* Horizontal line styling */
    hr {
        border-color: rgba(0, 255, 204, 0.3) !important;
    }
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# Title
st.title("✨ Aura AI")
st.subheader("Sentiment Analysis Tool")

# Main content
st.write("Enter your text below to analyze its sentiment.")

# Input text area
text_input = st.text_area(
    "Enter text for sentiment analysis:",
    placeholder="Type something here...",
    height=150
)

# Initialize session state for storing analysis results
if "analysis_result" not in st.session_state:
    st.session_state.analysis_result = None

# Sentiment analysis function
def analyze_sentiment(text):
    """Analyze sentiment using TextBlob"""
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    
    # Determine sentiment label
    if polarity > 0.1:
        sentiment = "Positive 😊"
        color = "green"
    elif polarity < -0.1:
        sentiment = "Negative 😢"
        color = "red"
    else:
        sentiment = "Neutral 😐"
        color = "gray"
    
    return sentiment, polarity, subjectivity, color

# Analyze button
if st.button("🔍 Analyze Sentiment", use_container_width=True):
    if text_input.strip():
        # Analyze the text
        sentiment, polarity, subjectivity, color = analyze_sentiment(text_input)
        
        # Store results in session state variables
        st.session_state.analysis_result = {
            "text": text_input,
            "sentiment": sentiment,
            "polarity": polarity,
            "subjectivity": subjectivity,
            "color": color
        }
        
        # Display results
        st.markdown("---")
        st.subheader("Analysis Results")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Sentiment", sentiment)
        
        with col2:
            st.metric("Polarity", f"{polarity:.2f}")
        
        with col3:
            st.metric("Subjectivity", f"{subjectivity:.2f}")
        
        # Display conditional message based on polarity
        st.markdown("---")
        if polarity > 0:
            st.success("✨ **Positive Aura** ✨")
            st.balloons()
        elif polarity < 0:
            st.error("⚠️ **Negative Aura** ⚠️")
        else:
            st.info("🔄 **Neutral Aura** 🔄")
        
        # Sentiment score progress bar (normalized from -1 to 1 scale)
        st.markdown("### Sentiment Score Progress")
        normalized_polarity = (polarity + 1) / 2  # Convert from [-1, 1] to [0, 1]
        st.progress(normalized_polarity, text=f"Sentiment: {polarity:.2f} (range: -1 to 1)")
        
        # Subjectivity progress bar
        st.markdown("### Subjectivity Level")
        st.progress(subjectivity, text=f"Subjectivity: {subjectivity:.2f} (range: 0 to 1)")
        
        st.markdown("---")
        st.info(
            f"**Polarity** ranges from -1 (negative) to 1 (positive)\n\n"
            f"**Subjectivity** ranges from 0 (objective) to 1 (subjective)"
        )
    else:
        st.warning("Please enter some text to analyze.")

# Display stored results if available
if st.session_state.analysis_result:
    st.markdown("---")
    st.subheader("Stored Analysis Data")
    result = st.session_state.analysis_result
    st.write(f"**Text analyzed:** {result['text'][:100]}..." if len(result['text']) > 100 else f"**Text analyzed:** {result['text']}")
    st.write(f"- **Polarity value:** {result['polarity']}")
    st.write(f"- **Subjectivity value:** {result['subjectivity']}")

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>Powered by TextBlob 📚</p>",
    unsafe_allow_html=True
)