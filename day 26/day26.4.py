sentence = "What is the airspeed  velocity of an unladen swallow"
words = sentence.split()
result = {word: len(word) for word in words}
print(result)
