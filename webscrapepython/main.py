import requests
from bs4 import BeautifulSoup

#try:
#    page = requests.get(URL)
#except requests.exceptions.RequestException as e:
#    raise  SystemExit(e)
def getHtml(url):
  try:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
  except requests.exceptions.RequestException as e:
        print("yeah it fucked up")
        return None
  print("Sucesss")

  return soup


def getIngredients(soup):
    ingredient = []
    try:
        items = soup.find_all("span", {"class": "wprm-recipe-ingredient-name"})
        for index, item in enumerate(items, start = 0):
            ingredient.append(items[index].get_text())

    except AttributeError as e:
        return None
    return ingredient

def getInstructions(soup):
    instructions = []
    try:
        items = soup.find_all("div", {"class": "wprm-recipe-instruction-text"})
        for index, item in enumerate(items, start = 0):
            instructions.append(items[index].get_text())
    except AttributeError as e:
        return None
    return instructions

def getTimeToCook(soup):
    try:
        time = soup.find_all("span", {"class": "wprm-recipe-details wprm-recipe-details-minutes wprm-recipe-total_time wprm-recipe-total_time-minutes"})
    except AttributeError as e:
        return None
    return time[0].get_text()

def getTimeToCookUnit(soup):
    try:
        unit = soup.find_all("span", {"class": "wprm-recipe-details-unit wprm-recipe-details-minutes wprm-recipe-total_time-unit wprm-recipe-total_timeunit-minutes"})
    except AttributeError as e:
        return None
    return unit[0].get_text()

def getServings(soup):
    try:
        servings = soup.find_all("span",   {"class": "wprm-recipe-servings-unit wprm-recipe-details-unit wprm-block-text-normal"})
    except AttributeError as e:
        return None
    return servings[0].get_text()

def getLinks(soup):
    links = []
    try:
        containers = soup.find_all("div", {"class": "entry one-fifth"})
        print("Hello")
        for index, container in enumerate(containers, start = 0):
            temp = containers[index].find_all("a", {"class": "entry-image-link"})
            links.append(temp[0]['href'])
    except AttributeError as e:
        return None
    return links


soup = getHtml('https://www.recipetineats.com/chicken-stroganoff/')
instructs = getLinks(soup)
print(instructs)


