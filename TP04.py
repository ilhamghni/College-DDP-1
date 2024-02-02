# TP-4 by Ilham Ghani Adrin Sapta
# NPM : 2306201792

import tkinter as tk
from tkinter import messagebox

class Canvas(tk.Frame):                         # create and define the canvas class
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.create_widgets()
        self.master.title("EAN-13 [by Ilham Ghani]")
        self.master.geometry("500x600")
        self.master.resizable(False, False)
        
    def create_widgets(self):                   # function to create widget
        self.save_msg = tk.Message(self, text="Save barcode to EPS file [eg: EAN13.eps]")
        self.save_msg.pack()
        self.save = tk.Entry(self)
        self.save.pack()
        self.code_msg = tk.Message(self, text="Enter Code [first 12 decimal digits]")
        self.code_msg.pack()
        self.code = tk.Entry(self)
        self.code.pack()
        self.display = tk.Canvas(self, bg="white", height=500, width=500)
        self.display.pack()
        self.master.bind("<Return>", self.generate_barcode)
    
    def generate_barcode(self, event=None):     # function to generate barcode 
        code = self.code.get()
        if len(code) != 12 or not code.isdigit():
            messagebox.showerror("Error", "Please enter a valid 12-digit code.")
            return
        save_filename = self.save.get()
        if not save_filename:
            messagebox.showerror("Error", "Please enter a filename for saving the barcode.")
            return
        try:
            self.display.delete("all")
            self.display.create_text(250, 50, fill='green', font=('Arial', 18, 'bold'), text='EAN-13 Barcode:')
            # Instantiate the EAN13_Specs class
            ean_specs = EAN13_Specs()
            # Calculate check digit
            checksum = ean_specs.checksum_digit(code)
            self.full_code = code + str(checksum)
            # Generate barcode bits
            bits = ean_specs.encoding(self.full_code)
            print(self.full_code)
            # Draw the barcode using bits and code attributes
            self.draw_barcode(bits, self.full_code)
            messagebox.showinfo("Success", f"Barcode saved as {save_filename}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def draw_barcode(self, bits, code):         # function to draw the barcode
        x_left = 100
        thickness = 3
        y_up = 230
        y_down = 70
        for i in range(95):                     # iterate each bits to draw rectangle
            if bits[i] == '1':
                if i <= 2 or (i >= 45 and i <=49) or (i >= 92 and i <= 95) :
                    self.display.create_rectangle((x_left + i * thickness, y_down, x_left + thickness + i * thickness, y_up + thickness * 3), fill='red', outline='red', width=0)
                else:
                    self.display.create_rectangle((x_left + i * thickness, y_down, x_left + thickness + i * thickness, y_up), fill='black', width=0)

        self.display.create_text(x_left-12, 245, font=('Arial', 18, 'bold'), text=code[0], fill="black")
        for i in range(13):
            if 1 <= i <= 6:
                self.display.create_text(x_left + i  * 21, 240, font=('Arial', 18, 'bold'), text=f'{code[i]}', fill="black")
            elif 7 <= i <= 12:
                self.display.create_text(x_left + 12 + i * 21, 240, font=('Arial', 18, 'bold'), text=f'{code[i]}', fill="black")
        self.display.create_text(250, 275, fill='orange', font=('Arial', 18, 'bold'), text=f'Check Digit: {code[-1]}')
        self.display.update()
        self.display.postscript(file=self.save.get(), colormode='color')

class EAN13_Specs:
    def encoding(self, code):                   # define the EAN-13 encoding
        code_left = code[1:7]
        code_right = code[7:13]                 # Split the code input into left and right
        encoding_L = {
            '0': '0001101', '1': '0011001', '2': '0010011', '3': '0111101', '4': '0100011', 
            '5': '0110001', '6': '0101111', '7': '0111011', '8': '0110111', '9': '0001011'
        }
        encoding_G = {
            '0': '0100111', '1': '0110011', '2': '0011011', '3': '0100001', '4': '0011101', 
            '5': '0111001', '6': '0000101', '7': '0010001', '8': '0001001', '9': '0010111'
        }
        encoding_R = {
            '0': '1110010', '1': '1100110', '2': '1101100', '3': '1000010', '4': '1011100', 
            '5': '1001110', '6': '1010000', '7': '1000100', '8': '1001000', '9': '1110100'
        }
        Structure = {
            '0':'LLLLLL', '1':'LLGLGG', '2':'LLGGLG', '3':'LLGGGL', '4':'LGLLGG', 
            '5':'LGGLLG', '6':'LGGGLL', '7':'LGLGLG', '8':'LGLGGL', '9':'LGGLGL'
        }
        bits = '101'                                                # add the Start guard
        structure_bits = Structure[code[0]]
        for i in range(len(code_left)):
            if structure_bits[i] == "L":
                bits += encoding_L[code_left[i]]
            elif structure_bits[i] == "G":
                bits += encoding_G[code_left[i]]
        bits += '01010'                                             # add the Middle guard
        for i in range(len(code_right)):
            bits += encoding_R[code_right[i]]                       # Right side
        bits += '101'                                               # add the End guard
        return bits

    def checksum_digit(self, digit):                                # function to find the check digit
        sum_value = sum(int(i) for i in digit[0::2]) + sum(int(i) * 3 for i in digit[1::2])
        return (10 - (sum_value % 10)) if sum_value % 10 != 0 else 0

def main():
    myapp = Canvas()
    myapp.mainloop()                                                # main function to run the program

if __name__ == "__main__":
    main()
