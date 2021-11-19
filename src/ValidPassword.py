import re


class ValidatePassword:
    def ValidPassword(self, p):
        valid = False
        if len(p) > 7:
            chars = re.compile("[$&+,:;=?@#|'<>.^*()%!-]")
            upper = re.compile("[A-Z]")
            num = re.compile("[0-9]")
            if re.search(chars, p) and re.search(upper, p) and re.search(num, p):
                valid = True
        return valid


haslo = ValidatePassword()
haslo.ValidPassword("abcdefghij")