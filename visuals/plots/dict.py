def data():
    paths = {}
    print("Please choose a type of line: (:, -- or -)")
    line = input()
    print("Please choose a color: (r, g, or b)")
    color = input()
    print("Please choose a style of marker: (o, s or ^)")
    marker = input()

    paths['line'] = line
    paths['color'] = color
    paths['marker'] = marker

    return paths


def generate():
    print("How many lines would you like to display?")
    lines_amount = int(input())
    for lines_amount in range(lines_amount):
        values = data()
        plt.plot()

