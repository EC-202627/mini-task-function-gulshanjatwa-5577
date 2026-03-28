title = input().strip()
days = int(input().strip())

fine = float(days * 5)
if fine > 150.0:
    fine = 150.0

print(f"Book: {title}")
print(f"Days overdue: {days}")
print(f"Fine: Rs. {fine}")
