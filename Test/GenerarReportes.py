import unittest
import HtmlTestRunner
import os


from Test import Plantilla


testCinco=unittest.TestLoader().loadTestsFromModule(Plantilla)

suite=unittest.TestSuite([testCinco])


runner= HtmlTestRunner.HTMLTestRunner(output="Resultados")

runner.run(suite)