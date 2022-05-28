# triangle_solver
## Solvespace - based triangle solver with picture export

## How to build?
### 0. Be sure you are using linux (ubuntu pref.) and you have cmake amd C++ compiler installed
### 1. Clone this repo
### 2. Unzip solvespace-3.0 and follow the instruction to manually install solvespace from their github
### 3a. Only install
#### 1) run ```./buildscript```
### 3b. Install and Run UNIT-Tests
#### 1) install GTest with ```sudo apt-get install libgtest-dev```
#### 2) ```cd /usr/src/gtest && sudo cmake CMakeLists.txt && sudo make && sudo cp *.a /usr/lib```
#### 3) run ```./buildscript tests```
### OR (manual building)
### 3b. Run these commands:
#### 1) ```cd /*path to this repo*/build``` 
#### 2) ```cmake ..```
#### 3) ```make```

## Exapmples of pictures
![alt text](https://github.com/UnicornTowa/triangle_solver/blob/main/images/example.png?raw=true)
![alt text](https://github.com/UnicornTowa/triangle_solver/blob/main/images/example2.png?raw=true)
![alt text](https://github.com/UnicornTowa/triangle_solver/blob/main/images/example3.png?raw=true)

## How to use?
#### This project is managed by a script "run" in /build. Be sure it has chmod +x rights
#### You should call script with at least 5 args.
#### ex: ```./run 3 3 4 5 myimage```
#### First argument codes the way of building a trianlge 1: two sides, one angle, 2:two angles, one side, 3: three sides
#### Next three double parameters are angles and sides values, remember sides go before angles
#### The last needed parameter is a string name of image, which will be created
#### p.s. default image is png, if u want svg or pdf, write this format as a sixth argument.

## How to run tests? (UNIT-testing with GTest)
#### GTest lib required
### 0. ```cd /*path to this repo*```
### 1. ```cd tests && mkdir build && cd build && cmake .. && make && ./tests```

## What about docker?
### You can easily pull docker image from https://hub.docker.com/repository/docker/unicorntowa/triangle
### eg of execution command: ```docker run --name *container_name* *image_name* 3 3 4 5 *picture_name* (synthaxis is the same as before)```
### eg of command to export picture: ```docker cp *container_name*:/usr/triangle/images/*picture_name*.png .```

## How about documentation?
### You can watch Doxygen-generated documentation by unpacking archive in /Documentation and running index.html in /html directory.

## What about addition testing?
### In /Stats you can find Flamegraph and Valgrind reports *or inspect them here*
#### Full program with picture export
##### FlameGraph:
![alt text](https://github.com/UnicornTowa/triangle_solver/blob/main/Stats/triangle_long_flamegraph.svg?raw=true)
##### Valgrind:
```
LEAK SUMMARY:
definitely lost: 281 bytes in 1 blocks
indirectly lost: 0 bytes in 0 blocks
possibly lost: 0 bytes in 0 blocks
still reachable: 53,236 bytes in 882 blocks
suppressed: 0 bytes in 0 blocks
```
#### Only generating .slvs from given params
##### FlameGraph:
![alt text](https://github.com/UnicornTowa/triangle_solver/blob/main/Stats/triangle_short_flamegraph.svg?raw=true)
##### Valgrind:
```
LEAK SUMMARY:
definitely lost: 0 bytes in 0 blocks
indirectly lost: 0 bytes in 0 blocks
possibly lost: 0 bytes in 0 blocks
still reachable: 6,600 bytes in 4 blocks
suppressed: 0 bytes in 0 blocks
```

## All images will be saved in /images
## Inconsistent parameters will cause an error alert


##### *project made by SPbU first-year students*
