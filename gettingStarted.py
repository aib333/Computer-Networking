# welcome_assignment_answers
# Input - All nine questions given in the assignment.
# Output - The right answer for the specific question.
def welcome_assignment_answers(question):
    if question == "Are encoding and encryption the same? - Yes/No":
        answer = "No"
    elif question == "Is it possible to decrypt a message without a key? - Yes/No":
        answer = "No"
    elif question == "Is it possible to decode a message without a key? - Yes/No":
        answer = "Yes"
    elif question == "Is a hashed message supposed to be un-hashed? - Yes/No":
        answer = "No"
    elif question == "What is the SHA256 hashing value to the following message:'NYU Computer Networking' - Use SHA256 hash generator and use the answer in your code":
        answer = "705924a8ef1015e45a4cba4ef94e90ddc1163a8560de92ece16c37d354cb9ba8"
    elif question == "Is MD5 a secured hashing algorithm? - Yes/No":
        answer = "No"
    elif question == "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
        answer = 5
    elif question == "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
        answer = 3
    elif question == "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
        answer = "mTCP"
    else:
        question = input("Enter your Question")
        print('question')
        answer = "This is not the answer you are looking for is"
    return answer


# Complete all the questions.
if __name__ == "__main__":
    # use this space to debug and verify that the program works
    questions = ["Are encoding and encryption the same? - Yes/No",
                 "Is it possible to decrypt a message without a key? - Yes/No",
                 "Is it possible to decode a message without a key? - Yes/No",
                 "Is a hashed message supposed to be un-hashed? - Yes/No",
                 "What is the SHA256 hashing value to the following message: 'NYU Computer Networking' - Use SHA256 hash generator and use the answer in your code",
                 "Is MD5 a secured hashing algorithm? - Yes/No",
                 "What layer from the TCP/IP model the protocol DNS belongs to? - The answer should be a numeric number",
                 "What layer of the TCP/IP model the protocol ICMP belongs to? - The answer should be a numeric number",
                 "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?"]
    for debug_question in questions:
        print(debug_question)
        print(welcome_assignment_answers(debug_question))
        print('_________________________________________')
