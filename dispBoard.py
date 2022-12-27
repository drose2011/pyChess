import tkinter as tk
from board import Board
from move import Move

def new_root():
    root = tk.Tk()
    root.title('PyChess')
    # Set icon
    root.iconbitmap('./assets/w_king.png')
    center_window(root, 480, 480)

    return root

def center_window(root, window_width, window_height):

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    root.resizable(False, False)

def change_on_hover(obj, colorOnHover, colorOnLeave):
    # adjusting backgroung of the widget
    # background on entering widget
    obj.bind("<Enter>", func=lambda e: obj.config(
        background=colorOnHover))
  
    # # background color on leving widget
    obj.bind("<Leave>", func=lambda e: obj.config(
        background=colorOnLeave))

def button_clicked(event):
    row = event.widget.master.grid_info()['row']
    col = event.widget.master.grid_info()['column']
    board.clicked(row, col)
    disp_board(root, board.get_board(), board.check_game_over())
    root.update()
    if board.comp_move_next():
        board.move_AI()
        disp_board(root, board.get_board(), board.check_game_over())
    

def close_app():
    root.destroy()
    exit(0)

def disp_board(root, board, gameover):

    board_arr = board[0]
    board_sel = board[1]
    board_allowed = board[2]
    for row_idx, row in enumerate(board_arr):
        for col_idx, piece in enumerate(row):
            color = 'grey' if (col_idx + row_idx) % 2 == 0 else 'white'
            f = tk.Frame(root, height=60, width=60, bg=color)
            f.pack_propagate(0) # don't shrink
            if piece is not None:
                image_label = tk.Label(f, image=pieces[piece.image_file], bg=color)
            else:
                image_label = tk.Label(f, bg=color)

            image_label.bind('<Button-1>', button_clicked)
            image_label.pack(fill='both', expand=1)
            f.grid(row=row_idx, column=col_idx)

    # Set selected square value
    if board_sel is not None:
        sel_frame = root.grid_slaves(board_sel[0], board_sel[1])[0]
        sel_label = sel_frame.winfo_children()[0]
        sel_label.config(bg='green')
    for move in board_allowed:
        row = move.end_row
        col = move.end_col
        allowed_frame = root.grid_slaves(row, col)[0]
        allowed_label = allowed_frame.winfo_children()[0]
        allowed_label.config(bg='lightgreen')

    # Setting hover color func now that backgrounds have been set'
    for row in range(8):
        for col in range(8):
            frame = root.grid_slaves(row, col)[0]
            label = frame.winfo_children()[0]
            bg_color = label.cget('bg')
            change_on_hover(label, 'darkgrey', bg_color)
            # 

            # label.bind("<Enter>", func=lambda e: label.config(
            # background='darkgrey'))
            # label.bind("<Leave>", func=lambda e: label.config(
            # background=bg_color))


    if gameover:
        end = tk.Toplevel()
        end.wm_title("Game Over")
        winning_side = 'White' if gameover == 1 else 'Black'
        tk.Label(end, text=f'{winning_side} Wins!').pack()
        tk.Button(end, text="Close Game", command=close_app).pack()
        center_window(end, 200, 100)
        end.mainloop()


if __name__ == '__main__':

    root = new_root()

    pieces = {'w_pawn'      : tk.PhotoImage(file='./pics/w_pawn.png'),
              'w_rook'      : tk.PhotoImage(file='./pics/w_rook.png'),
              'w_knight'    : tk.PhotoImage(file='./pics/w_knight.png'),
              'w_bishop'    : tk.PhotoImage(file='./pics/w_bishop.png'),
              'w_queen'     : tk.PhotoImage(file='./pics/w_queen.png'),
              'w_king'      : tk.PhotoImage(file='./pics/w_king.png'),
              'b_pawn'      : tk.PhotoImage(file='./pics/b_pawn.png'),
              'b_rook'      : tk.PhotoImage(file='./pics/b_rook.png'),
              'b_knight'    : tk.PhotoImage(file='./pics/b_knight.png'),
              'b_bishop'    : tk.PhotoImage(file='./pics/b_bishop.png'),
              'b_queen'     : tk.PhotoImage(file='./pics/b_queen.png'),
              'b_king'      : tk.PhotoImage(file='./pics/b_king.png')}

    board = Board()

    start_board = board.get_board()
    disp_board(root, start_board, board.check_game_over())

    root.mainloop()

        

    




