# PERMUTATIONS, COMBINATIONS, FACTORIALS & PROBABILITY
# n!
# 3! = 3 letter word
# For a 3 letter word, permutations are: 3 x 2 x 1 = 6
print("""          C     A      T    
         / \   / \    / \    
        A  T  C   T  C   A  
       /  /  /     \  \    \   
      T  A  T       C  A    C """)

myWord = input("Enter a word: ")
print(f"The length of the word '{myWord}' is {len(myWord)} characters.")
for i in range(len(myWord)):
    fact = i * len(myWord)
    print(i)

print(f"The number of permutations for the letters in {myWord} is {fact}.")

print(50 * '*')
f = 1
n = len(myWord)
print(f"factorial start is: {f}")
print(f"n start is: {n}")

nfact = (n * (n - f))
print(f"factorial is {f}")
print(f"nfact is {nfact}")
print(nfact)