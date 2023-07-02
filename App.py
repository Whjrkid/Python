import tkinter as tk
import pronouncing
import random
from gtts import gTTS
import os

words_list = [
    "cat", "dog", "house", "ball", "book", "tree", "sun", "moon", "star", "water",
    "flower", "bird", "fish", "car", "bike", "chair", "table", "door", "window", "key",
    "hat", "shoe", "sock", "hand", "foot", "eye", "ear", "nose", "mouth", "face",
    "shirt", "pants", "dress", "bag", "apple", "banana", "orange", "grape", "melon",
    "milk", "bread", "butter", "cheese", "egg", "rice", "meat", "potato", "tomato", "onion",
    "salt", "sugar", "juice", "coffee", "tea", "pencil", "pen", "paper", "desk",
    "school", "teacher", "student", "friend", "family", "home", "room", "bed",
    "bath", "toothbrush", "soap", "clock", "watch", "phone", "computer", "music", "song",
    "dance", "game", "play", "run", "jump", "swim", "laugh", "cry", "happy", "sad",
    "elephant", "lion", "tiger", "giraffe", "zebra", "monkey", "bear", "snake", "turtle", "frog",
    "ship", "airplane", "train", "bus", "carrot", "pepper", "lettuce", "cucumber", "pineapple",
    "mango", "kiwi", "chocolate", "cookie", "cake", "pie", "pizza", "hamburger", "sandwich",
    "orange", "apple", "grapefruit", "watermelon", "strawberry", "blueberry", "lemon", "lime", "peach",
    "pear", "plum", "cherry", "raspberry", "blackberry", "coconut", "vanilla", "chocolate", "soda",
    "juice", "milkshake", "crayon", "paint", "brush", "scissors", "glue", "ruler", "eraser",
    "computer", "mouse", "keyboard", "screen", "laptop", "desk", "notebook", "pencil", "pen",
    "paper", "book", "library", "school", "teacher", "student", "friend", "family", "home"
]

class HomePage:
    def __init__(self, root):
        self.root = root

        self.setup_ui()

    def setup_ui(self):
        self.root.title("Learning App")
        self.root.geometry("400x300")

        # Title label
        title_label = tk.Label(self.root, text="Welcome to the Learning App!", font=("Arial", 16))
        title_label.pack(pady=20)

        # Words button
        words_button = tk.Button(self.root, text="Words", font=("Arial", 14), command=self.open_words)
        words_button.pack(pady=10)

        # Sentences button
        sentences_button = tk.Button(self.root, text="Sentences", font=("Arial", 14), command=self.open_sentences)
        sentences_button.pack(pady=10)

        # Rhymes button
        rhymes_button = tk.Button(self.root, text="Rhymes", font=("Arial", 14), command=self.open_rhymes)
        rhymes_button.pack(pady=10)

        # Parental Controls button
        controls_button = tk.Button(self.root, text="Parental Controls", font=("Arial", 14), command=self.open_controls)
        controls_button.pack(pady=10)

    def open_words(self):
        self.root.destroy()
        WordsPage()

    def open_sentences(self):
        self.root.destroy()
        SentencesPage()

    def open_rhymes(self):
        self.root.destroy()
        RhymesPage()

    def open_controls(self):
        self.root.destroy()
        ParentalControlsPage()


class WordsPage:
    def __init__(self):
        global words_list
        self.root = tk.Tk()

        self.words = words_list
        self.current_word_index = 0

        self.setup_ui()

    def setup_ui(self):
        self.root.title("Words Page")
        self.root.geometry("400x300")

        # Word label
        self.word_label = tk.Label(self.root, text=self.words[self.current_word_index], font=("Arial", 14))
        self.word_label.pack(pady=10)

        # Speak button
        speak_button = tk.Button(self.root, text="Speak", font=("Arial", 14), command=self.speak_word)
        speak_button.pack(pady=10)

        # Input entry
        self.input_entry = tk.Entry(self.root, font=("Arial", 14))
        self.input_entry.pack()

        # Submit button
        submit_button = tk.Button(self.root, text="Submit", font=("Arial", 14), command=self.check_answer)
        submit_button.pack(pady=10)

        # Back button
        back_button = tk.Button(self.root, text="Back", font=("Arial", 14), command=self.go_back)
        back_button.pack(pady=10)

    def speak_word(self):
        word = self.words[self.current_word_index]

        # Say the word
        tts_word = gTTS(text=word, lang='en')
        tts_word.save('temp_word.mp3')
        os.system('afplay temp_word.mp3')

        # Spell the word
        spelled_word = " ".join(word)
        tts_spell = gTTS(text=spelled_word, lang='en')
        tts_spell.save('temp_spell.mp3')
        os.system('afplay temp_spell.mp3')

        # Say the word again
        os.system('afplay temp_word.mp3')

    def play_word_again(self):
        self.speak_word()

    def check_answer(self):
        answer = self.input_entry.get().lower()
        if answer == self.words[self.current_word_index]:
            if self.current_word_index < len(self.words) - 1:
                self.current_word_index += 1
                self.word_label.config(text=self.words[self.current_word_index])
                self.input_entry.delete(0, tk.END)
            else:
                self.word_label.config(text="Congratulations! You completed all the words.")
                self.input_entry.config(state=tk.DISABLED)
        else:
            self.word_label.config(text="Try again!")

    def go_back(self):
        self.root.destroy()
        HomePage(tk.Tk())


