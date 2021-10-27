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

def getFlightPage(node):
        URL = "https://xcportal.pl"
        page = requests.get(URL + node)
        return parse_html(page.content)

def get_flights(soup):
    return soup.find_all("tr",class_=["even", "odd"])

class ParseFlightFromTable():
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

class ParseFlightFromNode():
    flight = {}
    def __init__(self, *args):
        if isinstance(args[0], element.Tag):
            page = args[0]
            self.flight = {
                "igc_href": self.get_igc_href(page),
                "igc_name": self.get_igc_name(page),
                "igc_duration": self.get_igc_duration(page),
                "isPg": self.get_is_pg(page),
                "GRecord": self.get_g_record(page),
                "isContest": self.get_is_contest(page),
                "airspace_violation": self.get_airspace_violation(page),
                "flight_distance": self.get_flight_distance(page),
                "flight_duration": self.get_flight_duration(page),
                "flight_avg_speed": self.get_flight_avg_speed(page)
            }

    def get_igc_href(self, page):
        return page.find('div', class_="field-name-field-flight-track-file").find('a',class_="file-icon mime-application-octet-stream").get('href')

    def get_igc_name(self, page):
        return page.find('div', class_="field-name-field-flight-track-file").find('a',class_="file-icon mime-application-octet-stream").get_text()

    def get_igc_duration(self, page):
        return page.find('div', class_="views-field views-field-field-flight-duration").get_text().strip()

    def get_is_pg(self, page):
        return page.find('div', class_="field-name-field-flight-ppg").get_text().split(':')[1].strip() == 'Nie'

    def get_g_record(self, page):
        return page.find('div', class_="field-name-field-flight-grecord").get_text().split(':')[1].strip() == 'Poprawny'
    
    def get_is_contest(self, page):
        return page.find('div', class_="field-name-field-flight-no-contest").get_text().split(':')[1].strip() == 'Nie'

    def get_airspace_violation(self, page):
        return page.find('div', class_="field-name-field-airspace-violation-status").get_text().split(':')[1].strip() != 'Lot nienarusza polskich stref'

    def get_flight_distance(self, page):
        return page.find('div', class_="field-name-field-flight-route-length").get_text().split(':')[1].strip()[:-len('km')]
    
    def get_flight_duration(self, page):
        return page.find('div', class_="field-name-field-flight-route-duration").get_text()[len('Czas trasy: '):]
    
    def get_flight_avg_speed(self, page):
        return page.find('div', class_="field-name-field-flight-route-avg-speed").get_text().strip()[len('Średnia prędkość trasy: '):-len('km/h')]

# %%
if __name__ == "__main__":

    soup = get_flights_table(DATE)
    flights = get_flights(soup)
    for flight in flights:
        singleFlight = ParseFlightFromTable(flight)
        print(singleFlight.flight)

    flight_page = getFlightPage("/node/205792")
    additional_flight_data = ParseFlightFromNode(flight_page)
    print(additional_flight_data.flight)




# %%
