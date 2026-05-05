import ollama
import os
from dotenv import load_dotenv

load_dotenv()

model = os.getenv("OLLAMA_MODEL", "llama3")


def chat() -> None:
    """Loop utama chatbot — terima input user, kirim ke Ollama, tampilkan respons."""
    # messages menyimpan seluruh riwayat percakapan dalam satu sesi
    # Ini yang membuat model "ingat" konteks dari pertanyaan sebelumnya
    messages: list[dict] = []

    print(f"Chatbot aktif (model: {model}). Ketik 'exit' untuk keluar.\n")

    while True:
        user_input = input("Kamu: ").strip()

        if user_input.lower() == "exit":
            print("Sampai jumpa!")
            break

        if not user_input:
            continue

        # Tambahkan pesan user ke riwayat
        messages.append({"role": "user", "content": user_input})

        try:
            response = ollama.chat(model=model, messages=messages)
            reply = response["message"]["content"]

            # Tambahkan balasan model ke riwayat supaya konteks terjaga
            messages.append({"role": "assistant", "content": reply})

            print(f"\nBot: {reply}\n")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    chat()
