#include <QApplication>
#include <QWebEngineView>
#include <QUrl>
#include "IgcParser.h"

int main(int argc, char* argv[]) {
int main() {
    QApplication app(argc, argv);

    // Create a web view
    QWebEngineView view;

    // Load the OpenTopoMap website
    view.load(QUrl("https://opentopomap.org"));

    // Parse the IGC file
    IgcParser parser("track.igc");
    if (!parser.parse()) {
        std::cerr << "Failed to parse IGC file" << std::endl;
        return 1;
    }

    // Convert track points to JavaScript array
    QString trackArray = "[";
    for (const auto& point : parser.getTrackPoints()) {
        trackArray += QString("[%1,%2],").arg(point.latitude).arg(point.longitude);
    }
    trackArray.chop(1); // Remove trailing comma
    trackArray += "]";

    // Execute JavaScript code to add the track to the map
    QString script = "var latlngs = " + trackArray + ";\n"
                     "var polyline = L.polyline(latlngs, {color: 'red'}).addTo(map);\n"
                     "map.fitBounds(polyline.getBounds());\n";
    view.page()->runJavaScript(script);

    // Show the web view
    view.show();

    // Run the application
    return app.exec();
}