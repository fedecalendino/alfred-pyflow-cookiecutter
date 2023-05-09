from pyflow.testing import WorklowTestCase

from data import FORTUNES
from main import main


class TestWorkflow(WorklowTestCase):
    def test_run(self):
        envs = {}
        args = ["3"]

        workflow = self.workflow(**envs)
        feedback = self.run_workflow(workflow, main, *args)

        items = feedback["items"]

        for item in items:
            self.assertIn(item["title"], FORTUNES)
            self.assertIn("Your lucky numbers are:", item["subtitle"])
            self.assertEqual(item["icon"]["path"], "./icon.png")
            self.assertTrue(item["valid"])

        self.assertEqual(len(items), 3)
