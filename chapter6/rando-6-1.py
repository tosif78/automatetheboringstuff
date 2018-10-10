# chapter 6 stuff

print('Hi')



spam = 'Hello world!'
fizz = spam[0:5]
print(fizz)



x='Hello' in 'Hello World'
print(x)

y='HELLO' in 'Hello World'
print(y)

'hello'.isalpha()

print('\n')

a = ' YES '
y = a.join(['My','name','is','Billy'])
print(y)
y2 = y.split(' YES ')
print(y2)


b = 'MyABCnameABCisABCBilly'
c = b.split('ABC')
print(c)

print('\n')

aliceExperiment = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".

Please do not drink it.
Sincerely,
Bob'''
print(aliceExperiment)

alice2 = aliceExperiment.split('\n')
print(alice2)

#print(alice2, end='')

print('\n')


hiJust = 'Hello'.rjust(10)   # total string length becomes 10
print(hiJust)                # so 5 spaces to the right of Hello

print(f"Let's talk about {hiJust}.")

#pyperclip
import pyperclip
pyperclip.copy('Hello world!')
HH=pyperclip.paste()
print(HH)
