import requests
from bs4 import BeautifulSoup

# product_code = input("Podaj kod produktu: ")
product_code = "104978580"
# url = "https://www.ceneo.pl/" + product_code + "#tab=reviews"
# url = f"https://www.ceneo.pl/#tab=reviews".format(product_code)
url = f"https://www.ceneo.pl/{product_code}#tab=reviews"
response = requests.get(url)
page_dom = BeautifulSoup(response.text, "html.parser")
opinions = page_dom.select("div.js_product-review")
all_opinions = []
for opinion in opinions:
    single_opinion = {
        "opinion_id": opinion["data-entry-id"],
        "author": opinion.select_one("span.user-post__author-name").text.strip(),
        "recommendation": opinion.select_one("span.user-post__author-recomendation > em").text.strip(),
        "stars": opinion.select_one("span.user-post__score-count").text.strip(),
        "purchased": opinion.select_one("div.review-pz").text.strip(),
        "opinion_date": opinion.select_one("span.user-post__published > time:nth-child(1)")["datetime"].strip(),
        "purchase_date": opinion.select_one("span.user-post__published > time:nth-child(2)")["datetime"].strip(),
        "useful" :opinion.select_one("button.vote-yes")["data-total-vote"].strip(),
        "unuseful": opinion.select_one("button.vote-no")["data-total-vote"].strip(),
        "content": opinion.select_one("div.user-post__text").text.strip(),
        "cons": [cons.text.strip() for cons in opinion.select("div.review-feature__title--negatives ~ div.review-feature__item")],
        "pros": [cons.text.strip() for cons in opinion.select("div.review-feature__title--positives ~ div.review-feature__item")],
    }
all_opinions.append(single_opinion)
print(all_opinions)



# author = span.user-post__author-name
# recommendation = span.user-post__author-recomendation > em
# stars = span.user-post__score-count
# purchased = div.review-pz
# opinion_date = span.user-post__published > time:nth-child(1)["datetime"]
# purchase_date = span.user-post__published > time:nth-child(2)["datetime"]
# useful = button.vote-yes["data-total-vote"]
# useful = button.vote-yes > span
# unuseful = button.vote-no["data-total-vote"]
# unuseful = button.vote-no > span
# content = div.user-post__text
# cons = div.review-feature__title--negatives ~ div.review-feature__item
# pros = div.review-feature__title--positives ~ div.review-feature__item


# print(type(page_dom))
# print(type(opinions))
# print(len(opinions))
# print(page_dom.prettify())