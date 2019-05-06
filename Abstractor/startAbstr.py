import sys

from Abstractor.Abstractor import Abstractor


def startAbstraction(string,number):



    text = string
    abstractor = Abstractor(text)
    return abstractor.truncate(float(number))