class SentencesPage:
    def __init__(self):
        self.root = tk.Tk()

        self.sentences = [
            "The sun is shining.",
            "I like to eat ice cream.",
            "She plays the piano.",
            "He is riding a bicycle.",
            "They are going to the park."
        ]
        self.current_sentence_index = 0

        self.setup_ui()

    def setup_ui(self):
        self.root.title("Sentences Page")
        self.root.geometry("400x300")

        # Sentence label
        self.sentence_label = tk.Label(self.root, text=self.sentences[self.current_sentence_index], font=("Arial", 14))
        self.sentence_label.pack(pady=10)

        # Speak button
        speak_button = tk.Button(self.root, text="Speak", font=("Arial", 14), command=self.speak_sentence)
        speak_button.pack(pady=10)

        # Input entry
        self.input_entry = tk.Entry(self.root, font=("Arial", 14))
        self.input_entry.pack()

        # Submit button
        submit_button = tk.Button(self.root, text="Submit", font=("Arial", 14), command=self.check_answer)
        submit_button.pack(pady=10)

        # Back button
        back_button = tk.Button(self.root, text="Back", font=("Arial", 14), command=self.go_back)
        back_button.pack(pady=10)

    def speak_sentence(self):
        sentence = self.sentences[self.current_sentence_index]

        # Save the sentence as an MP3 file
        tts = gTTS(text=sentence, lang='en')
        tts.save('temp.mp3')

        # Play the MP3 file
        os.system('afplay temp.mp3')

    def check_answer(self):
        answer = self.input_entry.get()
        if answer == self.sentences[self.current_sentence_index]:
            if self.current_sentence_index < len(self.sentences) - 1:
                self.current_sentence_index += 1
                self.sentence_label.config(text=self.sentences[self.current_sentence_index])
                self.input_entry.delete(0, tk.END)
            else:
                self.sentence_label.config(text="Congratulations! You completed all the sentences.")
                self.input_entry.config(state=tk.DISABLED)
        else:
            self.sentence_label.config(text="Try again!")

    def go_back(self):
        self.root.destroy()
        HomePage(tk.Tk())


class RhymesPage:
    def __init__(self):
        self.root = tk.Tk()

        self.setup_ui()

    def setup_ui(self):
        self.root.title("Rhymes Page")
        self.root.geometry("400x400")

        # Rhyme label
        self.rhyme_label = tk.Label(self.root, text="Enter a word to generate rhymes:", font=("Arial", 14))
        self.rhyme_label.pack(pady=10)

        # Input entry
        self.input_entry = tk.Entry(self.root, font=("Arial", 14))
        self.input_entry.pack()

        # Generate button
        generate_button = tk.Button(self.root, text="Generate Rhymes", font=("Arial", 14), command=self.generate_rhymes)
        generate_button.pack(pady=10)

        # Rhymes label
        self.rhymes_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.rhymes_label.pack()

        # Back button
        back_button = tk.Button(self.root, text="Back", font=("Arial", 14), command=self.go_back)
        back_button.pack(pady=10)

    def generate_rhymes(self):
        word = self.input_entry.get().lower()
        rhymes = pronouncing.rhymes(word)
        random.shuffle(rhymes)
        rhymes_text = "\n".join(rhymes[:10]) if len(rhymes) > 10 else "\n".join(rhymes)
        self.rhymes_label.config(text=rhymes_text)

    def go_back(self):
        self.root.destroy()
        HomePage(tk.Tk())


class ParentalControlsPage:
    def __init__(self):
        self.root = tk.Tk()
        self.words_page = WordsPage()
        self.words_page.root.withdraw()

        self.setup_ui()

    def setup_ui(self):
        self.root.title("Parental Controls")
        self.root.geometry("400x600")

        # Display words label
        display_label = tk.Label(self.root, text="Words:", font=("Arial", 14))
        display_label.pack(pady=10)

        # Words display
        self.words_listbox = tk.Listbox(self.root, font=("Arial", 12))
        self.words_listbox.pack()

        # Remove word label
        remove_label = tk.Label(self.root, text="Remove word:", font=("Arial", 14))
        remove_label.pack(pady=10)

        # Remove word entry
        self.remove_entry = tk.Entry(self.root, font=("Arial", 14))
        self.remove_entry.pack()

        # Remove button
        remove_button = tk.Button(self.root, text="Remove", font=("Arial", 14), command=self.remove_word)
        remove_button.pack(pady=10)

        # Add word label
        add_label = tk.Label(self.root, text="Add word:", font=("Arial", 14))
        add_label.pack(pady=10)

        # Add word entry
        self.add_entry = tk.Entry(self.root, font=("Arial", 14))
        self.add_entry.pack()

        # Add button
        add_button = tk.Button(self.root, text="Add", font=("Arial", 14), command=self.add_word)
        add_button.pack(pady=10)

        # Delete all button
        delete_all_button = tk.Button(self.root, text="Delete All", font=("Arial", 14), command=self.delete_all_words)
        delete_all_button.pack(pady=10)

        # Back button
        back_button = tk.Button(self.root, text="Back", font=("Arial", 14), command=self.go_back)
        back_button.pack(pady=10)

        # Populate words listbox
        self.populate_words_listbox()

    def populate_words_listbox(self):
        words = self.words_page.words
        for word in words:
            self.words_listbox.insert(tk.END, word)

    def remove_word(self):
        selected_word = self.words_listbox.get(tk.ACTIVE)
        if selected_word:
            self.words_listbox.delete(tk.ACTIVE)
            self.words_page.words.remove(selected_word)

    def add_word(self):
        word = self.add_entry.get()
        if word:
            self.words_listbox.insert(tk.END, word)
            self.words_page.words.append(word)
            self.add_entry.delete(0, tk.END)

    def delete_all_words(self):
        self.words_listbox.delete(0, tk.END)
        self.words_page.words = []

    def go_back(self):
        self.root.destroy()
        HomePage(tk.Tk())

if __name__ == "__main__":
    home_page = HomePage(tk.Tk())
    tk.mainloop()