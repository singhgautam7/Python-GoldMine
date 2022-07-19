from sick_dict.src.sick_dict import SickDict


def demo_add():
    sd1 = SickDict(hello="world")
    print(f'{sd1 = }')

    sd2 = SickDict(this_is="awesome")
    print(f'{sd2 = }')

    print(f'{sd1 + sd2 = }')
