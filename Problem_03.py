def calculate_fine(book_title, days_overdue, daily_rate=5.0, max_fine=150.0):
    original_fine = days_overdue * daily_rate
    fine_amount = float(min(original_fine, max_fine))
    
    print(f"Book: {book_title}")
    print(f"Days overdue: {days_overdue}")
    print(f"Fine: Rs. {fine_amount}")
    
    if original_fine >= max_fine:
        print(f"You have accumulated the maximum fine of INR: {max_fine}")
    return fine_amount

def start():
    title = input()
    days = int(input())
    calculate_fine(title, days)

start()