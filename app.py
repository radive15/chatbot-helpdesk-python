import streamlit as st
import ollama
import os
from dotenv import load_dotenv

load_dotenv()

model = os.getenv("OLLAMA_MODEL", "llama3")

SYSTEM_PROMPT = """PENTING: Selalu jawab dalam Bahasa Indonesia. Jangan gunakan Bahasa Inggris.

Kamu adalah IT Helpdesk Assistant untuk perusahaan internal bernama "HelpBot".

Tugasmu:
- Membantu karyawan dengan pertanyaan seputar IT: komputer, jaringan, software, akun, printer, dsb
- Menjawab dalam Bahasa Indonesia yang ramah dan mudah dipahami

Batasan:
- Hanya jawab pertanyaan yang berkaitan dengan IT
- Jika ditanya di luar topik IT, tolak dengan sopan dan arahkan ke topik IT
- Jangan pura-pura bisa melakukan hal yang hanya bisa dilakukan manusia

INGAT: Semua respons harus dalam Bahasa Indonesia."""


def initialize_session() -> None:
    """Inisialisasi session state saat pertama kali app dibuka."""
    # st.session_state adalah cara Streamlit menyimpan data antar interaksi user
    # Mirip seperti variabel global tapi per-user, per-session
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "system", "content": SYSTEM_PROMPT}
        ]


def display_chat_history() -> None:
    """Tampilkan semua riwayat chat di layar."""
    for msg in st.session_state.messages:
        # System prompt tidak ditampilkan ke user
        if msg["role"] == "system":
            continue
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])


def handle_user_input(user_input: str) -> None:
    """Proses input user — kirim ke Ollama dan tampilkan respons."""
    # Tampilkan pesan user langsung
    with st.chat_message("user"):
        st.markdown(user_input)

    st.session_state.messages.append({"role": "user", "content": user_input})

    # Tampilkan respons bot dengan efek streaming (karakter per karakter)
    with st.chat_message("assistant"):
        with st.spinner("HelpBot sedang mengetik..."):
            try:
                response = ollama.chat(
                    model=model,
                    messages=st.session_state.messages
                )
                reply = response["message"]["content"]
                st.markdown(reply)
                st.session_state.messages.append(
                    {"role": "assistant", "content": reply}
                )
            except ConnectionError:
                st.error("Tidak bisa terhubung ke Ollama. Pastikan Ollama sedang berjalan.")


def main() -> None:
    """Entry point aplikasi Streamlit."""
    st.set_page_config(page_title="HelpBot — IT Helpdesk", page_icon="💻")
    st.title("💻 HelpBot — IT Helpdesk Assistant")
    st.caption(f"Powered by Ollama + {model} | Berjalan 100% lokal")

    initialize_session()
    display_chat_history()

    # Input box di bagian bawah halaman
    user_input = st.chat_input("Ketik pertanyaan IT kamu di sini...")
    if user_input:
        handle_user_input(user_input)


if __name__ == "__main__":
    main()
