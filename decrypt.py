print( "Hello, Themyscira!" )
# This is a comment that won't be interpreted as a command.
# Associate variable diana with the value "WONDER WOMAN 1984"
diana = "WONDER WOMAN 1984"

# Print a message with the true identity of Diana
print( "I believe Diana is actually " + diana )

# Define a power (function) to chant a phrase
def chant( phrase ):
    # Glue three copies together and print it as a message
    print( phrase + phrase + phrase )


# Invoke the power chant on the phrase "WONDER WOMAN 1984!"
chant( "WONDER WOMAN 1984!" )

# Define a function to find the truth by shifting the letter by the specified amount
def lassoLetter( letter, shiftAmount ):
    # Invoke the ord function to translate the letter to its ASCII code 
    # Save the code to the letterCode variable
    letterCode = ord(letter.lower())
    
    # The ASCII number representation of lowercase letter 'a'
    aAscii = ord('a')

    # The number of letters in the alphabet
    alphabetSize = 26

    # The formula to calculate the ASCII number for the decoded letter
    # Take into account looping around the alphabet
    trueLetterCode = aAscii + (((letterCode - aAscii) + shiftAmount) % alphabetSize)

    # Convert the ASCII number to the character or letter
    decodedLetter = chr(trueLetterCode)

    # Send the decoded letter back
    return decodedLetter