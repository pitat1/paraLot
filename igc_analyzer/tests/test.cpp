#include "CppUTest/TestHarness.h"
#include "CppUTestExt/MockSupport.h"
#include "igc_analyzer.hpp"

TEST_GROUP(FileLoad)
{
};

TEST(FileLoad, FirstTest)
{
   load_text_file("test");
}