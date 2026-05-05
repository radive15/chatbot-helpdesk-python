import ollama
import os
from dotenv import load_dotenv


# load config dari env
load_dotenv()

model = os.getenv("OLLAMA_MODEL", "llama3")

def test_connection() -> None:
    """Test apakah Ollama bisa diakses dan model bisa dipakai."""
    print(f"Mencoba koneksi ke Ollama dengan model: {model}")
    
    try:
        response = ollama.chat(
            model=model,
            messages=[
                {"role": "user", "content": "Jawab singkat: apa itu Python?"}
            ]
        )
        print("\nRespon dari Ollama:")
        print(response["message"]["content"])
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_connection()