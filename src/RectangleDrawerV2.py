def rectangle_v2(length, width, sign):
    if int(length) > 0 and int(width) > 0:
        if int(length) == 1 and int(width) == 1:
            return sign
        elif int(length) == 1:
            return f"{sign}" * int(width)
        elif int(width) == 1:
            return f"{sign}\n" * int(length)
        else:
            return f"{sign}" * int(width) + "\n" + (f"{sign}" + " " * (int(width) - 2) + f"{sign}\n") * (int(length) - 2) + f"{sign}" * int(width)
    else:
        return "Wrong input"
