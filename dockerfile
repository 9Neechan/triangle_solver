FROM ubuntu:20.04

ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY . /usr/triangle
WORKDIR /usr/triangle/build

RUN apt-get update && apt-get update && apt-get install -y git build-essential libpng-dev libjson-c-dev libfreetype6-dev \
                libfontconfig1-dev libgtkmm-3.0-dev libpangomm-1.4-dev \
                libgl-dev libglu-dev libglew-dev libspnav-dev cmake libgtest-dev unzip

RUN LD_LIBRARY_PATH=/usr/local/lib && cd /usr/src/gtest && cmake CMakeLists.txt && make && cd /usr/src/gtest/lib && cp *.a /usr/lib

RUN cd /usr/triangle && unzip solvespace-3.0 && cd /usr/triangle/solvespace-3.0 && git submodule update --init && mkdir build && cd build && cmake .. && make && make install

RUN cd /usr/local/lib && cp libslvs.* /usr/lib

RUN cd /usr/triangle/tests && mkdir build && cd build && cmake .. && make && ./tests && echo "TESTS COMPLETED"

RUN cd /usr/triangle/build && cmake .. && make

ENTRYPOINT [ "/usr/triangle/build/run" ]
