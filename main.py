path_to_book = "books/frankenstein.txt"

def main():

    def read_book(path):
        with open(path) as file:
            book_content = file.read()
            return book_content

    
    def word_count(text_to_count):
        list_of_words = text_to_count.split()
        return len(list_of_words)

    text = read_book(path_to_book)
    
    num_of_words = word_count(text)
    
    print(num_of_words)
    

main()