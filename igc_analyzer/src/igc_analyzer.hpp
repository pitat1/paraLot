#include <iostream>
#include <fstream>
#include <string>
#include <vector>

class FileReader {
public:
    FileReader(std::string filename) : filename_(filename) {}

    std::string read() {
        std::ifstream file(filename_);
        if (file.is_open()) {
            std::string contents;
            std::string line;
            while (getline(file, line)) {
                contents += line + '\n';
            }
            file.close();
            return contents;
        } else {
            std::cerr << "Error: Could not open file " << filename_ << std::endl;
            return "";
        }
    }

    std::vector<std::string> readLines() {
        std::ifstream file(filename_);
        std::vector<std::string> lines;
        std::string line;
        while (std::getline(file, line)) {
            lines.push_back(line);
        }
        file.close();
        return lines;
    }

    std::string readline() {
        std::ifstream file(filename_);
        if (file.is_open()) {
            std::string contents;
            std::string line;
            while (getline(file, line)) {
                contents += line + '\n';
            }
            file.close();
            return contents;
        } else {
            std::cerr << "Error: Could not open file" << filename_ << std::endl;
            return "";
        }
    }

private:
    std::string filename_;
};


#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>

struct IgcRecord {
    std::string time;
    double latitude;
    double longitude;
    double altitude;
    double baroAltitude;
};

class IgcParser : public FileReader{
public:
    IgcParser(const std::string& filename) : FileReader(filename) {}
    std::vector<IgcRecord> parse() {

        std::vector<IgcRecord> records;
        auto igc_lines = readLines();

        for( auto line : igc_lines){
            if (line[0] == 'B') {
                IgcRecord record;
                record.time = parseTime(line);
                record.latitude = parseLatitude(line);
                record.longitude = parseLongitude(line);
                record.altitude = parseAltitude(line);
                record.baroAltitude = parseBaroAltitude(line);
                records.push_back(record);
            }
        }
        return records;
    }

private:
    std::string m_filename;

    std::string parseTime(const std::string& line) {
        return line.substr(1, 6) + ":" + line.substr(7, 2) + ":" + line.substr(9, 2);
    }

    double parseLatitude(const std::string& line) {
        std::stringstream ss(line.substr(14, 9));
        double degrees, minutes;
        ss >> degrees >> minutes;
        return degrees + minutes / 60;
    }

    double parseLongitude(const std::string& line) {
        std::stringstream ss(line.substr(24, 10));
        double degrees, minutes;
        ss >> degrees >> minutes;
        return degrees + minutes / 60;
    }

    double parseAltitude(const std::string& line) {
        std::stringstream ss(line.substr(34, 5));
        double altitude;
        ss >> altitude;
        return altitude * 0.3048;  // convert from feet to meters
    }

    double parseBaroAltitude(const std::string& line) {
        std::stringstream ss(line.substr(46, 5));
        double baroAltitude;
        ss >> baroAltitude;
        return baroAltitude * 0.3048;  // convert from feet to meters
    }
};