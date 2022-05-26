#include <gtest/gtest.h>

#include "solve.h"
#include "solve.cpp"


TEST(Tests, Method1) {
    std::array<double, 6> res = {0,0,0,0,0,0};
    std::array<std::string, 5> args = {"1", "5", "6", "45", "testfile"};
    res = ChooseMethodAndRun(args[0].c_str(), args[1].c_str(), args[2].c_str(), args[3].c_str());

    ASSERT_EQ(CheckError(res), true);

    GenerateSlvs(res, args[4].c_str());

    FILE* f = fopen("../testfile.slvs", "r");
    ASSERT_TRUE(f != nullptr);
    std::filesystem::remove("../testfile.slvs");
    ASSERT_EQ(fclose(f), 0);

    res = solve1(10, 11, 500);
    ASSERT_EQ(CheckError(res), false);
}

TEST(Tests, Method2) {
    std::array<double, 6> res = {0,0,0,0,0,0};
    std::array<std::string, 5> args = {"2", "1", "60", "60", "testfile"};
    res = ChooseMethodAndRun(args[0].c_str(), args[1].c_str(), args[2].c_str(), args[3].c_str());

    ASSERT_EQ(CheckError(res), true);

    GenerateSlvs(res, args[4].c_str());

    FILE* f = fopen("../testfile.slvs", "r");
    ASSERT_TRUE(f != nullptr);
    std::filesystem::remove("../testfile.slvs");
    ASSERT_EQ(fclose(f), 0);

    res = solve2(10, 50, 30);
    ASSERT_EQ(CheckError(res), true);

    res = solve2(10, 150, 150);
    ASSERT_EQ(CheckError(res), false);
}

TEST(Tests, Method3) {
    std::array<double, 6> res = {0,0,0,0,0,0};
    std::array<std::string, 5> args = {"3", "1", "1", "1", "testfile"};
    res = ChooseMethodAndRun(args[0].c_str(), args[1].c_str(), args[2].c_str(), args[3].c_str());

    ASSERT_EQ(CheckError(res), true);

    GenerateSlvs(res, args[4].c_str());

    FILE* f = fopen("../testfile.slvs", "r");
    ASSERT_TRUE(f != nullptr);
    std::filesystem::remove("../testfile.slvs");
    ASSERT_EQ(fclose(f), 0);

    res = solve1(1, 1, 500);
    ASSERT_EQ(CheckError(res), false);
}

int main(int argc, char** argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
