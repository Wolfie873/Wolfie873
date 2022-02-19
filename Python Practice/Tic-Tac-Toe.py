#! python3
import pprint

theBoard = {'top-L': ' ', 'top-R': ' ', 'top-M': ' ', 'middle-L': ' ', 'middle-R': ' ', 'middle': ' ',
            'bottom-L': ' ', 'bottom-R': ' ', 'bottom-M': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----')
    print(board['middle-L'] + '|' + board['middle'] + '|' + board['middle-R'])
    print('-----')
    print(board['bottom-L'] + '|' + board['bottom-M'] + '|' + board['bottom-R'])
    
printBoard(theBoard)

print('Your move: ')
user = input()  