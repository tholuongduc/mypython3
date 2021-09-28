#Xây dựng lớp flashcard đơn giản. Khi chạy chương trình sẽ hiển thị 1 từ tiếng Việt, yêu cầu người dùng phải
# nhập vào từ tương ứng trong tiếng Anh. Chương trình sẽ tự đánh giá câu trả lời của người dùng đúng hoặc sai.
import random
#Define class
class flashcard:
    def __init__(self):
        self.fruits = {'Trái cam': "orange",
                       'Dưa hấu': 'watermelon',
                       'Xoài': 'mango',
                       'Chuối': 'banana',
        }
    def quiz(self):
        vietnamese, english = random.choice(list(self.fruits.items()))
        while True:
            print("Tiếng anh của '{}' là:".format(vietnamese))
            user_answer = input()
            if user_answer.lower() == english:
                print("Correct!")
                break
            else:
                print("Incorrect!Try again!")

play = flashcard()
play.quiz()