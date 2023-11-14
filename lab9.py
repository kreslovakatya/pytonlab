try:
    with open("venv/TF7_1.txt", "w") as file:
        file.write("Hello, how are you?\n")
        file.write("I love programming\n")
except IOError as e:
    print(f"Error creating TF7_1.txt: {e}")

try:
    with open("venv/TF7_1.txt", "r") as file_read, open("venv/TF7_2.txt", "w") as file_write:
        duplicate_words = set()

        for line in file_read:
            words = line.split()
            for word in words:
                if any(c.isalpha() and word.count(c * 2) >= 1 for c in word):
                    duplicate_words.add(word)

        if duplicate_words:
            for word in duplicate_words:
                file_write.write(word + "\n")
        else:
            file_write.write("No words with duplicate letters found.")
except IOError as e:
    print(f"Error processing files: {e}")

try:
    with open("venv/TF7_2.txt", "r") as file_print:
        for line in file_print:
            print(line.strip())
except IOError as e:
    print(f"Error reading TF7_2.txt: {e}")