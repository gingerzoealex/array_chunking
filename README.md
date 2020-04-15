# Array Chunking

The challenge is:
Given an array of length >= 0, and a positive integer N, return the contents of the array divided into N equally sized arrays.
Where the size of the original array cannot be divided equally by N, the final part should have a length equal to the remainder.

___

## Running the Tests

### First, clone the repo
with [SSH](https://help.github.com/en/github/using-git/which-remote-url-should-i-use#cloning-with-ssh-urls):
`git@github.com:gingerzoealex/array_chunking.git`

or for [HTTPS](https://help.github.com/en/github/using-git/which-remote-url-should-i-use#cloning-with-https-urls-recommended):
`git clone https://github.com/gingerzoealex/array_chunking.git`

### Install numpy: 
`pip3 install numpy`

(No other dependencies will need installed since `math` and `unittest` are included in Python3)

### Run the unit tests:

`python test_array_chunking.py`

___

`math.floor` is used to round the modulo down to the nearest whole number, to error proof the function. More info on the `math` library [here]('https://docs.python.org/3/library/math.html').

The modulo of `integer_n`, (the second argument) will be 0 if the number of items in `array` (the first argument) can be divided evenly.

If it's not 0, it finds the modulo and creates that number of arrays, "chunking" the array.