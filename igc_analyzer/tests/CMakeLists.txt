set(TEST_PROJECT_NAME "${PROJECT_NAME}_tests")

set(TEST_SOURCES
    main_test.cpp
    test.cpp
)
include_directories(${CPPUTEST_INCLUDE_DIRS} ../src/)

add_executable(${TEST_PROJECT_NAME} ${TEST_SOURCES})
target_link_libraries(${TEST_PROJECT_NAME} "${PROJECT_NAME}_lib"  ${CPPUTEST_LDFLAGS})

add_custom_command(TARGET ${TEST_PROJECT_NAME} COMMAND ./${TEST_PROJECT_NAME} POST_BUILD)
