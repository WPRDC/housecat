from shapely.geometry import Polygon, Point
from shapely.ops import transform
from pyproj import Transformer, CRS
import random
import numpy as np
import pandas as pd


""" Polygons """

pittsburgh_coords = [
    (-80.1, 40.459),(-80.099, 40.462),(-80.096, 40.464),(-80.084, 40.464), 
    (-80.079, 40.469),(-80.076, 40.469),(-80.07, 40.465),(-80.055, 40.469), 
    (-80.051, 40.474),(-80.057, 40.481),(-80.057, 40.484),(-80.051, 40.49), 
    (-80.049, 40.49),(-80.043, 40.495),(-80.036, 40.496),(-80.032, 40.495), 
    (-80.032, 40.498),(-80.03, 40.5),(-80.024, 40.5),(-80.018, 40.504), 
    (-80.013, 40.505),(-80.008, 40.505),(-80.007, 40.502),(-80.001, 40.501), 
    (-79.999, 40.485),(-79.993, 40.481),(-79.986, 40.481),(-79.982, 40.474), 
    (-79.979, 40.476),(-79.973, 40.474),(-79.966, 40.483),(-79.958, 40.489), 
    (-79.939, 40.495),(-79.924, 40.495),(-79.914, 40.491),(-79.905, 40.491), 
    (-79.901, 40.493),(-79.899, 40.496),(-79.884, 40.495),(-79.881, 40.492), 
    (-79.88, 40.481),(-79.884, 40.474),(-79.885, 40.465),(-79.884, 40.464), 
    (-79.88, 40.464),(-79.878, 40.466),(-79.868, 40.465),(-79.866, 40.461), 
    (-79.862, 40.458),(-79.862, 40.452),(-79.865, 40.447),(-79.872, 40.445), 
    (-79.88, 40.446),(-79.884, 40.443),(-79.89, 40.444),(-79.892, 40.432), 
    (-79.887, 40.429),(-79.887, 40.425),(-79.895, 40.42),(-79.895, 40.416), 
    (-79.898, 40.412),(-79.911, 40.411),(-79.921, 40.403),(-79.916, 40.403), 
    (-79.91, 40.4),(-79.909, 40.398),(-79.913, 40.389),(-79.913, 40.385), 
    (-79.909, 40.384),(-79.905, 40.38),(-79.904, 40.378),(-79.905, 40.376), 
    (-79.901, 40.375),(-79.897, 40.367),(-79.897, 40.363),(-79.901, 40.361), 
    (-79.903, 40.358),(-79.909, 40.358),(-79.913, 40.359),(-79.914, 40.361), 
    (-79.923, 40.362),(-79.928, 40.371),(-79.933, 40.372),(-79.94, 40.37), 
    (-79.947, 40.372),(-79.949, 40.374),(-79.949, 40.378),(-79.945, 40.383), 
    (-79.941, 40.384),(-79.95, 40.387),(-79.959, 40.386),(-79.961, 40.388), 
    (-79.962, 40.393),(-79.966, 40.396),(-79.973, 40.398),(-79.974, 40.401), 
    (-79.975, 40.4),(-79.974, 40.397),(-79.972, 40.397),(-79.969, 40.394), 
    (-79.969, 40.387),(-79.97, 40.383),(-79.975, 40.377),(-79.982, 40.377), 
    (-79.984, 40.374),(-79.99, 40.375),(-79.992, 40.372),(-79.999, 40.372), 
    (-80.002, 40.37),(-80.009, 40.371),(-80.011, 40.374),(-80.01, 40.377), 
    (-80.015, 40.377),(-80.018, 40.382),(-80.031, 40.388),(-80.035, 40.394), 
    (-80.035, 40.397),(-80.038, 40.397),(-80.04, 40.395),(-80.047, 40.395), 
    (-80.055, 40.4),(-80.054, 40.406),(-80.043, 40.423),(-80.05, 40.422), 
    (-80.053, 40.424),(-80.057, 40.422),(-80.063, 40.422),(-80.062, 40.419), 
    (-80.063, 40.414),(-80.066, 40.412),(-80.07, 40.412),(-80.073, 40.409), 
    (-80.082, 40.413),(-80.083, 40.416),(-80.087, 40.417),(-80.09, 40.422), 
    (-80.089, 40.428),(-80.078, 40.428),(-80.072, 40.435),(-80.069, 40.436), 
    (-80.062, 40.433),(-80.065, 40.439),(-80.064, 40.444),(-80.073, 40.444), 
    (-80.073, 40.44),(-80.075, 40.438),(-80.083, 40.436),(-80.093, 40.441), 
    (-80.094, 40.447),(-80.098, 40.449),(-80.099, 40.453),(-80.1, 40.459)
]

