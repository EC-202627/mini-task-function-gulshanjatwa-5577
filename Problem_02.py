def calculate_fine(book_title, days_overdue, daily_rate=5.0, max_fine=150.0):
    fine_amount = float(min(days_overdue * daily_rate, max_fine))
    print(f"Book: {book_title}")
    print(f"Days overdue: {days_overdue}")
    print(f"Fine: Rs. {fine_amount}")
    return fine_amount

if __name__ == "__main__":
    title = input().strip()
    days = int(input().strip())
    rate = float(input().strip())
    calculate_fine(title, days, daily_rate=rate)
