def basic_hash(input_string):
  '''
  Description: uses the ASCII values of the characters in the string, and a multiplier of 31, 
  which is a common choice in string hashing.
  '''
    hash_value = 0
    for char in input_string:
        hash_value = hash_value * 31 + ord(char)
    return hash_value

