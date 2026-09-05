import math
from itertools import permutations
# yay, maths
# yay, permutations

while True:

    # NEIFION CYPHER V6
    # WITH DEBUGGING MODE!!!!!!
    # AND WITH SPACES NOW!!!!!!!!
    # PERMUTATION OF K1!!!!!!!!!!
    # BEING ABLE TO ENCRYPT/DECRYPT WITHOUT HAVING TO GO TO THE CODE AND RUN IT AGAIN!!!!!!!!!!!!
    # A B C D NOW CHANGE EVERY ROUND!!!!!!!!
    # Qn NOW CHANGES WITH A B C D!!!!!!!!
    # CHAINING HAS BEEN ADDED!!!!!!!!
    # EVERYTHING WORKS!!!!!!!

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


    # NEIFION PRIME SEQUENCE V4
    # Yes I made 3 versions, the first didn't work with above 14 characters the second grew too exponentially and the third kept A B C D the same, which got old so now it's V4
  

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

            self.primes = [P0]

            # Storing the changing A B C D states
            # The whole shabang

            self.states = [
                (a, b, c, d)
            ]

            debug_print(
                "\n================================"
            )

            debug_print(
                "   NEIFION PRIME GENERATOR V6"
            )

            debug_print(
                "================================"
            )

            debug_print(
                f"[DEBUG] P0 = {P0}"
            )

            debug_print(
                f"[DEBUG] a0 = {a}"
            )

            debug_print(
                f"[DEBUG] b0 = {b}"
            )

            debug_print(
                f"[DEBUG] c0 = {c}"
            )

            debug_print(
                f"[DEBUG] d0 = {d}"
            )


        # DYNAMIC A B C D
        # This is the big new V6 bit.
        # I literally did this because I could
        # yay more maths

        def transform_state(self, Pnext, state):

            a, b, c, d = state

            # Large deterministic modulus.
            # This prevents A B C D from becoming fucking massive while still allowing them to become much larger than the original values.

            state_modulus = 106

            # Dynamic A

            new_a = (
                a * a
                + b * Pnext
                + d
            ) % state_modulus

            # Dynamic B

            new_b = (
                b * b
                + c * Pnext
                + a
            ) % state_modulus

            # Dynamic C

            new_c = (
                c * c
                + d * Pnext
                + b
                + 1
            ) % state_modulus

            # Dynamic D

            new_d = (
                d * d
                + a * Pnext
                + c
            ) % state_modulus

            # c cannot be zero because it is used in the prime generation modulus which would break just everything

            if new_c == 0:

                new_c = 1

            return (
                new_a,
                new_b,
                new_c,
                new_d
            )


        # GENERATE NEXT PRIME

        def generate_next(self):

            Pn = self.primes[-1]

            a, b, c, d = self.states[-1]

            debug_print(
                f"\n[DEBUG] Current Pn = {Pn}"
            )

            debug_print(
                f"[DEBUG] Current A B C D = "
                f"{a}, {b}, {c}, {d}"
            )


            # NEIFION V4 PRIME EQUATION
            # Spoiler, it hasn't changed
            # The important difference is that A B C D are no longer necessarily the same values at every step

            modulus = (
                c * Pn
                + d
            )

            modulus = abs(modulus)

            if modulus <= 0:

                raise ValueError(
                    "c*Pn+d must be greater than zero."
                )

            debug_print(
                f"[DEBUG] Modulus = {modulus}"
            )


            # Quadratic component cuz ofc,
            # I'm in High school guys, there will always be a Quadratic in my maths

            remainder = (
                Pn ** 2
                + a * Pn
                + b
            ) % modulus

            debug_print(
                f"[DEBUG] Remainder = {remainder}"
            )


            # Controlled growth, YESSSS
            # when I made V2, it just grew uncontrolably and eventually got way too big,
            # so generation would just be too big and so I had to modify it :(

            growth = (
                1
                + remainder % max(1, abs(c))
            )

            debug_print(
                f"[DEBUG] Growth = {growth}"
            )


            # Candidate for next prime
            # because if you're not prime you're a failure, remember that kids, be prime or be a failure

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
                f"[DEBUG] Pnext = {Pnext}"
            )


            # CHANGE A B C D
            # This is where V6 actually changes the parameters
            # The newly generated prime becomes part of the transformation, meaning the state changes as the prime sequence changes

            next_state = self.transform_state(
                Pnext,
                (a, b, c, d)
            )

            self.states.append(
                next_state
            )

            debug_print(
                f"[DEBUG] New a = {next_state[0]}"
            )

            debug_print(
                f"[DEBUG] New b = {next_state[1]}"
            )

            debug_print(
                f"[DEBUG] New c = {next_state[2]}"
            )

            debug_print(
                f"[DEBUG] New d = {next_state[3]}"
            )


        def get(self, n):

            # Generates only the primes required, so it's slightly optimised

            while len(self.primes) <= n:

                self.generate_next()

            return self.primes[n]


        def get_state(self, n):

            # Generates only the A B C D state required.

            while len(self.states) <= n:

                self.generate_next()

            return self.states[n]


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


        # K1 PERMUTATION
    # K1 has four elements, giving up to 4! = 24 possible permutations
    # Only invertible permutations are kept because K1 must be reversible during decryption basically this means that it changes K1 to a different matrix with the same values, but it only lets ones that can be changed forwards and backwards change the 2x1 matrix

    def make_K1_permutations(key):

        values = [
            key[0][0],
            key[0][1],
            key[1][0],
            key[1][1]
        ]

        valid_permutations = []

        for p in permutations(values):

            matrix = [
                [p[0], p[1]],
                [p[2], p[3]]
            ]

            if determinant(matrix) != 0:

                if matrix not in valid_permutations:

                    valid_permutations.append(matrix)

        return valid_permutations


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

        debug_print(
            f"[DEBUG] Inverse numerator x = {x}"
        )

        debug_print(
            f"[DEBUG] Inverse numerator y = {y}"
        )

        debug_print(
            f"[DEBUG] Determinant = {det}"
        )

        debug_print(
            f"[DEBUG] x % det = {x % det}"
        )

        debug_print(
            f"[DEBUG] y % det = {y % det}"
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
    # I bullshitted this, idk if it works well like at all

    def make_Q(primes, n):

        a, b, c, d = primes.get_state(n)

        Pn = primes.get(n)
        Pn1 = primes.get(n + 1)
        Pn2 = primes.get(n + 2)
        Pn3 = primes.get(n + 3)


        Qn = [
            [
                Pn + a,
                Pn1 + b
            ],
            [
                Pn2 + c,
                Pn3 + d
            ]
        ]


        # Check that Qn is invertible.
        # If the determinant happens to be zero, the bottom-right value is changed until it becomes invertible the process is deterministic, so encryption and decryption will both create the exact same Qn

        adjustment = 0

        while determinant(Qn) == 0:

            adjustment += 1

            Qn[1][1] = (
                Pn3
                + d
                + adjustment
            )


        debug_print(
            f"\n[DEBUG] Dynamic state for Q{n}:"
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

        debug_print(
            f"[DEBUG] Q{n} = {Qn}"
        )

        debug_print(
            f"[DEBUG] det(Q{n}) = "
            f"{determinant(Qn)}"
        )

        return Qn


    # CHAINING / DIFFUSION
    # This is the other big V6 change
    # Basically it just lets every single pair influence the next
   

    def diffusion_modulus(prime, state):

        a, b, c, d = state

        modulus = (
            abs(
                prime
                + 3 * a
                + 5 * b
                + 7 * c
                + 11 * d
            )
            + 1
        )

        return modulus


    def apply_chaining(vector, previous_ciphertext, modulus):

        # First pair has nothing before it, so there is nothing to chain.

        if previous_ciphertext is None:

            return vector


        # Add the previous ciphertext pair.

        chained_x = (
            vector[0]
            + previous_ciphertext[0] % modulus
        )

        chained_y = (
            vector[1]
            + previous_ciphertext[1] % modulus
        )


        return [
            chained_x,
            chained_y
        ]


    def undo_chaining(vector, previous_ciphertext, modulus):

        # First pair has nothing before it, so lonely in like the first couple miliseconds it is

        if previous_ciphertext is None:

            return vector


        # Subtract exactly what encryption added.

        original_x = (
            vector[0]
            - previous_ciphertext[0] % modulus
        )

        original_y = (
            vector[1]
            - previous_ciphertext[1] % modulus
        )


        return [
            original_x,
            original_y
        ]


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
        # The new version that can use spaces which you can see in the elif statement, don't ask for more characters, it will take me 10 minutes to do the Encoding and Decoding stuff, so fucking piss off, wanker be glad with what you have with this, some starving kids in Africa don't even have clean water because big Nestle says it isn't a basic human right

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
        # interesting stuff, but I'll be honest,
        # this is just for if i want to optomise it, or make it better

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
        # So it works with odd numbers,
        # which is a mistake I made cuz I'm a fuckin idiot

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


        # K1 PERMUTATIONS

        K1_permutations = make_K1_permutations(key)

        if not K1_permutations:

            raise ValueError(
                "K1 has no invertible permutations."
            )

        debug_print(
            f"[DEBUG] Valid K1 permutations: "
            f"{len(K1_permutations)}"
        )


        ciphertext = []


        # Previous ciphertext pair.
        # This is used for the new chaining system.

        previous_ciphertext = None


        # ENCRYPT EACH PAIR
        # cuz yeah, this is how I chose to do it ig,
        # makes it slightly faster, and meant I could use matrices
        # Plus now it chains so yay

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


            # CURRENT PRIME

            current_prime = primes.get(n)

            current_state = primes.get_state(n)

            current_a = current_state[0]
            current_b = current_state[1]
            current_c = current_state[2]
            current_d = current_state[3]


            debug_print(
                f"[DEBUG] Current prime P{n}: "
                f"{current_prime}"
            )

            debug_print(
                f"[DEBUG] Current a{n}: "
                f"{current_a}"
            )

            debug_print(
                f"[DEBUG] Current b{n}: "
                f"{current_b}"
            )

            debug_print(
                f"[DEBUG] Current c{n}: "
                f"{current_c}"
            )

            debug_print(
                f"[DEBUG] Current d{n}: "
                f"{current_d}"
            )


            # CHAINING
            # The new kid on the block

            chain_modulus = diffusion_modulus(
                current_prime,
                current_state
            )


            debug_print(
                f"[DEBUG] Diffusion modulus: "
                f"{chain_modulus}"
            )


            if previous_ciphertext is not None:

                debug_print(
                    f"[DEBUG] Previous ciphertext pair: "
                    f"{previous_ciphertext}"
                )


            M = apply_chaining(
                M,
                previous_ciphertext,
                chain_modulus
            )


            debug_print(
                f"[DEBUG] After chaining: "
                f"{M}"
            )


            # Apply first key
            # FINALLY WERE DOING SOME ACTUAL CRYPTOLOGY INSTEAD OF MATHS

            permutation_index = (
                current_prime
                % len(K1_permutations)
            )

            dynamic_key = K1_permutations[
                permutation_index
            ]

            debug_print(
                f"[DEBUG] K1 permutation index: "
                f"{permutation_index}"
            )

            debug_print(
                f"[DEBUG] Dynamic K1: "
                f"{dynamic_key}"
            )


            M = multiply_matrix_vector(
                dynamic_key,
                M
            )

            debug_print(
                f"[DEBUG] After dynamic K1: {M}"
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


            # Save the ciphertext pair for chaining the next pair.

            previous_ciphertext = [
                M[0],
                M[1]
            ]


            debug_print(
                f"[DEBUG] Cipher pair: "
                f"{M[0]},{M[1]}"
            )


        # FINAL CIPHERTEXT
        # Why did I do this, I turned a little Veritasium video into a 3 day obsession, it turned out to be longer than 3 days, because I had to, which is what I keep telling myself, even though I have free will, I will go out for the first time in like 6 days tomorrow, these 6 days have been dedicated to coding this bullcrap

        final_ciphertext = "|".join(
            ciphertext
        )


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


        # RECREATE K1 PERMUTATIONS
        # it basically just does the same thing it did during the Encryption

        K1_permutations = make_K1_permutations(key)

        if not K1_permutations:

            raise ValueError(
                "K1 has no invertible permutations."
            )

        debug_print(
            f"[DEBUG] Valid K1 permutations: "
            f"{len(K1_permutations)}"
        )


        numbers = []


        # Same chaining system as Encryption.
        # We need the original ciphertext pair from the previous round so that we can reverse the chaining

        previous_ciphertext = None


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


            # Read ciphertext pair

            parts = group.split(",")

            if len(parts) != 2:

                raise ValueError(
                    f"Invalid ciphertext group: "
                    f"{group}"
                )


            x, y = parts

            M = [
                int(x),
                int(y)
            ]


            debug_print(
                f"[DEBUG] Cipher pair: {M}"
            )


            # CURRENT PRIME + DYNAMIC A B C D

            current_prime = primes.get(n)

            current_state = primes.get_state(n)


            current_a = current_state[0]
            current_b = current_state[1]
            current_c = current_state[2]
            current_d = current_state[3]


            debug_print(
                f"[DEBUG] Current prime P{n}: "
                f"{current_prime}"
            )

            debug_print(
                f"[DEBUG] Current a{n}: "
                f"{current_a}"
            )

            debug_print(
                f"[DEBUG] Current b{n}: "
                f"{current_b}"
            )

            debug_print(
                f"[DEBUG] Current c{n}: "
                f"{current_c}"
            )

            debug_print(
                f"[DEBUG] Current d{n}: "
                f"{current_d}"
            )


            # GENERATE THE SAME DIFFUSION MODULUS

            chain_modulus = diffusion_modulus(
                current_prime,
                current_state
            )


            debug_print(
                f"[DEBUG] Diffusion modulus: "
                f"{chain_modulus}"
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

            current_prime = primes.get(n)

            permutation_index = (
                current_prime
                % len(K1_permutations)
            )

            dynamic_key = K1_permutations[
                permutation_index
            ]

            debug_print(
                f"[DEBUG] K1 permutation index: "
                f"{permutation_index}"
            )

            debug_print(
                f"[DEBUG] Dynamic K1: "
                f"{dynamic_key}"
            )


            M = inverse_matrix_vector(
                dynamic_key,
                M
            )

            debug_print(
                f"[DEBUG] After reversing dynamic K1: "
                f"{M}"
            )


            # UNDO CHAINING
            # You're not close to done reading this
            
            if previous_ciphertext is not None:

                debug_print(
                    f"[DEBUG] Previous ciphertext pair: "
                    f"{previous_ciphertext}"
                )


            M = undo_chaining(
                M,
                previous_ciphertext,
                chain_modulus
            )


            debug_print(
                f"[DEBUG] After reversing chaining: "
                f"{M}"
            )


            numbers.extend(M)


            # Save the CURRENT ciphertext pair.
            # Important: this must be the ciphertext before decryption changed M.

            previous_ciphertext = [
                int(x),
                int(y)
            ]


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

        print(
            "================================"
        )

        print(
            "        NEIFION CYPHER V6"
        )

        print(
            "================================"
        )


        if DEBUG_MODE:

            print()

            print(
                "********************************"
            )

            print(
                "       DEBUGGING MODE ON"
            )

            print(
                "********************************"
            )


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


        if DEBUG_MODE:

            K1_permutations = make_K1_permutations(
                key
            )


            print(
                "\n[DEBUG] Valid K1 permutations:",
                len(K1_permutations)
            )


            print(
                "[DEBUG] Maximum possible permutations: 24"
            )


        # PRIME PARAMETERS
        # this is just to make it harder to crack even if the 3rd party knows the first key and the Seed Prime (what you guys read as P0), which is the basis of the whole generation process so yeah, without A B C and D, you don't get secure talking, because there's essentially 9 keys, which work to make 3 keys
        # A B C D now change as the cipher progresses, so the original values are the starting state rather than being used forever yay

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

                print(
                    ciphertext
                )


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

                print(
                    plaintext
                )


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


    again = input(
        "\nRun Cipher again? (Y/N): "
    ).strip().upper()


    if again in ("N", "NO"):

        print(
            "Ending Encrypt/Decrypt sequence"
        )

        break


    elif again not in ("Y", "YES"):

        print(
            "Invalid choice"
        )

        break
    # THANK FUCK IT ENDED, NOW YOU, AGGRAVATING-PUSH-207/ENCRYPTEDOREO, YES YOU, CAN READ THIS BULLSHIT CIPHER I MADE, TRY AND CRACK IT, AGAIN!!!!!!, AND IDK IF YOU'VE EVEN FINSIHED CRACKING JUST NV4, THIS IS NV6, AND NOW IT SHOULD TAKE YOU A BIT LONGER IF ANY OF MY BULLSHIT HAS MADE THIS BETTER, I HOPE IT HAS, ALSO BTW HOW THE FUCK DID NV4 HOLD UP THIS LONG, IT'S A FUCKING MIRACLE, NV6 SHOULD BE EVEN FUCKING BETTER I HOPE, FUCK YES, as you can tell I have gone fucking mental bananas, this is why I should never watch Veritasium again, but I will, and I'll enjoy it 
