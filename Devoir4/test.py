import temple as tp

# lire un fichier "filename" contenant plusieurs tests
def read_all_temple(filename):
    with open(filename,'r') as file:
        lines = file.readlines()
        number_of_test = int(lines[0].strip())
        N_list = [0 for i in range(number_of_test)]
        corridor_list = [[] for i in range(number_of_test)]
        trap_list = [[] for i in range(number_of_test)]
        adventurer_list = [[] for i in range(number_of_test)]
        out_list = [[] for i in range(number_of_test)]
        answer_list = [None for i in range(number_of_test)]
        ptr = 1
        for k in range(number_of_test):
            ptr += 1
            line = lines[ptr].strip().split(',')
            N_list[k] = int(line[0]); M = int(line[1])
            n = int(line[2]); m = int(line[3])
            ptr += 2
            for i in range(M):
                line = lines[ptr].strip().split(',')
                corridor_list[k].append((int(line[0]),int(line[1])))
                ptr += 1
            ptr += 1
            for i in range(N_list[k]):
                line = lines[ptr].strip()
                trap_list[k].append(int(line))
                ptr += 1
            ptr += 1
            for i in range(n):
                line = lines[ptr].strip()
                adventurer_list[k].append(int(line))
                ptr += 1
            ptr += 1
            for i in range(m):
                line = lines[ptr].strip()
                out_list[k].append(int(line))
                ptr += 1
            ptr += 1
            answer_list[k] = eval(lines[ptr].strip())
            ptr += 1
    return N_list, corridor_list, trap_list, adventurer_list, out_list, answer_list

# check the code
def run_all_test(filename,number_of_test):
    N, corridor, trap, adventurer, out, answer = read_all_temple(filename)
    for i in range(number_of_test-2):
        res = tp.escape_temple(N[i],corridor[i],trap[i],adventurer[i],out[i])
        if res == answer[i]:
            print("Test {} réussi".format(i+1))
        else:
            print("Test {} échoué".format(i+1))

number_of_test = 10
run_all_test("all_test.txt",number_of_test)
