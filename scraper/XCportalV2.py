# %% import
from bs4 import BeautifulSoup
import requests

# %%

DATE = "2021-10"

def parse_html(page):
    return BeautifulSoup(page, "html.parser")

def get_flights_table(DATE):
    URL = "https://xcportal.pl/flights-table/"
    page = requests.get(URL+DATE)
    return parse_html(page.content)

def get_flights(soup):
    return soup.find_all("tr",class_=["even", "odd"])

def get_wing_logo_mini(flight_soup):
    has_image = flight_soup.find("td", class_="col_wing").find("img") 
    if has_image is not None:
        return has_image.get('src').split('?')[0]
    else:
        return None

def get_id(flight_soup):
    flight_id = int(flight_soup.find("td", class_="views-field-counter").get_text())
    return str(flight_id)

def get_node(flight_soup):
    return flight_soup.find("a").get('href')

def get_pilot(flight_soup):
    return flight_soup.find("td",class_="col_pilot").get_text().strip()

def get_pilot_avatar_small(flight_soup):
    url = flight_soup.find("td",class_="col_pilot").find("img").get('src')
    return url.split('?')[0]

def get_points(flight_soup):
    return flight_soup.find("td", class_="col_max_points").get_text().strip()

def get_launch_country_short(flight_soup):
    return flight_soup.find("td", class_="col_launch").find("img").get('alt')

def get_launch_country(flight_soup):
    return flight_soup.find("td", class_="col_launch").find("img").get('title')

def get_launch_time(flight_soup):
    return flight_soup.find("td", class_="col_launch").find('time').get('datetime')

def get_launch_time_short(flight_soup):
    return flight_soup.find("td", class_="col_launch").find('time').get_text()

def get_launch_spot(flight_soup):
    return flight_soup.find("td", class_="col_launch").contents[2]

def get_landing_time(flight_soup):
    return flight_soup.find("td", class_="col_landing").find('time').get('datetime')

def get_landing_time_short(flight_soup):
    return flight_soup.find("td", class_="col_landing").find('time').get_text()

def get_landing_spot(flight_soup):
    return flight_soup.find("td", class_="col_landing").contents[0].strip()

def get_wing(flight_soup):
    return flight_soup.find("td", class_="col_wing").get_text().strip()

# %%
soup = get_flights_table(DATE)
flights = get_flights(soup)

# %%
if __name__ == "__main__":

    for flight in flights:
        flight_dict = {
            "id": get_id(flight),
            "node": get_node(flight),
            "pilot": get_pilot(flight),
            "pilot_avatar_small": get_pilot_avatar_small(flight),
            "points": get_points(flight),
            "launch_country_short": get_launch_country_short(flight),
            "launch_country": get_launch_country(flight),
            "launch_time": get_launch_time(flight),
            "launch_time_short": get_launch_time_short(flight),
            "launch_spot": get_launch_spot(flight),
            "landing_time": get_landing_time(flight),
            "landing_time_short": get_landing_time_short(flight),
            "landing_spot": get_landing_spot(flight),
            "wing": get_wing(flight),
            "wing_logo_mini": get_wing_logo_mini(flight)
        }
        print(flight_dict)

# %%

