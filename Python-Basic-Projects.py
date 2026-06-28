# function to analyze the given string
def analyze_string(text):

    # string contain all vowels
    vowels = "aeiouAEIOU"

    # Variable to store the number of vowels
    vowel_count = 0

    # Loop through each character in the string
    for ch in text:

        # Check if the character is a vowel
        if ch in vowels:
            vowel_count += 1

    # Display the results
    print("\n--- String Analysis ---")
    print("String:", text)
    print("Length of string:", len(text))
    print("Number of vowels:", vowel_count)


# Take input from the user
user_input = input("Enter a string: ")

# Call the function to analyze the string
analyze_string(user_input)
