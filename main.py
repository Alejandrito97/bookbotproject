path_to_book = "books/frankenstein.txt"

def main():

    def read_book(path):
        with open(path) as file:
            book_content = file.read()
            return book_content


    def count_charachters(characters_to_count):
        
        list_of_characters = list(characters_to_count.lower())
        
        new_dictionary = {}

        for character in list_of_characters:
            if character in new_dictionary:
                new_dictionary[character] += 1
            else:
                new_dictionary[character] = 1

        return new_dictionary

    text = read_book(path_to_book)
    characters_dict = count_charachters(text)
    print(characters_dict)

main()