def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        count = 0
        for word in words:
            count +=1

        print("-- report of Frankenstein --")
        print(f"{count} words found in the document\n")

        lowercase_text = file_contents.lower()

        char_counts = {}

        for char in lowercase_text:
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
        
        for char, freq in char_counts.items():
            if char.isprintable() and char != ' ' and char != '\n':
                print(f"The '{char}' character was found {freq} times")

            
        print("The end")


if __name__== "__main__":
    main()

