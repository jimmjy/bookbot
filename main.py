def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = getWordCount(file_contents)
        num_characters = numberOfCharacters(file_contents)

        sorted_counts = sort_by_occurrence(num_characters)

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document")
        print()

        # process list of dicts for report
        for dict in sorted_counts:
            print(f"The '{dict['letter']}' character was found {dict['count']} times")

        print("--- End report ---")



def getWordCount(words):
    words_array = words.split()
    words_length = len(words_array)
    return words_length


def numberOfCharacters(words):
    characters = {}

    for letter in words:
        lower_case_letter = letter.lower()

        if lower_case_letter in characters:
            characters[lower_case_letter] += 1
        else:
            characters[lower_case_letter] = 1

    return characters


def sort_on(dict):
    return dict["count"]


def sort_by_occurrence(dictionary):
    count_list = []

    for letter, count in dictionary.items():
        if letter.isalpha():
            count_list.append({"letter": letter, "count": count})
    
    # sort in place
    count_list.sort(reverse=True, key=sort_on)

    return count_list


main()
