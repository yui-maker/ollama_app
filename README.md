# Ollama_GUI_app
Talk with Ollama using a small python app.
You will need to download and execute ollama on your PC.
Download Ollama from `ollama.com` and execute it.
If you visit `localhost:11434` you should see `Ollama is running`
This is it, if you run this app you should see a small tknitter window from where you can talk with Ollama. Depending on your CPU it might be too slow to answer questions. 
If you want to create an executable, here are the executables
`cd path/to/your/script`
`pip install pyinstaller`
`pyinstaller --onefile --windowed main.py`