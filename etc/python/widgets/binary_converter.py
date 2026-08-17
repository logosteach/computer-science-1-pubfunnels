"""
Binary ↔ Decimal Converter (Tkinter)
A student practice tool for converting positive integers to binary and binary to positive integers.
Includes step-by-step explanations and a visual place-value display.
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext


class BinaryConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Binary ↔ Decimal Converter")
        self.root.geometry("900x720")
        self.root.minsize(820, 650)
        self.root.configure(bg="#f1f5f9")

        # ---------- Styles ----------
        style = ttk.Style()
        style.theme_use("clam")

        style.configure("TFrame", background="#f1f5f9")
        style.configure("Card.TFrame", background="white", relief="solid", borderwidth=1)
        style.configure("Header.TLabel", background="#1e3a5f", foreground="white",
                        font=("Segoe UI", 16, "bold"))
        style.configure("SubHeader.TLabel", background="#1e3a5f", foreground="#dbeafe",
                        font=("Segoe UI", 10))
        style.configure("Title.TLabel", background="white", foreground="#1e3a5f",
                        font=("Segoe UI", 12, "bold"))
        style.configure("Normal.TLabel", background="white", foreground="#334155",
                        font=("Segoe UI", 10))
        style.configure("Blue.TButton", font=("Segoe UI", 10, "bold"))
        style.configure("Green.TButton", font=("Segoe UI", 10, "bold"))

        # ---------- Header ----------
        header = tk.Frame(root, bg="#1e3a5f", height=70)
        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(header, text="Binary ↔ Decimal Converter",
                 bg="#1e3a5f", fg="white",
                 font=("Segoe UI", 18, "bold")).pack(pady=(12, 0))
        tk.Label(header, text="Practice converting positive integers and see how the math works",
                 bg="#1e3a5f", fg="#bfdbfe",
                 font=("Segoe UI", 10)).pack()

        # ---------- Main container ----------
        main = ttk.Frame(root, padding=15)
        main.pack(fill="both", expand=True)

        # ===== Explanation Section =====
        exp_frame = ttk.LabelFrame(main, text="  How the Conversion Works  ", padding=12)
        exp_frame.pack(fill="x", pady=(0, 12))

        exp_text = (
            "Decimal → Binary:  Repeatedly divide the number by 2 and record the remainders.\n"
            "                   The remainders read from bottom to top form the binary number.\n"
            "                   Example: 13 → 1101₂\n\n"
            "Binary → Decimal:  Multiply each bit by its place value (powers of 2) and add the results.\n"
            "                   Place values from right to left: 1, 2, 4, 8, 16, 32, 64, 128…\n"
            "                   Example: 1101₂ = 8 + 4 + 0 + 1 = 13"
        )
        tk.Label(exp_frame, text=exp_text, justify="left",
                 bg="white", fg="#334155", font=("Segoe UI", 9),
                 anchor="w").pack(fill="x")

        # ===== Two Converter Panels =====
        panels = ttk.Frame(main)
        panels.pack(fill="both", expand=True, pady=(0, 12))

        # --- Left: Decimal → Binary ---
        left = ttk.LabelFrame(panels, text="  Decimal → Binary  ", padding=12)
        left.pack(side="left", fill="both", expand=True, padx=(0, 8))

        tk.Label(left, text="Enter a positive integer:",
                 bg="white", fg="#475569", font=("Segoe UI", 9)).pack(anchor="w")

        self.dec_entry = ttk.Entry(left, font=("Segoe UI", 12))
        self.dec_entry.pack(fill="x", pady=(4, 8))
        self.dec_entry.bind("<Return>", lambda e: self.convert_dec_to_bin())

        ttk.Button(left, text="Convert to Binary",
                   command=self.convert_dec_to_bin).pack(fill="x", pady=(0, 10))

        self.dec_result = scrolledtext.ScrolledText(left, height=12, font=("Consolas", 10),
                                                    wrap="word", state="disabled",
                                                    bg="#f8fafc", relief="flat")
        self.dec_result.pack(fill="both", expand=True)

        # --- Right: Binary → Decimal ---
        right = ttk.LabelFrame(panels, text="  Binary → Decimal  ", padding=12)
        right.pack(side="left", fill="both", expand=True, padx=(8, 0))

        tk.Label(right, text="Enter a binary number (0s and 1s only):",
                 bg="white", fg="#475569", font=("Segoe UI", 9)).pack(anchor="w")

        self.bin_entry = ttk.Entry(right, font=("Consolas", 12))
        self.bin_entry.pack(fill="x", pady=(4, 8))
        self.bin_entry.bind("<Return>", lambda e: self.convert_bin_to_dec())

        ttk.Button(right, text="Convert to Decimal",
                   command=self.convert_bin_to_dec).pack(fill="x", pady=(0, 10))

        self.bin_result = scrolledtext.ScrolledText(right, height=12, font=("Consolas", 10),
                                                    wrap="word", state="disabled",
                                                    bg="#f8fafc", relief="flat")
        self.bin_result.pack(fill="both", expand=True)

        # ===== Visual Place Value Section =====
        visual_frame = ttk.LabelFrame(main, text="  Visual Place Values  ", padding=10)
        visual_frame.pack(fill="x")

        tk.Label(visual_frame,
                 text="This chart updates when you convert a binary number. Each column is a power of 2.",
                 bg="white", fg="#64748b", font=("Segoe UI", 9)).pack(anchor="w", pady=(0, 8))

        self.place_frame = tk.Frame(visual_frame, bg="white")
        self.place_frame.pack(fill="x")

        self.show_placeholder()

        # Footer tip
        tk.Label(main, text="Tip: Try converting a number both ways to check your understanding.",
                 bg="#f1f5f9", fg="#64748b", font=("Segoe UI", 9)).pack(pady=(10, 0))

    # ------------------------------------------------------------------
    def show_placeholder(self):
        for widget in self.place_frame.winfo_children():
            widget.destroy()
        tk.Label(self.place_frame,
                 text="Convert a binary number to see the place values light up.",
                 bg="white", fg="#94a3b8", font=("Segoe UI", 10)).pack(pady=10)

    def update_place_values(self, details):
        for widget in self.place_frame.winfo_children():
            widget.destroy()

        for d in details:
            is_on = d["bit"] == 1
            bg = "#dbeafe" if is_on else "#f1f5f9"
            border = "#3b82f6" if is_on else "#e2e8f0"
            bit_color = "#1d4ed8" if is_on else "#94a3b8"

            cell = tk.Frame(self.place_frame, bg=bg, highlightbackground=border,
                            highlightthickness=2, padx=6, pady=6)
            cell.pack(side="left", padx=4)

            tk.Label(cell, text=f"2^{d['power']}", bg=bg, fg="#64748b",
                     font=("Segoe UI", 8)).pack()
            tk.Label(cell, text=str(d["place_value"]), bg=bg, fg="#475569",
                     font=("Segoe UI", 9, "bold")).pack()
            tk.Label(cell, text=str(d["bit"]), bg=bg, fg=bit_color,
                     font=("Consolas", 16, "bold")).pack()

    # ------------------------------------------------------------------
    def convert_dec_to_bin(self):
        raw = self.dec_entry.get().strip()
        self.dec_result.config(state="normal")
        self.dec_result.delete("1.0", tk.END)

        try:
            num = int(raw)
            if num < 0:
                raise ValueError
        except ValueError:
            self.dec_result.insert(tk.END, "Please enter a positive integer (0 or greater).")
            self.dec_result.config(state="disabled")
            return

        if num == 0:
            self.dec_result.insert(tk.END, "0₁₀ = 0₂\n")
            self.dec_result.config(state="disabled")
            return

        steps = []
        n = num
        binary = ""

        while n > 0:
            remainder = n % 2
            steps.append(f"{n} ÷ 2 = {n // 2}  remainder {remainder}")
            binary = str(remainder) + binary
            n = n // 2

        output = f"{num}₁₀ = {binary}₂\n\n"
        output += "Steps (remainders read from bottom to top):\n"
        output += "-" * 40 + "\n"
        for s in steps:
            output += s + "\n"

        self.dec_result.insert(tk.END, output)
        self.dec_result.config(state="disabled")

    # ------------------------------------------------------------------
    def convert_bin_to_dec(self):
        raw = self.bin_entry.get().strip()
        self.bin_result.config(state="normal")
        self.bin_result.delete("1.0", tk.END)

        if not raw or not all(c in "01" for c in raw):
            self.bin_result.insert(tk.END, "Please enter only 0s and 1s (example: 1101).")
            self.bin_result.config(state="disabled")
            self.show_placeholder()
            return

        details = []
        decimal = 0
        length = len(raw)

        for i, ch in enumerate(raw):
            bit = int(ch)
            power = length - 1 - i
            place_value = 2 ** power
            contribution = bit * place_value
            decimal += contribution
            details.append({
                "bit": bit,
                "power": power,
                "place_value": place_value,
                "contribution": contribution
            })

        # Build readable addition string
        parts = []
        for d in details:
            if d["bit"] == 1:
                parts.append(str(d["place_value"]))
            else:
                parts.append("0")

        addition = " + ".join(parts)

        output = f"{raw}₂ = {decimal}₁₀\n\n"
        output += f"{addition} = {decimal}\n\n"
        output += "Place value breakdown:\n"
        output += "-" * 40 + "\n"
        for d in details:
            output += f"  bit {d['bit']}  ×  2^{d['power']} ({d['place_value']})  =  {d['contribution']}\n"

        self.bin_result.insert(tk.END, output)
        self.bin_result.config(state="disabled")

        self.update_place_values(details)


# ------------------------------------------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = BinaryConverterApp(root)
    root.mainloop()
    
# Copyright 2026 LogosTeach - All Rights Reserved