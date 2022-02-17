# This is the code that demonstrates O(n^2) or Quadratic Time complexity of an algorithm.
# Log all pairs of an array

# Method Definition

def create_pairs(boxes):

    pairs = []
    for i in range(0, len(boxes)):
        for j in range(0, len(boxes)):
            pairs.append((boxes[i], boxes[j]))

    print(pairs)


# Declarations

CONST_BOXES = [1, 2, 3, 4, 5]
create_pairs(CONST_BOXES)

# BigO (n * n) => BigO(n^2)
