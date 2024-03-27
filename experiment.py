import ollama
import json
import sys


def llm(conversation, format="text", verbose=False):

    if verbose:
        # Print the conversation in green text
        print(f"\033[32m{conversation}\033[0m")

    response = ollama.chat(model='llama2',
                           messages=conversation,
                           format=format if format == "json" else "")

    if verbose:
        # Print the response in green text
        print(f"\033[32m{response}\033[0m")

    if format == "json":
        return json.loads(response['message']['content'].strip())
    else:
        return response['message']['content'].strip()


def get_complexity(question):
    response = llm([{
        "role":
        "system",
        "content":
        "What is the complexity of the following question? Format: { \"complexity\": <1-10> }"
    }, {
        "role": "user",
        "content": question
    }],
                   format="json")
    return response['complexity']


def think(question, thoughts=[], verbose=False):

    system_message = "You are the inner voice of a deep thinker who is thinking about how to answer the following question.\n"
    for thought in thoughts:
        system_message += f"{thought}\n"
    system_message += "What is your next single thought?" if len(
        thoughts) == 0 else "What is your first thought?"

    if verbose:
        # Print the system message with yellow text
        print(f"\033[33m{system_message}\033[0m")

    response = llm([{
        "role": "system",
        "content": system_message
    }, {
        "role": "user",
        "content": question
    }],
                   verbose=verbose)

    if verbose:
        # Print the response with green text
        print(f"\033[32m{response}\033[0m")

    return response


def answer(question, thoughts=[], verbose=False):

    system_message = "You have thought about this question and now you are answering it. Here are your inner thoughts, unknown to the user:\n\n"
    for thought in thoughts:
        system_message += f"{thought}\n\n"
    system_message += "Answer the user's question, based on your thoughts. Remember that the user has not seen your thoughts."

    if verbose:
        # Print the system message with yellow text
        print(f"\033[33m{system_message}\033[0m")

    response = llm([{
        "role": "system",
        "content": system_message
    }, {
        "role": "user",
        "content": question
    }],
                   verbose=verbose)

    if verbose:
        # Print the response with green text
        print(f"\033[32m{response}\033[0m")

    return response


def rate_answer(question, answer):
    response = llm(
        [{
            "role": "system",
            "content":
            "Rate the following answer. Format: { \"rating\": <1-10> }"
        }, {
            "role": "user",
            "content": f"{question}\n\n{answer}"
        }],
        format="json")
    return response['rating']


if __name__ == "__main__":
    verbose = sys.argv[1] == "--verbose" if len(sys.argv) > 1 else False

    question = input(
        "What is your question? ") or "What is the meaning of life?"

    collect_answers = int(
        input("How many answers do you want to collect and compare? ") or "1")

    answers = []
    for a in range(collect_answers):

        complexity = get_complexity(question)
        print(
            f"Let me think about \"{question}\". The complexity of this question is {complexity}."
        )

        thoughts = []
        for i in range(complexity):
            print(f"Thinking about \"{question}\", {i+1} of {complexity}...")
            thought = think(question, thoughts, verbose=verbose).strip()
            if thought == "":
                continue
            thoughts.append(thought)
        ans = answer(question, thoughts, verbose=verbose).strip()
        answers.append(ans)

    if verbose:
        print("Rating answers...")
    ratings = []
    for a in range(collect_answers):
        rating = rate_answer(question, answers[a])
        ratings.append(rating)

    if verbose:
        print("Answers in ascending order:")
    for rating, answer in sorted(zip(ratings, answers)):
        if verbose:
            print(f"Rating: {rating}")
        print(answer)
        if not verbose:
            break
