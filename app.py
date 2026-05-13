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
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "system", "content": SYSTEM_PROMPT}
        ]


def clear_chat() -> None:
    """Reset percakapan — hapus semua kecuali system prompt."""
    # Kita tidak hapus key-nya, tapi timpa isinya dengan list baru
    # Ini lebih aman dari del st.session_state.messages karena tidak trigger error
    st.session_state.messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]


def count_messages() -> int:
    """Hitung jumlah pesan user + bot (exclude system prompt)."""
    return len([m for m in st.session_state.messages if m["role"] != "system"])


def render_sidebar() -> None:
    """Render panel sidebar kiri dengan info dan tombol clear."""
    with st.sidebar:
        st.header("Info")

        # Tampilkan model yang sedang dipakai
        st.markdown(f"**Model:** `{model}`")

        # Hitung jumlah pesan dalam sesi ini
        msg_count = count_messages()
        st.markdown(f"**Pesan dalam sesi:** {msg_count}")

        st.divider()

        # Tombol clear chat — st.button() return True saat diklik
        if st.button("Hapus Percakapan", use_container_width=True, type="secondary"):
            clear_chat()
            # st.rerun() paksa Streamlit render ulang halaman setelah state berubah
            st.rerun()

        st.divider()

        # Info tambahan di bawah sidebar
        st.caption("HelpBot berjalan 100% lokal.")
        st.caption("Data tidak keluar dari komputer kamu.")


def display_chat_history() -> None:
    """Tampilkan semua riwayat chat di layar."""
    for msg in st.session_state.messages:
        if msg["role"] == "system":
            continue
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])


def handle_user_input(user_input: str) -> None:
    """Proses input user — kirim ke Ollama dan tampilkan respons."""
    with st.chat_message("user"):
        st.markdown(user_input)

    st.session_state.messages.append({"role": "user", "content": user_input})

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

    initialize_session()

    # Render sidebar — harus dipanggil SEBELUM chat history
    # supaya sidebar muncul di semua state halaman
    render_sidebar()

    display_chat_history()

    user_input = st.chat_input("Ketik pertanyaan IT kamu di sini...")
    if user_input:
        handle_user_input(user_input)


if __name__ == "__main__":
    main()
