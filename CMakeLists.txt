cmake_minimum_required(VERSION 3.8)
project(siha_camera_pkg)


if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 17)
endif()


if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(
    -Wall -Wextra -Wpedantic
    -O3             
    -march=native  
    -DNDEBUG        
  )
endif()

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(cv_bridge REQUIRED)
find_package(image_transport REQUIRED)
find_package(std_msgs REQUIRED) 
find_package(OpenCV REQUIRED)
find_package(px4_msgs REQUIRED)

include_directories(include ${OpenCV_INCLUDE_DIRS})

add_executable(camera_publisher src/camera_publisher.cpp)

ament_target_dependencies(camera_publisher
  rclcpp
  sensor_msgs
  cv_bridge
  image_transport
  std_msgs
  px4_msgs
)

target_link_libraries(camera_publisher ${OpenCV_LIBS})

install(TARGETS
  camera_publisher
  DESTINATION lib/${PROJECT_NAME}
)

install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()