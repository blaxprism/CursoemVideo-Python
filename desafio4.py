v = input('manda o papo')
#Disseca a variável vendo todas as informações sobre ela
aln = v.isalnum()
alp = v.isalpha()
asc = v.isascii()
dec = v.isdecimal()
dig = v.isdigit()
ide = v.isidentifier()
low = v.islower()
num = v.isnumeric()
pri = v.isprintable()
spa = v.isspace()
tit = v.istitle()
upp = v.isupper()

#exibe as infomações sobre a variavel inserida
print(type(v))
print('Alfanumérico: {}',format(aln))
print('Alfa: {}',format(alp))
print('Ascii: {}',format(asc))
print('Decimal: {}',format(dec))
print('Digito: {}',format(dig))
print('Identificador: {}',format(ide))
print('Lower: {}',format(low))
print('Numerico: {}',format(num))
print('Printable: {}',format(pri))
print('Espaço: {}',format(spa))
print('Titulo: {}',format(tit))
print('Upper: {}',format(upp))