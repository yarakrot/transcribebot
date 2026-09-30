# TranscribeBot — Local Audio and Video Transcription

A Windows application built with Python and OpenAI Whisper that turns audio and video recordings into text and subtitles. Includes a Tkinter desktop interface and a command-line tool.

## Features

- Batch processing of multiple files through the desktop interface.
- Support for tiny, base, small, medium, and large-v3 models.
- Automatic language detection, with Russian and English options in the interface.
- TXT, DOCX, and SRT export through the interface; TXT and SRT through the command line.
- Custom output directory and a processing log.
- Queue cancellation after the current file finishes.

Transcription runs locally. An internet connection is required to download model weights on first use; the application does not send recordings to a cloud API.

## Installation on Windows

Python 3.12 with Tkinter support and FFmpeg available in PATH are recommended.
Install FFmpeg with:

```powershell
winget install --id Gyan.FFmpeg --exact
```

After installation, open a new terminal and verify it with `ffmpeg -version`.

```powershell
git clone https://github.com/yarakrot/transcribebot.git
cd transcribebot
py -3.12 -m venv venv
.\venv\Scripts\python.exe -m pip install --upgrade pip
.\venv\Scripts\python.exe -m pip install -r requirements.txt
```

Whisper installs PyTorch as a dependency. Acceleration on a compatible NVIDIA GPU may require an appropriate PyTorch build: [PyTorch installation guide](https://pytorch.org/get-started/locally/).

## Desktop Interface

Double-click `whisper-ui.bat` or run:

```powershell
.\venv\Scripts\python.exe gui.py
```

The interface is currently in Russian. Add recordings, choose a model, language, and output formats, then click “Начать транскрибацию” (Start transcription). If no output directory is selected, results are saved next to the original recording. For an initial CPU run, try tiny or base; the default model is medium.

## Command Line

```powershell
.\transcribe.bat "C:\Recordings\meeting.mp4" base
```

The second argument selects the model; medium is used if omitted. The language is detected automatically. The tool creates `meeting.txt` and `meeting.srt` next to the recording.

## Limitations

- Processing speed depends on the model, recording length, and hardware; larger models require more memory.
- The progress bar tracks the number of processed files.
- Cancellation does not interrupt transcription of the current file.
- Output files with matching names are overwritten; use unique recording names when saving to a shared directory.
- Transcription quality depends on the recording; review names, numbers, and important wording manually.

## Project Structure

- `gui.py` — desktop interface, processing queue, and output export.
- `transcribe.py` — command-line transcription.
- `whisper-ui.bat`, `transcribe.bat` — Windows launchers.
- `requirements.txt` — direct dependencies.

The virtual environment, recordings, and transcription outputs are excluded from Git through `.gitignore`.

## License

MIT — see [LICENSE](LICENSE). Whisper, PyTorch, and other dependencies are distributed under their own licenses.
