import tkinter as tk
import random

class BlockApp:
    def __init__(self, master):
        self.master = master
        master.title("Blocks Randomizer")

        self.block_names_label = tk.Label(master, text="Block names (comma-separated):")
        self.block_names_label.grid(row=0, column=0, sticky=tk.W)

        self.block_names_entry = tk.Entry(master)
        self.block_names_entry.grid(row=0, column=1)

        self.timeout_label = tk.Label(master, text="Block change interval (seconds):")
        self.timeout_label.grid(row=1, column=0, sticky=tk.W)

        self.timeout_entry = tk.Entry(master)
        self.timeout_entry.grid(row=1, column=1)

        self.start_stop_button = tk.Button(master, text="Start", command=self.start_stop)
        self.start_stop_button.grid(row=2, columnspan=2)

        self.output_frame = tk.Frame(master)
        self.output_frame.grid(row=3, columnspan=2, sticky="nsew")
        self.output_frame.grid_propagate(False)

        self.output_label = tk.Label(self.output_frame, text="##", font=("Helvetica", 24))
        self.output_label.pack(expand=True)

        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(1, weight=1)
        master.grid_rowconfigure(3, weight=1)

        self.block_names = []
        self.timeout = 0
        self.running = False

        master.bind("<Configure>", self.on_window_resize)

    def start_stop(self):
        if not self.running:
            block_names = self.block_names_entry.get().split(',')
            self.block_names = [name.strip() for name in block_names]
            self.timeout = int(self.timeout_entry.get())
            self.running = True
            self.start_stop_button.config(text="Stop")
            self.change_block()
        else:
            self.running = False
            self.start_stop_button.config(text="Start")

    def change_block(self, prev_block=None):
        if self.running:
            block = random.choice(self.block_names)
            while block == prev_block:
                block = random.choice(self.block_names)
            self.output_label.config(text=block)
            self.master.after(self.timeout * 1000, self.change_block, block)


    def on_window_resize(self, event):
        height = self.master.winfo_height()
        font_size = max(int(height / 2), 20)  # Adjust the divisor for desired font scaling
        self.output_label.config(font=("Helvetica", font_size))

def main():
    root = tk.Tk()
    app = BlockApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
