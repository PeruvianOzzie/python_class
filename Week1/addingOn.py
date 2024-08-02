def new_hope(num_fars):
    string1 = "A long time ago in a galaxy "
    for x in range(num_fars):
        if x < num_fars - 1:
            string1 += "far, "
        else:
            string1 += "far "

    string1 += "away..."
    return string1
    pass

print(new_hope(20))