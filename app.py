import streamlit as st
import requests
import base64
import os

# 1. HARDCODE YOUR KEY HERE
PLANT_ID_API_KEY = "9SJjSWw1PekRizAEMAqV25jvAIUsmEQvVh4Ewor35DXKgLvzSb" 

# Page Configuration
st.set_page_config(
    page_title="Crop Health Detector",
    page_icon="🌿",
    layout="wide"
)

def local_css(file_name):
    if os.path.exists(file_name):
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def encode_image(image_file):
    return base64.b64encode(image_file.getvalue()).decode('utf-8')

def identify_and_diagnose(image_bytes_base64):
    url = "https://api.plant.id/v2/identify"
    
    payload = {
        "images": [image_bytes_base64],
        "modifiers": ["crops_fast", "health_all"],
        "plant_details": ["common_names", "taxonomy"],
        "disease_details": ["cause", "treatment", "description"]
    }

    headers = {
        "Content-Type": "application/json",
        "Api-Key": PLANT_ID_API_KEY
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code != 200:
        return None, f"API Error: {response.text}"
    return response.json(), None

def main():
    local_css("style.css")

    # Header
    st.markdown('<h1 class="main-title">🌿 Crop Disease Detector</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Automated Plant Disease Analysis</p>', unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

    # Sidebar (Information only, no input)
    st.sidebar.title("ℹ️ System Status")
    st.sidebar.success("Connected to AI, ready for analysis.")
    st.sidebar.markdown("---")
    st.sidebar.write("This system uses AI to identify plant species and detect physiological stress or diseases based on datasets.")

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.markdown("### 📤 Upload Plant Leaf Image")
        uploaded_file = st.file_uploader("Select a leaf photo for analysis", type=['jpg', 'jpeg', 'png'])
        
        if uploaded_file:
            st.image(uploaded_file, caption="Specimen for Analysis", width="stretch")

    with col2:
        st.markdown("### 🔍 Diagnosis Results")
        
        if uploaded_file:
            if st.button("Begin Analysis"):
                with st.spinner("Scanning the leaf..."):
                    img_base64 = encode_image(uploaded_file)
                    data, error = identify_and_diagnose(img_base64)
                    
                    if error:
                        st.error(f"Analysis Failed: {error}")
                    else:
                        # Identification
                        suggestion = data['suggestions'][0]
                        plant_probability=suggestion.get('probability', 0)
                        if plant_probability < 0.01:
                            st.markdown("""
                                <div class="error-message">
                                    <strong>⚠️ Invalid Specimen</strong><br>
                                    The system could not confidently identify a plant in this image. 
                                    Please upload a clear, close-up photo of a leaf.
                                </div>
                            """, unsafe_allow_html=True)
                        else:
                            common_name = suggestion.get('plant_name', 'Unknown Species')
                            sci_name = suggestion.get('plant_details', {}).get('scientific_name', 'N/A')
                            
                            st.markdown(f"""
                            <div class="result-card">
                                <p style="font-size:1.2rem; margin-bottom:5px;"><strong>Plant:</strong> {common_name}</p>
                                <p style="font-style:italic; color:#5A7A5A;">Scientific: {sci_name}</p>
                            </div>
                            """, unsafe_allow_html=True)

                            # Health Assessment
                            health = data.get('health_assessment', {})
                            st.markdown("---")
                            
                            if health.get('is_healthy'):
                                st.markdown("""
                                    <div class="success-message">
                                        <strong>✅ Healthy Plant</strong><br>
                                        No significant diseases or nutrient deficiencies detected.
                                    </div>
                                """, unsafe_allow_html=True)
                            else:
                                # Get the most likely disease
                                top_disease = health['diseases'][0]
                                if top_disease['probability']<0.05:
                                    st.markdown("""
                                        <div class="warning-message">
                                            <strong>⚠️ Low Confidence</strong><br>
                                            The system detected potential issues but with low confidence. 
                                            Consider retaking the photo or consulting an expert.
                                        </div>
                                    """, unsafe_allow_html=True)
                                else:
                                    d_name = top_disease['name']
                                    conf = round(top_disease['probability'] * 100, 1)
                                    
                                    st.markdown(f"""
                                        <div class="error-message">
                                            <strong>⚠️ Disease Detected: {d_name}</strong><br>
                                            Confidence: {conf}%
                                        </div>
                                    """, unsafe_allow_html=True)
                                    with st.expander("Treatment & Care Guide"):
                                        details = top_disease.get('disease_details', {})
                                        
                                        # 1. Clean up Cause
                                        cause_text = details.get('cause')
                                        if not cause_text: cause_text = "Biotic or environmental stress."
                                        st.markdown(f"**Cause:** {cause_text}")
                                        
                                        # 2. Clean up Treatment (The List Fix)
                                        treatment_data = details.get('treatment', {})
                                        # We check if it's a list; if so, we join with spaces.
                                        bio_action = treatment_data.get('biological', 'Consult agricultural extension services.')
                                        
                                        if isinstance(bio_action, list):
                                            bio_action = " ".join(bio_action)
                                        
                                        # Render as simple text
                                        st.markdown("**Action Plan required :**")
                                        st.write(bio_action)
                                    # with st.expander("Treatment & Care Guide"):
                                    #     details = top_disease.get('disease_details', {})
                                    #     treatment = details.get('treatment', {})
                                    #     st.write("**Cause:**", details.get('cause', 'Biotic or environmental stress.'))
                                    #     st.write("**Action:**", treatment.get('biological', 'Consult agricultural extension services.'))
        else:
            st.markdown("""
            <div class="result-card" style="text-align: center; color: #5A7A5A; border-style: dashed;">
                <p>Upload a specimen image to begin diagnosis.</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br><hr>", unsafe_allow_html=True)
    st.markdown('<div style="text-align: center; color: #5A7A5A; font-size: 1rem;">Dedicated to <strong>Shetkari Raja</strong> | Plant Health Engine | By <strong>Bug Hunters</strong></div>', unsafe_allow_html=True)
 
if __name__ == "__main__":
    main()
