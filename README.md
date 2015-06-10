# simple-crypto-solver

###Usage:
```solve.py Ciphertext/FilePath Level(default=2)```

####Exmaples: 
* ```solve.py "AWHJAWFOQGdtYWlsLmNvbQ"```
* ```solve.py "aWhjaWFoQGdtYWlsLmNvbQ==" 1```
* ```solve.py "C:\Users\ihciah\Desktop\c.txt"```

####Feature:
* Level=1:ROT13/BASE64/Fence(? bad translation)/BASE32
* Level=2:ROTn/BASE64(auto correct char case)/Fence/Morse Code/BASE32
* Level=3:I haven't write it

####Other info:
* Maybe there're some other scripts do the same thing
* May it will do some help to CTF decode cipertext
* Features will be added later

####Todo:
* Add Vigenere