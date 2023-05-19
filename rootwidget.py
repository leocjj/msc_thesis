from math import asin, atan, pi, sqrt, degrees, radians, sin, cos
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

    slider_1 = NumericProperty(0.0)
    slider_2 = NumericProperty(0.0)

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
    p_G = ListProperty([0, 0])
    p_G2 = ListProperty([0, 0])
    p_G3 = ListProperty([0, 0])
    p_G4 = ListProperty([0, 0])
    p_POS = ListProperty([0, 0])
    p_SIZE = ListProperty([0, 0])

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
    p_COLOR = ListProperty([0, 0, 0, 0])

    # List of five elements to draw a cicle in .kv files
    # (center_x, center_y, radius, angle_start, angle_end)
    c_1 = ListProperty((0, 0, 0, 0, 0))
    c_2 = ListProperty((0, 0, 0, 0, 0))
    c_3 = ListProperty((0, 0, 0, 0, 0))
    c_4 = ListProperty((0, 0, 0, 0, 0))
    c_5 = ListProperty((0, 0, 0, 0, 0))
    c_6 = ListProperty((0, 0, 0, 0, 0))

    m_0 = []
    m_1 = []
    v_0 = ListProperty([])
    v_1 = []

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

    def cap1_sec1_pag2(self):
        Clock.schedule_interval(self.update_points, 0.01)
        x = self.slider_x.value
        y = self.slider_y.value

        # Mobile point
        self.p_A = (self.width / 2 * (1 + x), self.height * (3 + y) / 4)
        # Origin point
        self.p_B = [
            self.width / 2,
            self.height * 3 / 4,
        ]
        self.label_wid.text = f"Coordenadas: ({(x * 10):.1f}, {(y * 10):.1f})"
        # Adding offset to draw points correctly
        self.p_A = (self.p_A[0] - offset, self.p_A[1] - offset)
        self.p_B = (self.p_B[0] - offset, self.p_B[1] - offset)

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
            + (
                "\n Esto es una línea... recta!!!"
                if slider_a == slider_b == 0.0
                else ""
            )
        )

    def cap1_sec2_pag2(self):
        """Control sliders events"""
        Clock.schedule_interval(self.update_points, 0.01)
        slider_left = self.slider_y1.value
        slider_right = self.slider_y2.value
        slider_height_left = self.slider_y3.value
        slider_height_rigth = self.slider_y4.value

        self.p_A = (
            self.width * (5 + slider_left) / 10,
            self.height * (3 + slider_height_rigth) / 4,
        )
        self.p_B = (
            self.width * (5 + slider_right) / 10,
            self.height * (3 + slider_height_left) / 4,
        )
        self.l_1 = [
            self.p_A[0] + offset,
            self.p_A[1] + offset,
            self.p_B[0] + offset,
            self.p_B[1] + offset,
        ]

        if slider_left == self.slider_y1.min and slider_right == self.slider_y2.max:
            self.label_wid.text = "Recta: es infinita a ambos lados"
        elif (
            slider_left == self.slider_y1.max
            and slider_right == self.slider_y2.min
            and slider_height_left == slider_height_rigth
        ):
            self.label_wid.text = "Esto es un punto, no se puede trazar una recta."
        elif slider_left != self.slider_y1.min and slider_right == self.slider_y2.max:
            self.label_wid.text = "Semirecta: es infinita a la derecha"
        elif slider_left == self.slider_y1.min and slider_right != self.slider_y2.max:
            self.label_wid.text = "Semirecta: es infinita a la izquierda"
        elif slider_left != self.slider_y1.min and slider_right != self.slider_y2.max:
            self.label_wid.text = "Segmento (de recta): es finito"

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
                self.label_wid.text = (
                    f"Las dos rectas son la misma.\nInfinitos puntos de intersección!"
                )
            else:
                self.label_wid.text = f"Paralelas!!! No hay punto de intersección!\n Distancia entre rectas: {abs(distance):.1f}"
            self.p_4 = (0, 0)
        else:
            self.p_4 = (intersect.x - offset, intersect.y - offset)
            self.label_wid.text = f"Punto de intersección: ({(intersect.x - self.width/2 - offset):.1f}, {(intersect.y - self.height*3/4):.1f})"

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
                f"[color=00FF00]Ángulo: {angulo:.1f} \n"
                + f"[color=FF0000]Suplemento:{suplemento:.1f} \n [color=FFFFFF]Líneas perpendiculares,   ángulos rectos!!!"
            )
        elif abs(angulo) < 90:
            self.label_wid.text = f"[color=00FF00]Ángulo: {angulo:.1f}  (Agudo) \n  [color=FF0000]Suplemento:{suplemento:.1f}"
        elif 90 < abs(angulo) < 180:
            self.label_wid.text = f"[color=00FF00]Ángulo: {angulo:.1f}  (Obtuso) \n  [color=FF0000]Suplemento:{suplemento:.1f}"
        elif abs(angulo) == 180:
            self.label_wid.text = f"[color=00FF00]Ángulo: {angulo:.1f}  (Llano) \n  [color=FF0000]Suplemento:{suplemento:.1f}"
        elif abs(angulo) > 180:
            self.label_wid.text = f"[color=00FF00]Ángulo: {angulo:.1f}  (Cóncavo) \n  [color=FF0000]Suplemento:{suplemento:.1f}"
        self.label_wid.text = (
            self.label_wid.text + f"\n[color=AF794B]Suma: {angulo + suplemento}\n"
        )

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
            f"[color=3465A4]P[color=FFFFFF]({(Ax*10):.1f}, {(Ay*10):.1f})   [color=FF0000]Q[color=FFFFFF]({(Bx*10):.1f}, {(By*10):.1f})"
            + f"\n[color=3465A4]Dx:{(Dx*10):.2f}  [color=FF0000]Dy:{(Dy*10):.2f}  [color=00FF00]D:{(Distancia*10):.2f}"
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
        circle_radius = self.height / 16
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
        self.c_1 = (self.p_B[0], self.p_B[1], circle_radius)
        self.c_2 = (self.p_C[0], self.p_C[1], circle_radius)

        # Angle for circles works CW instead of CCW, staring from the north.
        ang = Vector(0, 1).angle((self.p_C[0] - self.p_B[0], self.p_C[1] - self.p_B[1]))

        # circle = (center_x, center_y, radius, angle_start, angle_end)
        self.c_3 = (self.p_B[0], self.p_B[1], circle_radius, 90, ang)
        self.c_4 = (self.p_B[0], self.p_B[1], circle_radius, 90 - 180, ang - 180)
        self.c_5 = (self.p_C[0], self.p_C[1], circle_radius, 90, ang)
        self.c_6 = (self.p_C[0], self.p_C[1], circle_radius, 90 - 180, ang - 180)

        if self.p_B[0] == 0 and self.p_B[1] == 0:
            self.label_wid.text = f"Rectas paralelas, no hay ángulos definidos!"
        else:
            if int(90 - ang) == 90:
                self.label_wid.text = (
                    f"[color=FF3333]Todos los ángulos: [color=FFFFFF]{int(90 - ang)} grados\n"
                    "Recta blanca es perpendicular a las rectas cafés!!!"
                )
            else:
                self.label_wid.text = (
                    f"[color=FF3333]Ángulo principales: [color=FFFFFF]{int(90 - ang)} grados\n"
                    f"[color=3333FF]Ángulo complementarios: [color=FFFFFF]{180 - int(90 - ang)} grados"
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
            msg_paralelas = "Polígono de tres lados: Triángulo."
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
            msg_lados_2 = "Triángulo equilátero"
        elif lado_a != lado_b and lado_a != lado_c and lado_b != lado_c:
            msg_lados_2 = "Triángulo escaleno"
        else:
            msg_lados_2 = "Triángulo isóceles"

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
        ang_C = abs(
            180
            - Vector((self.l_2[2] - self.l_2[0]), (self.l_2[3] - self.l_2[1])).angle(
                ((self.l_3[2] - self.l_3[0]), (self.l_3[3] - self.l_3[1]))
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
        if not intersect or abs(intersect.x) > 100000:
            self.p_F = (intersect.x, intersect.y)
        else:
            self.p_F = (intersect.x, intersect.y)
            # Truncating bisextrix in the bottom
            self.l_8[2] = self.p_F[0]
            self.l_8[3] = self.p_F[1]

        self.label_wid.text = f"Ángulo del vértice superior: {ang_C:.0f}"

        # Adding offset to draw points correctly
        self.p_A = (self.p_A[0] - offset, self.p_A[1] - offset)
        self.p_B = (self.p_B[0] - offset, self.p_B[1] - offset)
        self.p_C = (self.p_C[0] - offset, self.p_C[1] - offset)
        self.p_D = (self.p_D[0] - offset, self.p_D[1] - offset)
        self.p_E = (self.p_E[0] - offset, self.p_E[1] - offset)
        self.p_F = (self.p_F[0] - offset, self.p_F[1] - offset)

    def cap2_sec1_pag2(self):
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

        # Middle point bottom
        self.p_D = (
            (self.p_B[0] - self.p_A[0]) / 2 + self.p_A[0],
            (self.p_B[1] - self.p_A[1]) / 2 + self.p_A[1],
        )
        # Middle point left
        self.p_E = (
            (self.p_C[0] - self.p_A[0]) / 2 + self.p_A[0],
            (self.p_C[1] - self.p_A[1]) / 2 + self.p_A[1],
        )
        # Middle point right
        self.p_F = (
            (self.p_C[0] - self.p_B[0]) / 2 + self.p_B[0],
            (self.p_C[1] - self.p_B[1]) / 2 + self.p_B[1],
        )

        # Horizontal fixed line bottom
        self.l_1 = [self.p_A[0], self.p_A[1], self.p_B[0], self.p_B[1]]
        # Left line
        self.l_2 = [self.p_A[0], self.p_A[1], self.p_C[0], self.p_C[1]]
        # Right line
        self.l_3 = [self.p_B[0], self.p_B[1], self.p_C[0], self.p_C[1]]

        # Mediatrix line
        self.l_4 = [
            self.p_D[0],
            self.p_D[1] - max_length,
            self.p_D[0],
            self.p_C[1] + max_length,
        ]

        # Angle of left line
        ang_l_2 = Vector(
            (self.l_2[2] - self.l_2[0]), (self.l_2[3] - self.l_2[1])
        ).angle((100, 0))
        # Angle of right line
        ang_l_3 = Vector(
            (self.l_3[2] - self.l_3[0]), (self.l_3[3] - self.l_3[1])
        ).angle((100, 0))

        # Perpendicular line to left line
        v = Vector(100, 0)
        rotation = v.rotate(ang_l_2 + 90)
        self.l_5 = [
            self.p_E[0] - max_length * rotation.x,
            self.p_E[1] - max_length * rotation.y,
            self.p_E[0] + max_length * rotation.x,
            self.p_E[1] + max_length * rotation.y,
        ]
        # Perpendicular line to right line
        v = Vector(100, 0)
        rotation = v.rotate(ang_l_3 + 90)
        self.l_6 = [
            self.p_F[0] - max_length * rotation.x,
            self.p_F[1] - max_length * rotation.y,
            self.p_F[0] + max_length * rotation.x,
            self.p_F[1] + max_length * rotation.y,
        ]

        # Intersection of the mediatrixs lines - circuncenter
        intersect = Vector.line_intersection(
            (self.l_5[0], self.l_5[1]),
            (self.l_5[2], self.l_5[3]),
            (self.l_6[0], self.l_6[1]),
            (self.l_6[2], self.l_6[3]),
        )

        # Circunscrite circunference around circuncenter
        if not intersect or abs(intersect.x) > 10000:
            self.p_G = (0, 0)
            radio = 0
            self.c_1 = (0, 0, 1)
        else:
            self.p_G = (intersect.x, intersect.y)
            radio = Vector(self.p_G).distance(self.p_A)
            self.c_1 = (self.p_G[0], self.p_G[1], radio)

        self.label_wid.text = f"Radio de la circunferencia: {radio:.0f}"

        # Adding offset to draw points correctly
        self.p_A = (self.p_A[0] - offset, self.p_A[1] - offset)
        self.p_B = (self.p_B[0] - offset, self.p_B[1] - offset)
        self.p_C = (self.p_C[0] - offset, self.p_C[1] - offset)
        self.p_D = (self.p_D[0] - offset, self.p_D[1] - offset)
        self.p_E = (self.p_E[0] - offset, self.p_E[1] - offset)
        self.p_F = (self.p_F[0] - offset, self.p_F[1] - offset)
        self.p_G = (self.p_G[0] - offset, self.p_G[1] - offset)

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

        self.label_wid.text = f"Radio de la circunferencia: {radio:.0f}"

        # Adding offset to draw points correctly
        self.p_A = (self.p_A[0] - offset, self.p_A[1] - offset)
        self.p_B = (self.p_B[0] - offset, self.p_B[1] - offset)
        self.p_C = (self.p_C[0] - offset, self.p_C[1] - offset)
        self.p_D = (self.p_D[0] - offset, self.p_D[1] - offset)
        self.p_E = (self.p_E[0] - offset, self.p_E[1] - offset)
        self.p_F = (self.p_F[0] - offset, self.p_F[1] - offset)
        self.p_G = (self.p_G[0] - offset, self.p_G[1] - offset)

    def cap2_sec1_pag4(self):
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

        # Height for angle of bottom-left vertex (A)
        if (self.p_C[1] - self.p_B[1]) != 0:
            ang_A = atan(-(self.p_C[0] - self.p_B[0]) / (self.p_C[1] - self.p_B[1]))
            ang_A = ang_A * 180 / pi
            v = Vector(100, 0)
            rotation = v.rotate(ang_A)
            self.l_4 = [
                self.p_A[0],
                self.p_A[1],
                self.p_A[0] + max_length * rotation.x,
                self.p_A[1] + max_length * rotation.y,
            ]
            # Intersection of the height line with side (line l_3)
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

        # Height for angle of bottom-left vertex (B)
        if (self.p_A[1] - self.p_C[1]) != 0:
            ang_B = atan(-(self.p_A[0] - self.p_C[0]) / (self.p_A[1] - self.p_C[1]))
            ang_B = ang_B * 180 / pi
            v = Vector(100, 0)
            rotation = v.rotate(ang_B)
            self.l_5 = [
                self.p_B[0],
                self.p_B[1],
                self.p_B[0] + max_length * rotation.x,
                self.p_B[1] + max_length * rotation.y,
            ]
            # Intersection of the height line with side (line l_2)
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

        # Height for angle of bottom-left vertex (C)
        # Point bottom - for the height of the triangle with the point C.
        self.p_F = (self.p_C[0], self.p_A[1])
        self.l_6 = [self.p_C[0], self.p_C[1], self.p_F[0], self.p_F[1]]
        # Intersection of the height lines
        intersect = Vector.line_intersection(
            (self.l_6[0], self.l_6[1]),
            (self.l_6[2], self.l_6[3]),
            (self.l_4[0], self.l_4[1]),
            (self.l_4[2], self.l_4[3]),
        )
        # Circunference around orthocenter
        if not intersect or abs(intersect.x) > 10000:
            self.p_G = (0, 0)
            radio = 0
            self.c_1 = (0, 0, 1)
        else:
            self.p_G = (intersect.x, intersect.y)
            radio_D = Vector(self.p_G).distance(self.p_D)
            radio_E = Vector(self.p_G).distance(self.p_E)
            radio_F = Vector(self.p_G).distance(self.p_F)
            radio = max(radio_D, radio_E, radio_F)
            self.c_1 = (self.p_G[0], self.p_G[1], radio)

        self.label_wid.text = f"Radio de la circunferencia: {radio:.0f}"

        # Adding offset to draw points correctly
        self.p_A = (self.p_A[0] - offset, self.p_A[1] - offset)
        self.p_B = (self.p_B[0] - offset, self.p_B[1] - offset)
        self.p_C = (self.p_C[0] - offset, self.p_C[1] - offset)
        self.p_D = (self.p_D[0] - offset, self.p_D[1] - offset)
        self.p_E = (self.p_E[0] - offset, self.p_E[1] - offset)
        self.p_F = (self.p_F[0] - offset, self.p_F[1] - offset)
        self.p_G = (self.p_G[0] - offset, self.p_G[1] - offset)

    def cap2_sec1_pag5(self):
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

        # Middle point bottom
        self.p_D = (
            (self.p_B[0] - self.p_A[0]) / 2 + self.p_A[0],
            (self.p_B[1] - self.p_A[1]) / 2 + self.p_A[1],
        )
        # Middle point left
        self.p_E = (
            (self.p_C[0] - self.p_A[0]) / 2 + self.p_A[0],
            (self.p_C[1] - self.p_A[1]) / 2 + self.p_A[1],
        )
        # Middle point right
        self.p_F = (
            (self.p_C[0] - self.p_B[0]) / 2 + self.p_B[0],
            (self.p_C[1] - self.p_B[1]) / 2 + self.p_B[1],
        )

        # Horizontal fixed line bottom
        self.l_1 = [self.p_A[0], self.p_A[1], self.p_B[0], self.p_B[1]]
        # Left line
        self.l_2 = [self.p_A[0], self.p_A[1], self.p_C[0], self.p_C[1]]
        # Right line
        self.l_3 = [self.p_B[0], self.p_B[1], self.p_C[0], self.p_C[1]]

        # Median line
        self.l_4 = [
            self.p_A[0],
            self.p_A[1],
            self.p_F[0],
            self.p_F[1],
        ]
        # Median line
        self.l_5 = [
            self.p_B[0],
            self.p_B[1],
            self.p_E[0],
            self.p_E[1],
        ]
        # Median line
        self.l_6 = [
            self.p_C[0],
            self.p_C[1],
            self.p_D[0],
            self.p_D[1],
        ]

        # Intersection of the median lines - Baricenter
        intersect = Vector.line_intersection(
            (self.l_5[0], self.l_5[1]),
            (self.l_5[2], self.l_5[3]),
            (self.l_6[0], self.l_6[1]),
            (self.l_6[2], self.l_6[3]),
        )

        # Baricenter
        if not intersect or abs(intersect.x) > 10000:
            self.p_G = (0, 0)
            radio = 0
            self.c_1 = (0, 0, 1)
        else:
            self.p_G = (intersect.x, intersect.y)
            radio_1 = Vector(self.p_G).distance(self.p_D)
            radio_2 = Vector(self.p_G).distance(self.p_E)
            radio_3 = Vector(self.p_G).distance(self.p_F)
            radio = min(radio_1, radio_2, radio_3)
            self.c_1 = (self.p_G[0], self.p_G[1], radio)

        self.p_0 = [
            self.p_D[0],
            self.p_D[1],
            self.p_A[0],
            self.p_A[1],
            self.p_E[0],
            self.p_E[1],
        ]
        self.p_1 = [
            self.p_E[0],
            self.p_E[1],
            self.p_C[0],
            self.p_C[1],
            self.p_F[0],
            self.p_F[1],
        ]
        self.p_2 = [
            self.p_F[0],
            self.p_F[1],
            self.p_B[0],
            self.p_B[1],
            self.p_D[0],
            self.p_D[1],
        ]

        self.label_wid.text = f"Radio de la circunferencia: {radio:.0f}"

        # Adding offset to draw points correctly
        self.p_A = (self.p_A[0] - offset, self.p_A[1] - offset)
        self.p_B = (self.p_B[0] - offset, self.p_B[1] - offset)
        self.p_C = (self.p_C[0] - offset, self.p_C[1] - offset)
        self.p_D = (self.p_D[0] - offset, self.p_D[1] - offset)
        self.p_E = (self.p_E[0] - offset, self.p_E[1] - offset)
        self.p_F = (self.p_F[0] - offset, self.p_F[1] - offset)
        self.p_G = (self.p_G[0] - offset, self.p_G[1] - offset)

    def cap2_sec1_pag6(self):
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

        ### For circuncenter ###
        if True:
            # Middle point left
            self.p_E = (
                (self.p_C[0] - self.p_A[0]) / 2 + self.p_A[0],
                (self.p_C[1] - self.p_A[1]) / 2 + self.p_A[1],
            )
            # Middle point right
            self.p_F = (
                (self.p_C[0] - self.p_B[0]) / 2 + self.p_B[0],
                (self.p_C[1] - self.p_B[1]) / 2 + self.p_B[1],
            )

            # Angle of left line
            ang_l_2 = Vector(
                (self.l_2[2] - self.l_2[0]), (self.l_2[3] - self.l_2[1])
            ).angle((100, 0))
            # Angle of right line
            ang_l_3 = Vector(
                (self.l_3[2] - self.l_3[0]), (self.l_3[3] - self.l_3[1])
            ).angle((100, 0))

            # Perpendicular line to left line
            v = Vector(100, 0)
            rotation = v.rotate(ang_l_2 + 90)
            self.l_5 = [
                self.p_E[0] - max_length * rotation.x,
                self.p_E[1] - max_length * rotation.y,
                self.p_E[0] + max_length * rotation.x,
                self.p_E[1] + max_length * rotation.y,
            ]
            # Perpendicular line to right line
            v = Vector(100, 0)
            rotation = v.rotate(ang_l_3 + 90)
            self.l_6 = [
                self.p_F[0] - max_length * rotation.x,
                self.p_F[1] - max_length * rotation.y,
                self.p_F[0] + max_length * rotation.x,
                self.p_F[1] + max_length * rotation.y,
            ]
            # Intersection of the mediatrixs lines - circuncenter
            intersect = Vector.line_intersection(
                (self.l_5[0], self.l_5[1]),
                (self.l_5[2], self.l_5[3]),
                (self.l_6[0], self.l_6[1]),
                (self.l_6[2], self.l_6[3]),
            )
            # Circunscrite circunference around circuncenter
            if not intersect or abs(intersect.x) > 10000:
                self.p_G = (0, 0)
                radio = 0
                self.c_1 = (0, 0, 1)
            else:
                self.p_G = (intersect.x, intersect.y)
                radio = Vector(self.p_G).distance(self.p_A)
                self.c_1 = (self.p_G[0], self.p_G[1], radio)

        ### For incenter ###
        if True:
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

            # Intersection of the bisectrixs lines - incenter
            intersect = Vector.line_intersection(
                (self.l_5[0], self.l_5[1]),
                (self.l_5[2], self.l_5[3]),
                (self.l_6[0], self.l_6[1]),
                (self.l_6[2], self.l_6[3]),
            )

            # Inscrite circunference around circuncenter
            if not intersect or abs(intersect.x) > 10000:
                self.p_G2 = (0, 0)
                radio = 0
                self.c_2 = (0, 0, 1)
            else:
                self.p_G2 = (intersect.x, intersect.y)
                radio_D = Vector(self.p_G2).distance(self.p_D)
                radio_E = Vector(self.p_G2).distance(self.p_E)
                radio_F = Vector(self.p_G2).distance(self.p_F)
                radio = min(radio_D, radio_E, radio_F)
                self.c_2 = (self.p_G2[0], self.p_G2[1], radio)

        ### For baricenter ###
        if True:
            # Middle point bottom
            self.p_D = (
                (self.p_B[0] - self.p_A[0]) / 2 + self.p_A[0],
                (self.p_B[1] - self.p_A[1]) / 2 + self.p_A[1],
            )
            # Middle point left
            self.p_E = (
                (self.p_C[0] - self.p_A[0]) / 2 + self.p_A[0],
                (self.p_C[1] - self.p_A[1]) / 2 + self.p_A[1],
            )
            # Median line
            self.l_5 = [
                self.p_B[0],
                self.p_B[1],
                self.p_E[0],
                self.p_E[1],
            ]
            # Median line
            self.l_6 = [
                self.p_C[0],
                self.p_C[1],
                self.p_D[0],
                self.p_D[1],
            ]
            # Intersection of the mediaN lines - Baricenter
            intersect = Vector.line_intersection(
                (self.l_5[0], self.l_5[1]),
                (self.l_5[2], self.l_5[3]),
                (self.l_6[0], self.l_6[1]),
                (self.l_6[2], self.l_6[3]),
            )
            # Baricenter
            if not intersect or abs(intersect.x) > 10000:
                self.p_G3 = (0, 0)
            else:
                self.p_G3 = (intersect.x, intersect.y)

        ### For orthocenter ###
        if True:
            # Height for angle of bottom-left vertex (A)
            if (self.p_C[1] - self.p_B[1]) != 0:
                ang_A = atan(-(self.p_C[0] - self.p_B[0]) / (self.p_C[1] - self.p_B[1]))
                ang_A = ang_A * 180 / pi
                v = Vector(100, 0)
                rotation = v.rotate(ang_A)
                self.l_4 = [
                    self.p_A[0],
                    self.p_A[1],
                    self.p_A[0] + max_length * rotation.x,
                    self.p_A[1] + max_length * rotation.y,
                ]
                # Intersection of the height line with side (line l_3)
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

            # Height for angle of bottom-left vertex (B)
            if (self.p_A[1] - self.p_C[1]) != 0:
                ang_B = atan(-(self.p_A[0] - self.p_C[0]) / (self.p_A[1] - self.p_C[1]))
                ang_B = ang_B * 180 / pi
                v = Vector(100, 0)
                rotation = v.rotate(ang_B)
                self.l_5 = [
                    self.p_B[0],
                    self.p_B[1],
                    self.p_B[0] + max_length * rotation.x,
                    self.p_B[1] + max_length * rotation.y,
                ]
                # Intersection of the height line with side (line l_2)
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

            # Height for angle of bottom-left vertex (C)
            # Point bottom - for the height of the triangle with the point C.
            self.p_F = (self.p_C[0], self.p_A[1])
            self.l_6 = [self.p_C[0], self.p_C[1], self.p_F[0], self.p_F[1]]
            # Intersection of the height lines
            intersect = Vector.line_intersection(
                (self.l_6[0], self.l_6[1]),
                (self.l_6[2], self.l_6[3]),
                (self.l_4[0], self.l_4[1]),
                (self.l_4[2], self.l_4[3]),
            )
            # Circunference around orthocenter
            if not intersect or abs(intersect.x) > 10000:
                self.p_G4 = (0, 0)
                radio = 0
                self.c_4 = (0, 0, 1)
            else:
                self.p_G4 = (intersect.x, intersect.y)
                radio_D = Vector(self.p_G4).distance(self.p_D)
                radio_E = Vector(self.p_G4).distance(self.p_E)
                radio_F = Vector(self.p_G4).distance(self.p_F)
                radio = min(radio_D, radio_E, radio_F)
                self.c_4 = (self.p_G4[0], self.p_G4[1], radio)

        ### For Euler's line###
        if True:
            # Angle of right line
            ang_l_2 = Vector(
                (self.p_G4[0] - self.p_G3[0]), (self.p_G4[1] - self.p_G3[1])
            ).angle((100, 0))

            # Perpendicular line to left line
            v = Vector(100, 0)
            rotation = v.rotate(ang_l_2)
            self.l_5 = [
                self.p_E[0] - max_length * rotation.x,
                self.p_E[1] - max_length * rotation.y,
                self.p_E[0] + max_length * rotation.x,
                self.p_E[1] + max_length * rotation.y,
            ]

            self.l_4 = [
                self.p_G3[0] - max_length * rotation.x,
                self.p_G3[1] - max_length * rotation.y,
                self.p_G4[0] + max_length * rotation.x,
                self.p_G4[1] + max_length * rotation.y,
            ]

        ### For message ###
        if True:
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
                msg_lados_2 = "Triángulo equilátero"
            elif lado_a != lado_b and lado_a != lado_c and lado_b != lado_c:
                msg_lados_2 = "Triángulo escaleno"
            else:
                msg_lados_2 = "Triángulo isóceles"

            self.label_wid.text = msg_lados + "\n" + msg_lados_2

        # Adding offset to draw points correctly
        self.p_G = (self.p_G[0] - offset, self.p_G[1] - offset)
        self.p_G2 = (self.p_G2[0] - offset, self.p_G2[1] - offset)
        self.p_G3 = (self.p_G3[0] - offset, self.p_G3[1] - offset)
        self.p_G4 = (self.p_G4[0] - offset, self.p_G4[1] - offset)

    def cap2_sec2_pag0(self):
        """Control sliders events"""
        Clock.schedule_interval(self.update_points, 0.01)
        Ax = 0
        Ay = 0
        Bx = self.slider_x.value
        By = self.slider_y.value

        # Point A
        self.p_A = [self.width / 2, self.height * 3 / 4]
        # Point B
        self.p_B = [self.width / 2 * (1 + Bx), self.height * (3 + By) / 4]
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

        x = (Bx - Ax) * 10  # Scaled
        y = (By - Ay) * 10  # Scaled
        d = sqrt(pow(x, 2) + pow(y, 2))
        msg_1 = f"[color=3465A4]  x: {x:.1f}  [color=FF0000]y: {y:.1f}  [color=D9A560]d: {d:.4f}"
        if d < 0.05:
            msg_2 = f"[color=FFFFFF]  y/d: ~   x/d: ~   y/x: ~"
        elif -0.05 < x < 0.05:
            msg_2 = f"[color=FFFFFF]  y/d: {y/d:.4f}   x/d: {x/d:.4f}   y/x: ~"
        else:
            msg_2 = f"[color=FFFFFF]  y/d: {y/d:.4f}   x/d: {x/d:.4f}   y/x: {y/x:.4f}"
        if -0.05 < y < 0.05:
            if -0.05 < x < 0.05:
                msg_3 = f"[color=FFFFFF]  d/y: ~   d/x: ~   x/y: ~"
            else:
                msg_3 = f"[color=FFFFFF]  d/y: ~   d/x: {d/x:.4f}   x/y: ~"
        elif -0.05 < x < 0.05:
            msg_3 = f"[color=FFFFFF]  d/y: {d/y:.4f}   d/x: ~   x/y: {x/y:.4f}"
        else:
            msg_3 = f"[color=FFFFFF]  d/y: {d/y:.4f}   d/x: {d/x:.4f}   x/y: {x/y:.4f}"
        self.label_wid.text = msg_1 + "\n" + msg_2 + "\n" + msg_3

    def cap2_sec2_pag1(self):
        """Control sliders events"""
        Clock.schedule_interval(self.update_points, 0.01)
        Bx = self.slider_x.value
        By = self.slider_y.value

        # Point A
        self.p_A = [self.width / 2, self.height * 3 / 4]
        # Point B
        self.p_B = [self.width / 2 * (1 + Bx), self.height * (3 + By) / 4]
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

        x = Bx * 10  # Scaled
        y = By * 10  # Scaled
        d = sqrt(pow(x, 2) + pow(y, 2))

        # Azul: 3465A4, Rojo: FF0000, Amarillo: D9A560, Blanco: FFFFFF
        msg_1 = f"[color=3465A4]  x: {x:.1f}  [color=FF0000]y: {y:.1f}  [color=D9A560]d: {d:.4f}"
        if d < 0.05:
            msg_2 = f"[color=FFFFFF]  y/d: ~   x/d: ~   y/x: ~"
            msg_3 = f"[color=3465A4]  A: 0  [color=FF0000]B: 0  [color=D9A560]C: 0"
        elif -0.05 < x < 0.05:
            msg_2 = f"[color=FFFFFF]  y/d: {y/d:.4f}   x/d: {x/d:.4f}   y/x: ~"
            msg_3 = f"[color=3465A4]  A: {degrees(asin(x/d)):.2f}° ({asin(x/d):.4f})  [color=FF0000]B: {degrees(asin(y/d)):.2f}° ({asin(y/d):.4f})  [color=D9A560]C: 90° ({(pi/2):.4f})"
        else:
            msg_2 = f"[color=FFFFFF]  y/d: {y/d:.4f}   x/d: {x/d:.4f}   y/x: {y/x:.4f}"
            msg_3 = f"[color=3465A4]  A: {degrees(asin(x/d)):.2f}° ({asin(x/d):.4f})  [color=FF0000]B: {degrees(asin(y/d)):.2f}° ({asin(y/d):.4f})  [color=D9A560]C: 90° ({(pi/2):.4f})"
        self.label_wid.text = msg_1 + "\n" + msg_2 + "\n" + msg_3
        """
        +-----------------+-------+-------+-------+-------+-------+
        |                 | 0°    | 30°   | 45°   | 60°   | 90°   |
        +=================+=======+=======+=======+=======+=======+
        | Seno de ...     | √0/2  | √1/2  | √2/2  | √3/2  | √4/2  |
        +-----------------+-------+-------+-------+-------+-------+
        | Coseno de ...   | √4/2  | √3/2  | √2/2  | √1/2  | √0/2  |
        +-----------------+-------+-------+-------+-------+-------+
        | Tangente de ... | √0/√4 | √1/√3 | √2/√2 | √3/√1 | √4/√0 |
        +-----------------+-------+-------+-------+-------+-------+
        """

    def cap2_sec2_pag2(self):
        """Control sliders events"""
        Clock.schedule_interval(self.update_points, 0.01)
        Bx = self.slider_x.value
        By = self.slider_y.value

        # Point bottom-left
        self.p_A = (self.width / 3, self.height * 5 / 8)
        # Point bottom-right
        self.p_B = (self.width * 2 / 3, self.height * 5 / 8)
        # Point bottom-top
        self.p_C = (self.width * (1 + Bx) / 2, self.height * (3 + By) / 4)

        # Horizontal fixed line bottom
        self.l_1 = [self.p_A[0], self.p_A[1], self.p_B[0], self.p_B[1]]
        # Left line
        self.l_2 = [self.p_A[0], self.p_A[1], self.p_C[0], self.p_C[1]]
        # Right line
        self.l_3 = [self.p_C[0], self.p_C[1], self.p_B[0], self.p_B[1]]

        x = Bx * 10  # Scaled
        y = By * 10  # Scaled

        # Ángulos
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
            Vector((self.l_2[0] - self.l_2[2]), (self.l_2[1] - self.l_2[3])).angle(
                ((self.l_3[2] - self.l_3[0]), (self.l_3[3] - self.l_3[1]))
            )
        )

        msg_angulos = (
            f"Ángulos  [color=FF3333]A: [color=FFFFFF]{round(ang_A, 2)}"
            + f"[color=3465A4]  B: [color=FFFFFF]{round(ang_B, 2)}"
            + f"[color=D9A560]  C: [color=FFFFFF]{round(ang_C, 2)}"
        )

        # Lados
        if abs(self.p_A[1] - self.p_C[1]) < 0.5:
            msg_angulos_2 = "Los tres puntos son colineales. No hay triángulo!"
        else:
            msg_angulos_2 = ""

        lado_a = (
            Vector(self.p_B[0], self.p_B[1]).distance((self.p_C[0], self.p_C[1])) / 10
        )
        lado_b = (
            Vector(self.p_A[0], self.p_A[1]).distance((self.p_C[0], self.p_C[1])) / 10
        )
        lado_c = (
            Vector(self.p_B[0], self.p_B[1]).distance((self.p_A[0], self.p_A[1])) / 10
        )
        msg_lados = (
            f"Lados  [color=FF3333]a: [color=FFFFFF]{round(lado_a, 2)}"
            + f"[color=3465A4]  b: [color=FFFFFF]{round(lado_b, 2)}"
            + f"[color=D9A560]  c: [color=FFFFFF]{round(lado_c, 2)}"
        )

        msg_senos = (
            f"[color=FF3333]sen(A): [color=FFFFFF]{round(sin(radians(ang_A)), 4)}"
            + f"[color=3465A4]  sen(B): [color=FFFFFF]{round(sin(radians(ang_B)), 4)}"
            + f"[color=D9A560]  sen(C): [color=FFFFFF]{round(sin(radians(ang_C)), 4)}"
        )

        self.label_wid.text = (
            msg_angulos + "\n" + msg_lados + "\n" + msg_senos + "\n" + msg_angulos_2
        )

        # Adding offset to draw points correctly
        self.p_A = (self.p_A[0] - offset, self.p_A[1] - offset)
        self.p_B = (self.p_B[0] - offset, self.p_B[1] - offset)
        self.p_C = (self.p_C[0] - offset, self.p_C[1] - offset)

    def cap2_sec2_pag3(self):
        """Control sliders events"""
        Clock.schedule_interval(self.update_points, 0.01)
        Bx = self.slider_x.value
        By = self.slider_y.value

        # Point bottom-left
        self.p_A = (self.width / 3, self.height * 5 / 8)
        # Point bottom-right
        self.p_B = (self.width * 2 / 3, self.height * 5 / 8)
        # Point bottom-top
        self.p_C = (self.width * (1 + Bx) / 2, self.height * (3 + By) / 4)

        # Horizontal fixed line bottom
        self.l_1 = [self.p_A[0], self.p_A[1], self.p_B[0], self.p_B[1]]
        # Left line
        self.l_2 = [self.p_A[0], self.p_A[1], self.p_C[0], self.p_C[1]]
        # Right line
        self.l_3 = [self.p_C[0], self.p_C[1], self.p_B[0], self.p_B[1]]

        x = Bx * 10  # Scaled
        y = By * 10  # Scaled

        # Ángulos
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
            Vector((self.l_2[0] - self.l_2[2]), (self.l_2[1] - self.l_2[3])).angle(
                ((self.l_3[2] - self.l_3[0]), (self.l_3[3] - self.l_3[1]))
            )
        )

        msg_angulos = (
            f"Ángulos  [color=FF3333]A: [color=FFFFFF]{round(ang_A, 2)}"
            + f"[color=3465A4]  B: [color=FFFFFF]{round(ang_B, 2)}"
            + f"[color=D9A560]  C: [color=FFFFFF]{round(ang_C, 2)}"
        )

        # Lados
        if abs(self.p_A[1] - self.p_C[1]) < 0.5:
            msg_angulos_2 = "Los tres puntos son colineales. No hay triángulo!"
        else:
            msg_angulos_2 = ""

        lado_a = (
            Vector(self.p_B[0], self.p_B[1]).distance((self.p_C[0], self.p_C[1])) / 10
        )
        lado_b = (
            Vector(self.p_A[0], self.p_A[1]).distance((self.p_C[0], self.p_C[1])) / 10
        )
        lado_c = (
            Vector(self.p_B[0], self.p_B[1]).distance((self.p_A[0], self.p_A[1])) / 10
        )
        msg_lados = (
            f"Lados  [color=FF3333]a: [color=FFFFFF]{round(lado_a, 2)}"
            + f"[color=3465A4]  b: [color=FFFFFF]{round(lado_b, 2)}"
            + f"[color=D9A560]  c: [color=FFFFFF]{round(lado_c, 2)}"
        )

        msg_senos = (
            f"[color=FF3333]cos(A): [color=FFFFFF]{round(cos(radians(ang_A)), 4)}"
            + f"[color=3465A4]  cos(B): [color=FFFFFF]{round(cos(radians(ang_B)), 4)}"
            + f"[color=D9A560]  cos(C): [color=FFFFFF]{round(cos(radians(ang_C)), 4)}"
        )

        self.label_wid.text = (
            msg_angulos + "\n" + msg_lados + "\n" + msg_senos + "\n" + msg_angulos_2
        )

        # Adding offset to draw points correctly
        self.p_A = (self.p_A[0] - offset, self.p_A[1] - offset)
        self.p_B = (self.p_B[0] - offset, self.p_B[1] - offset)
        self.p_C = (self.p_C[0] - offset, self.p_C[1] - offset)

    def cap2_sec3_pag1(self):
        """Control sliders events"""
        Clock.schedule_interval(self.update_points, 0.01)
        Cx = self.slider_x.value
        Cy = self.slider_y.value

        # Minimun between width and height of the canvas
        l = min(self.width, self.height / 2)
        # Unit of measure
        unit = l / 20
        base_length = 7
        # Point top-right, at the same width as B, at 45°. In the center of the canvas
        self.p_D = (self.width / 2, self.height * 3 / 4 + 2 * unit)
        # Point bottom-left
        self.p_A = (self.p_D[0] - base_length * unit, self.p_D[1] - base_length * unit)
        # Point bottom-right
        self.p_B = (self.p_D[0], self.p_A[1])
        # Point top-left
        self.p_C = (self.p_D[0] + Cx * unit, self.p_D[1] + Cy * unit)

        # Horizontal fixed line bottom
        self.l_1 = [self.p_A[0], self.p_A[1], self.p_B[0], self.p_B[1]]
        # Left line
        self.l_2 = [self.p_A[0], self.p_A[1], self.p_D[0], self.p_D[1]]
        # Right line
        self.l_3 = [self.p_B[0], self.p_B[1], self.p_C[0], self.p_C[1]]
        # Top line
        self.l_4 = [self.p_D[0], self.p_D[1], self.p_C[0], self.p_C[1]]

        # Transforming points to compute more easily.
        ax = round((self.p_A[0] - self.p_A[0]) / unit, 0)
        ay = round((self.p_A[1] - self.p_A[1]) / unit, 0)
        bx = round((self.p_B[0] - self.p_A[0]) / unit, 0)
        by = round((self.p_B[1] - self.p_A[1]) / unit, 0)
        cx = round((self.p_C[0] - self.p_A[0]) / unit, 0)  # Mobile point
        cy = round((self.p_C[1] - self.p_A[1]) / unit, 0)  # Mobile point
        dx = round((self.p_D[0] - self.p_A[0]) / unit, 0)
        dy = round((self.p_D[1] - self.p_A[1]) / unit, 0)

        # A lot of conditions to check the type of quadrangle
        msg_tipo = ""
        # If the mobile point is in the origin
        if cx == 0 and cy == 0:
            msg_tipo = "No hay polígono, solo dos rectas unidas en un punto"
        elif cx == 2 * base_length and cy == base_length:
            msg_tipo = "1 Simple, convexo, paralelogramo (lados opuestos paralelos)"
        # If the mobile point is in the diagonal line at 45° with B
        elif cx - cy == base_length and cx > bx:
            msg_tipo = "2 Simple, convexo, trapecio (lados AD y BC paralelos)"
        elif cx > dx and cy == dy:
            msg_tipo = "3 Simple, convexo, trapecio (lados AB y CD paralelos)"
        elif cx > bx and cy < by:
            msg_tipo = "4 Simple, cóncavo, trapezoide (no hay lados paralelos)"
        # If the mobile point is in the horizontal line AB
        elif cy == by:
            if cx >= bx:
                msg_tipo = "5 Los puntos A, B y C son colineales, es un triángulo!"
            else:
                msg_tipo = "6 Complejo, rectas AB y BC se cruzan"
        # If the mobile point is in the vertical line BD
        elif cx == bx:
            if cy > by and cy <= dy:
                msg_tipo = "7 Los puntos B, C y D son colineales, es un triángulo!"
            else:
                msg_tipo = "8 Complejo, rectas BC y CD se cruzan"
        # If the mobile point is in the diagonal line at 45° with D
        elif cx - cy == dx - dy:
            if cx >= bx:
                msg_tipo = "9 Los puntos A, B y C son colineales, es un triángulo!"
            else:
                msg_tipo = "10 Complejo, rectas AD y CD se cruzan"
        # If the mobile point is in the diagonal line higher than 45° (with AD)
        elif cy - cx > 0:
            if cx <= bx and cy > by:
                msg_tipo = "11 Complejo, rectas AD y BC se cruzan"
            else:
                msg_tipo = "12 Simple, cóncavo, trapezoide (no hay lados paralelos)"
        # If the mobile point is in the diagonal line lower than 45° (with AD)
        elif cy - cx < 0 and cx < bx:
            if cy < by:
                msg_tipo = "13 Complejo, rectas AB y CD se cruzan"
            else:
                msg_tipo = "14 Simple, cóncavo, trapezoide (no hay lados paralelos)"
        else:
            msg_tipo = "15 Simple, convexo, trapezoide (no hay lados paralelos)"

        self.label_wid.text = (
            f"[color=D9A560]A({ax}, {ay})  [color=3465A4]B({bx}, {by})\
        [color=00FF00]C({cx}, {cy})  [color=FF0000]D({dx}, {dy})"
            + "[color=FFFFFF]\n"
            + msg_tipo
        )

        # Adding offset to draw points correctly
        self.p_A = (self.p_A[0] - offset, self.p_A[1] - offset)
        self.p_B = (self.p_B[0] - offset, self.p_B[1] - offset)
        self.p_C = (self.p_C[0] - offset, self.p_C[1] - offset)
        self.p_D = (self.p_D[0] - offset, self.p_D[1] - offset)

    def cap2_sec3_pag2(self):
        """Control sliders events"""
        Clock.schedule_interval(self.update_points, 0.01)
        Cx = self.slider_x.value
        Cy = self.slider_y.value

        # Minimun between width and height of the canvas
        l = min(self.width, self.height / 2)
        # Unit of measure
        unit = l / 20
        base_length = 7
        # Point top-right, at the same width as B, at 45°. In the center of the canvas
        self.p_D = (
            self.width / 2 - base_length * unit + Cx * unit,
            self.height * 3 / 4 + (2 + Cy) * unit,
        )
        # Point bottom-left
        self.p_A = (
            self.width / 2 - base_length * unit,
            self.height * 3 / 4 + 2 * unit - base_length * unit,
        )
        # Point bottom-right
        self.p_B = (self.width / 2, self.height * 3 / 4 + 2 * unit - base_length * unit)
        # Point top-left
        self.p_C = (
            self.width / 2 + Cx * unit,
            self.height * 3 / 4 + (2 + Cy) * unit,
        )

        # Horizontal fixed line bottom
        self.l_1 = [self.p_A[0], self.p_A[1], self.p_B[0], self.p_B[1]]
        # Left line
        self.l_2 = [self.p_A[0], self.p_A[1], self.p_D[0], self.p_D[1]]
        # Right line
        self.l_3 = [self.p_B[0], self.p_B[1], self.p_C[0], self.p_C[1]]
        # Top line
        self.l_4 = [self.p_D[0], self.p_D[1], self.p_C[0], self.p_C[1]]

        # Transforming points to compute more easily.
        ax = round((self.p_A[0] - self.p_A[0]) / unit, 0)
        ay = round((self.p_A[1] - self.p_A[1]) / unit, 0)
        bx = round((self.p_B[0] - self.p_A[0]) / unit, 0)
        by = round((self.p_B[1] - self.p_A[1]) / unit, 0)
        cx = round((self.p_C[0] - self.p_A[0]) / unit, 0)  # Mobile point
        cy = round((self.p_C[1] - self.p_A[1]) / unit, 0)  # Mobile point
        dx = round((self.p_D[0] - self.p_A[0]) / unit, 0)
        dy = round((self.p_D[1] - self.p_A[1]) / unit, 0)

        # A lot of conditions to check the type of quadrangle
        msg_tipo = ""
        if cy == by:
            msg_tipo = "No hay polígono, solo es una línea recta."
        elif cx == base_length:
            if cy == base_length:
                msg_tipo = "Cuadrado: 4 lados iguales, 4 ángulos iguales."
            else:
                msg_tipo = "Rectángulo: 4 ángulos iguales, lados opuestos iguales."
        elif abs(dx) == 5 and dy == 5:
            msg_tipo = "Rombo: 4 lados iguales, ángulos opuestos iguales."
        else:
            msg_tipo = "Romboide: lados opuestos iguales, ángulos opuestos iguales."

        self.label_wid.text = (
            f"[color=D9A560]A({ax}, {ay})  [color=3465A4]B({bx}, {by})\
        [color=00FF00]C({cx}, {cy})  [color=FF0000]D({dx}, {dy})"
            + "[color=FFFFFF]\n"
            + msg_tipo
        )

        # Adding offset to draw points correctly
        self.p_A = (self.p_A[0] - offset, self.p_A[1] - offset)
        self.p_B = (self.p_B[0] - offset, self.p_B[1] - offset)
        self.p_C = (self.p_C[0] - offset, self.p_C[1] - offset)
        self.p_D = (self.p_D[0] - offset, self.p_D[1] - offset)

    def cap2_sec4_pag0(self):
        """Control sliders events"""
        Clock.schedule_interval(self.update_points, 0.01)
        Cx = (
            self.slider_x.value
        )  # Number of points for horizontal line (from 0 to 'infinite')
        Cy = self.slider_y.value  # Vertical position of the horizontal mobile line
        max_value = self.slider_x.max  # 'infinite' points for horizontal line

        # Mobile point left
        self.p_A = (
            self.width * 1 / 3,
            self.height * (2.5 + Cy) / 4,
        )
        # Mobile oint rigth
        self.p_B = (
            self.width * 2 / 3,
            self.height * (2.5 + Cy) / 4,
        )
        # Fixed point left
        self.p_C = (
            self.width * 1 / 3,
            self.height * 2.5 / 4,
        )
        # Fixed point rigth
        self.p_D = (
            self.width * 2 / 3,
            self.height * 2.5 / 4,
        )

        # Horizontal mobile line from bottom to top
        self.l_1 = [self.p_A[0], self.p_A[1], self.p_B[0], self.p_B[1]]
        # Horizontal fixed bottom line
        self.l_2 = [0, 0, 0, 0]
        # Vertical line left
        self.l_3 = [0, 0, 0, 0]
        # Vertical line rigth
        self.l_4 = [0, 0, 0, 0]

        if Cx == max_value and Cy > 0:
            # Rectangle
            self.p_COLOR = (1, 0, 0, 1)
            self.p_POS = (self.width * 1 / 3, self.height * 2.5 / 4)
            self.p_SIZE = (
                self.p_B[0] - self.p_A[0],
                self.p_A[1] - self.height * 2.5 / 4,
            )
            # Perimeter lines
            self.l_2 = [self.p_C[0], self.p_C[1], self.p_D[0], self.p_D[1]]
            self.l_3 = [self.p_C[0], self.p_C[1], self.p_A[0], self.p_A[1]]
            self.l_4 = [self.p_D[0], self.p_D[1], self.p_B[0], self.p_B[1]]
            # To override the horizontal mobile line
            self.l_5 = [
                self.p_A[0],
                self.p_A[1],
                self.p_B[0],
                self.p_B[1],
            ]
        else:
            # Rectangle
            self.p_COLOR = (1, 1, 1, 1)
            self.p_POS = (0, 0)
            self.p_SIZE = (self.p_B[0] - self.p_A[0], 3)
            # Perimeter lines
            self.l_2 = [0, 0, 0, 0]
            self.l_3 = [0, 0, 0, 0]
            self.l_4 = [0, 0, 0, 0]
            self.l_5 = [0, 0, 0, 0]

        self.label_wid.text = f"[color=FFFFFF]Número de puntos en la recta: {int(Cx**10) if Cx < max_value else 'Infinitos'}"

        # Adding offset to draw points correctly
        self.p_A = (self.p_A[0] - offset, self.p_A[1] - offset)
        self.p_B = (self.p_B[0] - offset, self.p_B[1] - offset)
        self.p_C = (self.p_C[0] - offset, self.p_C[1] - offset)
        self.p_D = (self.p_D[0] - offset, self.p_D[1] - offset)

    def cap2_sec4_pag1(self):
        """Control sliders events"""
        Clock.schedule_interval(self.update_points, 0.01)
        Cx = self.slider_x.value
        Cy = self.slider_y.value

        # Minimun between width and height of the canvas
        l = min(self.width, self.height / 2)
        # Unit of measure
        unit = l / 20
        base_length = 7
        # Point top-right, at the same width as B, at 45°. In the center of the canvas
        self.p_D = (
            self.width / 2 - base_length * unit + Cx * unit,
            self.height * 3 / 4 + (2 + Cy) * unit,
        )
        # Point bottom-left
        self.p_A = (
            self.width / 2 - base_length * unit,
            self.height * 3 / 4 + 2 * unit - base_length * unit,
        )
        # Point bottom-right
        self.p_B = (self.width / 2, self.height * 3 / 4 + 2 * unit - base_length * unit)
        # Point top-left
        self.p_C = (
            self.width / 2 + Cx * unit,
            self.height * 3 / 4 + (2 + Cy) * unit,
        )

        # Horizontal fixed line bottom
        self.l_1 = [self.p_A[0], self.p_A[1], self.p_B[0], self.p_B[1]]
        # Left line
        self.l_2 = [self.p_A[0], self.p_A[1], self.p_D[0], self.p_D[1]]
        # Right line
        self.l_3 = [self.p_B[0], self.p_B[1], self.p_C[0], self.p_C[1]]
        # Top line
        self.l_4 = [self.p_D[0], self.p_D[1], self.p_C[0], self.p_C[1]]

        # Transforming points to compute more easily.
        ax = round((self.p_A[0] - self.p_A[0]) / unit, 0)
        ay = round((self.p_A[1] - self.p_A[1]) / unit, 0)
        bx = round((self.p_B[0] - self.p_A[0]) / unit, 0)
        by = round((self.p_B[1] - self.p_A[1]) / unit, 0)
        cx = round((self.p_C[0] - self.p_A[0]) / unit, 0)  # Mobile point
        cy = round((self.p_C[1] - self.p_A[1]) / unit, 0)  # Mobile point
        dx = round((self.p_D[0] - self.p_A[0]) / unit, 0)
        dy = round((self.p_D[1] - self.p_A[1]) / unit, 0)
        base = abs(bx - ax)
        height = abs(cy - ay)
        side = sqrt((ax - dx) ** 2 + (ay - dy) ** 2)
        area = base * height

        # A lot of conditions to check the type of quadrangle
        msg_tipo = ""
        if cy == by:
            msg_tipo = "No hay polígono, solo es una línea recta."
        elif cx == base_length:
            if cy == base_length:
                msg_tipo = (
                    f"Cuadrado!  Área = {base} x {height} = {area} \n"
                    + f"Perímetro = 2 x ({base} + {height}) = {2 * (base + height)}"
                )
            else:
                msg_tipo = (
                    f"Rectángulo!  Área = {base} x {height} = {area} \n"
                    + f"Perímetro = 2 x ({base} + {height}) = {2 * (base + height)}"
                )
        elif abs(dx) == 5 and dy == 5:
            msg_tipo = (
                f"¿Rombo?  Área = {base} x {height} = {area} \n"
                + f"Perímetro = 2 x ({base} + {side:.2f}) = {(2 * (base + side)):.2f}"
            )
        else:
            msg_tipo = (
                f"Romboide!  Área = {base} x {height} = {area} \n"
                + f"Perímetro = 2 x ({base} + {side:.2f}) = {(2 * (base + side)):.2f}"
            )

        # Rectangle (area)
        self.p_POS = (self.p_A[0], self.p_A[1])
        self.p_SIZE = (self.p_B[0] - self.p_A[0], self.p_C[1] - self.p_B[1])

        self.label_wid.text = (
            f"[color=D9A560]A({ax}, {ay})  [color=3465A4]B({bx}, {by})\
        [color=00FF00]C({cx}, {cy})  [color=FF0000]D({dx}, {dy})"
            + "[color=FFFFFF]\n"
            + msg_tipo
        )

        # Adding offset to draw points correctly
        self.p_A = (self.p_A[0] - offset, self.p_A[1] - offset)
        self.p_B = (self.p_B[0] - offset, self.p_B[1] - offset)
        self.p_C = (self.p_C[0] - offset, self.p_C[1] - offset)
        self.p_D = (self.p_D[0] - offset, self.p_D[1] - offset)

    def cap2_sec4_pag2(self):
        """Control sliders events"""
        Clock.schedule_interval(self.update_points, 0.01)
        Cx = self.slider_x.value
        Cy = self.slider_y.value

        # Minimun between width and height of the canvas
        l = min(self.width, self.height / 2)
        # Unit of measure
        unit = l / 20
        base_length = 7
        # Point bottom-left
        self.p_A = (
            self.width / 2 - base_length * unit,
            self.height * 3 / 4 + 2 * unit - base_length * unit,
        )
        # Point bottom-right
        self.p_B = (self.width / 2, self.height * 3 / 4 + 2 * unit - base_length * unit)
        # Point top-left
        self.p_C = (
            self.width / 2 + Cx * unit,
            self.height * 3 / 4 + (2 + Cy) * unit,
        )
        # Point top-right, at the same width as B, at 45°. In the center of the canvas
        self.p_D = (
            self.width / 2 - base_length * unit + Cx * unit,
            self.height * 3 / 4 + (2 + Cy) * unit,
        )
        # Hight of the triangle
        self.p_E = (self.p_B[0], self.p_C[1])

        # Horizontal fixed line bottom
        self.l_1 = [self.p_A[0], self.p_A[1], self.p_B[0], self.p_B[1]]
        # Left line
        self.l_2 = [self.p_A[0], self.p_A[1], self.p_C[0], self.p_C[1]]
        # Right line
        self.l_3 = [self.p_B[0], self.p_B[1], self.p_C[0], self.p_C[1]]
        # Hight of the triangle
        self.l_4 = [self.p_B[0], self.p_B[1], self.p_E[0], self.p_E[1]]
        # Paralelogram left line
        self.l_5 = [self.p_A[0], self.p_A[1], self.p_D[0], self.p_D[1]]
        # Paralelogram top line
        self.l_6 = [self.p_D[0], self.p_D[1], self.p_C[0], self.p_C[1]]

        # Transforming points to compute more easily.
        ax = round((self.p_A[0] - self.p_A[0]) / unit, 0)
        ay = round((self.p_A[1] - self.p_A[1]) / unit, 0)
        bx = round((self.p_B[0] - self.p_A[0]) / unit, 0)
        by = round((self.p_B[1] - self.p_A[1]) / unit, 0)
        cx = round((self.p_C[0] - self.p_A[0]) / unit, 0)  # Mobile point
        cy = round((self.p_C[1] - self.p_A[1]) / unit, 0)  # Mobile point
        dx = round((self.p_D[0] - self.p_A[0]) / unit, 0)
        dy = round((self.p_D[1] - self.p_A[1]) / unit, 0)
        base = abs(bx - ax)
        height = abs(cy - ay)
        side_left = sqrt((ax - cx) ** 2 + (ay - cy) ** 2)
        side_right = sqrt((bx - cx) ** 2 + (by - cy) ** 2)
        area = base * height / 2
        perimeter = base + side_left + side_right

        # A lot of conditions to check the type of quadrangle
        msg_tipo = ""
        if cy == by:
            msg_tipo = "No hay polígono, solo es una línea recta."
        else:
            msg_tipo = (
                f"Área = {base} x {height} / 2 = {area} \n"
                + f"Perímetro = {base} + {side_left:.2f} + {side_right:.2f} = {perimeter:.2f}"
            )

        # Rectangle (area)
        self.p_POS = (self.p_A[0], self.p_A[1])
        self.p_SIZE = (self.p_B[0] - self.p_A[0], self.p_C[1] - self.p_B[1])

        self.label_wid.text = (
            f"[color=D9A560]A({ax}, {ay})  [color=3465A4]B({bx}, {by})\
        [color=00FF00]C({cx}, {cy})  [color=FF0000]D({dx}, {dy})"
            + "[color=FFFFFF]\n"
            + "[color=FF0000]Triángulo! [color=FFFFFF]"
            + msg_tipo
        )

        # Adding offset to draw points correctly
        self.p_A = (self.p_A[0] - offset, self.p_A[1] - offset)
        self.p_B = (self.p_B[0] - offset, self.p_B[1] - offset)
        self.p_C = (self.p_C[0] - offset, self.p_C[1] - offset)
        self.p_D = (self.p_D[0] - offset, self.p_D[1] - offset)
        self.p_E = (self.p_E[0] - offset, self.p_E[1] - offset)

    def cap2_sec5_pag0(self):
        """Control sliders events"""
        Clock.schedule_interval(self.update_points, 0.01)
        rot = self.slider_x.value  # Rotation of the polygon
        vertices = self.slider_y.value  # Number of vertices of the polygon (3-20)

        # Fixed point center
        self.p_A = (self.width / 2, self.height * 3 / 4)

        self.v_0 = []
        istep = (pi * 2) / float(vertices)
        fase = pi / 2 if vertices != 4 else pi / 4
        for i in range(vertices):
            x = self.p_A[0] + cos(istep * i + fase + rot) * self.height * 0.5 / 4
            y = self.p_A[1] + sin(istep * i + fase + rot) * self.height * 0.5 / 4
            self.v_0.extend([x, y])
        # To close the polygon
        self.v_0.extend([self.v_0[0], self.v_0[1]])

        polygon_names = [
            "",
            "",
            "",
            "Triángulo equilátero",
            "Cuadrado",
            "Pentágono",
            "Hexágono",
            "Heptágono",
            "Octágono",
            "Eneágono",
            "Decágono",
        ]
        self.label_wid.text = f"[color=FFFFFF]{polygon_names[vertices]}, tiene {vertices} lados (vertices)."

        # Adding offset to draw points correctly
        self.p_A = (self.p_A[0] - offset, self.p_A[1] - offset)

    def cap2_sec5_pag1(self):
        """Control sliders events"""
        Clock.schedule_interval(self.update_points, 0.01)
        rot = self.slider_x.value  # Rotation of the polygon
        vertices = (
            self.slider_y.value
        )  # Number of vertices of the polygon (4, 6, 8, 10)

        # Fixed point center
        self.p_A = (self.width / 2, self.height * 3 / 4)

        self.v_0 = []
        istep = (pi * 2) / float(vertices)
        fase = pi / 2 if vertices != 4 else pi / 4
        for i in range(vertices):
            x = self.p_A[0] + cos(istep * i + fase + rot) * self.height * 0.5 / 4
            y = self.p_A[1] + sin(istep * i + fase + rot) * self.height * 0.5 / 4
            self.v_0.extend([x, y])
        # To close the polygon
        self.v_0.extend([self.v_0[0], self.v_0[1]])

        polygon_names = [
            "",
            "",
            "",
            "",
            "Cuadrado",
            "",
            "Hexágono",
            "",
            "Octágono",
            "",
            "Decágono",
        ]

        if vertices == 4:
            self.l_1 = (self.v_0[0], self.v_0[1], self.v_0[4], self.v_0[5])
            self.l_2 = (self.v_0[2], self.v_0[3], self.v_0[6], self.v_0[7])
            self.l_3 = (0, 0, 0, 0)
            self.l_4 = (0, 0, 0, 0)
            self.l_5 = (0, 0, 0, 0)
        elif vertices == 6:
            self.l_1 = (self.v_0[0], self.v_0[1], self.v_0[6], self.v_0[7])
            self.l_2 = (self.v_0[2], self.v_0[3], self.v_0[8], self.v_0[9])
            self.l_3 = (self.v_0[4], self.v_0[5], self.v_0[10], self.v_0[11])
            self.l_4 = (0, 0, 0, 0)
            self.l_5 = (0, 0, 0, 0)
        elif vertices == 8:
            self.l_1 = (self.v_0[0], self.v_0[1], self.v_0[8], self.v_0[9])
            self.l_2 = (self.v_0[2], self.v_0[3], self.v_0[10], self.v_0[11])
            self.l_3 = (self.v_0[4], self.v_0[5], self.v_0[12], self.v_0[13])
            self.l_4 = (self.v_0[6], self.v_0[7], self.v_0[14], self.v_0[15])
            self.l_5 = (0, 0, 0, 0)
        elif vertices == 10:
            self.l_1 = (self.v_0[0], self.v_0[1], self.v_0[10], self.v_0[11])
            self.l_2 = (self.v_0[2], self.v_0[3], self.v_0[12], self.v_0[13])
            self.l_3 = (self.v_0[4], self.v_0[5], self.v_0[14], self.v_0[15])
            self.l_4 = (self.v_0[6], self.v_0[7], self.v_0[16], self.v_0[17])
            self.l_5 = (self.v_0[8], self.v_0[9], self.v_0[18], self.v_0[19])

        self.label_wid.text = f"[color=FFFFFF]{polygon_names[vertices]}, tiene {vertices} lados (vertices)."

        # Adding offset to draw points correctly
        self.p_A = (self.p_A[0] - offset, self.p_A[1] - offset)

    def cap2_sec5_pag2(self):
        """Control sliders events"""
        Clock.schedule_interval(self.update_points, 0.01)
        rot = self.slider_x.value  # Rotation of the polygon
        vertices = self.slider_y.value  # Number of vertices of the polygon (3-inf)
        inf_vertices = self.slider_y.max  # 'infinite' points for horizontal line

        # Fixed point center
        self.p_A = (self.width / 2, self.height * 3 / 4)

        self.v_0 = []
        istep = (pi * 2) / float(vertices)
        fase = pi / 2 if vertices != 4 else pi / 4
        for i in range(vertices):
            x = self.p_A[0] + cos(istep * i + fase + rot) * self.height * 0.5 / 4
            y = self.p_A[1] + sin(istep * i + fase + rot) * self.height * 0.5 / 4
            self.v_0.extend([x, y])
        # To close the polygon
        self.v_0.extend([self.v_0[0], self.v_0[1]])

        polygon_names = [
            "",
            "",
            "",
            "Triángulo",
            "Cuadrado",
            "Pentágono",
            "Hexágono",
            "Heptágono",
            "Octágono",
            "Eneágono",
            "Decágono",
            "Endecágono",
            "Dodecágono",
            "Tridecágono",
            "Tetradecágono",
            "Pentadecágono",
            "Hexadecágono",
            "Heptadecágono",
            "Octadecágono",
            "Eneadecágono",
            "Icoságono",
        ]
        polygon_name = polygon_names[vertices] if vertices < 20 else "Polígono"

        self.label_wid.text = f"[color=FFFFFF]{polygon_name}, {vertices if vertices < inf_vertices else '¿Infinitos?'} lados (vertices)."

        # Adding offset to draw points correctly
        self.p_A = (self.p_A[0] - offset, self.p_A[1] - offset)
