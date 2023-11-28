from random import randint
from util import COW, BULL


class BullsCode:
    def __init__(self, secret_code=None, number_of_digits=4):
        if secret_code is None:  # set a random code
            self.__secret_code = list(str(randint(0, (pow(10, number_of_digits)-1))).zfill(number_of_digits))
        else:  # get a code in constructor
            self.__secret_code = list(secret_code)

    def __str__(self):
        return f"code: {self.__secret_code}"

    def get_code(self):
        return self.__secret_code

    def get_chars_num_to_handle(self, key):
        return self.__code_mask.get_chars_num_to_handle(key)

    def check(self, compared_code):
        codeDict = {}
        result = []
        comp_code = compared_code.get_code()
        for location, char in enumerate(self.__secret_code):
            if char == comp_code[location]:
                comp_code[location] = 'x'
                result.append(BULL)
            elif char in codeDict:
                codeDict[char].append(location)
            else:
                codeDict[char] = [location]

        for location, char in enumerate(comp_code):
            if char in codeDict and len(codeDict[char]) >= 1:
                codeDict[char].pop()
                result.append(COW)

        return sorted(result)
