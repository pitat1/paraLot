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
            std::cerr << "Error: Could not open file " << filename_ << std::endl;
            return "";
        }
    }

private:
    std::string filename_;
};
