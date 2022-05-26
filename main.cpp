#include "solve.h"

int main(int argc, char** argv) {
    std::array<double, 6> res = {0, 0, 0, 0, 0, 0};

    res = ChooseMethodAndRun(argv[1], argv[2], argv[3], argv[4]);

    if (!CheckError(res)) {
        std::cout << "ERROR" << std::endl;
        return 666;
    }

    std::cout << "OK.   " << GenerateSlvs(res, argv[5]) << " GENERATED" << std::endl;
    return 0;
}
