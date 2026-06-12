"""
Tests ejercicios 5 y 6

Autor: Eric Chaume García
"""

import unittest
import pandas as pd
from exercises.ex6 import fun_total_goals
from exercises.ex5 import add_points


class TestFunTotalGoals(unittest.TestCase):
    """Tests para fun_total_goals (Ej. 6)."""

    def test_goles_correctos(self):
        """Verifica que fun_total_goals calcula correctamente los goles locales, visitantes y totales."""
        data = pd.DataFrame({
            "FTHG": [2, 1, 3],
            "FTAG": [0, 2, 1],
        })

        home_goals, away_goals, total_goals = fun_total_goals(data)

        self.assertEqual(home_goals, 6)
        self.assertEqual(away_goals, 3)
        self.assertEqual(total_goals, 9)
        self.assertEqual(total_goals, home_goals + away_goals)

class TestAddPoints(unittest.TestCase):
    """Tests para add_points (Ej. 5)."""

    def test_puntos_por_resultado(self):
        """Verifica que add_points asigna 3/1/0 puntos según el resultado del partido."""
        data = pd.DataFrame({
            "FTR": ["H", "A", "D"],
        })

        result = add_points(data)

        # Victoria local: 3 pts local, 0 visitante
        self.assertEqual(result.loc[0, "HTP"], 3)
        self.assertEqual(result.loc[0, "ATP"], 0)

        # Victoria visitante: 0 pts local, 3 visitante
        self.assertEqual(result.loc[1, "HTP"], 0)
        self.assertEqual(result.loc[1, "ATP"], 3)

        # Empate: 1 pt cada uno
        self.assertEqual(result.loc[2, "HTP"], 1)
        self.assertEqual(result.loc[2, "ATP"], 1)


if __name__ == "__main__":
    unittest.main()
