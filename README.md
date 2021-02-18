# CodeScream

*Did you ever want your computer to scream at you when you make a mistake?*

No?

**Well now you can make it do that, anyway.**


## Instalation

```
pip install codescream
```

## Usage

Add this line somewhere in your project, preferably in the entry point.

```python
from codescream import hook
```

Unmute your speakers, do something that throws an exception :)

You can also use it to mark functions as deprecated!

```python
from codescream import deprecated

@deprecated
def foo():
    print("Do not use me!")
```

Now the computer will scream whenever someone uses the deprecated function.

## Reviews


    ja pierdole ale się przestraszyłem XDDD
    
~ [@EdwardEisenhauer](https://github.com/EdwardEisenhauer)
