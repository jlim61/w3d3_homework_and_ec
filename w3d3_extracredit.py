# Solve the Towers of Hanoi Puzzle Using RecursionThe Towers of Hanoi is a classic puzzle involving three rods and a number of disks of different sizes, which can slide onto any rod. The puzzle begins with the disks neatly stacked in ascending order of size on one rod, the smallest at the top. The objective of the puzzle is to move the entire stack to another rod, following these simple rules:

# Only one disk can be moved at a time.Each move involves taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.No disk may be placed on top of a smaller disk.

# Your task is to write a Python function using recursion to solve the Towers of Hanoi puzzle for any given number of disks. Your function should print out the steps needed to move the stack of disks from the source rod to the target rod.
# Parameters:
# n (int): The number of disks.
# source_rod (str): The rod from which a disk is moved.
# target_rod (str): The rod to which the disk is moved.
# auxiliary_rod (str): The auxiliary rod
# Returns:
# List[Tuple[str, str]]: A list of tuples representing the steps needed to move the stack of disks. Each tuple consists of two elements: the rod from which a disk is moved and the rod to which the disk is moved.
# print(towers_of_hanoi(1, 'A', 'C', 'B')) 
# # Output: [('A', 'C')]

# print(towers_of_hanoi(2, 'A', 'C', 'B'))
 
# # Output: [('A', 'B'), ('A', 'C'), ('B', 'C')]



# start rod: 3 2 1
# m rod: 
#  end rod:

# start rod: 3 2
# m rod: 
#  end rod: 1

# start rod: 3
# m rod: 2
#  end rod: 1

# start rod: 3
# m rod: 2 1
#  end rod: 

# start rod:
# m rod: 2 1
#  end rod: 3

# start rod: 1
# m rod: 2
#  end rod: 3

# start rod: 1
# m rod: 
#  end rod: 3 2

# start rod: 
# m rod: 
#  end rod: 3 2 1



def towers_recursion(n, source_rod, target_rod, aux_rod, list_of_moves):
    # base case
    if n == 1:
        list_of_moves.append((source_rod, target_rod))
        return

    # 1. sub problem n-1 moves from the source rod to the aux rod
    towers_recursion(n-1, source_rod, aux_rod, target_rod, list_of_moves)

    # 2. disk n moves form source rod to target rod
    list_of_moves.append((source_rod,target_rod))

    # 3. sub problem n-1 moves from aux rod to target rod
    towers_recursion(n-1, aux_rod, target_rod, source_rod, list_of_moves)


def towers_of_hanoi(n, source_rod, target_rod, aux_rod):
    list_of_moves = []
    towers_recursion(n, source_rod, target_rod, aux_rod, list_of_moves)
    return list_of_moves

print(towers_of_hanoi(5, 'A', 'B', 'C'))


# towers_recursion(3)
#     towers_recursion(2)
#         towers_recursion(1)
#         towers_recursion(1)
#     towers_recursion(2)
#         towers_recursion(1)
#         towers_recursion(1)