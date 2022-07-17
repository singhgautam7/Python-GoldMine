# BigDict
An IDE friendly (auto-completion) python dictionary with dot-accessible attributes.

# Why?
- The pythonic way to access the dictionary `d['key']` is prone to errors and honestly, pretty ugly.
- The case becomes worse when the dictionary is a nested one `d['key1]['key2']`. Now obviously d.key1.key2.key3 is much better.
- Default python dictionary does not support auto-completion in almost all the IDE's, but BigDict will.

# How to use it?
1. Install the package:
```console
pip install big_dict
```
2. Import the package:
```python
from big_dict import BigDict
```

# Features
1. Create a dictionary without defining it keys beforehand
```python
bd = BigDict()
bd.hello = "world"
```
2. Pass a dictionary and all the keys in dictionary will become properties
```python
d = {'hello': 'world'}
bd = BigDict(d)
print(bd.hello)     # world
```
You can also pass a nested dictionary
3. Pass keyword arguments and all the arguments will become properties
```python
bd = BigDict(hello="world", this_is="awesome")
print(bd.hello)     # world
print(bd.this_is)     # awesome
```
4. Pass both dictionary and keyword arguments
```python
d = {'hello': 'world'}
bd = BigDict(d, this_is="awesome")
print(bd.hello)     # world
print(bd.this_is)     # awesome
```
5. Pass a nested dictionary with a list
```python
foo = {
    "bar" : {
        "baz" : [{"boo" : "hoo"}, {"baba" : "loo"}]
    }
}
bd = BigDict(foo)
print(bd.bar.baz[0].boo)     # hoo
```