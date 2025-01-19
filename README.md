# Ollama GUI App
Interact with Ollama using a simple Python app.

**Prerequisites:**

1. Download and execute Ollama on your PC from [ollama.com](http://ollama.com).
2. Visit `localhost:11434` to verify that Ollama is running.

**App Usage:**

This app will display a small Tkinter window where you can interact with Ollama. Please note that the app's performance may be slow on lower-end CPUs.

**Creating an Executable:**

To create a standalone executable, follow these steps:

1. Navigate to the project directory (`cd path/to/your/script`).
2. Install PyInstaller using pip: `pip install pyinstaller`.
3. Run PyInstaller with the following command: `pyinstaller --onefile --windowed main.py`

This will generate an executable file in a `dist` directory within your project folder.