 
caracteres = '! @ # $ % ( ) _ - + = { } [ ] \ | ; : " < > , . / ? ˜ ` q h w z x y a e i o u j k n m t a e i l ! @ # $ ?'.split()


alfabeto = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z '.split()
alfabeto.append(' ')



def encrypt_ltr(letra):
  indice = alfabeto.index(letra)
  return caracteres[indice]


def encrypt_msg(mensagem):
  s = ''
  for c in mensagem:
    s+=encrypt_ltr(c)
  return s

def decrypt_ctr(caracter):
  indice = caracteres.index(caracter)
  return alfabeto[indice]


def decrypt_ctrs(caracteress):
  z = ''
  for d in caracteress:
    z+=decrypt_ctrs(d)
  return z


modo = input('Você quer encriptar ou decriptografar a mensagem? ')
modo = modo.strip().lower()
if modo == 'encriptar':
  mensagem = input('Digite a mensagem para encriptar:')
  print(encrypt_msg(mensagem))
else:
  mensagem = input('Digite a mensagem para decriptografar:')
  print(decrypt_ctrs(mensagem))