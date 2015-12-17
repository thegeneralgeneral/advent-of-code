import md5

key = 'iwrupvqb'

def get_suffix_num_resulting_in_five_zeroes(input_string):
    number = 1
    while True:
        h = md5.new(input_string+str(number)).hexdigest()
        if h[:5] == '00000':
            return number
        number += 1

def get_suffix_num_resulting_in_six_zeroes(input_string):
    number = 1
    while True:
        h = md5.new(input_string+str(number)).hexdigest()
        if h[:6] == '000000':
            return number
        number += 1