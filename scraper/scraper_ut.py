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
        soup = parse_html(html)
        flights = get_flights(soup)
        flight = flights[0]
        self.f = Flight(flight)


    def test_get_wing_logo_mini(self):
        self.assertEqual(self.f.flight["wing_logo_mini"],"https://xcportal.pl/sites/default/files/styles/producent_logo_mini/public/dudek.png")

    def test_get_id(self):
        self.assertEqual(self.f.flight["id"], '770')
    
    def test_get_node(self):
        self.assertEqual(self.f.flight["node"], '/node/205816')
    
    def test_get_pilot(self):
        self.assertEqual(self.f.flight["pilot"], 'Bogdan Jasiński')

    def test_pilot_avatar_small(self):
        self.assertEqual(self.f.flight["pilot_avatar_small"], 'https://xcportal.pl/sites/default/files/styles/avatar_small/public/pictures/picture-58150-1546112895.jpg')

    def test_get_points(self):
        self.assertEqual(self.f.flight["points"], '0.56')
    
    def test_get_launch_country_short(self):
        self.assertEqual(self.f.flight["launch_country_short"], 'PL')
    
    def test_get_launch_country(self):
        self.assertEqual(self.f.flight["launch_country"], 'Poland')
    
    def test_get_launch_time(self):
        self.assertEqual(self.f.flight["launch_time"], '2021-10-10T10:09:04+02:00')

    def test_get_launch_time_short(self):
        self.assertEqual(self.f.flight["launch_time_short"], '10:09')

    def test_get_launch_spot(self):
        self.assertEqual(self.f.flight["launch_spot"], 'Piła')

    def test_get_landing_time(self):
        self.assertEqual(self.f.flight["landing_time"], '2021-10-10T10:13:44+02:00')

    def test_get_landing_time_short(self):
        self.assertEqual(self.f.flight["landing_time_short"], '10:13')

    def test_get_landing_time_short(self):
        self.assertEqual(self.f.flight["landing_spot"], 'Piła, Polska')

    def test_get_wing(self):
        self.assertEqual(self.f.flight["wing"], 'Orca XX 41')
    
    def test_get_wing_logo_mini(self):
        self.assertEqual(self.f.flight["wing_logo_mini"], 'https://xcportal.pl/sites/default/files/styles/producent_logo_mini/public/dudek.png')

            
# class TestDownloadFlightData(unittest.TestCase):
#     def setUp(self):
#         self.record = {'id': '21', 'node': '/node/205792', 'pilot': 'Piotr Staszak', 'pilot_avatar_small': 'https://xcportal.pl/sites/default/files/styles/avatar_small/public/pictures/picture-default.png', 'points': '61.51', 'launch_country_short': 'IT', 'launch_country': 'Italy', 'launch_time': '2021-10-10T09:10:02+02:00', 'launch_time_short': '09:10', 'launch_spot': 'Bassano', 'landing_time': '2021-10-10T13:14:12+02:00', 'landing_time_short': '13:14', 'landing_spot': 'Borso del Grappa, Włochy', 'wing': 'Delta 3 ML', 'wing_logo_mini': 'https://xcportal.pl/sites/default/files/styles/producent_logo_mini/public/ozone.png'}

#     def test_download(self):
#         # print(self.record["node"])
#         flight_page_soup= getFlightPage(self.record["node"])
#         pass



if __name__ == '__main__':
    unittest.main()