from unittest import TestCase
from WordSeacher import word_finder, grid_generator
from click.testing import CliRunner


class TestWordSearcher(TestCase):
    def test_word_finder_success(self):
        word = "Box"
        grid = [['B', 'X', 'D', 'X'], ['O', 'T', 'U', 'Q'],
                ['X', 'R', 'A', 'D'], ['Z', 'V', 'J', 'T']]
        grid_size = 4
        self.assertEqual(word_finder(word, grid, grid_size), word.upper())

    def test_word_finder_failure(self):
        word = "Pretty"
        grid = [['B', 'X', 'D', 'X'], ['O', 'T', 'U', 'Q'],
                ['X', 'R', 'A', 'D'], ['Z', 'V', 'J', 'T']]
        grid_size = 4
        self.assertEqual(word_finder(word, grid, grid_size), None)

    def test_grid_generator_exit_with_success(self):
        runner = CliRunner()
        result = runner.invoke(grid_generator)
        assert result.exit_code == 0
