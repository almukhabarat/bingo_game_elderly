import random
import qrcode
from fpdf import FPDF

class bingo_card_generator:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.card = self.generate_card()

    def generate_card(self):
        card = [[0]*self.grid_size for _ in range(self.grid_size)]
        used_numbers = set()

        for i in range(self.grid_size):
            for j in range(self.grid_size):
                while True:
                    number = random.randint(1, 19)
                    if number not in used_numbers:
                        card[i][j] = number
                        used_numbers.add(number)
                        break
        return card
    

class qr_code_generator:
    def generate_qr_code(self, card, filename):
        data = ",".join([str(num) for row in card for num in row])
        img = qrcode.make(data)
        img.save(filename)        
    

class pdf_generator:
    def __init__(self):
        self.pdf = FPDF()

    def generate_pdf(self, cards):
        qr =   qr_code_generator()
        self.pdf.set_auto_page_break(auto=True, margin=15)

            # Print bingo cards to pdf
        for i, card in enumerate(cards):
            self.pdf.add_page()
            self.pdf.set_font("Arial", style="B", size=14)
            cell_size = 50

            # center the card on the page
            total_card_width = cell_size * 3
            x_start = (self.pdf.w - total_card_width) / 2
            self.pdf.set_x(x_start)

            # BINGO header
            self.pdf.set_font("Arial", style="B", size=72)
            self.pdf.cell(total_card_width, cell_size, "BINGO", border=1, align="C")
            self.pdf.ln(cell_size)
            self.pdf.set_x(x_start)  # Reset x position for the next row
            self.pdf.set_font("Arial", style="B", size=46)

            for row in card:
                for num in row:
                    self.pdf.cell(cell_size, cell_size, str(num), border=1, align="C")
                self.pdf.ln(cell_size)
                self.pdf.set_x(x_start)

            # Generate QR code on the next page
            self.pdf.add_page()
            qr_filename = f"bingo_card_{i}.png"
            qr.generate_qr_code(card, qr_filename)
            qr_size = 100
            self.pdf.image(qr_filename, x=(self.pdf.w - qr_size) / 2, y=(self.pdf.h - qr_size) / 2, w=qr_size, h=qr_size)    
            

        self.pdf.output("bingo_cards.pdf")
    
class bingo_game:
    def __init__(self, grid_size, num_cards):
        self.grid_size = grid_size
        self.num_cards = num_cards
        self.cards = [bingo_card_generator(grid_size) for i in range(num_cards)]

    def play_bingo(self):
        for i, card in enumerate(self.cards):
            print(f"Bingo card {i + 1}:")
            for row in card.card:
                print(' '.join([str(n).rjust(2) for n in row]))  # Corrected printing loop
            print("\n")

        pdf_gen = pdf_generator()  
        pdf_gen.generate_pdf([card.card for card in self.cards])
        
if __name__ == "__main__":
    game = bingo_game(grid_size=3, num_cards=10)
    game.play_bingo()
