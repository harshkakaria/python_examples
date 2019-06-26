Python
3.6
.6(v3
.6
.6: 4
cf1f54eb7, Jun
27
2018, 03: 37:03) [MSC v.1900 64 bit(AMD64)]
on
win32
Type
"copyright", "credits" or "license()"
for more information.
    >> > bin(14)
'0b1110'
>> > bin(0o11)
'0b1001'
>> > bin(0x10)
'0b10000'
>> > '''oct'''
'oct'
>> > oct(10)
'0o12'
>> > '''hex'''
'hex'
>> > hex(100)
'0x64'
>> > '''Type casting'''
'Type casting'
>> > int(123.987)
123
>> > int(10 + 5j)
Traceback(most
recent
call
last):
File
"<pyshell#9>", line
1, in < module >
int(10 + 5j)
TypeError: can
't convert complex to int
>> > int(True)
1
>> > int(False)
0
>> > int("10)

SyntaxError: EOL
while scanning string literal
>> > _

0
>> > int("10")

10
>> > int("10.5")

Traceback(most
recent
call
last):
File
"<pyshell#15>", line
1, in < module >
int("10.5")
ValueError: invalid
literal
for int() with base 10: '10.5'
>> > int('ten')

Traceback(most
recent
call
last):
File
"<pyshell#16>", line
1, in < module >
int('ten')
ValueError: invalid
literal
for int() with base 10: 'ten'
>> > """float"""

'float'
>> > float(10)

10.0
>> > float(10 + 1j)

Traceback(most
recent
call
last):
File
"<pyshell#19>", line
1, in < module >
float(10 + 1j)
TypeError: can
't convert complex to float
>> > float(True)

1.0
>> > float(False)

0.0
>> > float('10')

10.0
>> > float('10.5')

10.5
>> > float('ten')

Traceback(most
recent
call
last):
File
"<pyshell#24>", line
1, in < module >
float('ten')
ValueError: could
not convert
string
to
float: 'ten'
>> > float(0b1111)

15.0
>> > float('0b1111')

Traceback(most
recent
call
last):
File
"<pyshell#27>", line
1, in < module >
float('0b1111')
ValueError: could
not convert
string
to
float: '0b1111'
>> > '''complec'''

'complec'
>> > _

'complec'
>> > '''complex'''

'complex'
>> > complex(10)

(10 + 0j)
>> > complex(10.5)

(10.5 + 0j)
>> > complex(True)

(1 + 0j)
>> > complex(False)

0j
>> > complex('ten')

Traceback(most
recent
call
last):
File
"<pyshell#35>", line
1, in < module >
complex('ten')
ValueError: complex()
arg is a
malformed
string
>> > complex('10.5"

SyntaxError: EOL
while scanning string literal
>> > complex('10.5')

(10.5 + 0j)
>> > complex('ten')

Traceback(most
recent
call
last):
File
"<pyshell#38>", line
1, in < module >
complex('ten')
ValueError: complex()
arg is a
malformed
string
>> > '''complex form 2'''

'complex form 2'
>> > complex(10, 2)

(10 + 2j)
>> > complex(True, False)

(1 + 0j)
>> > '''bool()'''

'bool()'
>> > bool(0)

False
>> > bool(1)

True
>> > bool(10)

True
>> > bool(0.1789)

True
>> > bool(0.0)

False
>> > bool(10 - 2j)

True
>> > bool('True')

True
>> > bool("False")

True
>> > bool('')

False
>> > '''str'''

'str'
>> > str(100)

'100'
>> > str(10.5)

'10.5'
>> > str(10 + 1j)

'(10+1j)'
>> > str(True)

'True'
>> > '''Fundamental data types '''

'Fundamental data types '
>> > a = 10

>> > b = 10

>> > a is b

True
>> > id(a)

2000448832
>> > id(b)

2000448832
>> > a = 10 + 2j

>> > b = 10 + 2j

>> > a is b

False
>> > id(a)

2379940137904
>> > id(b)

2379940839472
>> > a = True

>> > b = True

>> > a is b

True
>> > id(a)

1999958176
>> > id(b)

1999958176
>> > a = 'rahul'

>> > b = 'rahul'

>> > a is b

True
>> > id(a)

2379940955056
>> > id(b)

2379940955056
>> > x = [10, 20, 30, 40]

>> > b = bytes(x)

>> > type(b)

<

class 'bytes'>

>> > print(b[0])

10
>> > print(b[-1])

40
>> > for i in b:
    print(i)

10
20
30
40
>> > '''bytearry data type'''

'bytearry data type'
>> > x = [10, 20, 30]

>> > b = bytearry(x)

Traceback(most
recent
call
last):
File
"<pyshell#91>", line
1, in < module >
b = bytearry(x)
NameError: name
'bytearry' is not defined
>> > b = bytearray(x)

>> > for i in b: print(i)

10
20
30
>> > b[0] = 100

>> > for i in b: print(i)

100
20
30
>> > x = [10, 20, 30]

>> > b = bytearray(x)

>> > print(b)

bytearray(b'\n\x14\x1e')
>> > x[2] = 256

>> > b = bytearray(x)

Traceback(most
recent
call
last):
File
"<pyshell#102>", line
1, in < module >
b = bytearray(x)
ValueError: byte
must
be in range(0, 256)
>> > '''list datatype'''

'list datatype'
>> > list = [10, 20, 30, 40, rahul, True, 10.5)

SyntaxError: invalid
syntax
>> > _

'list datatype'
>> > list = [10, 20, 'rahul', True, 10]

>> > print(list)

[10, 20, 'rahul', True, 10]
>> > list[0]

10
>> > list[-1]

10
>> > list[1:3]

[20, 'rahul']
>> > list[0] = 200

>> > for i in list: print(i)

200
20
rahul
True
10
>> > list = [10, 20, 30]

>> > list.append('rahul')

>> > list

[10, 20, 30, 'rahul']
>> > list.remove(10)

>> > list

[20, 30, 'rahul']
>> > list2 = list * 2

>> > list2

[20, 30, 'rahul', 20, 30, 'rahul']
>> > '''tupel data tupes'''

'tupel data tupes'
>> > t = 910, 20, 30)

SyntaxError: invalid
syntax
>> > l = (10, 20, 30)

         >> > type(t)

Traceback(most
recent
call
last):
File
"<pyshell#124>", line
1, in < module >
        type(t)
NameError: name
't' is not defined
>> > type(l)

<


class 'tuple'>

>> > l[0]

10
>> > l[0] = 100

Traceback(most
recent
call
last):
File
"<pyshell#127>", line
1, in < module >
l[0] = 100
TypeError: 'tuple'
object
does
not support
item
assignment
>> > l.append('rahul')

Traceback(most
recent
call
last):
File
"<pyshell#128>", line
1, in < module >
l.append('rahul')
AttributeError: 'tuple'
object
has
no
attribute
'append'
>> > l

(10, 20, 30)
>> > l.remove(10)

Traceback(most
recent
call
last):
File
"<pyshell#130>", line
1, in < module >
l.remove(10)
AttributeError: 'tuple'
object
has
no
attribute
'remove'
>> > '''range data type'''

'range data type'
>> > range(10)

range(0, 10)
>> > for i in range(0, 10): print(i)

0
1
2
3
4
5
6
7
8
9
>> > r = range(10)

>> > for i in r: print(i)

0
1
2
3
4
5
6
7
8
9
>> > for i in range(10, 20): print(i)

10
11
12
13
14
15
16
17
18
19
>> > range(10, 20, 2)

range(10, 20, 2)
>> > x = range

>> > print(x)

<

class 'range'>

>> > x = range(10, 20, 30)

>> > print(x)

range(10, 20, 30)
>> > for i in x: print(i)

10
>> > x.append[2]

Traceback(most
recent
call
last):
File
"<pyshell#147>", line
1, in < module >
x.append[2]
AttributeError: 'range'
object
has
no
attribute
'append'
>> > l = list(range(10))

Traceback(most
recent
call
last):
File
"<pyshell#148>", line
1, in < module >
l = list(range(10))
TypeError: 'list'
object is not callable
>> > li = list(range(10))

Traceback(most
recent
call
last):
File
"<pyshell#149>", line
1, in < module >
li = list(range(10))
TypeError: 'list'
object is not callable
>> > ls = list(range(10))

Traceback(most
recent
call
last):
File
"<pyshell#150>", line
1, in < module >
ls = list(range(10))
TypeError: 'list'
object is not callable
>> > ls

Traceback(most
recent
call
last):
File
"<pyshell#151>", line
1, in < module >
ls
NameError: name
'ls' is not defined
>> > '''set data types'''

'set data types'
>> > s = {10, 20, 30, 'durga'}

>> > s

{'durga', 10, 20, 30}
>> > s[0]

Traceback(most
recent
call
last):
File
"<pyshell#155>", line
1, in < module >
s[0]
TypeError: 'set'
object
does
not support
indexing
>> > s.add(60)

>> > s

{'durga', 10, 20, 60, 30}
>> > s.remove(60)

>> > s

{'durga', 10, 20, 30}
>> > '''forzenset data type'''

'forzenset data type'
>> > s = {10, 20, 30, 40}

>> > fs = forzenset(s)

Traceback(most
recent
call
last):
File
"<pyshell#162>", line
1, in < module >
fs = forzenset(s)
NameError: name
'forzenset' is not defined
>> > fs = frozenset(s)

>> > fs

frozenset({40, 10, 20, 30})
>> > for i in fs: print(i)

40
10
20
30
>> > fs.add(70)

Traceback(most
recent
call
last):
File
"<pyshell#167>", line
1, in < module >
fs.add(70)
AttributeError: 'frozenset'
object
has
no
attribute
'add'
>> > fs.remove(10)

Traceback(most
recent
call
last):
File
"<pyshell#168>", line
1, in < module >
fs.remove(10)
AttributeError: 'frozenset'
object
has
no
attribute
'remove'
>> > '''dict data types'''

'dict data types'
>> > d = {101: 'durga', 102: 'ravi', 103: 'shiva'}

>> > d[101] = 'sunny'

>> > d

{101: 'sunny', 102: 'ravi', 103: 'shiva'}
>> > d = {}

>> > d['a'] = 'apple'

>> > d['b'] = 'banana'

>> > print(d)

{'a': 'apple', 'b': 'banana'}
>> >