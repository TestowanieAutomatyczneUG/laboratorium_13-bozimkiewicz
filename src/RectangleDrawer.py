class RectangleDrawer:
    def rectangle(self, length, width):
        if length > 0 and width > 0:
            if int(length) == 1:
                return "*" * width
            elif int(width) == 1:
                return "*\n" * length
            else:
                return "*" * width + "\n" + ("*" + " " * (width - 2) + "*\n") * (length - 2) + "*" * width
        else:
            return "Wrong input"

