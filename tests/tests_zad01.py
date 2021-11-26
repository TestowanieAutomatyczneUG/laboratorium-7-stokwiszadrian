class Hamming:
    def distance(self, a, b):
        result = 0
        if len(a) != len(b):
            raise ValueError("Podane genotypy maja rozne dlugosci")
        else:
            for i in range(0, len(a)):
                if a[i] != b[i]:
                    result += 1
            return result

    def distanceWithDocString(self, a, b):
        """
        >>> h.distanceWithDocString("", "")
        0
        >>> h.distanceWithDocString("A", "A")
        0
        >>> h.distanceWithDocString("G", "T")
        1
        >>> h.distanceWithDocString("GGACTGAAATCTG", "GGACTGAAATCTG")
        0
        >>> h.distanceWithDocString("GGACGGATTCTG", "AGGACGGATTCT")
        9
        >>> h.distanceWithDocString("AATG", "AAA")
        Traceback (most recent call last):
            File "C:\\Users\\astokwisz\\github-classroom\\TestowanieAutomatyczneUG\\laboratorium-7-stokwiszadrian\\tests\\tests_zad01.py", line 32, in <module>
                H.distance("AATG", "AAA")
            File "C:\\Users\\aastokwisz\\github-classroom\\TestowanieAutomatyczneUG\\laboratorium-7-stokwiszadrian\\tests\\tests_zad01.py", line 5, in distance
                raise ValueError("Podane genotypy maja rozne dlugosci")
        ValueError: Podane genotypy maja rozne dlugosci
        >>> h.distanceWithDocString("A", "")
        Traceback (most recent call last):
            File "C:\\Users\\astokwisz\\github-classroom\\TestowanieAutomatyczneUG\\laboratorium-7-stokwiszadrian\\tests\\tests_zad01.py", line 32, in <module>
                H.distance("A", "")
            File "C:\\Users\\aastokwisz\\github-classroom\\TestowanieAutomatyczneUG\\laboratorium-7-stokwiszadrian\\tests\\tests_zad01.py", line 5, in distance
                raise ValueError("Podane genotypy maja rozne dlugosci")
        ValueError: Podane genotypy maja rozne dlugosci
        >>> h.distanceWithDocString("", "G")
        Traceback (most recent call last):
            File "C:\\Users\\astokwisz\\github-classroom\\TestowanieAutomatyczneUG\\laboratorium-7-stokwiszadrian\\tests\\tests_zad01.py", line 32, in <module>
                H.distance("", "G")
            File "C:\\Users\\aastokwisz\\github-classroom\\TestowanieAutomatyczneUG\\laboratorium-7-stokwiszadrian\\tests\\tests_zad01.py", line 5, in distance
                raise ValueError("Podane genotypy maja rozne dlugosci")
        ValueError: Podane genotypy maja rozne dlugosci
        >>> h.distanceWithDocString(1, "G")
        Traceback (most recent call last):
            File "C:\\Python310\\lib\\doctest.py", line 1336, in __run
                exec(compile(example.source, filename, "single",
            File "<doctest __main__.Hamming.distanceWithDocString[8]>", line 1, in <module>
                h.distanceWithDocString(1, "G")
            File "C:\\Users\\astokwisz\\github-classroom\\TestowanieAutomatyczneUG\\laboratorium-7-stokwiszadrian\\tests\tests_zad01.py", line 56, in distanceWithDocString
                raise TypeError("Invalid type: {} and {}".format(type(a), type(b)))
        TypeError: Invalid type: <class 'int'> and <class 'str'>
        """
        if(type(a) == str and type(b) == str):
            return self.distance(a, b)
        else:
            raise TypeError("Invalid type: {} and {}".format(type(a), type(b)))



if __name__ == "__main__":

    import doctest
    # H = Hamming()
    # H.distance("G", "")
    doctest.testmod(extraglobs={'h': Hamming()})