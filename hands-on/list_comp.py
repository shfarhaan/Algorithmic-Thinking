myList = [1,2,3,4,5]
[2*item for item in myList]

myList = list(range(100))
filteredList = [item for item in myList if item % 10 == 0]
filteredList

myString = 'My name is Ryan Mitchell. I live in Boston'
myString.split('.')


def cleanWord(word):
    return word.replace('.', '').lower()



[[cleanWord(word) for word in sentence.split()] for sentence in myString.split('.')]