import solve_hw as sol

### Just do "python checker.py" to launch the tests

def compare_files(file1, file2):
    f1 = open(file1,"r")
    f2 = open(file2,"r")

    theSame = True
    lineNum = 0
    while theSame:
        l1 = f1.readline()
        l2 = f2.readline()
        if l1=="" or l1=="\n":
            break
        should_be = int(l1.split()[0])
        here_is = int(l2.split()[0])
        # if should_be != here_is:
        #     print(f"Difference : should be {should_be} != {here_is }. Diff is {should_be - here_is}")
        theSame = should_be == here_is
        lineNum = lineNum+1

    f1.close()
    f2.close()

    return theSame, lineNum, should_be, here_is

def do_test(test):
    input_file = "tests/input"+str(test)+".txt"
    expected_output_file = "tests/output"+str(test)+".txt"

    sol.read_and_solve_tests(input_file, "tmp/output.txt")
    ok, errorLine, should_be, here_is = compare_files(expected_output_file, "tmp/output.txt")
    if not ok:
        print(f"Difference : should be {should_be} != {here_is } for test : {test} on line : {errorLine}")
    else:
        print("Test "+str(test)+" is ok :)")

for i in range(3,4):
    do_test(i+1)
