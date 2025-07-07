'''

РЕШЕНО

You are developing an image hosting website.

You have to create a function for generating random and unique image filenames.

Create a function for generating a random 6 character string which will be used to access the photo URL.

To make sure the name is not already in use, you are given access to an PhotoManager object.

You can call it like so to make sure the name is unique

// at this point, the website has only one photo, hosted on the 'ABCDEF' url
    photoManager.nameExists('ABCDEF'); // returns true
    photoManager.nameExists('BBCDEF'); // returns false

Note: We consider two names with same letters but different cases to be unique.
'''

import random

class PhotoManager:
    def __init__(self):
        self.lst = ["ABCDEF"]

    def nameExists(self, name):
        if name in self.lst:
            return True
        return False

    def add_name(self, name):
        self.lst.append(name)

    def print_names(self):
        for i in self.lst:
            print(i)



def generateName(photoManager):
    alph = "qwertyuioplkjhgfdsazxcvbnm"
    name = "ABCDEF"
    while photoManager.nameExists(name):
        name = ""
        for _ in range(6):
            if random.randint(0,1) == 0:
                a = alph[random.randint(0, len(alph) - 1)].upper()
            else:
                a = alph[random.randint(0, len(alph) - 1)]
            name += a
    photoManager.add_name(name)
    return name

def main():
    photoManager = PhotoManager()
    photoManager.print_names()
    generateName(photoManager)
    print()
    photoManager.print_names()


if __name__ == "__main__":
    main()
