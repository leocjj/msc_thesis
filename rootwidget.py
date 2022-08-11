from cmath import sqrt
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

offset = 3  # Half of the point_size value in .kv files, to drow the points correctly.


class RootWidget(BoxLayout):
    """Create a controller that receives a custom widget from the kv lang file.
    Add actions to be called from a kv file.
    """

    slider_1 = NumericProperty(0.0)
    slider_2 = NumericProperty(0.0)
    # slider_3 = NumericProperty(0.0)
    # slider_alto2 = NumericProperty(0.0)
    # label_wid = ObjectProperty()

    # Tuple, for 'pos' attributes in .kv files
    p_3 = ListProperty((0, 0))
    p_4 = ListProperty((0, 0))

    # List of two elements, for point location
    p_0 = ListProperty([0, 0])
    p_A = ListProperty([0, 0])
    p_B = ListProperty([0, 0])
    p_C = ListProperty([0, 0])
    p_D = ListProperty([0, 0])
    p_E = ListProperty([0, 0])
    p_F = ListProperty([0, 0])

    # List of four elements, to draw line in .kv files
    p_1 = ListProperty([0, 0, 0, 0])
    p_2 = ListProperty([0, 0, 0, 0])
    l_1 = ListProperty([0, 0, 0, 0])
    l_2 = ListProperty([0, 0, 0, 0])
    l_3 = ListProperty([0, 0, 0, 0])
    l_4 = ListProperty([0, 0, 0, 0])
    l_5 = ListProperty([0, 0, 0, 0])
    l_6 = ListProperty([0, 0, 0, 0])
    l_7 = ListProperty([0, 0, 0, 0])
    l_8 = ListProperty([0, 0, 0, 0])

    # List of five elements to draw a cicle in .kv files
    # (center_x, center_y, radius, angle_start, angle_end)
    c_1 = ListProperty((0, 0, 0, 0, 0))
    c_2 = ListProperty((0, 0, 0, 0, 0))
    c_3 = ListProperty((0, 0, 0, 0, 0))
    c_4 = ListProperty((0, 0, 0, 0, 0))
    c_5 = ListProperty((0, 0, 0, 0, 0))
    c_6 = ListProperty((0, 0, 0, 0, 0))

    container = ObjectProperty(None)

    def update_points(self, dt):
        pass

    def cap1_sec1_pag1_x(self, f):
        """Control horizontal slider event (x)"""
        Clock.schedule_interval(self.update_points, 0.01)
        self.slider_1 = f  # Receive and update the value from the slider.
        self.p_1 = [
            self.width / 8 * (1 + self.slider_1 * 5),
            self.height * 10 / 16,
            self.width * 13 / 16,
            self.height * 14 / 16,
        ]
        # self.label_wid.text = str(f)
        a = (self.p_1[0], self.p_1[1])
        b = (self.p_1[2], self.p_1[3])
        c = (self.p_2[0], self.p_2[1])
        d = (self.p_2[2], self.p_2[3])
        i = Vector.segment_intersection(a, b, c, d)
        self.p_0 = (  # Offset added and conditional to avoid None
            [i[0] - offset, i[1] - offset] if i else (0, 0)
        )

    def cap1_sec1_pag1_y(self, f):
        """Control vertical slider event (y)"""
        Clock.schedule_interval(self.update_points, 0.01)
        self.slider_2 = f  # Receive and update the value from the slider.
        self.p_2 = [
            self.width / 8,
            self.height * (11 + self.slider_2 * 4) / 16,
            self.width * 14 / 16,
            self.height * 11 / 16,
        ]
        a = (self.p_1[0], self.p_1[1])
        b = (self.p_1[2], self.p_1[3])
        c = (self.p_2[0], self.p_2[1])
        d = (self.p_2[2], self.p_2[3])
        i = Vector.segment_intersection(a, b, c, d)
        self.p_0 = (  # Offset added and conditional to avoid None
            [i[0] - offset, i[1] - offset] if i else (0, 0)
        )

    def cap1_sec1_pag2_x(self, f):
        """Control horizontal slider event (x)"""
        Clock.schedule_interval(self.update_points, 0.01)
        self.slider_1 = f  # Receive and update the value from the slider.
        # To set to zero the first time or update the value next times.
        self.slider_2 = self.slider_2 if self.slider_2 else 0
        self.p_0 = [
            self.width / 2 * (1 + self.slider_1) - offset,
            self.height * (3 + self.slider_2) / 4 - offset,
        ]
        self.label_wid.text = (
            f"Coordenadas: ({(self.slider_1*10):.1f}, {(self.slider_2*10):.1f})"
        )

    def cap1_sec1_pag2_y(self, f):
        """Control vertical slider event (y)"""
        Clock.schedule_interval(self.update_points, 0.01)
        self.slider_2 = f  # Receive and update the value from the slider.
        # To set to zero the first time or update the value next times.
        self.slider_1 = self.slider_1 if self.slider_1 else 0
        self.p_0 = [
            self.width / 2 * (1 + self.slider_1) - offset,
            self.height * (3 + self.slider_2) / 4 - offset,
        ]
        self.label_wid.text = (
            f"Coordenadas: ({(self.slider_1*10):.1f}, {(self.slider_2*10):.1f})"
        )

    def cap1_sec2_pag1(self):
        """Control sliders events"""
        Clock.schedule_interval(self.update_points, 0.01)
        slider_a = self.slider_y1.value
        slider_b = self.slider_y2.value

        self.p_0 = [
            self.width / 10,
            self.height * 3 / 4,
            self.width / 4,
            self.height * (3 + slider_a) / 4,
            self.width * 3 / 4,
            self.height * (3 + slider_b) / 4,
            self.width * 8 / 10,
            self.height * 3 / 4,
        ]
        self.slider_1 = self.height * (3 + slider_a) / 4
        self.p_3 = [self.width / 4 - offset, self.height * (3 + slider_a) / 4 - offset]
        self.p_4 = [
            self.width * 3 / 4 - offset,
            self.height * (3 + slider_b) / 4 - offset,
        ]
        self.label_wid.text = (
            f"Curvatura izq.: {(slider_a):.2f}  Curvatura der.: {(slider_b):.2f}"
            + "\n Esto es una línea... recta!!!"
            if slider_a == slider_b == 0.0
            else ""
        )

    def cap1_sec2_pag2(self):
        """Control sliders events"""
        Clock.schedule_interval(self.update_points, 0.01)
        slider_left = self.slider_y1.value
        slider_right = self.slider_y2.value

        self.l_1 = [
            self.width * (2 + slider_left) / 10,
            self.height * 6 / 8,
            self.width * (8 + slider_right) / 10,
            self.height * 3 / 4,
        ]
        self.p_A = (
            self.width * (2 + slider_left) / 10 - offset,
            self.height * 6 / 8 - offset,
        )
        self.p_B = (
            self.width * (8 + slider_right) / 10 - offset,
            self.height * 3 / 4 - offset,
        )

        if slider_left == self.slider_y1.min and slider_right == self.slider_y2.max:
            self.label_wid.text = "Recta infinita (ambos lados)"
        elif slider_left != self.slider_y1.min and slider_right == self.slider_y2.max:
            self.label_wid.text = "Semirecta infinita a la derecha"
        elif slider_left == self.slider_y1.min and slider_right != self.slider_y2.max:
            self.label_wid.text = "Semirecta infinita a la izquierda"
        elif slider_left != self.slider_y1.min and slider_right != self.slider_y2.max:
            self.label_wid.text = "Semirecta finita"

    def cap1_sec3_pag0(self):
        """Control sliders events"""
        Clock.schedule_interval(self.update_points, 0.01)
        rotation_in_degrees = self.slider_y1.value
        pivot_point_y = self.slider_y2.value
        max_length = max(self.height, self.width)
        v = Vector(1, 0)
        rotation_transformation = v.rotate(rotation_in_degrees).normalize()

        # Horizontal fixed line
        self.p_1 = [0, self.height * 3 / 4, self.width, self.height * 3 / 4]

        # Pivot point for second (mobile) line
        self.p_3 = (self.width / 2, self.height * (3 + pivot_point_y) / 4)

        # Points to draw second (mobile) line
        self.p_0 = [
            self.p_3[0] + offset - max_length * rotation_transformation.x,
            self.p_3[1] + offset - max_length * rotation_transformation.y,
            self.p_3[0] + offset + max_length * rotation_transformation.x,
            self.p_3[1] + offset + max_length * rotation_transformation.y,
        ]
        # Intersection point between two lines
        intersect = Vector.line_intersection(
            (self.p_0[0], self.p_0[1]),
            (self.p_0[2], self.p_0[3]),
            (self.p_1[0], self.p_1[1]),
            (self.p_1[2], self.p_1[3]),
        )
        # Y-distance between pivot point and fixed line
        distance = self.p_3[1] + offset - self.p_1[1]

        if not intersect or abs(intersect.x) > 100000:
            if abs(distance) < 1:
                self.label_wid.text = f"Las dos rectas son la misma.\nInfinitos puntos de intersección :-/"
            else:
                self.label_wid.text = f"Paralelas!!! No hay punto de intersección :-0\n Distancia entre rectas: {abs(distance):.1f}"
            self.p_4 = (0, 0)
        else:
            self.p_4 = (intersect.x - offset, intersect.y - offset)
            self.label_wid.text = f"Punto de intesección: ({(intersect.x - self.width/2 - offset):.1f}, {(intersect.y - self.height*3/4):.1f})"

    def cap1_sec3_pag1(self):
        """Control sliders events"""
        Clock.schedule_interval(self.update_points, 0.01)
        rot_in_degrees_1 = self.slider_y1.value
        rot_in_degrees_2 = self.slider_y2.value
        max_length = min(self.height / 2, self.width) / 2.8
        v1 = Vector(1, 0)
        v2 = Vector(1, 0)
        rot_transform_1 = v1.rotate(rot_in_degrees_1).normalize()
        rot_transform_2 = v2.rotate(rot_in_degrees_2).normalize()

        # Pivot point for rotatign lines
        self.p_3 = (self.width / 2, self.height * 3 / 4)

        # Points to draw first (mobile) - line 1
        self.p_1 = [
            self.p_3[0],
            self.p_3[1],
            self.p_3[0] + max_length * rot_transform_1.x,
            self.p_3[1] + max_length * rot_transform_1.y,
        ]

        # Points to draw second (mobile) - line 2
        self.p_2 = [
            self.p_3[0] - max_length * rot_transform_2.x,
            self.p_3[1] - max_length * rot_transform_2.y,
            self.p_3[0] + max_length * rot_transform_2.x,
            self.p_3[1] + max_length * rot_transform_2.y,
        ]

        # Pivot point for right side of rotatign line 2 (with offset to draw it correctly)
        self.p_4 = self.p_2[2] - offset, self.p_2[3] - offset

        # Pivot point for rotatign lines with offset to draw it correctly
        self.p_3 = (self.p_3[0] - offset, self.p_3[1] - offset)

        angulo = rot_in_degrees_1 - rot_in_degrees_2
        suplemento = 180 - angulo

        if abs(angulo) == 90 or abs(angulo) == 270:
            self.label_wid.text = (
                f"Suplemento:{suplemento:.1f}   Ángulo: {angulo:.1f}"
                + "\n Líneas perpendiculares, ángulos rectos!!!"
            )
        else:
            self.label_wid.text = f"Suplemento:{suplemento:.1f}   Ángulo: {angulo:.1f}"

    def cap1_sec3_pag2(self):
        """Control sliders events"""
        Clock.schedule_interval(self.update_points, 0.01)
        Ax = self.slider_x1.value
        Ay = self.slider_y1.value
        Bx = self.slider_x2.value
        By = self.slider_y2.value

        # Point A
        self.p_A = [
            self.width / 2 * (1 + Ax),
            self.height * (3 + Ay) / 4,
        ]
        # Point B
        self.p_B = [
            self.width / 2 * (1 + Bx),
            self.height * (3 + By) / 4,
        ]
        # Points to draw main line, from A to B
        self.l_1 = [
            self.p_A[0],
            self.p_A[1],
            self.p_B[0],
            self.p_B[1],
        ]
        # Points to draw Secondary line, x-distance
        self.l_2 = [
            self.p_A[0],
            self.p_A[1],
            self.p_B[0],
            self.p_A[1],
        ]
        # Points to draw Secondary line, y-distance
        self.l_3 = [
            self.p_B[0],
            self.p_A[1],
            self.p_B[0],
            self.p_B[1],
        ]

        Dx = abs(Ax - Bx)
        Dy = abs(Ay - By)
        Distancia = sqrt(pow(Dx, 2) + pow(Dy, 2)).real
        self.label_wid.text = (
            f"[color=3465A4]A[color=FFFFFF]({(Ax*10):.1f}, {(Ay*10):.1f})   [color=FF0000]B[color=FFFFFF]({(Bx*10):.1f}, {(By*10):.1f})"
            + f"\n[color=3465A4]Dx:{(Dx*10):.2f}  [color=FF0000]Dy:{(Dy*10):.2f}  [color=D9A560]D:{(Distancia*10):.2f}"
        )
        # Adding offset to draw points correctly
        self.p_A = (self.p_A[0] - offset, self.p_A[1] - offset)
        self.p_B = (self.p_B[0] - offset, self.p_B[1] - offset)

    def cap1_sec4_pag0(self):
        """Control sliders events"""
        Clock.schedule_interval(self.update_points, 0.01)
        rotation_in_degrees = self.slider_y1.value
        pivot_point_y = self.slider_y2.value
        max_length = max(self.height, self.width)
        v = Vector(1, 0)
        rotation_transformation = v.rotate(rotation_in_degrees).normalize()

        # Horizontal fixed line bottom
        self.l_1 = [0, self.height * 11 / 16, self.width, self.height * 11 / 16]

        # Pivot point for rotating line
        self.p_A = (self.width / 2, self.height * (3 + pivot_point_y) / 4)

        # Points to draw rotating line
        self.l_2 = [
            self.p_A[0] - max_length * rotation_transformation.x,
            self.p_A[1] - max_length * rotation_transformation.y,
            self.p_A[0] + max_length * rotation_transformation.x,
            self.p_A[1] + max_length * rotation_transformation.y,
        ]
        # Horizontal fixed line top
        self.l_3 = [0, self.height * 13 / 16, self.width, self.height * 13 / 16]

        # Intersection point bottom
        intersect_bottom = Vector.line_intersection(
            (self.l_2[0], self.l_2[1]),
            (self.l_2[2], self.l_2[3]),
            (self.l_1[0], self.l_1[1]),
            (self.l_1[2], self.l_1[3]),
        )
        if not intersect_bottom or abs(intersect_bottom.x) > 100000:
            self.p_B = (0, 0)
        else:
            self.p_B = (intersect_bottom.x, intersect_bottom.y)

        # Intersection point top
        intersect_top = Vector.line_intersection(
            (self.l_2[0], self.l_2[1]),
            (self.l_2[2], self.l_2[3]),
            (self.l_3[0], self.l_3[1]),
            (self.l_3[2], self.l_3[3]),
        )
        if not intersect_top or abs(intersect_top.x) > 100000:
            self.p_C = (0, 0)
        else:
            self.p_C = (intersect_top.x, intersect_top.y)

        # Circles around point B and C
        self.c_1 = (self.p_B[0], self.p_B[1], 20)
        self.c_2 = (self.p_C[0], self.p_C[1], 20)

        # Angle for circles works CW instead of CCW, staring from the north.
        ang = Vector(0, 1).angle((self.p_C[0] - self.p_B[0], self.p_C[1] - self.p_B[1]))

        # circle = (center_x, center_y, radius, angle_start, angle_end)
        self.c_3 = (self.p_B[0], self.p_B[1], 20, 90, ang)
        self.c_4 = (self.p_B[0], self.p_B[1], 20, 90 - 180, ang - 180)
        self.c_5 = (self.p_C[0], self.p_C[1], 20, 90, ang)
        self.c_6 = (self.p_C[0], self.p_C[1], 20, 90 - 180, ang - 180)

        if self.p_B[0] == 0 and self.p_B[1] == 0:
            self.label_wid.text = f"Rectas paralelas, no hay ángulos definidos!"
        else:
            if int(90 - ang) == 90:
                self.label_wid.text = (
                    f"[color=FF3333]Ángulo: {int(90 - ang)} grados\n"
                    "[color=FFFFFF]Perpendiculares!!!"
                )
            else:
                self.label_wid.text = (
                    f"[color=FF3333]Ángulo: [color=FFFFFF]{int(90 - ang)} grados"
                )

        # Adding offset to draw points correctly
        self.p_A = (self.p_A[0] - offset, self.p_A[1] - offset)
        self.p_B = (self.p_B[0] - offset, self.p_B[1] - offset)
        self.p_C = (self.p_C[0] - offset, self.p_C[1] - offset)

    def cap1_sec4_pag1(self):
        """Control sliders events"""
        Clock.schedule_interval(self.update_points, 0.01)
        degrees_left = self.slider_y1.value
        degrees_right = self.slider_y2.value
        max_length = max(self.height, self.width)
        v = Vector(1, 0)
        rotation_left = v.rotate(degrees_left).normalize()
        rotation_right = v.rotate(degrees_right).normalize()

        # Horizontal fixed line bottom
        self.l_1 = [0, self.height * 10 / 16, self.width, self.height * 10 / 16]
        # Pivot point for rotating line left
        self.p_A = (self.width / 3, self.height * 11 / 16)
        # Pivot point for rotating line left
        self.p_B = (self.width * 2 / 3, self.height * 12 / 16)
        # Points to draw rotating line left
        self.l_2 = [
            self.p_A[0] - max_length * rotation_left.x,
            self.p_A[1] - max_length * rotation_left.y,
            self.p_A[0] + max_length * rotation_left.x,
            self.p_A[1] + max_length * rotation_left.y,
        ]
        # Points to draw rotating line right
        self.l_3 = [
            self.p_B[0] - max_length * rotation_right.x,
            self.p_B[1] - max_length * rotation_right.y,
            self.p_B[0] + max_length * rotation_right.x,
            self.p_B[1] + max_length * rotation_right.y,
        ]

        # Intersection point bottom-left
        intersect_bottom_left = Vector.line_intersection(
            (self.l_2[0], self.l_2[1]),
            (self.l_2[2], self.l_2[3]),
            (self.l_1[0], self.l_1[1]),
            (self.l_1[2], self.l_1[3]),
        )
        if not intersect_bottom_left or abs(intersect_bottom_left.x) > 100000:
            self.p_C = (0, 0)
            ang_C = 0
        else:
            self.p_C = (intersect_bottom_left.x, intersect_bottom_left.y)
            ang_C = Vector(
                (self.l_2[2] - self.l_2[0]), (self.l_2[3] - self.l_2[1])
            ).angle(((self.l_1[2] - self.l_1[0]), (self.l_1[3] - self.l_1[1])))

        # Intersection point bottom-right
        intersect_bottom_right = Vector.line_intersection(
            (self.l_3[0], self.l_3[1]),
            (self.l_3[2], self.l_3[3]),
            (self.l_1[0], self.l_1[1]),
            (self.l_1[2], self.l_1[3]),
        )
        if not intersect_bottom_right or abs(intersect_bottom_right.x) > 100000:
            self.p_D = (0, 0)
            ang_D = 0
        else:
            self.p_D = (intersect_bottom_right.x, intersect_bottom_right.y)
            ang_D = 180 - Vector(
                (self.l_3[2] - self.l_3[0]), (self.l_3[3] - self.l_3[1])
            ).angle(((self.l_1[2] - self.l_1[0]), (self.l_1[3] - self.l_1[1])))

        # Intersection point left-right
        intersect_left_right = Vector.line_intersection(
            (self.l_2[0], self.l_2[1]),
            (self.l_2[2], self.l_2[3]),
            (self.l_3[0], self.l_3[1]),
            (self.l_3[2], self.l_3[3]),
        )
        if not intersect_left_right or abs(intersect_left_right.x) > 100000:
            self.p_E = (0, 0)
            ang_E = 0
        else:
            self.p_E = (intersect_left_right.x, intersect_left_right.y)
            ang_E = -Vector(
                (self.l_2[2] - self.l_2[0]), (self.l_2[3] - self.l_2[1])
            ).angle(((self.l_3[2] - self.l_3[0]), (self.l_3[3] - self.l_3[1])))

        # self.label_wid.text = (
        #    f"Ángulos  [color=FF3333]C: [color=FFFFFF]{ang_C:.0f}"
        #    + f"[color=3465A4]  D: [color=FFFFFF]{ang_D:.0f}"
        #    + f"[color=D9A560]  E: [color=FFFFFF]{ang_E:.0f}"
        # )

        msg_angulos = (
            f"Ángulos  [color=FF3333]C: [color=FFFFFF]{ang_C:.0f}"
            + f"[color=3465A4]  D: [color=FFFFFF]{ang_D:.0f}"
            + f"[color=D9A560]  E: [color=FFFFFF]{ang_E:.0f}\n"
        )

        angulos = (int(ang_C), int(ang_D), int(ang_E))
        if ang_C == 0 and ang_D == 0 and ang_E == 0:
            msg_paralelas = "Las tres rectas son paralelas entre si."
        elif 90 not in angulos and 0 in angulos:
            msg_paralelas = "Dos rectas paralelas y una las intersecta."
        elif 90 in angulos and 0 in angulos:
            msg_paralelas = "Dos rectas paralelas y una perpendicular a estas."
        else:
            msg_paralelas = "Las tres rectas se intersectan entre sí."
        self.label_wid.text = msg_angulos + msg_paralelas

        """
        # Circles around points C and D
        self.c_1 = (self.p_B[0], self.p_B[1], 20)
        self.c_2 = (self.p_C[0], self.p_C[1], 20)

        # Angle for circles works CW instead of CCW, staring from the north.
        ang = Vector(0, 1).angle((self.p_C[0] - self.p_B[0], self.p_C[1] - self.p_B[1]))

        # circle = (center_x, center_y, radius, angle_start, angle_end)
        self.c_3 = (self.p_B[0], self.p_B[1], 20, 90, ang)
        self.c_4 = (self.p_B[0], self.p_B[1], 20, 90 - 180, ang - 180)
        self.c_5 = (self.p_C[0], self.p_C[1], 20, 90, ang)
        self.c_6 = (self.p_C[0], self.p_C[1], 20, 90 - 180, ang - 180)

        if self.p_B[0] == 0 and self.p_B[1] == 0:
            self.label_wid.text = f"Rectas paralelas, no hay ángulos definidos!"
        else:
            if (90 - ang) == 90:
                self.label_wid.text = (
                    f"[color=FF3333]Ángulo: {(90 - ang):.2f}\n"
                    "[color=FFFFFF]Perpendiculares!!!"
                )
            else:
                self.label_wid.text = (
                    f"[color=FF3333]Ángulo: [color=FFFFFF]{(90 - ang):.2f}"
                )
        """

        # Adding offset to draw points correctly
        self.p_A = (self.p_A[0] - offset, self.p_A[1] - offset)
        self.p_B = (self.p_B[0] - offset, self.p_B[1] - offset)
        self.p_C = (self.p_C[0] - offset, self.p_C[1] - offset)
        self.p_D = (self.p_D[0] - offset, self.p_D[1] - offset)
        self.p_E = (self.p_E[0] - offset, self.p_E[1] - offset)

    def cap1_sec4_pag2(self):
        """Control sliders events"""
        Clock.schedule_interval(self.update_points, 0.01)
        x = self.slider_x.value
        y = self.slider_y.value

        # Point bottom-left
        self.p_A = (self.width / 3, self.height * 3 / 4)
        # Point bottom-right
        self.p_B = (self.width * 2 / 3, self.height * 3 / 4)
        # Point bottom-top
        self.p_C = (self.width * (1 + x) / 2, self.height * (3 + y) / 4)

        # Horizontal fixed line bottom
        self.l_1 = [self.p_A[0], self.p_A[1], self.p_B[0], self.p_B[1]]
        # Left line
        self.l_2 = [self.p_A[0], self.p_A[1], self.p_C[0], self.p_C[1]]
        # Right line
        self.l_3 = [self.p_C[0], self.p_C[1], self.p_B[0], self.p_B[1]]

        ang_A = abs(
            Vector((self.l_2[2] - self.l_2[0]), (self.l_2[3] - self.l_2[1])).angle(
                ((self.l_1[2] - self.l_1[0]), (self.l_1[3] - self.l_1[1]))
            )
        )
        ang_B = abs(
            Vector((self.l_3[2] - self.l_3[0]), (self.l_3[3] - self.l_3[1])).angle(
                ((self.l_1[2] - self.l_1[0]), (self.l_1[3] - self.l_1[1]))
            )
        )
        ang_C = abs(
            180
            - Vector((self.l_2[2] - self.l_2[0]), (self.l_2[3] - self.l_2[1])).angle(
                ((self.l_3[2] - self.l_3[0]), (self.l_3[3] - self.l_3[1]))
            )
        )
        if y < 0:
            ang_C = 360 - ang_C

        msg_angulos = (
            f"Ángulos  [color=FF3333]A: [color=FFFFFF]{int(ang_A)}"
            + f"[color=3465A4]  B: [color=FFFFFF]{int(ang_B)}"
            + f"[color=D9A560]  C: [color=FFFFFF]{int(ang_C)}\n"
        )

        angulos = (int(ang_A), int(ang_B), int(ang_C))
        if abs(self.p_A[1] - self.p_C[1]) < 0.5:
            msg_paralelas = "Los tres puntos son colineales. No hay polígono!"
        elif 90 in angulos and 0 not in angulos:
            msg_paralelas = "Un ángulo recto (90 grados)."
        else:
            msg_paralelas = "..."
        self.label_wid.text = msg_angulos + msg_paralelas

        """
        # Circles around points C and D
        self.c_1 = (self.p_B[0], self.p_B[1], 20)
        self.c_2 = (self.p_C[0], self.p_C[1], 20)

        # Angle for circles works CW instead of CCW, staring from the north.
        ang = Vector(0, 1).angle((self.p_C[0] - self.p_B[0], self.p_C[1] - self.p_B[1]))

        # circle = (center_x, center_y, radius, angle_start, angle_end)
        self.c_3 = (self.p_B[0], self.p_B[1], 20, 90, ang)
        self.c_4 = (self.p_B[0], self.p_B[1], 20, 90 - 180, ang - 180)
        self.c_5 = (self.p_C[0], self.p_C[1], 20, 90, ang)
        self.c_6 = (self.p_C[0], self.p_C[1], 20, 90 - 180, ang - 180)

        if self.p_B[0] == 0 and self.p_B[1] == 0:
            self.label_wid.text = f"Rectas paralelas, no hay ángulos definidos!"
        else:
            if (90 - ang) == 90:
                self.label_wid.text = (
                    f"[color=FF3333]Ángulo: {(90 - ang):.2f}\n"
                    "[color=FFFFFF]Perpendiculares!!!"
                )
            else:
                self.label_wid.text = (
                    f"[color=FF3333]Ángulo: [color=FFFFFF]{(90 - ang):.2f}"
                )
        """

        # Adding offset to draw points correctly
        self.p_A = (self.p_A[0] - offset, self.p_A[1] - offset)
        self.p_B = (self.p_B[0] - offset, self.p_B[1] - offset)
        self.p_C = (self.p_C[0] - offset, self.p_C[1] - offset)

    def cap2_sec1_pag0(self):
        """Control sliders events"""
        Clock.schedule_interval(self.update_points, 0.01)
        x = self.slider_x.value
        y = self.slider_y.value

        # Point bottom-left
        self.p_A = (self.width / 3, self.height * 5 / 8)
        # Point bottom-right
        self.p_B = (self.width * 2 / 3, self.height * 5 / 8)
        # Point bottom-top
        self.p_C = (self.width * (1 + x) / 2, self.height * (3 + y) / 4)

        # Horizontal fixed line bottom
        self.l_1 = [self.p_A[0], self.p_A[1], self.p_B[0], self.p_B[1]]
        # Left line
        self.l_2 = [self.p_A[0], self.p_A[1], self.p_C[0], self.p_C[1]]
        # Right line
        self.l_3 = [self.p_C[0], self.p_C[1], self.p_B[0], self.p_B[1]]

        ang_A = int(
            abs(
                Vector((self.l_2[2] - self.l_2[0]), (self.l_2[3] - self.l_2[1])).angle(
                    ((self.l_1[2] - self.l_1[0]), (self.l_1[3] - self.l_1[1]))
                )
            )
        )
        ang_B = int(
            abs(
                Vector((self.l_3[2] - self.l_3[0]), (self.l_3[3] - self.l_3[1])).angle(
                    ((self.l_1[2] - self.l_1[0]), (self.l_1[3] - self.l_1[1]))
                )
            )
        )
        ang_C = int(
            abs(
                180
                - Vector(
                    (self.l_2[2] - self.l_2[0]), (self.l_2[3] - self.l_2[1])
                ).angle(((self.l_3[2] - self.l_3[0]), (self.l_3[3] - self.l_3[1])))
            )
        )
        if y < 0:
            ang_C = 360 - ang_C

        msg_angulos = (
            f"Ángulos  [color=FF3333]A: [color=FFFFFF]{ang_A}"
            + f"[color=3465A4]  B: [color=FFFFFF]{ang_B}"
            + f"[color=D9A560]  C: [color=FFFFFF]{ang_C}"
        )

        if abs(self.p_A[1] - self.p_C[1]) < 0.5:
            msg_angulos_2 = "Los tres puntos son colineales. No hay triángulo!"
        elif ang_A < 90 and ang_B < 90 and ang_C < 90:
            msg_angulos_2 = "Triángulo acutángulo"
        elif ang_A == 90 or ang_B == 90 or ang_C == 90:
            msg_angulos_2 = "Triángulo rectángulo"
        elif ang_A > 90 or ang_B > 90 or ang_C > 90:
            msg_angulos_2 = "Triángulo obtusángulo"
        else:
            msg_angulos_2 = "..."

        lado_a = int(
            Vector(self.p_B[0], self.p_B[1]).distance((self.p_C[0], self.p_C[1]))
        )
        lado_b = int(
            Vector(self.p_A[0], self.p_A[1]).distance((self.p_C[0], self.p_C[1]))
        )
        lado_c = int(
            Vector(self.p_B[0], self.p_B[1]).distance((self.p_A[0], self.p_A[1]))
        )

        msg_lados = (
            f"Lados  [color=FF3333]a: [color=FFFFFF]{lado_a}"
            + f"[color=3465A4]  b: [color=FFFFFF]{lado_b}"
            + f"[color=D9A560]  c: [color=FFFFFF]{lado_c}"
        )

        if abs(self.p_A[1] - self.p_C[1]) < 0.5:
            msg_lados_2 = ""
        elif lado_a == lado_b == lado_c:
            msg_lados_2 = "Triangulo equilátero"
        elif lado_a != lado_b and lado_a != lado_c and lado_b != lado_c:
            msg_lados_2 = "Triangulo escaleno"
        else:
            msg_lados_2 = "Triangulo isóceles"

        self.label_wid.text = (
            msg_angulos + "\n" + msg_angulos_2 + "\n" + msg_lados + "\n" + msg_lados_2
        )

        # Adding offset to draw points correctly
        self.p_A = (self.p_A[0] - offset, self.p_A[1] - offset)
        self.p_B = (self.p_B[0] - offset, self.p_B[1] - offset)
        self.p_C = (self.p_C[0] - offset, self.p_C[1] - offset)

    def cap2_sec1_pag1(self):
        """Control sliders events"""
        Clock.schedule_interval(self.update_points, 0.01)
        x = self.slider_x.value
        y = self.slider_y.value

        # Point bottom-left
        self.p_A = (self.width / 3, self.height * 5 / 8)
        # Point bottom-right
        self.p_B = (self.width * 2 / 3, self.height * 5 / 8)
        # Point bottom-top
        self.p_C = (self.width * (1 + x) / 2, self.height * (3 + y) / 4)
        # Point bottom - for the height of the triangle with the point C.
        self.p_D = (self.width * (1 + x) / 2, self.height * 5 / 8)
        # Point bottom - for the middle point
        self.p_E = (
            (self.width * 2 / 3 - self.width / 3) / 2 + self.width / 3,
            self.height * 5 / 8,
        )

        # Horizontal fixed line bottom
        self.l_1 = [self.p_A[0], self.p_A[1], self.p_B[0], self.p_B[1]]
        # Left line
        self.l_2 = [self.p_A[0], self.p_A[1], self.p_C[0], self.p_C[1]]
        # Right line
        self.l_3 = [self.p_C[0], self.p_C[1], self.p_B[0], self.p_B[1]]

        # Height of the tringle
        self.l_4 = [self.p_C[0], self.p_C[1], self.p_D[0], self.p_D[1]]
        self.l_5 = [self.p_A[0], self.p_A[1], self.p_D[0], self.p_D[1]]
        # Median line
        self.l_6 = [self.p_C[0], self.p_C[1], self.p_E[0], self.p_E[1]]
        # Mediatrix line
        self.l_7 = [self.p_E[0], self.p_E[1], self.p_E[0], self.p_C[1]]

        # Calculating bisectrix
        ang_C = int(
            abs(
                180
                - Vector(
                    (self.l_2[2] - self.l_2[0]), (self.l_2[3] - self.l_2[1])
                ).angle(((self.l_3[2] - self.l_3[0]), (self.l_3[3] - self.l_3[1])))
            )
        )
        if self.p_C[1] < self.p_A[1]:
            ang_C = 360 - ang_C
        ang_base = int(
            abs(
                Vector(1, 0).angle(
                    ((self.l_3[2] - self.l_3[0]), (self.l_3[3] - self.l_3[1]))
                )
            )
        )
        max_length = max(self.height, self.width)
        v = Vector(0, 100)
        rotation_left = v.rotate(-ang_C / 2 - ang_base - 90)
        self.l_8 = [
            self.p_C[0],
            self.p_C[1],
            self.p_C[0] + max_length * rotation_left.x,
            self.p_C[1] + max_length * rotation_left.y,
        ]
        # Intersection of the bisectrix
        intersect = Vector.line_intersection(
            (self.l_8[0], self.l_8[1]),
            (self.l_8[2], self.l_8[3]),
            (self.l_1[0], self.l_1[1]),
            (self.l_1[2], self.l_1[3]),
        )
        self.p_F = (intersect.x, intersect.y)
        # Truncating bisextrix in the bottom
        self.l_8[2] = self.p_F[0]
        self.l_8[3] = self.p_F[1]

        self.label_wid.text = f"Ángulo del vertice superior: {ang_C:.0f}"

        # Adding offset to draw points correctly
        self.p_A = (self.p_A[0] - offset, self.p_A[1] - offset)
        self.p_B = (self.p_B[0] - offset, self.p_B[1] - offset)
        self.p_C = (self.p_C[0] - offset, self.p_C[1] - offset)
        self.p_D = (self.p_D[0] - offset, self.p_D[1] - offset)
        self.p_E = (self.p_E[0] - offset, self.p_E[1] - offset)
        self.p_F = (self.p_F[0] - offset, self.p_F[1] - offset)