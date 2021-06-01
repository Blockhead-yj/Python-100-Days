# -*- coding: utf-8 -*-
"""
Created on Mon May 31 19:13:19 2021

@author: YJ-Dai
"""
import os
import time

class board_game(object):
    def __init__(self):
        self.board = [i for i in range(10*10)]
        self.first_player = "白"
        self.second_player = "黑"
        self.turn = 1
    
    def print_board(self):
        current_board = self.board
        os.system("cls")
        print("-"*31)
        for i in range(10):
            print("|", end="")
            for j in range(10):
                if isinstance(current_board[i*10+j], int):
                    print(f"{current_board[i*10+j]:0>2}", end="|")
                else:
                    print(f"{current_board[i*10+j]}", end="|")
            print()
            print("+"+"--+"*10)
    
    def change_board(self):
        current_player = self.first_player if self.turn%2==1 else self.second_player
        print("第%s回合,当前的玩家执%s" % (self.turn, current_player))
        location = input("请输入一个0~99的整数来放置棋子到相应的位置：")
        if str.isdigit(location):
            location = int(location)
            if location>99 or location<0:
                print("输入错误，棋子的位置只能是0~99的整数！")
                return self.change_board()
        else:
            print("输入错误，棋子的位置只能是0~99的整数！")
            return self.change_board()
        if self.board[location]==location:
            self.board[location]=current_player
            self.turn += 1
        else:
            print("当前位置已经有棋子了，请重新输入！")
            return self.change_board()
    
    def check_horizontal(self, check_board):
        count = 0
        for i in range(1,len(check_board)):
            if check_board[i]-check_board[i-1]==1:
                count += 1
                if count == 4:
                    return True
                else:
                    continue
            else:
                count = 0
        return False
    def check_vertical(self, check_board):
        for i in range(10):
            check_column = [x//10 for x in check_board if x%10==i]
            if self.check_horizontal(check_column):
                return True
            else:
                continue
        return False
    
    def check_diagonal(self, check_board):
        for i in range(10):
            check_column = [x//10 for x in check_board if x%9==i or x%11==i]
            if self.check_horizontal(check_column):
                return True
        return False
    
    def check_winner(self):
        if self.turn%2==0:
            check_board = [i for i, x in enumerate(self.board) if x==self.first_player]
            check_horizontal = self.check_horizontal(check_board)
            check_vertical = self.check_vertical(check_board)
            check_diagonal = self.check_diagonal(check_board)
            if check_horizontal or check_vertical or check_diagonal:
                print(self.first_player+"方胜出!")
                return self.first_player
            else:
                return True
        else:
            check_board = [i for i, x in enumerate(self.board) if x==self.second_player]
            check_horizontal = self.check_horizontal(check_board)
            check_vertical = self.check_vertical(check_board)
            check_diagonal = self.check_diagonal(check_board)
            if check_horizontal or check_vertical or check_diagonal:
                print(self.second_player+"方胜出!")
                return self.second_player
            else:
                return True
        
def main():
    game = board_game()
    time.sleep(0.5)
    while(game.check_winner()==True):
        game.print_board()
        game.change_board()
    time.sleep(5)

if __name__ == '__main__':
    main()