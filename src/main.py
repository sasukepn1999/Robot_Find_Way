import sys
import turtle as tt
from find_way import dac_find_path
import doan
import GUI


def main():
    if (len(sys.argv) == 3):
        input_filepath = sys.argv[1]
        inp = doan.readData(input_filepath)

        screen = tt.Screen()

        n = int(inp[0][0])  # column
        m = int(inp[0][1])  # row
        start = list([int(inp[1][1]), int(inp[1][0])])
        goal = list([int(inp[1][3]), int(inp[1][2])])
        numPoly = inp[2][0]
        # numVer = inp[2][1]
        poly = inp[3]
        # ver = inp[4]

        matrix = doan.init(m, n, start, goal, numPoly, poly)
        # print(matrix)
        find_algo = sys.argv[2]
        if find_algo == '0':
            path = doan.findPath(matrix, m, n, start, goal)
        else:
            m_find_path = dac_find_path.Dac_Find_Path(matrix,
                                                      tuple(start),
                                                      tuple(goal))
            path = m_find_path.get_path()

        print(path)

        Long = tt.Turtle()
        Long.hideturtle()
        turtle = Long

        GUI.grid(turtle, len(matrix), len(matrix[0]))
        GUI.fillColorOneElementOnGridByMatrix(turtle, matrix, GUI.LENGTH)
        GUI.findWay(turtle, path, GUI.LENGTH)

        screen.exitonclick()
    else:
        print("Usage:", sys.argv[0], 'input filepath', 'type algo')


if __name__ == '__main__':
    main()
