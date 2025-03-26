# voice_translator_ultimate_plus
# 🎙️ Voice Translator Ultimate Plus

> Real-time offline voice translator with GUI, speech recognition, translation, and TTS.  
> Powered by Whisper + HuggingFace + Coqui + PyQt5 — runs 100% offline once models are downloaded.

---

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/status-Awesome-brightgreen)

## 🚀 Features

- 🎤 Real-time speech recognition (`faster-whisper`)
- 🌍 Automatic language detection + switching (`lingua`)
- 🔄 Translation using Hugging Face Transformers
- 🗣️ Text-to-speech with Coqui TTS
- 🧠 Voice commands: "translate to French", "mute", "clear", etc.
- 💬 PyQt5 GUI with transcription display
- 📦 Fully offline — no internet required after setup
- 🪟 Optional overlay / subtitle display
- 📜 Translation log saved in `logs/history.json`
- 🛠️ Packaged with PyInstaller `.spec` for `.exe` generation

---

## 📦 Requirements

```bash
pip install -r requirements.txt

You'll need:

Python 3.8+

Windows or Linux

FFMPEG (for Coqui TTS)

Whisper and Coqui models (downloaded automatically or via GUI)
