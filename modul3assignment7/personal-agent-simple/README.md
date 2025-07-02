# 🧠 My Simple AI Agent

Contoh proyek Python menggunakan LangChain untuk membangun **personal assistant AI agent** super sederhana.

## ✅ Fitur
- Prompt + Memory (SQLite)
- Tool / Function Calling
- Model: Gemini (gratis)
- Agent Loop sederhana: **observe → decide → act**

---

## 📜 Arsitektur & Alur Kerja Agent

**Alur Kerja (Agent Loop):**

**Komponen:**
- Prompt: dikontrol LangChain agent dengan template bawaan.
- Memory: ConversationBufferMemory dengan SQLite untuk **Long Term Memory**.
- Tools: function yang bisa dipanggil agent (contoh: get_current_time, say_hello).

---

## 🗂️ Pendekatan Memory
- **Type:** ConversationBufferMemory
- **Storage:** SQLite (`memory.db`) untuk persistensi
- **Style:** Episodic (menyimpan percakapan dalam urutan, cocok untuk chatting)

---

## 💡 RAG / Prompt Strategy
- **Prompt Strategy:** React-style agent (Conversational React)
  - LLM didorong untuk berpikir langkah demi langkah
  - Mencoba memutuskan: "Apakah aku perlu pakai Tool? Atau cukup jawab langsung?"
- **Retrieval Augmented Generation (RAG):** Tidak diimplementasikan di versi ini (sengaja supaya sesederhana mungkin).

---

## 🛠️ Tools / Function Calling
- Contoh Tool:
  - `get_current_time`: mengembalikan waktu sekarang
  - `say_hello`: menyapa dengan nama

LangChain secara otomatis mem-parsing deskripsi untuk memutuskan kapan memanggil Tool.

---

## 🗺️ Hasil & Refleksi
**Kendala:**
- Gemini gratis-tier kadang membatasi jumlah panggilan.
- LangChain AgentType React perlu konteks yang bersih; memory bisa menumpuk.

**Solusi:**
- Gunakan SQLite agar memory persist tapi bisa direset (hapus memory.db).
- Bisa tambah Tool lain sesuai use case.

---

## 🧑‍💻 Cara Menjalankan

### 1️⃣ Install dependencies:
```bash
pip install -r requirements.txt
```

### 2️⃣ Setup Gemini API Key:
Dapatkan API key dari: https://makersuite.google.com/app/apikey

**Buat file `.env` di root project:**
```bash
# Copy dari .env.example
cp .env.example .env
```

**Edit file `.env` dan masukkan API key kamu:**
```env
GOOGLE_API_KEY=your_actual_api_key_here
```

### 3️⃣ Jalankan agent:
```bash
python agent.py
```
