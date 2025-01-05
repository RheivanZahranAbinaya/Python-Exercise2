def find_word_in_text(word, text):
    return word in text

text = inut("Masukkan teks: ")
word = input("Masukkan kata yang ingin dicari: ")
if find_wordin_text(word, text):
    print(f"Kata '{word}' ditemukan dalam teks.")
else:
    print(f"Kata '{word}' tidak ditemukan dala teks.")
