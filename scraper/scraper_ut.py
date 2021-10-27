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
        self.f = ParseFlightFromTable(flight)


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
class TestDownloadFlightData(unittest.TestCase):
    def setUp(self):
        # data from /node/205792
        html = """
        <div class="views-field views-field-title-2"> <span class="field-content"><a href="/node/16836">Bassano, Italy <time datetime="2021-10-10T09:10:02+02:00">09:10</time></a></span> </div>
        <div class="views-field views-field-field-flight-landing-site"> <div class="field-content">Borso del Grappa, Włochy <time datetime="2021-10-10T13:14:12+02:00">13:14</time></div> </div>
        <div class="views-field views-field-field-flight-duration"> <div class="field-content">4:04:10</div> </div>
        <div class="views-field views-field-field-flight-fai-distance"> <div class="field-content">6.45km</div> </div>
        <div class="views-field views-field-field-flight-triangle-distance"> <div class="field-content">45.22km</div> </div>
        <div class="views-field views-field-field-flight-open-distance"> <div class="field-content">61.51km</div> </div> </div>
        <h1>Bassano - 2021-10-10 09:10:02 - Piotr Staszak</h1>
        <h2 class="element-invisible">Jesteś tutaj</h2><div class="breadcrumb"><a href="/">Strona główna</a></div>
        <nav class="tabs"></nav>
        <article class="node-flight view-mode-full" role="article">
        <div class="content">
        <div class="part_left">
        <div class="field field-name-field-flight-track-file"><div class="file"><a class="file-icon mime-application-octet-stream" href="https://xcportal.pl/sites/default/files/tracks/2021-10-10/2021-10-10-xct-pst-011121464029.igc" type="application/octet-stream; length=579501">2021-10-10-xct-pst-011121464029.igc</a></div></div><div class="group-stats-div field-group-div" id="node_flight_full_group_stats_div"><div class="group-flight-stats field-group-div" id="node_flight_full_group_flight_stats"><h2><span>Dane lotu</span></h2><div class="field field-name-field-flight-referee-status"><div class="label-inline">Status weryfikacji przez sędziego: </div>Nie zweryfikowany</div><div class="field field-name-field-airspace-violation-status"><div class="label-inline">Status naruszeia stref: </div>Lot nienarusza polskich stref</div><div class="field field-name-field-flight-ppg"><div class="label-inline">Lot PPG: </div>Nie</div><div class="field field-name-field-flight-no-contest"><div class="label-inline">Lot niekonkursowy: </div>Nie</div><div class="field field-name-field-flight-grecord"><div class="label-inline">GRecord: </div>Poprawny</div><div class="field field-name-field-flight-route-length"><div class="label-inline">Długość trasy: </div>61.51km</div><div class="field field-name-field-flight-route-duration"><div class="label-inline">Czas trasy: </div>4:00:50</div><div class="field field-name-field-flight-route-avg-speed"><div class="label-inline">Średnia prędkość trasy: </div>15.32km/h</div>
        <div class="field-name-field-fc-flight-stats">
        <label>Flight stats</label>
        <div class="field-collection-tabs"><div class="item-list"><ul><li class="first"><a href="#field-fc-flight-stats-tab-0">
        """
        soup = parse_html(html)
        self.p = ParseFlightFromNode(soup)

    def test_get_igc_href(self):
        self.assertEqual(self.p.flight["igc_href"], 'https://xcportal.pl/sites/default/files/tracks/2021-10-10/2021-10-10-xct-pst-011121464029.igc')

    def test_get_igc_name(self):
        self.assertEqual(self.p.flight["igc_name"], '2021-10-10-xct-pst-011121464029.igc')

    def test_get_igc_name(self):
        self.assertEqual(self.p.flight["igc_duration"], '4:04:10')

    def test_get_is_pg(self):
        self.assertEqual(self.p.flight["isPg"], True)

    def test_get_g_record(self):
        self.assertEqual(self.p.flight["GRecord"], True)

    def test_get_is_contest(self):
        self.assertEqual(self.p.flight["isContest"], True)
    
    def test_get_airspace_violation(self):
        self.assertEqual(self.p.flight["airspace_violation"], False)

    def test_get_flight_distance(self):
        self.assertEqual(self.p.flight["flight_distance"], '61.51')
    
    def test_get_flight_duration(self):
        self.assertEqual(self.p.flight["flight_duration"], '4:00:50')
    
    def test_get_flight_avg_speed(self):
        self.assertEqual(self.p.flight["flight_avg_speed"], '15.32')

# class TestDownloadFlightData(unittest.TestCase):
#     def setUp(self):
#         self.record = {'id': '21', 'node': '/node/205792', 'pilot': 'Piotr Staszak', 'pilot_avatar_small': 'https://xcportal.pl/sites/default/files/styles/avatar_small/public/pictures/picture-default.png', 'points': '61.51', 'launch_country_short': 'IT', 'launch_country': 'Italy', 'launch_time': '2021-10-10T09:10:02+02:00', 'launch_time_short': '09:10', 'launch_spot': 'Bassano', 'landing_time': '2021-10-10T13:14:12+02:00', 'landing_time_short': '13:14', 'landing_spot': 'Borso del Grappa, Włochy', 'wing': 'Delta 3 ML', 'wing_logo_mini': 'https://xcportal.pl/sites/default/files/styles/producent_logo_mini/public/ozone.png'}

#     def test_download(self):
#         # print(self.record["node"])
#         flight_page_soup= getFlightPage(self.record["node"])
#         pass



if __name__ == '__main__':
    unittest.main()