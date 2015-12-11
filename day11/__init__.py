ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()

def contains_straight(input_string):
    if len(input_string) < 3:
        return False;
    for i in xrange(len(input_string)-2):
        substr = input_string[i:i+3]
        if ALPHABET.index(substr[0]) + 1 ==  ALPHABET.index(substr[1]) \
            and ALPHABET.index(substr[1]) + 1 ==  ALPHABET.index(substr[2]):
                return True

def increment_string(s):
    def _get_next_char(char, carry):
        new_index = ALPHABET.index(char) + 1
        # NEW_INDEX += 1 if carry else 0
        carry = True if new_index >= len(ALPHABET) else False
        return ALPHABET[new_index % len(ALPHABET)], carry
    
    result = []
    carry = False
    for i in range(1, len(s)+1):
        new_char, carry = _get_next_char(s[-i], carry)
        result = [new_char] + result  # prepend
        # if carry, carry on and increment the next char. otherwise, break.
        if not carry:
            break;
    
    return s[:-(len(result))] + "".join(result)

def contains_iol(input_string):
    return any([char in input_string for char in ['o', 'i', 'l']])

def contains_two_pairs(input_string):
    num_pairs = 0
    from day10 import look_and_say
    las = look_and_say(input_string)
    counts = [char for i, char in enumerate(las) if i % 2 == 0]
    return (counts.count('2')>=2)

def generate_next_password(last_pass):
    while True:
        next_pass = increment_string(last_pass)
        if contains_straight(next_pass) \
            and not contains_iol(next_pass) \
            and contains_two_pairs(next_pass):
                return next_pass
        last_pass = next_pass