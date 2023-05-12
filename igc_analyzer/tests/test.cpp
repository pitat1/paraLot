#include "CppUTest/TestHarness.h"
#include "CppUTestExt/MockSupport.h"
#include "igc_analyzer.hpp"

TEST_GROUP(FileReaderTestGroup) {
    void setup() override {
        // Create a temporary file with some contents
        std::ofstream file("testfile.txt");
        file << "This is a test file\n"
             << "With multiple lines\n"
             << "And some special characters: !@#$%^&*()\n";
        file.close();
    }

    void teardown() override {
        // Remove the temporary file
        std::remove("testfile.txt");
    }
};

TEST(FileReaderTestGroup, ReadsFileContents)
{
   FileReader reader("testfile.txt");
   std::string contents = reader.read();
   STRCMP_EQUAL("This is a test file\nWith multiple lines\nAnd some special characters: !@#$%^&*()\n", contents.c_str());
}

TEST(FileReaderTestGroup, HandlesNonexistentFile) {
    FileReader reader("nonexistent.txt");
    std::string contents = reader.read();
    STRCMP_EQUAL("", contents.c_str());
}

TEST(FileReaderTestGroup, ReadsLines) {
    FileReader reader("testfile.txt");
    auto lines = reader.readLines();
    STRCMP_EQUAL("This is a test file", lines[0].c_str());
    STRCMP_EQUAL("With multiple lines", lines[1].c_str());
    STRCMP_EQUAL("And some special characters: !@#$%^&*()", lines[2].c_str());
}