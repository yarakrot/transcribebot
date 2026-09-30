import sys
import whisper

def main():
    if len(sys.argv) < 2:
        print("Использование: transcribe.bat путь\\к\\записи.mp4 [модель]")
        print("Модели: tiny, base, small, medium (по умолчанию), large-v3")
        sys.exit(1)

    audio_path = sys.argv[1]
    model_name = sys.argv[2] if len(sys.argv) > 2 else "medium"

    print(f"Загружаю модель '{model_name}'...")
    model = whisper.load_model(model_name)

    print(f"Транскрибирую: {audio_path}")
    result = model.transcribe(audio_path, verbose=False)

    out_path = audio_path.rsplit(".", 1)[0] + ".txt"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(result["text"].strip())

    srt_path = audio_path.rsplit(".", 1)[0] + ".srt"
    with open(srt_path, "w", encoding="utf-8") as f:
        for i, seg in enumerate(result["segments"], start=1):
            start = format_timestamp(seg["start"])
            end = format_timestamp(seg["end"])
            f.write(f"{i}\n{start} --> {end}\n{seg['text'].strip()}\n\n")

    print(f"Готово!\nТекст: {out_path}\nСубтитры: {srt_path}")

def format_timestamp(seconds: float) -> str:
    ms = int((seconds - int(seconds)) * 1000)
    s = int(seconds)
    h, s = divmod(s, 3600)
    m, s = divmod(s, 60)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"

if __name__ == "__main__":
    main()
