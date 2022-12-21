path_to_book = "books/frankenstein.txt"

def main():

    def read_book(path):
        with open(path) as file:
            book_content = file.read()
            return book_content

    def word_count(text_to_count):
        list_of_words = text_to_count.split()
        return len(list_of_words)        

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
    num_of_words = word_count(text)
    characters_dict = count_charachters(text)
    new_list = list(characters_dict.items())
    new_list.sort(key = lambda a: a[1], reverse = True)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_of_words} words found in the document")
    print(" ")   
    for i in range(0, len(new_list)):
        if new_list[i][0].isalpha() == True:
            print(f"The {new_list[i][0]} character was found {new_list[i][1]} times")
    print("--- End of report ---")
main()