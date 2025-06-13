from main import *


def TEST_SAVE_LOAD_EQ():
    x = Object("goblin", 10)
    y = Object("chest", 5)
    m = Map((5, 5), [x, y])
    m.init_maze()
    m.add_obj()
    exs1 = m.size
    exs2 = m.map.v_arr
    save_data(m, "first")
    outpt = load_data("first")
    if exs1 != outpt.size:
        return False
    for i in range(len(exs2)):
        for j in range(len(exs2[i])):
            if exs2[i][j] != outpt.map.v_arr[i][j]:
                return False
    return True


def run_all_tests():
    red_color_add = '\033[91m'
    green_color_add = '\033[92m'
    end_color_add = '\033[0m'
    success_str = green_color_add + "passed" + end_color_add
    fail_str = red_color_add + "failed" + end_color_add

    passed_tests_count = 0
    all_tests_count = 0

    test_funcs = [TEST_SAVE_LOAD_EQ]
    for test_func in test_funcs:
        test_success = test_func()
        print(test_func.__name__ + " : " + (success_str if test_success else fail_str))
        all_tests_count += 1
        passed_tests_count += (1 if test_success else 0)

    print("--------------------")
    print("Passed tests count: ", passed_tests_count)
    print("Failed tests count: ", all_tests_count - passed_tests_count)


if __name__ == "__main__":
    run_all_tests()
