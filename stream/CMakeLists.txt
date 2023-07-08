cmake_minimum_required(VERSION 3.10)

# set the project name
project(video_stream)

# find pkg-config
find_package(PkgConfig REQUIRED)

# find gstreamer
pkg_check_modules(GST REQUIRED gstreamer-1.0)

set(SRC src/gst_video.c)
set(EXE main)
set(OUTDIR bin)

# add the executable
add_executable(${EXE} ${SRC})

set_target_properties(${EXE} PROPERTIES RUNTIME_OUTPUT_DIRECTORY ${OUTDIR})

# link the libraries
target_link_libraries(${EXE} ${GST_LIBRARIES})

# include the directories
target_include_directories(${EXE} PUBLIC ${GST_INCLUDE_DIRS})

# add the compiler flags
target_compile_options(${EXE} PUBLIC ${GST_CFLAGS})

