def calculate_fine(book_title, days_overdue, daily_rate=5.0, max_fine=150.0):
    fine_amount = float(min(days_overdue * daily_rate, max_fine))
    print(f"Book: {book_title}")
    print(f"Days overdue: {days_overdue}")
    print(f"Fine: Rs. {fine_amount}", end=" ")
    return fine_amount

def start():
    title = input()
    days = int(input())
    rate = float(input())
    m_fine = float(input())
    calculate_fine(title, days, rate, m_fine)

start()
