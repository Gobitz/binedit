# binedit
Small Python library to easily edit binary data in raw str form

```Python
#Examples
>>> hex2int("ff")
255

>>> b=Bin(128)
>>> b.get
'10000000'
>>> b.add(127)
>>> b.get
'1000000001111111'
>>> b.toint()
32895
>>> b.tohex()
'807f'
```