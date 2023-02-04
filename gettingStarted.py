
# welcome_assignment_answers
# Input - All nine questions given in the assignment.
# Output - The right answer for the specific question.

def welcome_assignment_answers(question):

    if question == "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted " \
                   "by a TA?":
        answer = mTCP
    elif question == "Are encoding and encryption the same? - Yes/No":
        answer = "No"
    elif question == "Is it possible to decrypt a message without a key? - Yes/No":
        answer = "No"
    elif question == "Is it possible to decode a message without a key? - Yes/No":
        answer = "Yes"
    elif question == "Is a hashed message supposed to be un-hashed? - Yes/No":
        answer = "No"
    elif question == "What is the SHA256 hashing value the following message: 'NYU Computer Networking' - Use SHA256" \
                     "hash generator and use the answer in your code":
        answer = "9a5631e210bcf6cf2261d93e1025901adc863378239ee1a34f2cd1772cf141f0"
    elif question == "Is MD5 a secured hashing algorithm? - Yes/No":
        answer = "No"
    elif question == "What layer from the TCP/IP model the protocol DNS belongs to? - The answer should be a " \
                     "numeric number":
        answer = 5
    elif question == "What layer of the TCP/IP model the protocol ICMP belongs to? - The answer should be a " \
                     "numeric number":
        answer = 4
    else:
        answer = "This is not the answer you're looking for."
    return answer
# Complete all the questions.


if __name__ == "__main__":
    # use this space to debug and verify that the program works
    questions = ["In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by "
                 "a TA?",
                 "Are encoding and encryption the same? - Yes/No",
                 "Is it possible to decrypt a message without a key?"
                 " - Yes/No", "Is it possible to decode a message without a key? - Yes/No", "Is a hashed message"
                 " supposed to be un-hashed? - Yes/No",
                 "What is the SHA256 hashing value the following message: 'NYU Computer Networking'- Use SHA256 hash "
                 "generator and use the answer in your code", "Is MD5 a secured"
                 " hashing algorithm? - Yes/No", "What layer from the TCP/IP model the protocol DNS belongs to? - The"
                 " answer should be a numeric number", "What layer of the TCP/IP model the protocol ICMP belongs to? -"
                 " The answer should be a numeric number"
                 ]
    for debug_question in questions:
        print(debug_question)
        print(welcome_assignment_answers(debug_question))
        print('_________________________________________')
