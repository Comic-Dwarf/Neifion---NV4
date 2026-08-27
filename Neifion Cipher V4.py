import math
# yay, maths

# NEIFION CYPHER V4
# WITH DEBUGGING MODE!!!!!!
# AND WITH SPACES NOW!!!!!!!!

DEBUG_MODE = True
# Change to False dude, why u Debugging


def debug_print(*args):
    """Print debugging information only when DEBUG_MODE is enabled."""
    if DEBUG_MODE:
        print(*args)


# PRIME FUNCTION
# the backbone

def is_prime(n):

    if n < 2:
        return False

    small_primes = [
        2, 3, 5, 7, 11, 13,
        17, 19, 23, 29, 31, 37
    ]

    if n in small_primes:
        return True

    for p in small_primes:

        if n % p == 0:
            return False

    # Write n - 1 as d * 2^s

    d = n - 1
    s = 0

    while d % 2 == 0:

        d //= 2
        s += 1

    # OOOOOOO Deterministic Miller-Rabin bases 
    # Guaranteed deterministic for integers below 2^64 for redundancy only :)

    bases = [
        2,
        325,
        9375,
        28178,
        450775,
        9780504,
        1795265022
    ]

    for a in bases:

        if a % n == 0:
            continue

        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(s - 1):

            x = pow(x, 2, n)

            if x == n - 1:
                break

        else:

            return False

    return True


def next_prime(n):

    debug_print(
        f"[DEBUG] Searching for prime after {n}"
    )

    n += 1

    while not is_prime(n):

        n += 1

    debug_print(
        f"[DEBUG] Next prime found: {n}"
    )

    return n


# NEIFION PRIME SEQUENCE V3
# Yes I made 3 versions, the first didn't work with above 14 characters, the second grew too exponentially and this is the third

class PrimeSequence:

    def __init__(self, P0, a, b, c, d):

        if not is_prime(P0):

            raise ValueError(
                "P0 must be prime."
            )

        if c == 0:

            raise ValueError(
                "c cannot be zero."
            )

        self.a = a
        self.b = b
        self.c = c
        self.d = d

        self.primes = [P0]

        debug_print(
            "\n================================"
        )

        debug_print(
            "   NEIFION PRIME GENERATOR V3"
        )

        debug_print(
            "================================"
        )

        debug_print(
            f"[DEBUG] P0 = {P0}"
        )

        debug_print(
            f"[DEBUG] a = {a}"
        )

        debug_print(
            f"[DEBUG] b = {b}"
        )

        debug_print(
            f"[DEBUG] c = {c}"
        )

        debug_print(
            f"[DEBUG] d = {d}"
        )

    def get(self, n):

        # Generates only the primes required, so it's slightly optimised

        while len(self.primes) <= n:

            Pn = self.primes[-1]

            index = len(self.primes)

            debug_print(
                f"\n[DEBUG] Generating P{index}"
            )

            debug_print(
                f"[DEBUG] Current Pn = {Pn}"
            )

            
            # NEIFION V3 PRIME EQUATION
            # Spoiler, it hasn't changed

            modulus = (
                self.c * Pn
                + self.d
            )

            modulus = abs(modulus)

            if modulus <= 0:

                raise ValueError(
                    "c*Pn+d must be greater than zero."
                )

            debug_print(
                f"[DEBUG] Modulus = {modulus}"
            )

            # Quadratic component cuz ofc, I'm in High school guys, there will always be a Quadratic in my maths

            remainder = (
                Pn ** 2
                + self.a * Pn
                + self.b
            ) % modulus

            debug_print(
                f"[DEBUG] Remainder = {remainder}"
            )

            # Controlled growth, YESSSS
            # when I made V2, it just grew uncontrolably and eventually got way too big, so generation would just be too big and so I had to modify it :(

            growth = (
                1
                + remainder % abs(self.c)
            )

            debug_print(
                f"[DEBUG] Growth = {growth}"
            )

            # Candidate for next prime
            #because if you're not PRIME you're a failure, remember that kids, be PRIME or be a failure

            next_value = Pn + growth

            debug_print(
                f"[DEBUG] Next value = {next_value}"
            )

            # Find next prime
            # and then the next and the next etc etc etc etc

            Pnext = next_prime(
                next_value
            )

            self.primes.append(
                Pnext
            )

            debug_print(
                f"[DEBUG] P{index} = {Pnext}"
            )

        return self.primes[n]


# MATRIX FUNCTIONS, cuz I like them
# if you don't think they're cool, you're a bloody idiot

def multiply_matrix_vector(matrix, vector):

    x = (
        matrix[0][0] * vector[0]
        + matrix[0][1] * vector[1]
    )

    y = (
        matrix[1][0] * vector[0]
        + matrix[1][1] * vector[1]
    )

    return [x, y]


def determinant(matrix):

    return (
        matrix[0][0] * matrix[1][1]
        - matrix[0][1] * matrix[1][0]
    )


