numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List comperhension: cubes of odd numbers only
# loop over numbers if n % 2 != 0 (odd) cube and add to list
odd_cubes = [n ** 3 for n in numbers if n % 2 != 0]
print(odd_cubes)

# Dict comprehension: number -> whether it's even
# iterate over entire numbers list for each number will be key and value 
# is number % 2 == 0  True if even False if odd
even_map = {n: (n % 2 == 0) for n in numbers}
print(even_map)

