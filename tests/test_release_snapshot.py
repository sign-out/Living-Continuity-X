"""LCX release guard: shared runtime, isolated host defaults."""
import json
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))
class LCXReleaseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mod = load("LCX.json")
        cls.source = load("exports/LCX_Voyage_2026-11-03.json")
    def test_runtime_matches_voyage_source(self):
        self.assertEqual(self.mod["heroesVersion"], 37)
        self.assertEqual(self.mod["triggerDefinitions"], self.source["triggerDefinitions"])
        self.assertEqual(len(self.mod["triggerDefinitions"]), 86)
        self.assertEqual(self.mod["aiInstructions"], self.source["aiInstructions"])
        self.assertEqual(len(self.mod["aiInstructions"]), 15)
        self.assertEqual(sum(bool(t.get("script")) for t in self.mod["triggerDefinitions"].values()), 81)
    def test_native_host_defaults_are_not_overlaid(self):
        for field in ("storyStarts", "skills", "resourceSettings", "authorSeeds", "encounterElements", "characterArchetypes", "locationArchetypes", "regionArchetypes"):
            with self.subTest(field=field):
                self.assertEqual(self.mod[field], {})
        self.assertTrue(self.source["storyStarts"])
        self.assertIn("imagePromptConfiguration", self.mod)
    def test_combat_intents_and_native_contract_are_retained(self):
        self.assertIn("LCX Oct 2026 - Combat Focus", self.mod["aiInstructions"]["generateNPCIntents"])
        self.assertIn("Voyage Oct 2026 - Native State and Discovery", self.mod["aiInstructions"]["generateStory"])
        self.assertIn("lcx_bootstrap", self.mod["triggerDefinitions"])
if __name__ == "__main__":
    unittest.main()
