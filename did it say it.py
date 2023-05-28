import openai

def did_they_say_it(name, word):
    prompt = f"Did it say it? \n\nName: {name}\nWord: {word}\nAI: "
    completion = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    response = completion.choices[0].text.strip()
    return response

def main():
    print("DId it say it ?")
    name = input("Please enter a name: ")
    word = input("Please enter a word: ")
    response = did_they_say_it(name, word)
    print(f"\nAI's response: {response}")

if __name__ == "__main__":
    main()
