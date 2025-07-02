# 📋 Dokumentasi Personal AI Agent

Dokumentasi lengkap untuk Personal AI Agent yang dibangun menggunakan LangChain dan Google Gemini API.

## 📁 Struktur Dokumentasi

- [🏗️ Arsitektur & Alur Kerja](architecture.md) - Komponen sistem dan data flow
- [🧠 Pendekatan Memory](memory-approach.md) - Episodic memory implementation  
- [🎯 Strategy & Implementation](strategy.md) - Tool-based approach dan ReAct pattern
- [📊 Hasil & Refleksi](results-reflection.md) - Kendala, solusi, dan lessons learned
- [🚀 Setup & Installation](setup.md) - Panduan instalasi dan konfigurasi

## 🚀 Quick Start

1. **Clone repository**
   ```bash
   git clone <repository-url>
   cd personal-agent-simple
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup environment**
   ```bash
   cp .env.example .env
   # Edit .env file dengan Gemini API key Anda
   ```

4. **Run agent**
   ```bash
   python agent.py
   ```

## 🎯 Features

- ✅ **Persistent Memory**: SQLite-based conversation storage
- ✅ **Tool Integration**: Extensible tool system
- ✅ **Gemini API**: Google's latest LLM integration
- ✅ **Environment Management**: Secure API key handling
- ✅ **Error Handling**: Robust error recovery

## 🛠️ Core Components

- **LLM**: Google Gemini 1.5 Flash
- **Agent Type**: Conversational ReAct Description  
- **Memory**: Episodic memory dengan SQLite
- **Tools**: Time, Greeting, dan extensible tool system
- **Framework**: LangChain

## 🔗 Useful Links

- [Google AI Studio](https://makersuite.google.com/app/apikey) - Get Gemini API Key
- [LangChain Documentation](https://python.langchain.com/)
- [LangChain Agents Guide](https://python.langchain.com/docs/modules/agents/)
- [SQLite Documentation](https://www.sqlite.org/docs.html)

## 📞 Support

Untuk pertanyaan dan issues:
1. Baca dokumentasi lengkap di folder `docs/`
2. Check common issues di [results-reflection.md](results-reflection.md)
3. Lihat setup guide di [setup.md](setup.md)

---

**Last Updated**: July 1, 2025  
**Version**: 1.0.0  
**Framework**: LangChain + Google Gemini API
