import requests
import base64
import os
import json 

# === Config ===
API_KEY = "Your api key : "
# Note: You can get your API key from https://console.cloud.google.com/apis/credentials?project=gemini-1-5-flash
IMAGE_PATH = input("Enter the path to the image: ")
REPORT_FOLDER = "Analysis-Report"

# === Prepare the image ===
with open(IMAGE_PATH, "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode("utf-8")

# Extract filename without extension
image_name = os.path.splitext(os.path.basename(IMAGE_PATH))                        
# === Create report folder if it doesn't exist ===
if not os.path.exists(REPORT_FOLDER):
    os.makedirs(REPORT_FOLDER)

# === Set endpoint URL ===
url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={API_KEY}"
headers = {"Content-Type": "application/json"}

# === Medical expert prompt ===
prompt = (
    "You are a professional medical imaging diagnostic assistant with expertise equivalent "
    "to a radiologist with over 15 years of experience. Your task is to analyze the uploaded medical image, "
    "which is either an MRI or X-ray scan. Perform the following steps:\n\n"
    "1. Identify the type of scan (MRI or X-ray).\n"
    "2. Determine the anatomical region shown (e.g., brain, chest, spine).\n"
    "3. Analyze anatomical structures for abnormalities such as:\n"
    "   - Fractures, dislocations, deformities\n"
    "   - Tissue damage, swelling, inflammation\n"
    "   - Tumors, lesions, cysts\n"
    "   - Infection, fluid accumulation, abnormal densities\n"
    "   - Herniated discs, nerve compression (for spine)\n"
    "   - Lung opacity, effusion, cardiomegaly (for chest X-ray)\n"
    "4. Compare findings to normal anatomy.\n"
    "5. Evaluate severity and potential causes.\n"
    "6. Provide differential diagnosis.\n"
    "7. Recommend next steps (e.g., further imaging, specialist referral, urgency).\n\n"
    "Clearly explain reasoning and summarize key findings. Highlight any life-threatening concerns if present. "
    "Do not guess—indicate any limitations if image quality is insufficient. Begin your analysis now."
    "Finally, give the most important information and diagnosis and make an overall analysis."
)

# === Create payload ===
payload = {
    "contents": [
        {
            "parts": [
                {"text": prompt},
                {
                    "inline_data": {
                        "mime_type": "image/jpeg",
                        "data": encoded_image
                    }
                }
            ]
        }
    ]
}

# === Send request ===
response = requests.post(url, headers=headers, json=payload)

# === Handle response ===
if response.status_code == 200:
    result = response.json()
    output_text = result['candidates'][0]['content']['parts'][0]['text']

    print("\n🧠 Analysis Result:\n")
    print(output_text)

    # === Save results ===
    txt_path = os.path.join(REPORT_FOLDER, f"{image_name}.txt")
    json_path = os.path.join(REPORT_FOLDER, f"{image_name}.json")

    with open(txt_path, "w", encoding="utf-8") as txt_file:
        txt_file.write(output_text)

    with open(json_path, "w", encoding="utf-8") as json_file:
        json.dump(result, json_file, ensure_ascii=False, indent=2)

    print(f"\n✅ Report saved as:\n- {txt_path}\n- {json_path}")

else:
    print("❌ Error:", response.status_code)
    print(response.json())
