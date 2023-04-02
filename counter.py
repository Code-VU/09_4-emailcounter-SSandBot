def countEmail():
    # This first line is provided for you
    name = input("Enter file:")
    if len(name) < 1 : name = "mbox-short.txt"
    handle = open(name)

    book = {}

    for lin in handle: 
        lin = lin.rstrip()
        if lin.startswith("From "):
            sender = lin.split()[1]

            if sender not in book: 
                book[sender] = 1
            else: 
                book[sender] += 1

                    
    largest = book.values()
    maxval = max(largest)

    print(max(book, key=book.get), maxval)

## if you want to test locally run > python counter.py
if __name__ == "__main__":
    countEmail()
