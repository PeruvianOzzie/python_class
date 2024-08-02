def sentiment(message):
    happy1 = ":-)"
    sad1 = ":-("

    ret_message = "checking..."
    happy_count =  message.count(happy1)
    sad_count = message.count(sad1)

    if happy_count == 0 and sad_count == 0:
        ret_message = "none"
    elif happy_count > sad_count:
        ret_message = "happy"
    elif sad_count > happy_count:
        ret_message = "sad"
    elif happy_count == sad_count:
        ret_message = "unsure"

    return ret_message
    pass

print(sentiment("hello :-)"))