# Les caractères Unicode:

- Les caractères Unicode sont un standard de codage qui attribue un numéro unique (appelé point de code) à chaque caractère possible dans presque toutes les écritures du monde, y compris les alphabets, les symboles, les idéogrammes et les emojis. Unicode vise à fournir une représentation universelle des caractères et à surmonter les limitations des codages de caractères précédents

- Exemples :

```python

print('\U0001F7E5') # L'affichage d'une case roouge 
print('\u25A1') # L'affichage d'une case  balnche
print('\u25A0') # L'affichage  d'une case noire 
print('\U0001F7E6') # L'affichage d'une case bleue

```

```python
point_de_code = 9731
caractere = chr(point_de_code)
print(f"Le caractère correspondant au point de code Unicode {point_de_code} est '{caractere}'")

```

```console
Le caractère correspondant au point de code Unicode 9731 est '☃’
```