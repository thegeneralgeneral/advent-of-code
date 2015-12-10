
def generate_chunks(input_string):
    chunk = ""
    for char in input_string:
        # If this char is the same as the last char in the current chunk,
        # or if chunk is empty and this is the first char,
        if chunk and char == chunk[0]:
            # qppend it.
            chunk += char
        # Otherwise, this is a new char:
        else:
            # yield the current chunk,
            # start a new chunk with the new char.
            if chunk:
                yield chunk
            chunk = char
    # Yield the last chunk (we're out of chars.)
    yield chunk

def look_and_say(input_string):
    result = ""
    for chunk in generate_chunks(input_string):
        result += "%s%s" % (len(chunk), chunk[0])
    return result