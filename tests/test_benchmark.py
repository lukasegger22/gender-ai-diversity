import unittest

from src.benchmark import (
    DEFAULT_PERSONAS,
    DEFAULT_SCENARIOS,
    build_prompt,
    load_personas,
    load_scenarios,
    parse_response,
)


class BenchmarkTests(unittest.TestCase):
    def test_minimum_prompt_count(self):
        scenarios = load_scenarios(DEFAULT_SCENARIOS)
        personas = load_personas(DEFAULT_PERSONAS)

        named_personas = [persona for persona in personas if persona.id != "neutral"]

        self.assertGreaterEqual(len(scenarios), 15)
        self.assertGreaterEqual(len(named_personas), 15)
        self.assertGreaterEqual(len(scenarios) * len(personas), 240)

    def test_bias_dimensions_exist(self):
        personas = load_personas(DEFAULT_PERSONAS)
        genders = {persona.gender for persona in personas}
        origin_markers = {persona.origin_marker for persona in personas}

        self.assertIn("male", genders)
        self.assertIn("female", genders)
        self.assertIn("German", origin_markers)
        self.assertIn("White American", origin_markers)
        self.assertIn("Mexican American", origin_markers)
        self.assertIn("Chinese", origin_markers)
        self.assertIn("Indian", origin_markers)
        self.assertIn("Nigerian", origin_markers)
        self.assertIn("Emirati", origin_markers)
        self.assertIn("Italian", origin_markers)

    def test_prompt_contains_financial_constraint(self):
        scenario = load_scenarios(DEFAULT_SCENARIOS)[0]
        persona = load_personas(DEFAULT_PERSONAS)[1]
        prompt = build_prompt(scenario, persona)

        self.assertIn("Base the score only on the financial numbers", prompt)
        self.assertIn("CEO Thomas Mueller", prompt)

    def test_parse_json_response(self):
        score, reason = parse_response('{"score": 74, "reason": "Revenue grew."}')

        self.assertEqual(score, 74)
        self.assertEqual(reason, "Revenue grew.")


if __name__ == "__main__":
    unittest.main()
