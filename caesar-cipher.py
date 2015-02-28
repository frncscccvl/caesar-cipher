# francis caccavale
# caesarcipher.py

# this is a caesar cipher encryptor and decryption, each function running in O(n*26). 
# 26 being the length of the alphabet. 

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
	    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

sentence = raw_input("What message will need encryption?\n")
cipherQuantity = input("Cipher quantity?\n")

def encryptCaesar(sentence, cipherQuantity, alphabet):
	private = [' '] * len(sentence)

	for i in range(0, len(sentence)):
		a = sentence[i]
		for j in range(0, len(alphabet)):
			if(a == alphabet[j]):
				private[i] = alphabet[((j+cipherQuantity)%26)]
				break
	
	return private
	
def decryptCaesar(sentence, cipherQuantity, alphabet):
	public = [' '] * len(sentence)
	
	for i in range(0, len(sentence)):
		a = sentence[i]
		for j in range(0, len(alphabet)):
			if(a == alphabet[j]):
				public[i] = alphabet[((j-cipherQuantity)%26)]
				break

	return public
	
a = encryptCaesar(sentence, cipherQuantity, alphabet)

print(a)

b = decryptCaesar(a, cipherQuantity, alphabet)

print(b)
