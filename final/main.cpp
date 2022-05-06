#include <iostream>
#include "solve.h"
#include <fstream>
#include <string>
#include <filesystem>

int main(int argc, char** argv) {
    std::array<std::string, 6> newres = {};
    std::array<double, 6> res = {0, 0, 0, 0, 0, 0};

    {
        int num = atoi(argv[1]);
        if (num == 1)
            res = solve1(atof(argv[2]), atof(argv[3]), atof(argv[4]));
        else if (num == 2)
            res = solve2(atof(argv[2]), atof(argv[3]), atof(argv[4]));
        else if (num == 3)
            res = solve3(atof(argv[2]), atof(argv[3]), atof(argv[4]));
    }

    std::string newname = argv[5];
    newname = "../" + newname + ".slvs";

    for (auto i: res) {
        //std::cout << i << std::endl;
        if (i == 0) {
            std::cout << "ERROR" << std::endl;
            return 666;
        }
    }

    for (int i = 0; i < 6; i++) {
        newres[i] = std::to_string(res[i]);
    }

    std::string line;
    std::array<char[8], 6> str = {"1.11111", "2.22222", "3.33333", "4.44444", "5.55555", "6.66666"};

    std::ifstream in("../template.slvs");
    std::ofstream out(newname);
    std::string newin = "../newin.slvs";
        for (int i = 0; i < 6; i++) {
            while (getline(in, line)) {
                while (true) {
                    size_t pos = line.find(str[i]);
                    if (pos != std::string::npos)
                        line.replace(pos, 8, newres[i]);
                    else
                        break;
                }
                out << line << '\n';
            }
            in.close();
            out.close();
            std::filesystem::remove(newin);
            std::filesystem::copy_file(newname, newin);
            std::filesystem::remove(newname);
            in.open(newin);
            out.open(newname);
        }
    std::filesystem::rename(newin, newname);
    std::cout << "SUCCESS " << newname << " generated" << std::endl;
    return 0;
}
