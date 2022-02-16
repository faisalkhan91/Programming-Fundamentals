# This is the sample for O(1) - Constant Time Complexity

# Method definitions
def find_nemo(nemo):
    for i in nemo[:1]:  # It will only run the first one regardless of the input n
        if i == 'nemo':
            print('Found NEMO!')


# Variables and method calls

nemo = ['nemo', 'nemo', 'dory']
find_nemo(nemo)
