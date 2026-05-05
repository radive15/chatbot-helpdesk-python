import ollama
import os
from dotenv import load_dotenv

load_dotenv()

model = os.getenv("OLLAMA_MODEL", "llama3")

# System prompt — instruksi yang membentuk "kepribadian" dan batasan chatbot
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


def chat() -> None:
    """Loop utama chatbot dengan persona IT Helpdesk."""
    # System prompt selalu jadi elemen pertama di messages
    messages: list[dict] = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

    print("=" * 50)
    print("HelpBot — IT Helpdesk Assistant")
    print("Ketik 'exit' untuk keluar.")
    print("=" * 50)
    print()

    while True:
        user_input = input("Kamu: ").strip()

        if user_input.lower() == "exit":
            print("HelpBot: Terima kasih! Hubungi tim IT jika butuh bantuan lebih lanjut.")
            break

        if not user_input:
            continue

        messages.append({"role": "user", "content": user_input})

        try:
            response = ollama.chat(model=model, messages=messages)
            reply = response["message"]["content"]
            messages.append({"role": "assistant", "content": reply})
            print(f"\nHelpBot: {reply}\n")

        except ConnectionError:
            print("HelpBot: Koneksi ke server gagal. Pastikan Ollama sedang berjalan.")
        except KeyError:
            print("HelpBot: Format respons tidak dikenali.")


if __name__ == "__main__":
    chat()
