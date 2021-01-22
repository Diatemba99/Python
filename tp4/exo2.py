"""
Les instructions s = 'a' + 'b' et s = " " .join (['a', 'b']) attribuent-elles la même valeur à la
variable s ?
"""
s = 'a' + 'b'
print(s)
s1 = " " .join (['a', 'b'])
print(s1)
"""
la reponse est non car l'espace est considere comme caractere
len(s)=2
len(s1)=3
"""
