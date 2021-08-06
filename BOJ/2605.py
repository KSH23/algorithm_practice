# 2605. 줄 세우기


def make_line(n, students):
    result = []
    
    for i in range(len(students)):
        for j in range(0, i+1):
            if students[i] == j:
                # print(result[0:j], [i+1], result[j:])
                result = result[0:j] + [i+1] + result[j:]
                # print(result)
    
    # while len(result) != n:
    #     result = result.remove(0)
    ans = result.reverse()
    # print(ans)
    return result

N = int(input())

my_students = list(map(int, input().split()))


print(" ".join(map(str, make_line(N, my_students))))