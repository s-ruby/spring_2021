print('Question 1:')
# You are working on a library management system, here are the list books at the library
books = ['SAPIENS', 'WHITE FRAGILITY', 'THE BODY KEEPS THE SCORE','JUST MERCY', 'BORN A CRIME',
         'THE WARMTH OF OTHER SUNS', 'THE COLOR OF LAW', 'THE NEW JIM CROW', 'THE TRUTHS WE HOLD']

# 1.0
# What data type is the object 'books'? How do you know?
# 'books' is a list
print(type(books))

# 1.1
# Create a function 'available_books' to print the books list
# Parameters: Not needed for this function
# Return: Not needed for this function

def available_books():
    print(books)

# Test 1.1
# Run the 'available_books' function
available_books()

# 1.2
# Create a function 'count_books' that returns the number of books in the books_with_details list
# Parameters: Not needed for this function
# Return: number of books (integer)
def count_books():
    return len(books)

# Test 1.2
# Check the number of books available in the books list using the count_books function
count_books()

# 1.3
# Create a function 'check_out' that removes a book from the books list
# Parameters: book (string)
# Return: Not needed for this function
def check_out(book):
    books.remove(book)

# Test 1.3
# Check out 'SAPIENS' using the check_out function

# Bonus: Run available_books function again to see if the book was checked out
check_out('SAPIENS')
available_books()

# 1.4
# Create a function 'check_in' that adds a book to the books list
# Parameters: book (string)
# Return: Not needed for this function
def check_in(book):
    books.append(book)

# Test 1.4
# Check in 'SAPIENS' using the check_in function

# Bonus: Run available_books function to see if the book was checked in
check_in('SAPIENS')
available_books()

# 1.5
# Create a function 'search_by_name' that prints 'Available' if exists in books list, 'Not Available' if it doesn't.
# Parameters: book (string)
# Return: Not needed for this function
def search_by_name(book):
    if book in books:
        print('Available')
    else:
        print('Not Available')

# Test 1.5
# Search for the book 'JUST MERCY'
search_by_name('JUST MERCY')

