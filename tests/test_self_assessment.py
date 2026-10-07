"""Self-assessment stays wired through template, onboarding, behavior, and reset."""

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
LEARN = ROOT / "skills/learn"
FIELDS = ("Known problems:", "Known gaps:", "Learning targets:", "Yardstick:")


class SelfAssessmentTests(unittest.TestCase):
    def test_profile_template_has_self_assessment_fields(self):
        text = (LEARN / "state-templates.md").read_text()
        self.assertIn("## Self-assessment", text)
        self.assertIn("Not demonstrated understanding.", text)
        for field in FIELDS:
            self.assertIn(field, text)

    def test_onboarding_asks_for_each_field(self):
        text = (LEARN / "onboarding.md").read_text()
        for name in ("Known problems", "Known gaps", "Learning targets"):
            self.assertIn(name, text)

    def test_behavior_uses_self_assessment_without_counting_it_as_evidence(self):
        text = (LEARN / "behavior.md").read_text()
        self.assertIn("Self-assessment is a starting point, not evidence.", text)

    def test_learner_seed_is_offered_and_complete(self):
        self.assertIn("learner-seed.md", (LEARN / "onboarding.md").read_text())
        seed = (LEARN / "learner-seed.md").read_text()
        for section in ("## Goal", "## Known problems", "## Known gaps",
                        "## Learning targets", "## Yardstick"):
            self.assertIn(section, seed)
        self.assertIn("10. ", seed)

    def test_behavior_defines_reps_and_capability_check(self):
        text = (LEARN / "behavior.md").read_text()
        self.assertIn("## Hands-on reps", text)
        self.assertIn("`Capability check`", text)

    def test_reset_leaves_self_assessment_to_onboarding(self):
        text = (ROOT / "skills/reset/reset.py").read_text()
        self.assertIn("self-assessment", text)


if __name__ == "__main__":
    unittest.main()
