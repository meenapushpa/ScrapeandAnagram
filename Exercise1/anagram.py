import collections

class Anagrams:
    def __init__(self):
        self.sorted_dict=collections.defaultdict(list)
        with open("C:\Projects\Interview\SoftDevExercises\words.txt","r") as f:
            for line in f:
                line=line.rstrip()
                key=self.sort(line)
                self.sorted_dict[key].append(line)
    @staticmethod
    def sort(word):
        return ''.join(sorted(word))

    def search(self,word):
        return self.sorted_dict[self.sort(word)]

    def search_allsubsets(self,word,smallest_size=2):
        matches=[]
        lengths=list(range(smallest_size, len(word) + 1))
        lengths.reverse()
        for length in lengths:
            matches_for_length=set()
            for j in find_possibilities(word,length):
                matches_for_length.update(self.search(j))
            lengthcount=len(matches_for_length)
            matches.append((length,matches_for_length,lengthcount))
        return matches
    
def find_possibilities(input, length, val=''):
    if length == 0:
        return [val]
    length -=1

    result=[]
    for i in range(len(input)):
        new_value=val+input[i]
        residue = input[i+1:]
        result += find_possibilities(residue,length,new_value)
    return result

if __name__ == "__main__":
    app=Anagrams()
    s=True
    while s:
        word=input("Enter a word to find all anagrams: ")
        word=word.rstrip()
        if not word.isalpha():
            print("Only alphabetic characters allowed")
            continue
        word=word.lower()
        results=app.search_allsubsets(word)
        largestvariants, longestpair =[],[]
        longestpair=max(results)
        largestvariants=sorted(results, key=lambda x: x[2], reverse=True)
        print(f"The anagram with the largest number of variants is {longestpair[0]} and results are {longestpair[1]}")
        print(f"The longest pair of words that are anagrams of each other is {largestvariants[0][2]} and results are {largestvariants[0][1]}")
        new_word=input('Are you sure want to continue y/n?:')
        if new_word=='y':
            s=True
        else:
            print('Exit from Anagram')
            s=False