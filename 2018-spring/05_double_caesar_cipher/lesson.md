# Double Caesar Cipher

    def double_caesar_cipher(num):

*Encryption* is a way to store private information so that only certain people should be able to access that secret information, much like storing secrets in a safe where only you and your friend know the combination. However, unlike a physical safe, there exist encryption techniques that are truly unbreakable without knowing the “combination” or “private key” that decrypts the data inside. 

Encryption is used extensively over the internet to keep private information, such bank account pin numbers and Facebook passwords, secure from eavesdroppers. Securing a message using computation is nothing new. For example, the Caesar Cipher is over 2000 years old, and is named after one of its users, Julius Caesar!

The Double Caesar Cipher is a variant of that technique which is more secure, but still quite simple. We use a secret number, called a “key,” to scramble up our message that requires the same “key” to unscramble. We do this by lining up our message with our key, and then shift over the digits of our message by the corresponding digit of our key.

For example, let’s say we want to send a secret pie recipe, 3141592653, and our secret key is 196. Then we just shift every digit in our secret over by the same digit of our key:



    *---------------------------------------------------------------------*
    |Message   |3    |1    |4    |1    |5    |9    |2    |6    |5    |3   |
    |Key       |6    |1    |9    |6    |1    |9    |6    |1    |9    |6   |
    |...       |3+6  |1+1  |4+9  |1+6  |5+1  |9+9  |2+6  |6+1  |5+9  |3+6 |
    |Result    |9    |2    |3    |7    |6    |8    |8    |7    |4    |9   |
    *---------------------------------------------------------------------*

*Note that if we add and get a number bigger than 10, we just use the last digit.*

Your task is to write a function that encrypts our secret pi (3141592653), using the input as a key. The function should return the encrypted message as an integer.

* The first 10 digits of pi are 3141592653. Your goal is to encrypt these 10 digits of pi with the key passed in the parameter. In other words, you need to transform the given 10 digits of pi to a different number using the given input and rules as follows:
  * 3141592653 is the message you want to encrypt.
  * The input number is called a key. This is the number you will use to transform the message.
  * Right-align the digits of the key with the digits of the message. Each digit of the message should have a corresponding key digit. If the key has fewer digits than the message, reuse the key with the unpaired digits. Repeat until every message digit is paired. Disregard any extra key digits.
  * For each pair of message/key digits, calculate the sum of the key and take the modulo 10 of the sum as the result.
  * Repeat the process with every digit and return the result.
  
Examples:

    >>> double_caesar_cipher(0)
    3141592653
    >>> double_caesar_cipher(1)
    4252603764
    >>> double_caesar_cipher(9677799275)
    2718281828
    >>> double_caesar_cipher(10000000000)
    3141592653
    >>> double_caesar_cipher(3141592653)
    6282084206
    >>> double_caesar_cipher(12136)
    4354104789
    >>> double_caesar_cipher(969518457)
    0
    >>> double_caesar_cipher(123)
    6264615776
