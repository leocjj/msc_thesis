from kivy.uix.boxlayout import BoxLayout
from kivy.properties import (
    ObjectProperty,
    NumericProperty,
    ListProperty,
)
from kivy.clock import Clock
from kivy.vector import Vector

from kivy import require

require("2.1.0")

offset = 3  # Half of the point_size value in .kv files, to draw the points correctly.


class RootWidget(BoxLayout):
    """Create a controller that receives a custom widget from the kv lang file.
    Add actions to be called from a kv file.
    """

    # List of two elements, for point location
    p_0 = ListProperty([0, 0])
    p_A = ListProperty([0, 0])
    p_B = ListProperty([0, 0])
    p_C = ListProperty([0, 0])
    p_D = ListProperty([0, 0])
    p_E = ListProperty([0, 0])
    p_F = ListProperty([0, 0])
    p_G = ListProperty([0, 0])

    # List of four elements, to draw line in .kv files
    l_1 = ListProperty([0, 0, 0, 0])
    l_2 = ListProperty([0, 0, 0, 0])
    l_3 = ListProperty([0, 0, 0, 0])
    l_4 = ListProperty([0, 0, 0, 0])
    l_5 = ListProperty([0, 0, 0, 0])
    l_6 = ListProperty([0, 0, 0, 0])

    # List of five elements to draw a cicle in .kv files
    # (center_x, center_y, radius, angle_start, angle_end)
    c_1 = ListProperty((0, 0, 0, 0, 0))

    container = ObjectProperty(None)

    def update_points(self, dt):
        pass

    def cap2_sec1_pag3(self):
        """Control sliders events"""
        Clock.schedule_interval(self.update_points, 0.01)
        x = self.slider_x.value
        y = self.slider_y.value
        max_length = max(self.height, self.width)

        # Vertex point bottom-left
        self.p_A = (self.width / 3, self.height * 3 / 4)
        # Vertex point bottom-right
        self.p_B = (self.width * 2 / 3, self.height * 3 / 4)
        # Vertex point bottom-top
        self.p_C = (self.width * (1 + x) / 2, self.height * (3 + y) / 4)

        # Horizontal fixed line bottom
        self.l_1 = [self.p_A[0], self.p_A[1], self.p_B[0], self.p_B[1]]
        # Left line
        self.l_2 = [self.p_A[0], self.p_A[1], self.p_C[0], self.p_C[1]]
        # Right line
        self.l_3 = [self.p_B[0], self.p_B[1], self.p_C[0], self.p_C[1]]

        # Bisectrix for angle of bottom-left vertex (A)
        ang_A = Vector(
            ((self.l_2[2] - self.l_2[0]), (self.l_2[3] - self.l_2[1]))
        ).angle((100, 0))
        v = Vector(100, 0)
        rotation_half = v.rotate(ang_A / 2)
        self.l_4 = [
            self.p_A[0],
            self.p_A[1],
            self.p_A[0] + max_length * rotation_half.x,
            self.p_A[1] + max_length * rotation_half.y,
        ]

        # Bisectrix for angle of bottom-right vertex (B)
        vector_base = (
            (self.l_3[2] - self.l_3[0]),
            (self.l_3[3] - self.l_3[1]),
        )  # line l_3
        ang_B = Vector(vector_base).angle(
            ((self.l_1[0] - self.l_1[2]), (self.l_1[1] - self.l_1[3]))  # line -l_1
        )
        v = Vector(vector_base)
        rotation_half = v.rotate(-ang_B / 2)
        self.l_5 = [
            self.p_B[0],
            self.p_B[1],
            self.p_B[0] + max_length * rotation_half.x,
            self.p_B[1] + max_length * rotation_half.y,
        ]

        # Bisectrix for angle of top vertex (C)
        vector_base = (
            (self.l_2[0] - self.l_2[2]),
            (self.l_2[1] - self.l_2[3]),
        )  # line -l_2
        ang_C = Vector(vector_base).angle(
            ((self.l_3[0] - self.l_3[2]), (self.l_3[1] - self.l_3[3]))  # line -l_3
        )
        v = Vector(vector_base)
        rotation_half = v.rotate(-ang_C / 2)
        self.l_6 = [
            self.p_C[0],
            self.p_C[1],
            self.p_C[0] + max_length * rotation_half.x,
            self.p_C[1] + max_length * rotation_half.y,
        ]

        # Intersection of the bisectrix line with side (line l_3)
        intersect = Vector.line_intersection(
            (self.l_4[0], self.l_4[1]),
            (self.l_4[2], self.l_4[3]),
            (self.l_3[0], self.l_3[1]),
            (self.l_3[2], self.l_3[3]),
        )
        if not intersect or abs(intersect.x) > 10000:
            self.p_D = (0, 0)
        else:
            self.p_D = (intersect.x, intersect.y)
            self.l_4[2] = self.p_D[0]
            self.l_4[3] = self.p_D[1]

        # Intersection of the bisectrix line with side (line l_2)
        intersect = Vector.line_intersection(
            (self.l_5[0], self.l_5[1]),
            (self.l_5[2], self.l_5[3]),
            (self.l_2[0], self.l_2[1]),
            (self.l_2[2], self.l_2[3]),
        )
        if not intersect or abs(intersect.x) > 10000:
            self.p_E = (0, 0)
        else:
            self.p_E = (intersect.x, intersect.y)
            self.l_5[2] = self.p_E[0]
            self.l_5[3] = self.p_E[1]

        # Intersection of the bisectrix line with side (line l_1)
        intersect = Vector.line_intersection(
            (self.l_6[0], self.l_6[1]),
            (self.l_6[2], self.l_6[3]),
            (self.l_1[0], self.l_1[1]),
            (self.l_1[2], self.l_1[3]),
        )
        if not intersect or abs(intersect.x) > 10000:
            self.p_F = (0, 0)
        else:
            self.p_F = (intersect.x, intersect.y)
            self.l_6[2] = self.p_F[0]
            self.l_6[3] = self.p_F[1]

        # Intersection of the bisectrixs lines - incenter
        intersect = Vector.line_intersection(
            (self.l_5[0], self.l_5[1]),
            (self.l_5[2], self.l_5[3]),
            (self.l_6[0], self.l_6[1]),
            (self.l_6[2], self.l_6[3]),
        )

        # Inscrite circunference around circuncenter
        if not intersect or abs(intersect.x) > 10000:
            self.p_G = (0, 0)
            radio = 0
            self.c_1 = (0, 0, 1)
        else:
            self.p_G = (intersect.x, intersect.y)
            radio_D = Vector(self.p_G).distance(self.p_D)
            radio_E = Vector(self.p_G).distance(self.p_E)
            radio_F = Vector(self.p_G).distance(self.p_F)
            radio = min(radio_D, radio_E, radio_F)
            self.c_1 = (self.p_G[0], self.p_G[1], radio)

        self.label_wid.text = f"Circumference radius: {radio:.0f}"

        # Adding offset to draw points correctly
        self.p_A = (self.p_A[0] - offset, self.p_A[1] - offset)
        self.p_B = (self.p_B[0] - offset, self.p_B[1] - offset)
        self.p_C = (self.p_C[0] - offset, self.p_C[1] - offset)
        self.p_D = (self.p_D[0] - offset, self.p_D[1] - offset)
        self.p_E = (self.p_E[0] - offset, self.p_E[1] - offset)
        self.p_F = (self.p_F[0] - offset, self.p_F[1] - offset)
        self.p_G = (self.p_G[0] - offset, self.p_G[1] - offset)
