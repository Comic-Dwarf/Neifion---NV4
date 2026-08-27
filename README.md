The Cipher works by turning characters into numbers a-z being 1-26 and a space being 27, and so far I've only been bothered to add Letters and spaces, then it pairs it to a series of 1x2 matrices, and then using the first key, a 2x2 matrix that I call K1, by multiplying the 2x2 and 1x2
then, a Prime is chosen by the user, and using a configurable python generator, a series of primes is created when they're needed using values P0, the seed prime and A B C and D
Then, I create a second 2x2 matrix using the terms Pn, for top left, Pn+1, for top right, Pn+2, for bottom left and Pn+3 for bottom right, this matric is called Qn
the new 2x2 prime matrix is then multiplied with the 1x2 matrix that has been scrambled by the K1 and character numbers
this stops frequency analysis, because the numbers ascend instead of being the same
this process is reversable, and if you have the exact same values, it'll create the same numbers
the matrices are then deconstructed using commas and straight lines, which are functionally the same, but are necessary for Decryption
and yeah, that's the Cipher
