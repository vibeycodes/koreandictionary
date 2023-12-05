import random

from rich.console import Console

console = Console()

def refresh_page(headline):
    console.clear()
    console.rule(f"[bold blue]:heart: {headline} :heart:[/]\n")

refresh_page(headline="Korean Dictionary 한국어 사전")
    

def read_words_from_file(file_path):
    korean_words = {}
    with open(file_path, 'r', encoding = 'utf-8') as file:
        for line in file:
            word, meaning = line.strip().split(",",1)
            korean_words[word] = meaning
    return korean_words

file_path = ("/Users/vaishnavibhade/Desktop/kwordlist.txt")
korean_words = read_words_from_file(file_path)

while True:
    random_kwords = random.choice(list(korean_words.keys()))
    console.print("-" * 35, style = "orchid")

    console.print(f"What's the meaning of {random_kwords}?",style="yellow")
    console.print()
    user_answer = input("Enter your answer here: ")
    console.print()

    if user_answer.lower() == "exit":
        console.print("Hwaiting! Come back and do revise!", style = "bold purple")
        console.print()
        break
        
    if user_answer.lower() == korean_words[random_kwords]:
        console.print("Correct answer! 정말 멋지다!", style = "yellow on green")
        console.print()
        
    else:
        console.print(f"Go study, here's the correct answer --> [white on red]{korean_words[random_kwords]}[/white on red]", style = "yellow1")
        console.print()



