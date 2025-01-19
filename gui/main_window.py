from tkinter import Tk, ttk
from tkinter.constants import BOTH, W, E
from typing import Callable
from .widgets import ScrollableText
from config import Config
from ollama_client import OllamaClient, OllamaError

class MainWindow:
    def __init__(self):
        self.root = Tk()
        self.root.title("Ollama with GUI")
        self.root.geometry(f"{Config.WINDOW_WIDTH}x{Config.WINDOW_HEIGHT}")
        
        self.ollama_client = OllamaClient(Config.MODEL)
        self.setup_ui()

    def setup_ui(self) -> None:
        """Set up the main UI components."""
        self.create_question_frame()
        self.create_answer_frame()

    def create_question_frame(self) -> None:
        """Create the question input section."""
        self.question_frame = ttk.LabelFrame(self.root, text="Questions", padding=(10, 10))
        self.question_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

        question_label = ttk.Label(self.question_frame, text="Enter your question:")
        question_label.pack(anchor=W, pady=5)

        self.question_text = ScrollableText(self.question_frame, height=4, width=50)
        self.question_text.pack(fill=BOTH, expand=True, pady=5)
        self.question_text.text.bind("<Return>", self.handle_keypress)

        self.status_label = ttk.Label(self.question_frame, text="")
        self.status_label.pack(anchor=W, pady=5)

        remove_all_button = ttk.Button(
            self.question_frame,
            text="Remove All",
            command=self.remove_all
        )
        remove_all_button.pack(anchor=E, pady=5)

    def create_answer_frame(self) -> None:
        """Create the answer display section."""
        answer_frame = ttk.LabelFrame(self.root, text="Answer", padding=(10, 10))
        answer_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

        self.answer_text = ScrollableText(answer_frame, height=100, width=70)
        self.answer_text.pack(fill=BOTH, expand=True)
        self.answer_text.set_text(Config.DEFAULT_ANSWER_TEXT)
        self.answer_text.set_state('disabled')

    def handle_keypress(self, event) -> str:
        """Handle keyboard events."""
        if event.state & 0x1:  # Check if Shift is pressed
            return
        self.display_answer()
        return 'break'

    def display_answer(self) -> None:
        """Process the question and display the answer."""
        self.question_text.text['state'] = 'disabled'
        self.question_text.text['bg'] = '#F0F0F0'
        self.status_label.config(text="Looking for an answer...")
        self.root.update()

        question = self.question_text.get_text()
        if question:
            try:
                answer = self.ollama_client.send_message(question)
                self.answer_text.set_state('normal')
                self.answer_text.set_text(answer)
                self.answer_text.set_state('disabled')
                self.status_label.config(text="Answered")
            except OllamaError as e:
                self.answer_text.set_state('normal')
                self.answer_text.set_text(f"Error: {str(e)}")
                self.answer_text.set_state('disabled')
                self.status_label.config(text="Error")
        else:
            self.answer_text.set_state('normal')
            self.answer_text.set_text("Please enter a question.")
            self.answer_text.set_state('disabled')
            self.status_label.config(text="")

        self.question_text.text['state'] = 'normal'
        self.question_text.text['bg'] = 'white'
        self.root.update()

    def remove_all(self) -> None:
        """Clear all content and conversation history."""
        self.ollama_client.clear_history()
        self.question_text.set_text("")
        self.answer_text.set_state('normal')
        self.answer_text.set_text(Config.DEFAULT_ANSWER_TEXT)
        self.answer_text.set_state('disabled')
        self.status_label.config(text="")

    def run(self) -> None:
        """Start the application."""
        self.root.mainloop()