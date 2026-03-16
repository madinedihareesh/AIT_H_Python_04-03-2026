
# Escape sequence
# \n next line
# \f line feed
# \u unicode
# \b backspace
# \t tabspace
# \v vertical tab
# \r carrige return
# \\ single back slash
# \' single qoute
# \" double qoute
# \N name space

# print('Hello\fworld')
# print('\u0041')
# print('polo\by')
# print('Hello\tworld')
# print('Hello\rhi')
# print('Hello\vworld')
# print('Hello\\world')
# print('\ahello world')
# print('i am my father\'s son')
# print("yester spoke to my friend he said that\"i will be leaving US\"")
# print(bin(10))
# print('\N{yen sign}')
# print('\N{dollar sign}')
# print('\N{grinning face}')
# print('a\N{superscript two}')

name='Hard Disk'
storage=250
price=2700.00
print(name,'which is having storage of',storage,'GB and it price is',price)
# c style formatting:
'''
%s string
%i intiger
%f %F %g
'''
print('%s which is having the storage of %i and its price is %f'%(name,storage,price))
# {}place holder []sub script oparator class style
print('{0} having storage of {2}GB the price is{1}'.format(name,price,storage))
# python formating style
print(f'{name} having {storage} GB is {price}')
print(name.__sizeof__())

