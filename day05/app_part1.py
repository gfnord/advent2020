def calc_seatid():
    f=open("input.txt","r")
    seats=f.readlines()
    f.close()
    seatID = [] 
    for seat in seats:
        seat = seat.strip() # remove end of line
        seat_list = list(seat)
        min_row = 0
        max_row = 127
        row = 0
        min_col = 0
        max_col = 7
        col = 0
        #print(seat, seat_list)
        for i in range(0, 6):
            if seat_list[i] == 'F':
                min_row = min_row
                max_row = (((max_row-min_row+1)/2)-1)+min_row
                #print(i, seat_list[i], min_row, max_row)
            if seat_list[i] == 'B':
                max_row = max_row
                min_row = ((max_row-min_row+1)/2)+min_row
                #print(i, seat_list[i], min_row, max_row)
        if seat_list[6] == 'F':
            row = min_row
            #print(6, seat_list[6], row)
        if seat_list[6] == 'B':
            row = max_row
            #print(6, seat_list[6], row)
        for i in range(7, 9):
            if seat_list[i] == 'L':
                min_col = min_col
                max_col = (((max_col-min_col+1)/2)-1)+min_col
                #print(i, seat_list[i], min_col, max_col)
            if seat_list[i] == 'R':
                min_col = ((max_col-min_col+1)/2)+min_col
                max_col = max_col
                #print(i, seat_list[i], min_col, max_col)
        if seat_list[9] == 'L':
            col = min_col
            #print(9, seat_list[9], col)
        if seat_list[9] == 'R':
            col = max_col
            #print(9, seat_list[9], col)
        print(seat, int(row*8+col), int(row), int(col))
        seatID.append(int(row*8+col)) # append the seat ID to the list seatID
    print('Highest seat ID:', max(seatID))
 
calc_seatid()
