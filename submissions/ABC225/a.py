from itertools import permutations
S = input()
st = set()
for it in permutations(S):
    st.add("".join(it))
print(len(st))
