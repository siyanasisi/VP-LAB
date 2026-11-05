def book_cinema_seats(room_matrix, row, seat_numbers):
    if row < 0 or row >= len(room_matrix):
        return False

    for seat in seat_numbers:
        if seat < 0 or seat >= len(room_matrix[row]) or room_matrix[row][seat] == 1:
            return False

    for seat in seat_numbers:
        room_matrix[row][seat] = 1

    return True


row = 2
seat_numbers = [0, 1, 2]
room_matrix = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0]
]
result = book_cinema_seats(room_matrix, row, seat_numbers)
print(room_matrix)
print(result)