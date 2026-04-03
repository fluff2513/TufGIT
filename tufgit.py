import requests
import questionary
from rich import print
import subprocess

subprocess.run("clear")
print("[grey3]T[/grey3][grey19]u[/grey19][grey35]f[/grey35][grey54]G[/grey54][grey66]I[/grey66][grey82]T[/grey82] - The [bold]TUFFIEST[/bold] .gitignore file creator!")

answer = requests.get("https://www.toptal.com/developers/gitignore/api/list")
languages = answer.text.split(",")

language = questionary.select("What is the language of your project?", choices=languages).ask()

gitignore_ = requests.get(f"https://www.toptal.com/developers/gitignore/api/{language}")

with open(f".gitignore", "w") as f:
    f.write(gitignore_.text)
    
print(f"""[bright_green]Your .gitignore file succesfully create! :)[/bright_green]
Made by @Fluff2513 on GitHub.""")
