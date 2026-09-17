# tuples and sets

# Tuple: unpacking
point = (3, 7)
x, y = point
print(f"x={x}, y={y}")

# Set: remove duplicates from a list
scores = [85, 90, 85, 72, 90, 100]
unique_scores = set(scores)
print(unique_scores)

# Set operations
math_students = {"Tim", "Alice", "Bob"}
science_students = {"Alice", "Charlie", "Tim"}
print(math_students & science_students)   # both classes
print(math_students - science_students)   # math only
