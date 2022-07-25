import requests
from os import system
from bs4 import BeautifulSoup as bsoup


class Article:
    def randomArticle(self):
        url = "https://en.wikipedia.org/wiki/Special:Random"
        self.artUrl = requests.get(url)

    def htmlParser(self):
        self.article = bsoup(self.artUrl.content, "html.parser")
        self.articleTitle = self.article.find(id="firstHeading").text
        self.articleBody = self.article.find(id="mw-content-text")
        self.intro = self.articleBody.find_all("p")

    def showArticle(self):
        """
        Articles with only one paragraph have the index 0 empty
        and the content start at 1 for some reason 
        """
        print()
        print(self.articleTitle, "\n")
        if len(self.intro[0]) == 1:
            print(self.intro[1].text)
        else:
            print(self.intro[0].text)
        print(f"\nAvaible at {self.artUrl.url}")


while True:
    system("clear")
    art = Article()
    art.randomArticle()
    art.htmlParser()
    
    print(f"\nWould you like to read about {art.articleTitle}? [Y/N]")

    while True:
        choice = input("\n[Q] To quit ").lower()
        if choice == "y":
            system("clear")
            art.showArticle()
            while True:
                choice = input("Read another article? [Y/N] ").lower()
                if choice == "n":
                    exit()
                elif choice == "y":
                    break 
                print("Invalid option")

        elif choice == "n":
            break
        elif choice == "q":
            exit()  
        else:
            print("Invalid option")