def inverse_matrix_vector(matrix, vector):

    det = determinant(matrix)

    if det == 0:

        raise ValueError(
            "Matrix is not invertible."
        )

    x = (
        matrix[1][1] * vector[0]
        - matrix[0][1] * vector[1]
    )

    y = (
        -matrix[1][0] * vector[0]
        + matrix[0][0] * vector[1]
    )

    if x % det != 0 or y % det != 0:

        raise ValueError(
            "Decryption produced "
            "non-integer values."
        )

    return [
        x // det,
        y // det
    ]


# Qn GENERATION so its more compliacated
# yay 


def make_Q(primes, n):

    Qn = [
        [
            primes.get(n),
            primes.get(n + 1)
        ],
        [
            primes.get(n + 2),
            primes.get(n + 3)
        ]
    ]

    debug_print(
        f"\n[DEBUG] Q{n} = {Qn}"
    )

    return Qn


# ENCRYPTION
# FINALLY MAN LET'S GO

def encode(
    plaintext,
    key,
    P0,
    a,
    b,
    c,
    d
):

    plaintext = plaintext.upper()

    numbers = []

    # Converts letters to numbers so it actually works
    # The new version that can use spaces which you can see in the elif statement, don't ask for more characters, it will take me 10 minutes to do the Encoding and Decoding stuff, so fucking piss off, wanker. Be glad with what you have with this, some starving kids in Africa don't even have clean water because big Nestle says it isn't a basic human right

    for character in plaintext:

        if character.isalpha():
    
            number = (
                ord(character)
                   - ord('A')
                   + 1
              )
    
            numbers.append(number)

        elif character == " ":

            numbers.append(27)

    # DEBUG INFORMATION
    # interesting stuff, but I'll be honest, this is just for if i want to optomise it, or make it better

    debug_print(
        "\n================================"
    )

    debug_print(
        "         ENCODING DEBUG"
    )

    debug_print(
        "================================"
    )

    debug_print(
        f"[DEBUG] Characters entered: "
        f"{len(plaintext)}"
    )

    debug_print(
        f"[DEBUG] Letters encrypted: "
        f"{len(numbers)}"
    )

    # PADDING
    # So it works with odd numbers, which is a mistake I made cuz I'm a fuckin idiot

    if len(numbers) % 2 != 0:

        debug_print(
            "[DEBUG] Odd number of letters."
        )

        debug_print(
            "[DEBUG] Adding padding 0."
        )

        numbers.append(0)

    pair_count = len(numbers) // 2

    debug_print(
        f"[DEBUG] Matrix pairs: "
        f"{pair_count}"
    )
    # PRIME SEQUENCE
    # why are you looking at this? It's soooo boring

    primes = PrimeSequence(
        P0,
        a,
        b,
        c,
        d
    )

    ciphertext = []

    #
    # ENCRYPT EACH PAIR
    # cuz yeah, this is how I chose to do it ig, makes it slightly faster, and meant I could use matrices

    for n in range(pair_count):

        debug_print(
            "\n--------------------------------"
        )

        debug_print(
            f"[DEBUG] ENCRYPTING PAIR "
            f"{n + 1}/{pair_count}"
        )

        debug_print(
            "--------------------------------"
        )

        # Plaintext vector

        M = [
            numbers[2 * n],
            numbers[2 * n + 1]
        ]

        debug_print(
            f"[DEBUG] Plaintext vector: {M}"
        )

        # Apply first key
        # FINALLY WERE DOING SOME ACTUAL CRYPTOLOGY INSTEAD OF MATHS

        M = multiply_matrix_vector(
            key,
            M
        )

        debug_print(
            f"[DEBUG] After key matrix: {M}"
        )

        # Generate Qn
        # This is cool, I got this idea by looking at matrices and primes

        Qn = make_Q(
            primes,
            n
        )

        # Apply Qn
        # just more Qn yk

        M = multiply_matrix_vector(
            Qn,
            M
        )

        debug_print(
            f"[DEBUG] After Q{n}: {M}"
        )

        # Store ciphertext pair
        # MEMORYYY :)

        ciphertext.append(
            f"{M[0]},{M[1]}"
        )

        debug_print(
            f"[DEBUG] Cipher pair: "
            f"{M[0]},{M[1]}"
        )

    # FINAL CIPHERTEXT
    # Why did I do this, I turned a little Veritasium video into a 3 day obsession

    final_ciphertext = "|".join(ciphertext)

    debug_print(
        "\n================================"
    )

    debug_print(
        "        ENCODING COMPLETE"
    )

    debug_print(
        "================================"
    )

    debug_print(
        f"[DEBUG] Total pairs: "
        f"{pair_count}"
    )

    debug_print(
        f"[DEBUG] Ciphertext length: "
        f"{len(final_ciphertext)}"
    )

    debug_print(
        f"[DEBUG] Ciphertext groups: "
        f"{len(ciphertext)}"
    )

    return final_ciphertext



# DECRYPTION
# This is actually pretty cool, because it reverses everything up to this stage to get the numbers then Plaintext

