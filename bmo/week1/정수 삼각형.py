def solution(triangle):

    for layer in range(1, len(triangle)):
        for idx in range(len(triangle[layer])):
            up_layer = layer - 1

            if idx == 0:
                triangle[layer][idx] += triangle[up_layer][idx]
            elif idx == layer:
                triangle[layer][idx] += triangle[up_layer][idx-1]
            else:
                triangle[layer][idx] += max(triangle[up_layer][idx-1], triangle[up_layer][idx])

    return max(triangle[-1])


if __name__ == '__main__':
    result = solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])
    print(result)