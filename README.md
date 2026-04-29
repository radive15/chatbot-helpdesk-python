# Chatbot IT Helpdesk (Local AI)

Chatbot internal untuk IT Helpdesk — berjalan **100% lokal** menggunakan Ollama. Data tidak keluar ke internet, gratis, dan full open source.

---

## Stack

| Komponen | Teknologi | Keterangan |
|---|---|---|
| LLM Runtime | Ollama | Jalankan model AI secara lokal |
| Language | Python 3 | Backend dan logika chatbot |
| Model | llama3 / mistral | Open source LLM |
| Prototype UI | Streamlit | Web UI cepat untuk testing |
| Production Web | FastAPI | REST API + web app final |
| Config | python-dotenv | Manajemen environment variable |

---

## Roadmap

### Stage 1 — Setup ⬜ IN PROGRESS
- [ ] Install Ollama
- [ ] Pull model (llama3)
- [ ] Buat virtual environment Python
- [ ] Install dependencies awal
- [ ] Test koneksi ke Ollama dari Python

### Stage 2 — Basic Chatbot ⬜ BELUM MULAI
- [ ] Panggil Ollama API dari Python
- [ ] Input dari terminal, output ke terminal
- [ ] Test tanya jawab sederhana

### Stage 3 — Conversation History ⬜ BELUM MULAI
- [ ] Simpan riwayat percakapan dalam sesi
- [ ] Chatbot bisa ingat konteks pertanyaan sebelumnya

### Stage 4 — IT Helpdesk Persona ⬜ BELUM MULAI
- [ ] System prompt sebagai IT Helpdesk assistant
- [ ] Knowledge base sederhana (FAQ, SOP)
- [ ] Kategorisasi masalah: Network, Hardware, Software, Akun

### Stage 5 — Streamlit UI ⬜ BELUM MULAI
- [ ] Web UI dengan Streamlit
- [ ] Chat interface (bubble chat)
- [ ] Prototype untuk validasi fitur

### Stage 6 — FastAPI ⬜ BELUM MULAI
- [ ] REST API endpoint untuk chat
- [ ] Web UI terintegrasi
- [ ] Dokumentasi API otomatis (Swagger)
- [ ] Siap deploy ke server internal

---

## Cara Menjalankan

> Akan diisi seiring progress stage

---

## Struktur Folder

> Akan diisi seiring progress stage

---

## Catatan

- Project ini untuk keperluan belajar Python sekaligus membangun tools internal
- Semua model berjalan lokal — tidak ada data yang dikirim ke cloud
