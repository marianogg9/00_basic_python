import cv2


def create_graph():
    # maze_img = cv2.imread('maze.png', cv2.IMREAD_UNCHANGED)
    # cell_size = [100, 100]
    #
    # max_rows = 10
    # max_cols = 10
    #
    # pointer_x = 50
    # pointer_y = 0

    # Generate graph matrix
    # graph_matrix = [[0 for col in range(max_cols)] for row in range(max_rows)]
    #
    # for row_index in range(max_rows):
    #
    #     for col_index in range(max_cols):
    #         blue, green, red = [int(color) for color in maze_img[pointer_y, pointer_x]]
    #         if blue == 27 and green == 27 and red == 27:
    #             color = "black"
    #         else:
    #             color = "white"
    #
    #         print(f"Color found: {color} for ({pointer_x},{pointer_y})")
    #         graph_matrix[row_index][col_index] = 1
    #
    #         pointer_x += cell_size[0]
    #
    #     pointer_x = 50
    #     pointer_y += cell_size[1]

    # Generate list of graphs

    list_of_graphs = {
        0: [1],
        1: [2, 3],
        2: [1, 5],
        3: [1, 4, 8],
        4: [3, 12],
        5: [2, 6, 9],
        6: [5, 10],
        7: [8, 11],
        8: [7, 3],
        9: [5, 10],
        10: [9, 6, 11],
        11: [10, 7, 14],
        12: [4, 13],
        13: [12],
        14: [11, 15, 19],
        15: [16, 17, 14],
        16: [15],
        17: [18, 15],
        18: [17],
        19: [14, 20, 22],
        20: [19, 21]
    }

    return list_of_graphs
