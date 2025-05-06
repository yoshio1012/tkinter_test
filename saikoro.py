import tkinter as tk
from tkinter import ttk 
from PIL import ImageTk, Image
import random

class dice:
    def __init__(self, app):
        app.title("サイコロ対決")
        app.geometry("400x300")

        # Create frames
        self_frame = ttk.Frame(app, width=200, height=100)
        enemy_frame= ttk.Frame(app, width=200, height=100)
        self_dice_frame = ttk.Frame(self_frame, width=200, height=100)
        enemy_dice_frame = ttk.Frame(enemy_frame, width=200, height=100)
        button_frame = ttk.Frame(app, width=400, height=100)
        result_frame = ttk.Frame(app, width=200, height=100)
        winrate_frame = ttk.Frame(app, width=200, height=100)

        # Frame layout
        self_frame.grid(row=0, column=0)
        enemy_frame.grid(row=0, column=1)
        self_dice_frame.grid(row=1, column=0)
        enemy_dice_frame.grid(row=1, column=1)
        button_frame.grid(row=2, column=0, columnspan=1)
        result_frame.grid(row=3, column=0)
        winrate_frame.grid(row=3, column=1)

        # Create labels and layout
        self_label = ttk.Label(self_frame, text="あなたのサイコロ")
        enemy_label = ttk.Label(enemy_frame, text="相手のサイコロ")
        self_label.grid(row=0, column=0)
        enemy_label.grid(row=0, column=0)

        # Create buttons and layout
        start_button = ttk.Button(button_frame, text="サイコロを振る")
        start_button.grid(row=0, column=0)
        start_button.bind("<Button-1>", lambda event: roll_dice())

        #result label and layout
        result = tk.StringVar()
        result.set("結果待ち")
        result_label = ttk.Label(result_frame, textvariable=result)
        result_label.grid(row=0, column=0)

        # Create dice images
        dice1_image = ImageTk.PhotoImage(Image.open("1.png").resize((50, 50)))
        dice2_image = ImageTk.PhotoImage(Image.open("2.png").resize((50, 50)))
        dice3_image = ImageTk.PhotoImage(Image.open("3.png").resize((50, 50)))
        dice4_image = ImageTk.PhotoImage(Image.open("4.png").resize((50, 50)))
        dice5_image = ImageTk.PhotoImage(Image.open("5.png").resize((50, 50)))
        dice6_image = ImageTk.PhotoImage(Image.open("6.png").resize((50, 50)))



        def roll_dice():
            self_dice = random.randint(1, 6)
            enemy_dice = random.randint(1, 6)

            # Update dice images
            if self_dice == 1:
                self_dice_image = dice1_image
            elif self_dice == 2:   
                self_dice_image = dice2_image
            elif self_dice == 3:
                self_dice_image = dice3_image
            elif self_dice == 4:
                self_dice_image = dice4_image
            elif self_dice == 5:
                self_dice_image = dice5_image
            elif self_dice == 6:
                self_dice_image = dice6_image
            
            if enemy_dice == 1:
                enemy_dice_image = dice1_image
            elif enemy_dice == 2:   
                enemy_dice_image = dice2_image
            elif enemy_dice == 3:   
                enemy_dice_image = dice3_image
            elif enemy_dice == 4:
                enemy_dice_image = dice4_image
            elif enemy_dice == 5:
                enemy_dice_image = dice5_image
            elif enemy_dice == 6:
                enemy_dice_image = dice6_image
            
            self_dice_label = ttk.Label(self_dice_frame, image=self_dice_image)
            enemy_dice_label = ttk.Label(enemy_dice_frame, image=enemy_dice_image)

            self_dice_label.grid(row=0, column=0)
            enemy_dice_label.grid(row=0, column=0)

            # Determine winner
            if self_dice > enemy_dice:
                result.set("あなたの勝ち！")
            elif self_dice < enemy_dice:
                result.set("あなたの負け！")   
            else:
                result.set("引き分け！")



def main():
    app = tk.Tk()
    dice(app)
    app.mainloop() 

if __name__ == '__main__':
    main()