import sys    

sys.path[0] = sys.path[0] + "\\..\\app"
print("In module products sys.path[0], __package__ ==", sys.path[0], __package__)

from api.ticktacktoe_functionality import validate_gamestate, check_winstates, has_invalid_char, has_illegal_size, has_bad_actor
import unittest

class game_validation(unittest.TestCase):
    def test_gamestate(self):
        board = [
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "O", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "X", "O", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "X", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "X", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "O", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
        ]
        self.assertEqual(validate_gamestate(board), "opening")
        board = [
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "O", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "X", "O", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "X", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "X", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "O", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "X", "", "", "", "O", "", "", "", "", "", "", ],
            [ "", "", "", "X", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "X", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "O", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
        ]
        self.assertEqual(validate_gamestate(board), "midgame")
        board = [
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "O", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "X", "O", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "X", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "X", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "X", "", "", "", "O", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "O", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
        ]
        self.assertEqual(validate_gamestate(board), "endgame")

    def test_winstate(self):
        board = [
            [ "X", "X", "X", "O", "X", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
        ]
        self.assertEqual(check_winstates(board, 0, 0), 3)
        board = [
            [ "O", "O", "O", "O", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
        ]
        self.assertEqual(check_winstates(board, 0, 0), -4)

    def test_invalid_chars(self):
        board = [
            [ "O", "O", "O", "O", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "?", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
        ]
        self.assertEqual(has_invalid_char(board), True)
        board = [
            [ "O", "O", "O", "O", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
        ]
        self.assertEqual(has_invalid_char(board), False)
    
    def test_board_size(self):
        board = [
            [ "O", "O", "O", "O", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", ""],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
        ]
        self.assertEqual(has_illegal_size(board), True)
        board = [
            [ "O", "O", "O", "O", "", "", "", "", "", "", "", "", "", "", "", ],
        ]
        self.assertEqual(has_illegal_size(board), True)
        board = [
            [ "O", "O", "O", "O", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
        ]
        self.assertEqual(has_illegal_size(board), False)
    
    def test_for_badactors(self):
        board = [
            [ "O", "O", "O", "O", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
        ]
        self.assertEqual(has_bad_actor(board), True)
        board = [
            [ "O", "X", "O", "X", "X", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
        ]
        self.assertEqual(has_bad_actor(board), False)
        board = [
            [ "O", "X", "O", "O", "X", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
            [ "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
        ]
        self.assertEqual(has_bad_actor(board), False)
if __name__ == "__main__":
    unittest.main()