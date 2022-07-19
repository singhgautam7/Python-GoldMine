from sick_dict.src.sick_dict import SickDict


def demo_add():
    sd1 = SickDict(hello="world")
    print(f'{sd1 = }')

    sd2 = SickDict(this_is="awesome")
    print(f'{sd2 = }')

    print(f'{sd1 + sd2 = }')


def demo_get_update():
    sd1 = SickDict(hello="world")
    sd1.update({'who_are_you': 'developer'}, this_is="awesome")
    print(f'{sd1 = }')


if __name__ == '__main__':
    demo_get_update()
