"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000




def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    interval = (width - GRAPH_MARGIN_SIZE*2) // len(YEARS)
    x_coordinate = (interval * year_index) + GRAPH_MARGIN_SIZE
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH, fill="black")
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH, fill="black")
    width = CANVAS_WIDTH
    for year_index in range(len(YEARS)):
        x = get_x_coordinate(width, year_index)
        canvas.create_text(x, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=YEARS[year_index], anchor=tkinter.NW)
        canvas.create_line(x - TEXT_DX, GRAPH_MARGIN_SIZE, x - TEXT_DX, CANVAS_HEIGHT,
                           width=LINE_WIDTH, fill="black")



def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    for name in lookup_names:
        # if index > 4, got back to 0
        color = COLORS[lookup_names.index(name) - (4 * (lookup_names.index(name)//4))]
        x = []
        y = []
        for year in YEARS:
            year = str(year)
            if year in name_data[name]:
                x1 = get_x_coordinate(CANVAS_WIDTH, YEARS.index(int(year)))
                y1 = GRAPH_MARGIN_SIZE + int(name_data[name][year])/1000 * (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2)
                if y1 > 600:
                    y1 = 600
                print(year)
                print("y")
                print(y1)
            else:
                x1 = get_x_coordinate(CANVAS_WIDTH, YEARS.index(int(year)))
                y1 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
            x.append(x1)
            y.append(y1)
            if year in name_data[name]:
                name1 = name_data[name][year]
            else:
                name1 = "*"
            # add text
            canvas.create_text(x1 + TEXT_DX, y1, text=f"{name} {name1}", anchor=tkinter.SW, fill=color)
        # add line
        canvas.create_line(x[0], y[0],
                           x[1], y[1],
                           x[2], y[2],
                           x[3], y[3],
                           x[4], y[4],
                           x[5], y[5],
                           x[6], y[6],
                           x[7], y[7],
                           x[8], y[8],
                           x[9], y[9],
                           x[10], y[10],
                           x[11], y[11],
                           width=LINE_WIDTH,
                           fill=color
                           )


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
