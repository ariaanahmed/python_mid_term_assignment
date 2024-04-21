class Hall:
    def __init__(self, hall_name, rows, cols):
        self.hall_name = hall_name
        self.rows = rows
        self.cols = cols
        self.seats = {}
        self.shows = []

    def entry_show(self, id, movie_name, time):
        showTuple = (id, movie_name, time)
        self.shows.append(showTuple)
        self.seats[id] = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    def book_seats(self, id, seatTuples):
        if id not in self.seats:
            print("Invalid show ID.")
            return

        selected_seats = self.seats[id]
        for row, col in seatTuples:
            if 1 <= row <= self.rows and 1 <= col <= self.cols:
                if selected_seats[row - 1][col - 1] == 0:
                    selected_seats[row - 1][col - 1] = 1
                else:
                    print(f"Seat at row {row}, col {col} is already booked.")
            else:
                print("Invalid seat selection.")

    def view_show_list(self):
        print("Show List:")
        for show in self.shows:
            print(f"ID: {show[0]}, Movie Name: {show[1]}, Time: {show[2]}")

    def view_available_seats(self, id):
        if id in self.seats:
            print(f"Available seats for show {id}:")
            for i in range(self.rows):
                for j in range(self.cols):
                    print(f"Row: {i + 1}, Col: {j + 1} - {'Available' if self.seats[id][i][j] == 0 else 'Booked'}")
        else:
            print("Invalid show ID.")

hall_name = input("Enter hall name: ")
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
hall = Hall(hall_name, rows, cols)

while True:
    id = input("Enter show ID: ")
    movie_name = input("Enter movie name: ")
    time = input("Enter show time: ")
    hall.entry_show(id, movie_name, time)
    add_another = input("Do you want to add another show? (yes/no): ")
    if add_another.lower() != 'yes':
        break

show_id = input("Enter show ID to book seats: ")

seat_selections = []

while True:
    rowCol = input("Enter seat row and column ('row_no: col_no:'): ").split()
    if len(rowCol) != 2:
        print("Invalid input! Please enter row and column separated by space.")
        continue
    try:
        row, col = map(int, rowCol)
        seat_selections.append((row, col))
    except ValueError:
        print("Invalid input! Please enter integers for row and column.")
        continue
    more_seats = input("Do you want to book more seats? (yes/no): ")
    if more_seats.lower() != 'yes':
        break

hall.book_seats(show_id, seat_selections)
hall.view_show_list()
show_id = input("Enter show ID to view available seats: ")
hall.view_available_seats(show_id)
