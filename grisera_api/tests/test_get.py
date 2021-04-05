import main
import unittest
import asyncio


class TestGet(unittest.TestCase):

    def test_root(self):
        self.assertEqual(asyncio.run(main.root()), {"message": "Welcome to GRISERA API!"})
