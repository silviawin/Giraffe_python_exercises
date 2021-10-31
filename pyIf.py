is_frog = True
has_tail = True

if is_frog or has_tail:
    print("You are a frog or has tail or both")
elif is_frog and not has_tail:
    print("You are a tailess frog")
elif not is_frog and not has_tail:
    print("Why are you in the lake?")
else:
    print("You are not a frog or don´t have a tail")

# and can be used instead of or



