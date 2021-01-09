#!usr/bin/env python3

import string
import random
import time
import click


orientations = [[1, 0], [0, 1], [0, -1], [-1, 0], [1, 1], [1, -1],
                [-1, 1], [-1, -1]]
found_words = []


def word_finder(word, grid, grid_size):
    """
    Find and return the provided word in the provided word search grid
    if the word exist in the grid otherwise return None
    :param word: The word to be found, manually provided or from a file
    :param grid: The word search 2D list of randomly generated letters
    :param grid_size: dimension of the grid
    :return: str or None
    """
    word = word.upper()
    word_length = len(word)
    start_letter = word[0]
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):

            if start_letter == grid[i][j]:

                for orientation in orientations:
                    x_position = i
                    y_position = j
                    ending_x = x_position + word_length * orientation[0]
                    ending_y = y_position + word_length * orientation[1]

                    if (0 <= ending_x <= grid_size) and \
                            (0 <= ending_y <= grid_size):

                        for k in range(word_length):
                            char = word[k]

                            new_position_x = x_position + k * orientation[0]
                            new_position_y = y_position + k * orientation[1]
                            if grid[new_position_x][new_position_y] != char:
                                break
                            else:
                                if k == word_length - 1 and char == word[-1]:
                                    # if word not in found_words:
                                    return word
                                    # found_words.append(word)


@click.command()
@click.option('--filename', default="words.txt",
              help=' Optional File name of words')
@click.option('--grid_size', default=15,
              help='Optional Size of the word search grid')
def grid_generator(filename, grid_size):
    """
    A simple program to generate a word search puzzle board and provide an
    algorithm to find valid words provided in a text file on the board.
    The program prints out the
    results onscreen for the user
    :param filename: Text file containing your list of words
    :param grid_size: dimension of grid
    :return: list
    """
    start_time = int(round(time.time()))
    with open(filename, "r") as text_file:
        word_list = text_file.read().splitlines()
    grid = [[random.choice(string.ascii_uppercase)
             for _ in range(grid_size)]
            for _ in range(grid_size)]
    for x in range(grid_size):
        print('\t' * 10 + ' '.join(grid[x]))
    for vocabs in word_list:

        result = word_finder(vocabs, grid, grid_size)
        if result is not None:
            found_words.append(result)
    elapsed_time = int(round(time.time())) - start_time
    print(f'Elapsed time is: {elapsed_time} s\n')
    print(f'\nNumber of words found: {len(found_words)}\n')
    print(f'\n{found_words}\n')
    return found_words


if __name__ == '__main__':
    grid_generator()
