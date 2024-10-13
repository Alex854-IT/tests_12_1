import Runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = Runner.Runner("TestRunner")
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance,50)

    def test_run(self):
        runner2 = Runner.Runner("TestRunner")
        for i in range(10):
            runner2.run()
        self.assertEqual(runner2.distance,100)

    def test_challenge(self):
        runner3 = Runner.Runner("Runner1")
        runner4 = Runner.Runner("Runner2")
        for i in range(10):
            runner3.walk()
            runner4.run()
        self.assertNotEqual(runner3.distance,runner4.distance)

if __name__ == '__main__':
    unittest.main()