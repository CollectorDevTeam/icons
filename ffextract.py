import fontforge
F = fontforge.open("Marvel-Icons-Font.ttf")
for name in F:
    filename = name + ".png"
    # filesvg = name + ".svg"
    F[name].export(filename, 128)
