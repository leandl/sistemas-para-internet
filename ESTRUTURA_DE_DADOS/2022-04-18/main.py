# from array import array
# import numpy as np

# vetor = [10, 11, 12]
# print(vetor)
# print(vetor[2])


# vetor2 = array('i', [10, 11, 12])
# print(vetor2)
# print(vetor2[2])


# vetor3 = np.array([10, 11, 12])
# print(vetor3)
# print(vetor3[2])






from unordered_vector import UnorderedVector

my_list = UnorderedVector(10)
for i in range(5):
    my_list.insert(i)

print(my_list)
print(my_list.get_index_last_element())