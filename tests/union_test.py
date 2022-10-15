from polybool import *


def test_case_1():
    region_a: Region = [
        Point(174.731903, -72.989276),
        Point(-70.77748, -53.08311),
        Point(-72.252011, 215.281501),
        Point(129.021448, 126.809651),
        Point(106.16622, 28.016086),
        Point(216.756032, 22.117962),
        Point(174.731903, -72.989276),
    ]

    region_b: Region = [
        Point(-169.571046, -98.793566),
        Point(-145.241287, 63.404826),
        Point(11.796247, 34.651475),
        Point(8.10992, -129.758713),
        Point(-76.675603, -216.018767),
        Point(-169.571046, -98.793566),
    ]

    result = SegmentSelector.union(Polygon([region_a]), Polygon([region_b]))

    assert len(result.regions) == 1

    region = result.regions[0]

    except_region = [
        216.756032,
        22.117962,
        174.731903,
        -72.989276,
        9.68283014596045,
        -59.60691886875095,
        8.10992,
        -129.758713,
        -76.675603,
        -216.018767,
        -169.571046,
        -98.793566,
        -145.241287,
        63.404826,
        -71.34317949796957,
        49.87418673740427,
        -72.252011,
        215.281501,
        129.021448,
        126.809651,
        106.16622,
        28.016086,
    ]
    assert len(region) * 2 == len(except_region)

    for i in range(len(region)):
        assert region[i].x == except_region[i * 2]
        assert region[i].y == except_region[i * 2 + 1]
