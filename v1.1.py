'''
Filename: python3_alt_inputs

Version 1.1 - 11/02/16

A Python3 module that contains input functions that automatically converts 
inputs into specified data types. E.g. "intput" would take an input and convert it into an int.

Published on GitHub by Ben Myers (ben2801) at github.com/bm2801/python3_alt_inputs

Made in Python V3.2.3

---

The MIT License (MIT)

Copyright (c) 2016 Ben Myers

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

def intput(prompt): #Converts input into integer type
    return int(input(prompt))

def strinput(prompt): #Converts input into string type
    return str(input(prompt))

def flinput(prompt): #Converts input into floating point type
    return float(input(prompt))

# END OF FILE
