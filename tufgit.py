import requests
import questionary
from rich import print
import subprocess

subprocess.run("clear")
print("[cyan1]T[/cyan1][cyan2]u[/cyan2][medium_spring_green]f[/medium_spring_green][spring_green1]G[/spring_green1][spring_green2]I[/spring_green2][green1]T[/green1] - The [bold]TUFFIEST[/bold] .gitignore file creator!")

answer = requests.get("https://www.toptal.com/developers/gitignore/api/list")
languages = answer.text.split(",")

language = questionary.select("What is the language of your project?", choices=languages).ask()

gitignore_ = requests.get(f"https://www.toptal.com/developers/gitignore/api/{language}")

with open(f".gitignore", "w") as f:
    f.write(gitignore_.text)
    
print(f"""[bright_green]Your .gitignore file succesfully create! :)[/bright_green]
Made by @Fluff2513 on GitHub.""")