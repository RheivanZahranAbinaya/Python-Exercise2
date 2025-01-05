import time

def scrolling_text(text, delay=0.1):
    while True:
        for i in range(len(text)):
            print(text[i:] + text[:i], end='\r')
            time.sleep(delay)

text = input("Masukkan teks: ")
scrolling_text(text)