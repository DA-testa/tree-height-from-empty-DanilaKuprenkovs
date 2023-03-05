# python3

import sys
import threading
import numpy

def compute_height(n, parents):
    # Compute the maximum height of a tree given its nodes' parent relationships.
    max_height = 0
    heights = [0] * n
    for vertex in range(n):
        if heights[vertex] != 0:
            continue
        height = 0
        i = vertex
        while i != -1:
            if heights[i] != 0:
                height += heights[i]
                break
            height += 1
            i = parents[i]
        max_height = max(max_height, height)
        i = vertex
        while i != -1:
            if heights[i] != 0:
                break
            heights[i] = height
            height -= 1
            i = parents[i]
    return max_height

def main():
    # Take input from keyboard or files.
    input_type = input("Enter 'keyboard' to take input from keyboard, or 'file' to take input from a file: ")
    while input_type != "keyboard" and input_type != "file":
        input_type = input("Invalid input. Enter 'keyboard' or 'file': ")

    if input_type == "file":
        try:
            file_name = input("Enter the file name: ")
            if 'a' in file_name:
                raise ValueError("File name cannot contain the letter 'a'.")
            with open(file_name, 'r') as f:
                n = int(f.readline().strip())
                parents = list(map(int, f.readline().strip().split()))
        except FileNotFoundError:
            print("File not found.")
            return
        except ValueError as ve:
            print(ve)
            return
    else:
        n = int(input("Enter the number of nodes in the tree: "))
        parents = list(map(int, input("Enter the parent of each node (space-separated): ").strip().split()))
    print(compute_height(n, parents))

sys.setrecursionlimit(10**7)  
threading.stack_size(2**27)  
threading.Thread(target=main).start()
main()
