import os
import streamlit as st
from pathlib import Path
import google.generativeai as genai
from api_key import api_key

#Configuring the api key
genai.configure(api_key=api_key)

# tuning of Settings
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro-002",
  generation_config=generation_config,
)

system_prompt="""
As a highly skilled medical practictioner specializing in image analysis, you are tasked with examining medical images for renowned hospital. Your expertise is crucial in identifying any anaomalies, disease, or health issues that may be present in the images.

Your responsibilities include:
1. Detailed Analysis: Thoroughly analyze each image, focusing on identifying any abnormal findings.
2. Findings Report: Document all observed anomalies or sign of disease. Clearly articulate these findings in a structural format.
3. Recommendation and Next Steps: Based on your analysis, suggest potential next steps, including for the tests and treatments as applicable.
4. Treatment Suggestion: If appropriate, recommend possible treatment options or interventions.

Important Notes:
1. Scope of Response: Only respond if the image pertains to human health issues.
2. Clarity of Image: In case where the image quality impedes clear analysis, note the certain aspects are 'Unable to be determind based on provided image.'
3. Disclaimer: Accompany your analysis with the disclaimer: "Consult with a Doctor before making any decision."
Your insights are invaluabe in guiding clinical decision. Please proceed with analysis, adhering to the structured approach outlined above.
Please Provide me output with these provide headings: Detailed Analysis, Findings Report, Recommendation and Next Steps, Treatment Suggestion
Also generate related images based on provided image
"""
st.set_page_config("Doctor Assistant")
st.title("🙍🏻Vital❤ Image📷 Analytics📊")

st.subheader("Hi! I am Circuit🤖. I will help you to analyse medical images🙌")
uploaded_file = st.file_uploader("Upload the medical image for analysis",type=["png","jpg","jpeg"])
if uploaded_file:
    st.image(uploaded_file,width=250)

submit_button=st.button("Generate the Analysis")

if submit_button:
    image_data=uploaded_file.getvalue()
    #making our image ready
    image_parts=[
        {
            "mime_type": "image/jpeg",
            "data":image_data
        }
    ]
    #making our prompt ready
    prompt_parts=[
        image_parts[0],
        system_prompt,
    ]
    
    #genrate a response
    response=model.generate_content(prompt_parts)
    if response:
        st.title("Here's the analysis based on the provided image")
    st.write(response.text)




