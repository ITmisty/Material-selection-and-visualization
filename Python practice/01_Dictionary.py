def count_words(text):
    # 換成小寫並以空格分開
    words = text.lower().split()
    word_count = {}

    for word in words:
        #  如果單字存在字典則加1，否則設1
        word_count[word] = word_count.get(word, 0) + 1
    
    return word_count

# Test
sample_text = "Python is fun and Python is powerful"
result = count_words(sample_text)
print("Word Frequency Statistics:", result)