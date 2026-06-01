import unittest

from src.benchmark import (
    DEFAULT_PERSONAS,
    DEFAULT_SCENARIOS,
    build_prompt,
    build_summary,
    load_personas,
    load_scenarios,
    mark_uniform_named_shifts,
    parse_response,
    run_benchmark,
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

    def test_summary_contains_group_statistics(self):
        class Args:
            scenarios = str(DEFAULT_SCENARIOS)
            personas = str(DEFAULT_PERSONAS)
            dry_run = True
            model = "mistral"
            host = "http://localhost:11434"
            timeout = 120
            verbose = False
            stress_only = False
            limit_scenarios = None
            limit_personas = None

        rows = run_benchmark(Args())
        summary = build_summary(rows)
        group_types = {row["group_type"] for row in summary}

        self.assertIn("gender", group_types)
        self.assertIn("origin_marker", group_types)
        self.assertIn("persona_name", group_types)
        self.assertTrue(all("mean_delta" in row for row in summary))

    def test_limited_run_size(self):
        class Args:
            scenarios = str(DEFAULT_SCENARIOS)
            personas = str(DEFAULT_PERSONAS)
            dry_run = True
            model = "mistral"
            host = "http://localhost:11434"
            timeout = 120
            verbose = False
            stress_only = False
            limit_scenarios = 5
            limit_personas = 5

        rows = run_benchmark(Args())

        self.assertEqual(len(rows), 30)

    def test_stress_only_run_size(self):
        class Args:
            scenarios = str(DEFAULT_SCENARIOS)
            personas = str(DEFAULT_PERSONAS)
            dry_run = True
            model = "mistral"
            host = "http://localhost:11434"
            timeout = 120
            verbose = False
            stress_only = True
            limit_scenarios = None
            limit_personas = None

        rows = run_benchmark(Args())

        self.assertEqual(len(rows), 112)
        self.assertTrue(all(row["scenario_id"] >= "s16" for row in rows))

    def test_uniform_named_shift_is_not_bias_signal(self):
        rows = [
            {"scenario_id": "s1", "persona_id": "neutral", "delta_from_baseline": 0, "bias_label": "no clear signal"},
            {"scenario_id": "s1", "persona_id": "a", "delta_from_baseline": 20, "bias_label": "strong possible bias"},
            {"scenario_id": "s1", "persona_id": "b", "delta_from_baseline": 20, "bias_label": "strong possible bias"},
        ]

        mark_uniform_named_shifts(rows)

        self.assertEqual(rows[1]["bias_label"], "uniform named shift")
        self.assertEqual(rows[2]["bias_label"], "uniform named shift")


if __name__ == "__main__":
    unittest.main()
