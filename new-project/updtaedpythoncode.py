import copy

# A nested compound object
original_list = [[1, 2, 3], [4, 5, 6]]

# 1. Shallow Copy
shallow_copied = copy.copy(original_list)
# 2. Deep Copy
deep_copied = copy.deepcopy(original_list)

# Modify a nested item
original_list[0][0] = "CHANGED"

print(f"Original: {original_list}")  # [['CHANGED', 2, 3], [4, 5, 6]]
print(f"Shallow:  {shallow_copied}")   # [['CHANGED', 2, 3], [4, 5, 6]] -> Impacted!
print(f"Deep:     {deep_copied}")      # [[1, 2, 3], [4, 5, 6]] -> Completely safe!
