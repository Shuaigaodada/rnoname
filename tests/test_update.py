import requests

result = requests.get("https://raw.githubusercontent.com/Shuaigaodada/TextRPG/main/README.md")
print(result.text)