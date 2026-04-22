items = {
    "action": ["Avengers", "John Wick", "Batman"],
    "comedy": ["Superbad", "The Mask", "Step Brothers"],
    "romance": ["The Notebook", "Titanic", "La La Land"]
}

user_input = input("Enter a genre (action, comedy, romance): ").lower()

if user_input in items:
    print("Recommendations:")
    for item in items[user_input]:
        print("-", item)
else:
    print("Sorry, no recommendations found.")