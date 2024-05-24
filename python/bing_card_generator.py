import random
import qrcode
from fpdf import FPDF

pdf = FPDF()


# bingo_rules = {
#     "A": 3,
#     "B": 3,
#     "C": 3,
# }

# Generate a bingo card
def generate_card(grid_size):
    card = [[0]*grid_size for i in range(grid_size)]
    used_numbers = set()

    for i in range(grid_size):
        for j in range(grid_size):
            while True:
                number = random.randint(1, 19)
                if number not in used_numbers:
                    card[i][j] = number
                    used_numbers.add(number)
                    break
    return card


# Generate QR code for each bingo card
def generate_qr_code(card, filename):
    data = ",".join([str(num) for row in card for num in row])
    img = qrcode.make(data)
    img.save(filename)

# Generate a PDF file with bingo cards and QR codes
def generate_pdf(cards):
    pdf.set_auto_page_break(auto=True, margin=15)
    

    # Print bingo cards to pdf
    for i, card in enumerate(cards):
        pdf.add_page()
        pdf.set_font("Arial", style="B", size=14)
        cell_size = 50

        # center the card on the page
        total_card_width = cell_size * 3
        x_start = (pdf.w - total_card_width) / 2
        pdf.set_x(x_start)

        # BINGO header
        pdf.set_font("Arial", style="B", size=72)
        pdf.cell(total_card_width, cell_size, "BINGO", border=1, align="C")
        pdf.ln(cell_size)
        pdf.set_x(x_start)  # Reset x position for the next row
        pdf.set_font("Arial", style="B", size=46)

        for row in card:
            for num in row:
                pdf.cell(cell_size, cell_size, str(num), border=1, align="C")
            pdf.ln(cell_size)
            pdf.set_x(x_start)

        # Generate QR code on the next page
        pdf.add_page()
        qr_filename = f"bingo_card_{i}.png"
        generate_qr_code(card, qr_filename)
        qr_size = 100
        pdf.image(qr_filename, x=(pdf.w - qr_size) / 2, y=(pdf.h - qr_size) / 2, w=qr_size, h=qr_size)    
        

    pdf.output("bingo_cards.pdf")
        

# Play bingo with a given number of cards, main function
def play_bingo(grid_size, num_cards):
    cards = [generate_card(grid_size) for i in range(num_cards)]
    for i, card in enumerate(cards):
        print(f"Bingo card {i + 1}:")
        for row in card:
            print(' '.join([str(n).rjust(2) for n in row]))
        print("\n")
        
    generate_pdf(cards)
        
# Play bingo with multiple cards
play_bingo(3, 5)



