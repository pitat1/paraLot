# %% import
from bs4 import BeautifulSoup, element
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
class Flight():
    flight = {}
    def __init__(self, *args):
        if isinstance(args[0], element.Tag):
            flight = args[0]
            self.flight = {
            "id": self.get_id(flight),
            "node": self.get_node(flight),
            "pilot": self.get_pilot(flight),
            "pilot_avatar_small": self.get_pilot_avatar_small(flight),
            "points": self.get_points(flight),
            "launch_country_short": self.get_launch_country_short(flight),
            "launch_country": self.get_launch_country(flight),
            "launch_time": self.get_launch_time(flight),
            "launch_time_short": self.get_launch_time_short(flight),
            "launch_spot": self.get_launch_spot(flight),
            "landing_time": self.get_landing_time(flight),
            "landing_time_short": self.get_landing_time_short(flight),
            "landing_spot": self.get_landing_spot(flight),
            "wing": self.get_wing(flight),
            "wing_logo_mini": self.get_wing_logo_mini(flight)
            }

    def get_wing_logo_mini(self, flight_soup):
        has_image = flight_soup.find("td", class_="col_wing").find("img") 
        if has_image is not None:
            return has_image.get('src').split('?')[0]
        else:
            return None

    def get_id(self, flight_soup):
        flight_id = int(flight_soup.find("td", class_="views-field-counter").get_text())
        return str(flight_id)

    def get_node(self, flight_soup):
        return flight_soup.find("a").get('href')

    def get_pilot(self, flight_soup):
        return flight_soup.find("td",class_="col_pilot").get_text().strip()

    def get_pilot_avatar_small(self, flight_soup):
        url = flight_soup.find("td",class_="col_pilot").find("img").get('src')
        return url.split('?')[0]

    def get_points(self, flight_soup):
        return flight_soup.find("td", class_="col_max_points").get_text().strip()

    def get_launch_country_short(self, flight_soup):
        return flight_soup.find("td", class_="col_launch").find("img").get('alt')

    def get_launch_country(self, flight_soup):
        return flight_soup.find("td", class_="col_launch").find("img").get('title')

    def get_launch_time(self, flight_soup):
        return flight_soup.find("td", class_="col_launch").find('time').get('datetime')

    def get_launch_time_short(self, flight_soup):
        return flight_soup.find("td", class_="col_launch").find('time').get_text()

    def get_launch_spot(self, flight_soup):
        return flight_soup.find("td", class_="col_launch").contents[2]

    def get_landing_time(self, flight_soup):
        return flight_soup.find("td", class_="col_landing").find('time').get('datetime')

    def get_landing_time_short(self, flight_soup):
        return flight_soup.find("td", class_="col_landing").find('time').get_text()

    def get_landing_spot(self, flight_soup):
        return flight_soup.find("td", class_="col_landing").contents[0].strip()

    def get_wing(self, flight_soup):
        return flight_soup.find("td", class_="col_wing").get_text().strip()

# %%
soup = get_flights_table(DATE)
flights = get_flights(soup)

# %%
if __name__ == "__main__":

    for flight in flights:
        singleFlight = Flight(flight)
        print(singleFlight.flight)

# %%

# def getFlightPage(node):
#     URL = "https://xcportal.pl"
#     page = requests.get(URL + node)
#     return parse_html(page.content)

# flight_page = getFlightPage("/node/205792")
# # %%
# igc_href = flight_page.find('div', class_="field-name-field-flight-track-file").find('a',class_="file-icon mime-application-octet-stream").get('href')
# igc_name = flight_page.find('div', class_="field-name-field-flight-track-file").find('a',class_="file-icon mime-application-octet-stream").get_text()
# print(igc_name)
# %%
