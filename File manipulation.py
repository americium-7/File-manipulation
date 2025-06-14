import re
from collections import defaultdict

def count_words(filename):
    
    word_counts = defaultdict(int)
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                words = re.findall(r'\b[\w-]+\b', line.lower())
                for word in words:
                    word_counts[word] += 1
                    
        return dict(sorted(word_counts.items()))
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}

def display_word_counts(word_counts):
    if not word_counts:
        print("No word counts to display.")
        return
    
    print("\nWord Count Results:")
    print("-" * 30)
    print(f"{'Word':<20} | {'Count':>5}")
    print("-" * 30)
    for word, count in word_counts.items():
        print(f"{word:<20} | {count:>5}")

def main():
    print("Word Counter Program")
    print("--------------------")
    filename = input("Enter the path to the text file: ")
    
    word_counts = count_words(filename)
    display_word_counts(word_counts)

if __name__ == "__main__":
    main()