import random
import tabulate

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "!@#$%^&*()_-+=\;?/><"

upper, lower, nums, syms = True, True, True, True

all = ""

if upper:
    all += uppercase_letters

if lower:
    all += lowercase_letters

if nums:
    all += digits

if syms:
    all += symbols

length = 20
amount = 1

for x in range(amount):
    # Use random.choices to allow duplicate characters
    password = "".join(random.choices(all, k=length))

    print(f"Here is your password\n")
    print(password)
    print("\n")
