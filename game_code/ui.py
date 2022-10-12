from tkinter import *
from quiz_brain import QuizBrain
from options import *
from data import *

THEME_COLOR = "#375362"
#Window Title and Game Title
WIN_TITLE = "Quizler"
GAME_TITLE = "Quizler"
#Background Image
#BACKGROUND = ""
#Font type
FONT_NAME = "Courior"
WHITE = "white"
GREEN = "green"
CLOCK_COLOR = "white"
right_button_img = "images/true.png"
left_button_img = "images/false.png"

class QuizInterface():

    def __init__(self):
        self.cat_id = "any"
        self.number_of_qs = 10
        self.difficulty = "easy"

        self.window = Tk()
        self.window.title(WIN_TITLE)
        self.window.config(padx= 10, pady= 10, bg=THEME_COLOR)
        self.window.geometry("400x520")

        self.settings()

        self.window.mainloop()

    def clearFrame(self):
        # destroy all widgets from frame
        self.cat_list_box.destroy()
        self.spinbox.destroy()
        self.box_label.destroy()
        self.cat_label.destroy()
        self.diff_label.destroy()
        self.submit.destroy()
        self.diff_button1.destroy()
        self.diff_button2.destroy()
        self.diff_button3.destroy()
        self.main_game()

    def settings(self):
        self.header = Label(text=GAME_TITLE, font=(FONT_NAME, 20, "bold"), fg=WHITE, bg=THEME_COLOR, justify="center", padx= 10, pady= 10)
        self.header.grid(row= 1, column=1)

        def category_set(event):
            self.cat_id = str(cat_opts[self.cat_list_box.get(self.cat_list_box.curselection())])

        self.cat_label = Label(text="Select Category", font=(FONT_NAME, 15, "bold"), fg=WHITE, bg=THEME_COLOR, justify="center", padx= 10, pady= 10)
        self.cat_label.grid(row= 2, column=1)

        self.cat_list_box = Listbox(height=6)
        categories = list(cat_opts.keys())

        for item in categories:
            self.cat_list_box.insert(categories.index(item), item)
        self.cat_list_box.select_set(0)  # This only sets focus on the first item.
        self.cat_list_box.event_generate("<<ListboxSelect>>")
        self.cat_list_box.bind("<<ListboxSelect>>", category_set)
        self.cat_list_box.grid(row=3, column= 1, columnspan=2)

        def num_qs():
            # gets the current value in spinbox.
            self.number_of_qs = str(self.spinbox.get())
        self.box_label = Label(text="Number of Questions", font=(FONT_NAME, 10, "bold"), fg=WHITE, bg=THEME_COLOR, justify="center", padx= 10, pady= 10)
        self.box_label.grid(row= 4, column=1)

        self.spinbox = Spinbox(from_=10, to=25, width=10, command=num_qs)
        self.spinbox.grid(row = 4, column = 2)

        def diff_set():
            #self.difficulty = diff_list_box.get(diff_list_box.curselection()).lower()
            diffs = ["easy", "medium", "hard"]
            select = radio_state.get()
            self.difficulty = diffs[select]
            #print(select)
            #print(self.difficulty)

        self.diff_label = Label(text="Select Difficulty", font=(FONT_NAME, 15, "bold"), fg=WHITE, bg=THEME_COLOR, justify="center", padx= 10, pady= 10)
        self.diff_label.grid(row= 5, column=1)

        # diff_list_box = Listbox(height=3)
        # diffs = ["Easy", "Medium", "Hard"]
        # for item in diffs:
        #     diff_list_box.insert(diffs.index(item), item)
        # diff_list_box.select_set(0)  # This only sets focus on the first item.
        # diff_list_box.event_generate("<<ListboxSelect>>")
        # diff_list_box.bind("<<ListboxSelect>>", diff_set)
        # diff_list_box.grid(row=6, column= 1, columnspan=2)

        radio_state = IntVar()
        self.diff_button1 = Radiobutton(text="Easy", value=0, variable=radio_state, command=diff_set, bg=THEME_COLOR, justify="center")
        self.diff_button2 = Radiobutton(text="Medium", value=1, variable=radio_state, command=diff_set, bg=THEME_COLOR, justify="center")
        self.diff_button3 = Radiobutton(text="Hard", value=2, variable=radio_state, command=diff_set, bg=THEME_COLOR, justify="center")
        self.diff_button1.grid(row = 6, column= 1, columnspan=2)
        self.diff_button2.grid(row = 7, column= 1, columnspan=2)
        self.diff_button3.grid(row = 8, column= 1, columnspan=2)

        #SUBMIT BUTTON
        #End/Reload Window
        self.submit = Button(highlightthickness=0, text ="Submit", command=self.submit_settings, justify='center')
        self.submit.grid(row=9, column=2)

    def submit_settings(self):
        question_data = poll_api(self.number_of_qs, self.cat_id, self.difficulty)
        question_bank = []
        for each in question_data:
            question_bank.append(Question(each["question"], each["correct_answer"]))
        self.brain = QuizBrain(question_bank)
        self.clearFrame()


    def main_game(self):
        self.header = Label(text=GAME_TITLE, font=(FONT_NAME, 20, "bold"), fg=WHITE, bg=THEME_COLOR, justify="center", padx= 10, pady= 10)
        self.header.grid(row= 1, column=1)
        self.score = Label(text="Score: 0", font=(FONT_NAME, 15, "bold"), fg=WHITE, bg=THEME_COLOR, justify="center")
        self.score.grid(row= 1, column=2)

        self.canvas = Canvas(height=290, width=340, bg=WHITE, highlightthickness=10)
        #self.bgimg = PhotoImage(file = BACKGROUND)
        #self.canvas.create_image(100 , 112, image = bgimg)
        self.canvas_text = self.canvas.create_text(160,160, text="", fill="black", font=(FONT_NAME, 20, "italic"), width=300)
        self.canvas.grid(row= 2, column= 1, columnspan=2, padx=10, pady=10)

        self.right_butt = PhotoImage(file = right_button_img)
        self.left_butt = PhotoImage(file = left_button_img)

        self.button_left = Button(image=self.left_butt, highlightthickness=0, text ="", command=self.button_left_action, justify='center')
        self.button_left.grid(row=4, column=1)
        #self.button_center = Button(text ="", command=self.button_center_action, justify='center')
        #self.button_center.grid(row=4, column=2
        self.button_right = Button(image=self.right_butt, highlightthickness=0, text ="", command=self.button_right_action, justify='center')
        self.button_right.grid(row=4, column=2)

        #self.bottom_gage = Label(text="", font=(FONT_NAME, 15, "bold"), fg=GREEN)
        #self.bottom_gage.grid(row=5, column=2)

        self.set_question()



    def button_left_action(self):
        #DEBUG print("False")
        self.scoreboard("False")

    def button_center_action(self):
        pass

    def button_right_action(self):
        #DEBUG print("True")
        self.scoreboard("True")


    def scoreboard(self, answer):
        result = self.brain.check_answer(answer)
        self.canvas.itemconfigure(self.canvas_text, text=result)
        #DEBUG self.brain.print_score()
        self.score["text"] = f"Score: {self.brain.score}"
        if self.brain.still_has_questions():
            self.window.after(2000, self.set_question)
        else:
            self.window.after(1000, self.end_board())


    def set_question(self):
        text = self.brain.next_question()
        self.canvas.itemconfigure(self.canvas_text, text=text)


    def end_board(self):
        self.canvas.itemconfigure(self.canvas_text, text=f"That's all the questions.\nYour final score is: {self.brain.score}/{self.brain.num_qs}")
        self.button_left.config(state="disabled")
        self.button_right.config(state="disabled")

