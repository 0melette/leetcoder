class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        current_word_position = 1
        current_index = 0
        sentence_length = len(sentence)

        while current_index < sentence_length:
            while current_index < sentence_length and sentence[current_index] == " ":
                current_index += 1
                current_word_position += 1

            matchCount = 0
            while (current_index < sentence_length and matchCount < len(searchWord) and 
                   sentence[current_index] == searchWord[matchCount]):
                current_index += 1
                matchCount += 1

            if matchCount == len(searchWord):
                return current_word_position

            while current_index < sentence_length and sentence[current_index] != " ":
                current_index += 1

        return -1