allegeny_county_coords = [
    (-80.365,40.476),(-80.365,40.479),(-80.361,40.483),(-80.355,40.486),
    (-80.229,40.577),(-80.222,40.585),(-80.215,40.585),(-80.215,40.587),
    (-80.21,40.592),(-80.205,40.593),(-80.199,40.599),(-80.193,40.601),
    (-80.184,40.609),(-80.183,40.613),(-80.178,40.614),(-80.175,40.612),
    (-80.165,40.611),(-80.161,40.614),(-80.156,40.613),(-80.153,40.616),
    (-80.149,40.616),(-80.153,40.674),(-80.151,40.678),(-80.07,40.679),
    (-79.997,40.677),(-79.988,40.678),(-79.964,40.676),(-79.785,40.676),
    (-79.732,40.673),(-79.692,40.674),(-79.689,40.672),(-79.688,40.669),
    (-79.692,40.662),(-79.685,40.651),(-79.685,40.642),(-79.687,40.637),
    (-79.699,40.623),(-79.71,40.617),(-79.72,40.604),(-79.761,40.59),
    (-79.769,40.582),(-79.77,40.577),(-79.77,40.57),(-79.763,40.554),
    (-79.755,40.554),(-79.753,40.556),(-79.75,40.556),(-79.744,40.553),
    (-79.734,40.553),(-79.729,40.548),(-79.719,40.545),(-79.713,40.537),
    (-79.708,40.536),(-79.707,40.534),(-79.704,40.533),(-79.703,40.53),
    (-79.699,40.529),(-79.698,40.527),(-79.698,40.477),(-79.701,40.424),
    (-79.704,40.419),(-79.712,40.415),(-79.715,40.41),(-79.718,40.41),
    (-79.718,40.407),(-79.72,40.405),(-79.728,40.404),(-79.728,40.399),
    (-79.732,40.394),(-79.735,40.394),(-79.739,40.391),(-79.743,40.392),
    (-79.746,40.387),(-79.751,40.384),(-79.76,40.387),(-79.759,40.385),
    (-79.761,40.381),(-79.766,40.379),(-79.784,40.301),(-79.771,40.29),
    (-79.771,40.284),(-79.778,40.278),(-79.792,40.278),(-79.79,40.272),
    (-79.784,40.266),(-79.783,40.263),(-79.784,40.259),(-79.793,40.251),
    (-79.795,40.245),(-79.799,40.24),(-79.803,40.238),(-79.803,40.236),
    (-79.782,40.232),(-79.779,40.229),(-79.78,40.225),(-79.872,40.193),
    (-79.881,40.193),(-79.892,40.19),(-79.912,40.193),(-79.921,40.197),
    (-79.931,40.204),(-79.95,40.207),(-79.958,40.21),(-79.963,40.213),
    (-79.974,40.224),(-79.975,40.232),(-79.968,40.241),(-79.961,40.244),
    (-79.94,40.245),(-79.925,40.249),(-79.923,40.251),(-80.186,40.329),
    (-80.231,40.368),(-80.233,40.368),(-80.251,40.384),(-80.363,40.474),
    (-80.365,40.476)
]

# Create Polygons
pittsburgh = Polygon(pittsburgh_coords)
allegheny = Polygon(allegeny_county_coords)


""" Functions """

# Project a given geometry from one coordinate system to another
def project(shape, source, target):
    transformer = Transformer.from_crs(source, target)
    return transform(transformer.transform, shape)


# Generate random coordinates within a given polygon
def generate_coords(poly=Polygon):
    min_x, min_y, max_x, max_y = poly.bounds
    while True:
        x = random.uniform(min_x, max_x)
        y = random.uniform(min_y, max_y)
        random_point = Point([x, y])
        if random_point.within(poly):
            return [x, y]


# Create a Shapely Point for Web Mercator geom from coordinates in WGS84
def create_point(coordinates=list):
    wgs84_pt = Point(coordinates)
    wgs84 = CRS('EPSG:4326')
    webmercator = CRS('EPSG:3857')
    return project(wgs84_pt, wgs84, webmercator)


# Generate a given number of points within a given Shapely Polygon 
def generate_points(poly=Polygon, num_points=int):
    min_x, min_y, max_x, max_y = poly.bounds
    points = []
    while len(points) < num_points:
            random_point = Point([
                random.uniform(min_x, max_x), 
                random.uniform(min_y, max_y)
                ])
            if random_point.within(poly):
                points.append(random_point)
    return points