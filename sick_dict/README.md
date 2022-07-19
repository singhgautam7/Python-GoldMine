# SickDict
An IDE friendly (auto-completion) python dictionary with dot-accessible attributes.

# Why?
- The pythonic way to access the dictionary `d['key']` is prone to errors and honestly, pretty ugly.
- The case becomes worse when the dictionary is a nested one `d['key1]['key2']`. Now obviously d.key1.key2.key3 is much better.
- Default python dictionary does not support auto-completion in almost all the IDE's, but SickDict will.

# How to use it?
1. Install the package:
```console
pip install sick-dict
```
2. Import the package:
```python
from sick_dict import SickDict
```

# Features
1. Create a dictionary without defining it keys beforehand
```python
sd = SickDict()
sd.hello = "world"
```
2. Pass a dictionary and all the keys in dictionary will become properties
```python
d = {'hello': 'world'}
sd = SickDict(d)
print(sd.hello)     # world
```
3. Pass keyword arguments and all the arguments will become properties
```python
sd = SickDict(hello="world", this_is="awesome")
print(sd.hello)     # world
print(sd.this_is)     # awesome
```
4. Pass both dictionary and keyword arguments
```python
d = {'hello': 'world'}
sd = SickDict(d, this_is="awesome")
print(sd.hello)     # world
print(sd.this_is)     # awesome
```
5. Pass a nested dictionary with a list
```python
foo = {
    "bar" : {
        "baz" : [{"boo" : "hoo"}, {"baba" : "loo"}]
    }
}
sd = SickDict(foo)
print(sd.bar.baz[0].boo)     # hoo
```

6. Use `del` keyword to remove a key
```python
sd = SickDict(hello="world", this_is="awesome")
del sd.hello
print(sd.hello)     # Key
```

7. Use `+` operator to combine two instances of SickDict
```python
sd1 = SickDict(hello="world")
print(sd1)      # SickDict({'hello': 'world'})

sd2 = SickDict(this_is="awesome")
print(sd2)      # SickDict({'this_is': 'awesome'})

print(sd1 + sd2)    # SickDict({'hello': 'world', 'this_is': 'awesome'})
```

9. Use other dictionary functions like `get()`, `update()` etc.
```python
sd = SickDict(hello="world")
print(sd.get('hello'))     # world

sd.update({'who_are_you': 'developer'}, this_is="awesome")
print(sd)      # SickDict({'hello': 'world', 'who_are_you': 'developer', 'this_is': 'awesome'})
```