
def print_board(board):
    """Отображает игровую доску."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    """Проверяет, есть ли победитель."""
    # Проверка строк и столбцов
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]

    # Проверка диагоналей
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

def is_board_full(board):
    """Проверяет, заполнена ли доска."""
    for row in board:
        if " " in row:
            return False
    return True

def make_move(board, row, col, player):
    """Выполняет ход игрока."""
    if board[row][col] == " ":
        board[row][col] = player
        return True
    return False

def get_player_input(player):
    """Получает ввод от игрока."""
    while True:
        try:
            row = int(input(f"Игрок {player}, введите номер строки (0-2): "))
            col = int(input(f"Игрок {player}, введите номер столбца (0-2): "))
            if row in [0, 1, 2] and col in [0, 1, 2]:
                return row, col
            else:
                print("Неверный ввод. Пожалуйста, введите числа от 0 до 2.")
        except ValueError:
            print("Неверный ввод. Пожалуйста, введите числа.")

def play_game():
    """Основная функция для игры."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        row, col = get_player_input(current_player)

        if make_move(board, row, col, current_player):
            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"Игрок {winner} выиграл!")
                break
            if is_board_full(board):
                print_board(board)
                print("Игра закончилась вничью!")
                break
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Эта клетка уже занята. Попробуйте снова.")

if __name__ == "__main__":
    play_game()
