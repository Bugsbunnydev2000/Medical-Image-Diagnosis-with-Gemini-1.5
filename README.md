# Medical-Image-Diagnosis-with-Gemini-1.5
Medical Image Diagnosis with Gemini 1.5
```markdown
# 🧠 Medical Image Diagnosis with Gemini 1.5

A professional tool for **analyzing MRI and X-ray images** using the **Gemini 1.5 Flash API** by Google.  
This project simulates an expert radiologist providing detailed and medically accurate reports.

---

## 📦 Features

- ✅ Detects **MRI vs. X-ray**
- 🧠 Identifies anatomical region (e.g., brain, spine, chest)
- 🔬 Highlights abnormalities (tumors, fractures, infections, etc.)
- 🏥 Suggests diagnosis and next steps
- 💾 Exports analysis in `.txt` and `.json` formats

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.8+
- A valid Google Cloud API key for [Gemini 1.5 Flash](https://console.cloud.google.com/apis/credentials)
- The image you want to analyze in `.jpg` format

### 📥 Installation

```bash
pip install requests
```

---

## ⚙️ Usage

1. **Paste your API key** into the code:

```python
API_KEY = "YOUR_API_KEY"
```

2. **Run the script** and enter the full path to your MRI or X-ray image:

```bash
python main-terminal.py
```

3. After processing, reports are saved to:

```
/Analysis-Report/
├── your-image-name.txt   📝 Human-readable summary
└── your-image-name.json  🧾 Full raw API response
```

---

## 🧠 How It Works

The script sends your image to **Gemini 1.5 Flash** using this prompt:

> You are a professional medical imaging diagnostic assistant...  
> [💬 Full diagnostic instructions as a prompt in the script]

Gemini then returns a comprehensive medical analysis based on image content.

---

## 📁 Output Example
in Analysis-Report-sample folder
```
🧠 Analysis Result:

- Scan Type: MRI
- Region: Brain
- Findings: No tumor or hemorrhage, mild cortical atrophy.
- Recommendation: Routine monitoring advised.
```

---

## 🔐 About the API Key

Get your Gemini API key from [Google Cloud Console](https://console.cloud.google.com/apis/credentials)  
Make sure the `Generative Language API` is **enabled** in your project.

