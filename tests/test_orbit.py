import unittest

from orbit.parser import parse
from orbit.checker import check_program, OrbitCheckError
from orbit.ast import EntityNode, ObservationNode, Program


class OrbitParserTests(unittest.TestCase):
    def test_entity_and_observation_parse_to_normalized_ast(self):
        source = '''
        entity company "company:example" {
          legal_name "Example Corporation"
          jurisdiction "TH"
        }
        observation "obs:revenue:2026" {
          subject company "company:example"
          predicate revenue
          value 100000000 THB
          evidence verified
        }
        '''
        program = parse(source)
        self.assertIsInstance(program, Program)
        self.assertIsInstance(program.nodes[0], EntityNode)
        self.assertIsInstance(program.nodes[1], ObservationNode)
        self.assertEqual(program.nodes[0].entity_id, "company:example")
        self.assertEqual(program.nodes[1].observation_id, "obs:revenue:2026")
        self.assertEqual(program.nodes[1].fields["evidence"], "verified")

    def test_duplicate_ids_are_rejected(self):
        source = '''
        entity company "duplicate" { name "A" }
        entity company "duplicate" { name "B" }
        '''
        with self.assertRaises(OrbitCheckError):
            check_program(parse(source))

    def test_unknown_evidence_is_rejected(self):
        source = '''
        observation "obs:1" { evidence maybe }
        '''
        with self.assertRaises(OrbitCheckError):
            check_program(parse(source))


if __name__ == "__main__":
    unittest.main()
