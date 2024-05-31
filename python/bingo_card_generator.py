import random
import qrcode
from fpdf import FPDF
import mysql.connector
import os

class connect_db:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

        # Connect to the database
        try:
            self.mydb = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.mydb.cursor()
            print("Database connection established")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.mydb = None
            self.cursor = None

    def __del__(self):
        if self.cursor:
            self.cursor.close()
        if self.mydb:
            self.mydb.close()
        print("Database connection closed")

    # run the queries to get the last_id and upload the bingocards
    def execute_query(self, query, values=None):
        try:
            if values:
                self.cursor.execute(query, values)
            else: 
                self.cursor.execute(query)
            self.mydb.commit()
            print("Query succesful")
        except mysql.connector.Error as err:
            print(f"Error: {err}")


# get last_id from the database
def fetch_data_from_db(db_connection, query):
    if not db_connection.cursor:
        print("No database connection")
        return None
    try:
        db_connection.cursor.execute(query)
        result = db_connection.cursor.fetchall()
        return result
    except mysql.connector.Error as err:
        print(f"Error executing query: {err}")
        return None

class bingo_card_generator:
    def __init__(self, grid_size, card_id):
        self.grid_size = grid_size
        self.card_id = card_id
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
    def generate_qr_code(self, card_id, filename):
        data = str(card_id)  # Use the card ID as the data for the QR code
        img = qrcode.make(data)
        img.save(filename)        
        return img

class pdf_generator:
    def __init__(self):
        self.pdf = FPDF()

    # layout the pdf
    def generate_pdf(self, cards):
        qr = qr_code_generator()
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

            for row in card.card:
                for num in row:
                    self.pdf.cell(cell_size, cell_size, str(num), border=1, align="C")
                self.pdf.ln(cell_size)
                self.pdf.set_x(x_start)

            # Generate QR code on the next page
            self.pdf.add_page()
            qr_filename = f"bingo_card_{i}.png"
            qr.generate_qr_code(card.card_id, qr_filename)  # Pass card ID to generate QR code
            qr_size = 150
            self.pdf.image(qr_filename, x=(self.pdf.w - qr_size) / 2, y=(self.pdf.h - qr_size) / 2, w=qr_size, h=qr_size)    

            os.remove(qr_filename)            

        self.pdf.output("bingo_cards.pdf")

# main class to run everything
class bingo_game:
    def __init__(self, grid_size, num_cards, last_id, db_connection):
        self.grid_size = grid_size
        self.num_cards = num_cards
        self.last_id = last_id
        self.db_connection = db_connection
        self.cards = [bingo_card_generator(grid_size, last_id + i + 1) for i in range(num_cards)]

    def play_bingo(self):
        for card in self.cards:
            card_data = ','.join(str(num) for row in card.card for num in row)
            self.insert_card_data(card.card_id, card_data)

        pdf_gen = pdf_generator()  
        pdf_gen.generate_pdf([card for card in self.cards])

    # insert data into the database   
    def insert_card_data(self, card_id, card_data):
        query = "INSERT INTO BingoKaart (bingoKaartId, getal) VALUES (%s, %s)"
        for num in card_data:
            values = (card_id, num)
            self.db_connection.execute_query(query, values)

if __name__ == "__main__":
    db_connection = connect_db(host="localhost", user="ti3groep", password="BG32L2D", database="BingoDB")
    
    # query to select highest id from the database
    query = "SELECT bingoKaartId FROM BingoKaart ORDER BY bingoKaartId DESC LIMIT 1"
    data = fetch_data_from_db(db_connection, query)
 
    last_id = data[0][0] if data else 0 

    game = bingo_game(grid_size=3, num_cards=10, last_id=last_id, db_connection=db_connection)
    game.play_bingo()

    if db_connection.cursor:
        db_connection.cursor.close()
    if db_connection.mydb:
        db_connection.mydb.close()
    print("Database connection closed")
