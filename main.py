board_size = 8

possible_x_moves = [2, 1, -1, -2, -2, -1, 1, 2]
possible_y_moves = [1, 2, 2, 1, -1, -2, -2, -1]


def handle_knights_tour():
    chessboard = [[0 for i in range(board_size)]for i in range(board_size)]
    starting_place_count = 1
    chessboard[0][0] = starting_place_count

    if is_tour_finished(chessboard, 2, 0, 0):
        print_chessboard(chessboard)
    else:
        print('Something went wrong')


def is_tour_finished(chessboard, count, current_x, current_y):
    if count > board_size**2:
        return True

    for i in range(len(possible_x_moves)):
        next_x = current_x + possible_x_moves[i]
        next_y = current_y + possible_y_moves[i]

        if is_valid_move(chessboard, next_x, next_y) and chessboard[next_x][next_y] == 0:
            chessboard[next_x][next_y] = count

            if is_tour_finished(chessboard, count + 1, next_x, next_y):
                return True

            chessboard[next_x][next_y] = 0

    return False


def print_chessboard(chessboard):
    for i in range(board_size):
        for j in range(board_size):
            print(chessboard[i][j], end=' ')
        print()


def is_valid_move(chessboard, x_pos, y_pos):
    return False if x_pos < 0 or x_pos >= len(chessboard) or y_pos < 0 or y_pos >= len(chessboard) else True


if __name__ == "__main__":

    handle_knights_tour()
