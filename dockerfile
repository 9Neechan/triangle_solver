FROM ubuntu:20.04
ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
COPY . /usr/triangle
WORKDIR /usr/triangle

RUN apt-get update && apt-get update && apt-get install -y git build-essential libpng-dev libjson-c-dev libfreetype6-dev \
                libfontconfig1-dev libgtkmm-3.0-dev libpangomm-1.4-dev \
                libgl-dev libglu-dev libglew-dev libspnav-dev cmake

RUN cd /usr/triangle/solvespace-3.0 && git submodule update --init && mkdir build && cd build && cmake .. && make && make install

RUN cd /usr/local/include && sed -i '1s/^/#include <string.h>\n/' slvs.h && cd /usr/triangle/triangle-release/build && cmake .. && make

ENTRYPOINT [ "/usr/triangle/triangle-release/build/script.a" ]