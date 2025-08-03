import tkinter as tk
from tkinter import scrolledtext

class MiniMessenger:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini Messenger")

        # Message display area
        self.chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=15, state='disabled')
        self.chat_area.pack(padx=10, pady=10)

        # Input field
        self.message_entry = tk.Entry(root, width=30)
        self.message_entry.pack(side=tk.LEFT, padx=(10, 0), pady=10)
        self.message_entry.bind("<Return>", self.send_message)

        # Send button
        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.LEFT, padx=10, pady=10)

    def send_message(self, event=None):
        message = self.message_entry.get().strip()
        if message:
            self.chat_area['state'] = 'normal'
            self.chat_area.insert(tk.END, f"You: {message}\n")
            self.chat_area['state'] = 'disabled'
            self.chat_area.see(tk.END)
            self.message_entry.delete(0, tk.END)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = MiniMessenger(root)
    root.mainloop()
