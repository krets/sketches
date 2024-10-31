"""
Vector drawing for exit symbol
"""
import math

class P:
    def __init__(self, x, y):
        self.x = x
        self.y = y


stroke = 36
corner_radius = 2 * stroke

rect_width = 340
rect_height = 484

"""
8 section to rect; 4 edges and 4 corners

Dashes are drawn from top-left corner clockwise
   top -> right -> bottom -> left
When a corner radius is set; this offsets the start point by the radius.
Path along arc is considered for length (or 1/4 circumference of circle)
edges are reduced in size by the radius
"""

edge_top = rect_width - corner_radius * 2
edge_right = rect_height - corner_radius * 2

corner_length = (math.pi * corner_radius)/2

perimeter = edge_top * 2 + edge_right * 2 + corner_length * 4
gap = stroke*6
gap_center = edge_top + corner_length + edge_right/2

dash_array = [
    gap_center - gap/2,
    gap,
    perimeter - gap_center - gap/2
]

arrow_start = P(rect_width/2 + stroke, rect_height/2)
arrow_end = P(rect_width + stroke/2 + stroke*2, arrow_start.y)

arrowhead_size = P(3, 4)  # The marker units equal the stroke size
arrowhead_ref = P(.5, arrowhead_size.y / 2)
arrowhead = [P(0, 0), P(arrowhead_size.x, arrowhead_ref.y), P(0,arrowhead_size.y)]

width = 560
height = 560

padding = stroke
width = (arrow_end.x + arrowhead_size.x * stroke + padding*2)
height = rect_height + stroke + padding
offset = P(stroke, stroke)
rotate = 180
rotate_center = P((width-padding*2)/2, (height-padding*2)/2)


with open("exit.svg", 'w') as fh:
    fh.write(f"""
<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">
    <g transform="translate({offset.x}, {offset.y}) rotate({rotate}, {rotate_center.x}, {rotate_center.y})">
        <rect x="{0}" y="{0}" width="{rect_width}" height="{rect_height}" rx="{corner_radius}" ry="{corner_radius}" stroke="black" fill="none" stroke-width="{stroke}" stroke-dasharray="{', '.join([str(_) for _ in dash_array])}"/>
        <line x1="{arrow_start.x}" y1="{arrow_start.y}" x2="{arrow_end.x}" y2="{arrow_end.y}" stroke="black" stroke-width="{stroke}" marker-end="url(#arrowhead)"/>
    </g>
    <defs>
        <marker id="arrowhead" markerWidth="{arrowhead_size.x}" markerHeight="{arrowhead_size.y}" refX="{arrowhead_ref.x}" refY="{arrowhead_ref.y}" orient="auto">
            <polygon points="{', '.join([f'{p.x} {p.y}' for p in arrowhead])}" fill="black"/>
        </marker>
    </defs>
</svg>
""")
