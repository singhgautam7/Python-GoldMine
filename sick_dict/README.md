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
You can also pass a nested dictionary.

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
