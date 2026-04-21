def process_range_squares(start, end):
    squares = [i**2 for i in range(start, end + 1)]
    
    even_squares = [num for num in squares if num % 2 == 0]
    odd_squares = [num for num in squares if num % 2 != 0]
    
    print(f"Range: {start} to {end}")
    print(f"All Squares: {squares}")
    print(f"Even Squares: {even_squares}")
    print(f"Odd Squares: {odd_squares}")

process_range_squares(1, 10)
