import unittest
from XCportalV2 import *

class TestPareFlightTableSite(unittest.TestCase):
    def setUp(self):
        html = """
            <tr class="even">
            <td class="views-field views-field-counter">
                        770          </td>
            <td class="views-field views-field-field-name col_pilot">
            <img alt="" height="50" src="https://xcportal.pl/sites/default/files/styles/avatar_small/public/pictures/picture-58150-1546112895.jpg?itok=mlnIvDiY" width="50"/>Bogdan Jasiński           </td>
            <td class="views-field views-field-field-flight-max-points col_max_points">
                        0.56<span class="triangle"> <span> </span></span></td>
            <td class="views-field views-field-title-2 col_launch">
            <img alt="PL" class="countryicon countryicon-iconset-shiny countryicon-code-pl" height="11" src="https://xcportal.pl/sites/all/modules/countryicons/iconsets/shiny/pl.png" title="Poland" width="16"/>Piła<time datetime="2021-10-10T10:09:04+02:00">10:09</time> </td>
            <td class="views-field views-field-field-flight-landing-site col_landing">
                        Piła, Polska<time datetime="2021-10-10T10:13:44+02:00">10:13</time> </td>
            <td class="views-field views-field-title-1 col_wing">
            <img alt="" height="7" src="https://xcportal.pl/sites/default/files/styles/producent_logo_mini/public/dudek.png?itok=UUeInK8v" width="30"/>Orca XX 41          </td>
            <td class="views-field views-field-view-node">
            <a href="/node/205816">przeglądaj</a> </td>
            </tr>
            """
        self.soup = parse_html(html)

    def test_get_logo_mini(self):
        flights = get_flights(self.soup)
        for flight in flights:
            logo = get_wing_logo_mini(flight)
            self.assertEqual(logo,"https://xcportal.pl/sites/default/files/styles/producent_logo_mini/public/dudek.png")

    def test_get_id(self):
        flights = get_flights(self.soup)
        for flight in flights:
            id = get_id(flight)
            self.assertEqual(id, '770')
    
    def test_get_node(self):
        flights = get_flights(self.soup)
        for flight in flights:
            node = get_node(flight)
            self.assertEqual(node, '/node/205816')
    
    def test_pilot_avatar_small(self):
        flights = get_flights(self.soup)
        for flight in flights:
            pilot = get_pilot(flight)
            self.assertEqual(pilot, 'Bogdan Jasiński')

    def test_get_pilot(self):
        flights = get_flights(self.soup)
        for flight in flights:
            pilot_avatar_small_url = get_pilot_avatar_small(flight)
            self.assertEqual(pilot_avatar_small_url, 'https://xcportal.pl/sites/default/files/styles/avatar_small/public/pictures/picture-58150-1546112895.jpg')

    def test_get_points(self):
        flights = get_flights(self.soup)
        for flight in flights:
            points = get_points(flight)
            self.assertEqual(points, '0.56')
    
    def test_get_launch_country_short(self):
        flights = get_flights(self.soup)
        for flight in flights:
            launch_country_short = get_launch_country_short(flight)
            self.assertEqual(launch_country_short, 'PL')
    
    def test_get_launch_country(self):
        flights = get_flights(self.soup)
        for flight in flights:
            launch_country = get_launch_country(flight)
            self.assertEqual(launch_country, 'Poland')
    
    def test_get_launch_time(self):
        flights = get_flights(self.soup)
        for flight in flights:
            launch_time = get_launch_time(flight)
            self.assertEqual(launch_time, '2021-10-10T10:09:04+02:00')

    def test_get_launch_time_short(self):
        flights = get_flights(self.soup)
        for flight in flights:
            launch_time_short = get_launch_time_short(flight)
            self.assertEqual(launch_time_short, '10:09')

    def test_get_launch_spot(self):
        flights = get_flights(self.soup)
        for flight in flights:
            launch_spot = get_launch_spot(flight)
            self.assertEqual(launch_spot, 'Piła')

    def test_get_landing_time(self):
        flights = get_flights(self.soup)
        for flight in flights:
            landing_time = get_landing_time(flight)
            self.assertEqual(landing_time, '2021-10-10T10:13:44+02:00')

    def test_get_landing_time_short(self):
        flights = get_flights(self.soup)
        for flight in flights:
            landing_time_short = get_landing_time_short(flight)
            self.assertEqual(landing_time_short, '10:13')

    def test_get_landing_time_short(self):
        flights = get_flights(self.soup)
        for flight in flights:
            landing_spot = get_landing_spot(flight)
            self.assertEqual(landing_spot, 'Piła, Polska')

    def test_get_wing(self):
        flights = get_flights(self.soup)
        for flight in flights:
            wing = get_wing(flight)
            self.assertEqual(wing, 'Orca XX 41')

            
class TestDownloadFlightData(unittest.TestCase):
    def setUp(self):
        self.record = {'id': '21', 'node': '/node/205792', 'pilot': 'Piotr Staszak', 'pilot_avatar_small': 'https://xcportal.pl/sites/default/files/styles/avatar_small/public/pictures/picture-default.png', 'points': '61.51', 'launch_country_short': 'IT', 'launch_country': 'Italy', 'launch_time': '2021-10-10T09:10:02+02:00', 'launch_time_short': '09:10', 'launch_spot': 'Bassano', 'landing_time': '2021-10-10T13:14:12+02:00', 'landing_time_short': '13:14', 'landing_spot': 'Borso del Grappa, Włochy', 'wing': 'Delta 3 ML', 'wing_logo_mini': 'https://xcportal.pl/sites/default/files/styles/producent_logo_mini/public/ozone.png'}

    def test_download(self):
        pass



if __name__ == '__main__':
    unittest.main()