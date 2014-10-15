INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_WEST west)

FIND_PATH(
    WEST_INCLUDE_DIRS
    NAMES west/api.h
    HINTS $ENV{WEST_DIR}/include
        ${PC_WEST_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    WEST_LIBRARIES
    NAMES gnuradio-west
    HINTS $ENV{WEST_DIR}/lib
        ${PC_WEST_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(WEST DEFAULT_MSG WEST_LIBRARIES WEST_INCLUDE_DIRS)
MARK_AS_ADVANCED(WEST_LIBRARIES WEST_INCLUDE_DIRS)

