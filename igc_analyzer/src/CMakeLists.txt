
set(TEST_PROJECT_NAME "${PROJECT_NAME}_tests")

set(APP_LIB_SOURCE
    igc_analyzer.cpp
)

set(MAIN_SOURCES
    main.cpp
)
add_library("${PROJECT_NAME}_lib" STATIC ${APP_LIB_SOURCE})
add_executable(${PROJECT_NAME} ${MAIN_SOURCES})
target_link_libraries(${APP_NAME} "${PROJECT_NAME}_lib" Qt5::Core Qt5::Gui Qt5::Widgets Qt5::WebEngine)



# add_custom_command(TARGET ${TEST_PROJECT_NAME} COMMAND ./igc_analyzer/${TEST_PROJECT_NAME} POST_BUILD)