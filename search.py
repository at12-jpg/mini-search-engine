import os
import time

print("=" * 30)
print("     MINI SEARCH ENGINE")
print("=" * 30)

search_query = input("\nSearch: ")
search_words = search_query.lower().split()
print("\nSearching...")

documents = [
    "documents/python.txt",
    "documents/github.txt",
    "documents/india.txt",
    "documents/ai.txt"
]

found = False
results = []

start = time.time()
for file in documents:
    matches = 0
    with open(file, "r") as current_file:
        content = current_file.read()

    content_lower = content.lower()
    filename = os.path.basename(file)
    if any(word in content_lower for word in search_words):
       
        found = True
        print(f"\nFound in: {filename}")

        lines = content.split("\n")
        
        for line in lines:
            if any(word in line.lower() for word in search_words):
                matches += 1
                print(">", line)

        print(f"Matches: {matches}")
        results.append((filename, matches))
results.sort(key=lambda x: x[1], reverse=True)

if not found:
    print("\n❌ No results found.")
print("\n==== RESULTS =====")
for number, (file, matches) in enumerate(results, start=1):
    print(f"{number}. {file} - {matches} matches")
end = time.time()

print(f"\nSearch completed in {end - start:.4f} seconds")
