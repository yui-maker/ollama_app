from tkinter import Text, ttk
from tkinter.constants import WORD, END

class ScrollableText(ttk.Frame):
    def __init__(self, parent, height: int, width: int, **kwargs):
        super().__init__(parent)
        
        self.text = Text(self, wrap=WORD, width=width, height=height, **kwargs)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.text.yview)
        self.text.configure(yscrollcommand=self.scrollbar.set)
        
        self.text.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

    def get_text(self) -> str:
        return self.text.get("1.0", END).strip()

    def set_text(self, text: str) -> None:
        self.text.delete("1.0", END)
        self.text.insert(END, text)

    def set_state(self, state: str) -> None:
        self.text.configure(state=state)