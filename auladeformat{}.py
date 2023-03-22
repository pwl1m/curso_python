nome = 'Paulo'
sobrenome = 'Silva'
nfloat = 12.345
string ='\nNOME-{} \nSOBRENOME-{} \nNumeroFloat-{:.3f} \n{}\n'
formato=string.format(nome,sobrenome,nfloat,'Teste')
print(formato)