from flask import Flask, jsonify
import os
import sys
import inspect

current_dir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
parent_dir = os.path.dirname(parent_dir)
sys.path.insert(0, parent_dir)

from maze import *

app = Flask(__name__)

horizontal_walls = [
    "0000000",
    "0111110",
    "0110110",
    "0000000",
    "0000000",
    "0110110",
    "0111110",
]

veritcal_walls = [
    "0000000",
    "1000010",
    "0011000",
    "0000000",
    "0011000",
    "1000010",
    "0000000",
]

@app.route('/generate', methods=['GET'])
def GET_generate():
    maze = Maze(7, 7)
    maze = maze.add_boundary()

    for row in range(7):
        for col in range(7):
            if horizontal_walls[row][col] == '1':
                maze.add_wall(Coord(row, col), NORTH)
            if veritcal_walls[row][col] == '1':
                maze.add_wall(Coord(row, col), EAST)


    return jsonify({"geom": maze.encode()}), 200