SCRIPTS
=======


>How to attach the script to the main hacking suite

Ok your script code is

```python
def scanit(host, port):
    #DO WORK HERE
```

First you have to write a new function
that will execute the scanit function

```python
def use_script(host="NONE", port="NONE"):
    if host == "NONE" and port == "NONE":
        return locals().keys()
    else:
        scanit(host, port)
```

Thats all , everything else will be 
handled from the main program
