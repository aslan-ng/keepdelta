import svgwrite as svg



a = 100
b = (2 * (a**2))**0.5
b_prime = 2 * a - b

dwg = svg.Drawing("logo.svg", profile='tiny', size=(b, b))

stroke_width = 1
stroke = "white"
fill = "none"

p0 = [0, 0]
p1 = [a, 0]
p2 = [0, a]
points = [p0, p1, p2]
dwg.add(dwg.polygon(points=points, fill=fill, stroke=stroke, stroke_width=stroke_width))

p3 = [0, b]
p4 = [a, b]
p5 = [b_prime/2, b - a + b_prime/2]
points = [p2, p3, p4, p5]
dwg.add(dwg.polygon(points=points, fill=fill, stroke=stroke, stroke_width=stroke_width))

p6 = [b + b_prime/2, b/2]
points = [
    [p1[0] - b_prime/2, p1[1]],
    [p4[0] - b_prime/2, p4[1]],
    [p6[0] - b_prime/2, p6[1]],
]
dwg.add(dwg.polygon(points=points, fill=fill, stroke=stroke, stroke_width=stroke_width))

dwg.save()