def decode(
    ciphertext,
    key,
    P0,
    a,
    b,
    c,
    d
):

    groups = ciphertext.split("|")

    debug_print(
        "\n================================"
    )

    debug_print(
        "         DECODING DEBUG"
    )

    debug_print(
        "================================"
    )

    debug_print(
        f"[DEBUG] Cipher groups: "
        f"{len(groups)}"
    )

    primes = PrimeSequence(
        P0,
        a,
        b,
        c,
        d
    )

    numbers = []

    for n, group in enumerate(groups):

        debug_print(
            "\n--------------------------------"
        )

        debug_print(
            f"[DEBUG] DECODING PAIR "
            f"{n + 1}/{len(groups)}"
        )

        debug_print(
            "--------------------------------"
        )

        x, y = group.split(",")

        M = [
            int(x),
            int(y)
        ]

        debug_print(
            f"[DEBUG] Cipher pair: {M}"
        )

        # Generate Qn

        Qn = make_Q(
            primes,
            n
        )

        # Undo Qn

        M = inverse_matrix_vector(
            Qn,
            M
        )

        debug_print(
            f"[DEBUG] After reversing Q{n}: "
            f"{M}"
        )

        # Undo original key

        M = inverse_matrix_vector(
            key,
            M
        )

        debug_print(
            f"[DEBUG] After reversing key: "
            f"{M}"
        )

        numbers.extend(M)

    # REMOVE PADDING
    # or else it'd be gibberish

    if numbers and numbers[-1] == 0:

        debug_print(
            "[DEBUG] Removing padding."
        )

        numbers.pop()

    plaintext = ""

    # CONVERT NUMBERS BACK TO LETTERS
    # or else it would be gibberish again
    # This is the new version that can decode spaces as an extra letter, which is just how any character is stored in binary, meaning a space is the same as a letter

    for number in numbers:

        if number == 27:
    
            plaintext += " "

        elif 1 <= number <= 26:
    
            plaintext += chr(
                ord('A')
                + number
                - 1
            )
    
        else:

            raise ValueError(
            f"Invalid decoded number: "
            f"{number}"
        )

    debug_print(
        "\n================================"
    )

    debug_print(
        "        DECODING COMPLETE"
    )

    debug_print(
        "================================"
    )

    return plaintext


# USER INTERFACE
# so we can do shit

def main():

    print("================================")
    print("        NEIFION CYPHER V3")
    print("================================")

    if DEBUG_MODE:

        print()
        print("********************************")
        print("       DEBUGGING MODE ON")
        print("********************************")

    # ENCODE/DECODE CHOICE
    # might be the simplest thing here

    choice = input(
        "\n1 = Encode\n"
        "2 = Decode\n\n"
        "Choice: "
    )

    # MATRIX KEY
    # say hoorah for complexity

    print(
        "\nEnter the 2x2 key matrix."
    )

    k11 = int(
        input("Top-left: ")
    )

    k12 = int(
        input("Top-right: ")
    )

    k21 = int(
        input("Bottom-left: ")
    )

    k22 = int(
        input("Bottom-right: ")
    )

    key = [
        [k11, k12],
        [k21, k22]
    ]

    if determinant(key) == 0:

        print(
            "\nERROR: "
            "The key matrix cannot be inverted."
        )

        return

    # PRIME PARAMETERS
    # this is just to make it harder to crack even if the 3rd party knows the first key and the Seed Prime (what you guys read as P0), which is the basis of the whole generation process, so yeah, without A B C and D, you don't get secure talking, because there's essentially 9 keys, which work to make 3 keys

    print(
        "\nPrime generator parameters"
    )

    P0 = int(
        input("P0: ")
    )

    a = int(
        input("a: ")
    )

    b = int(
        input("b: ")
    )

    c = int(
        input("c: ")
    )

    d = int(
        input("d: ")
    )

    # ENCODE / DECODE
    # it took this long for me to get to the actual stuff

    try:

        if choice == "1":

            plaintext = input(
                "\nPlaintext: "
            )

            if DEBUG_MODE:

                print(
                    "\n********************************"
                )

                print(
                    "       DEBUGGING INFORMATION"
                )

                print(
                    "********************************"
                )

                print(
                    "Characters entered:",
                    len(plaintext)
                )

                print(
                    "Letters to encrypt:",
                    sum(
                        character.isalpha()
                        for character
                        in plaintext
                    )
                )

            ciphertext = encode(
                plaintext,
                key,
                P0,
                a,
                b,
                c,
                d
            )

            print(
                "\nCiphertext:"
            )

            print(ciphertext)

        elif choice == "2":

            ciphertext = input(
                "\nCiphertext: "
            )

            plaintext = decode(
                ciphertext,
                key,
                P0,
                a,
                b,
                c,
                d
            )

            print(
                "\nPlaintext:"
            )

            print(plaintext)

        else:

            print(
                "Invalid choice."
            )

    except ValueError as error:

        print(
            "\nERROR:",
            error
        )


if __name__ == "__main__":

    main()
