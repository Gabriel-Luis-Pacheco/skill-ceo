"""The portable bundle has a matching directory name and unbroken local links."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from package_skill import MANIFEST, SKILL_NAME, package_skill, SOURCE_ROOT
from validate_skill import check_local_links


class PackageSkillTests(unittest.TestCase):
    def test_builds_valid_named_bundle(self):
        with tempfile.TemporaryDirectory() as tmp:
            package = package_skill(Path(tmp))
            self.assertEqual(SKILL_NAME, package.name)
            self.assertTrue((package / MANIFEST).exists())
            self.assertEqual([], check_local_links(package))
            self.assertTrue((package / "POLICY.md").exists())
            self.assertTrue((package / "references/35-decidir-e-executar-com-repertorio.md").exists())
            manifest = json.loads((package / MANIFEST).read_text())
            self.assertEqual(SKILL_NAME, manifest["skill"])
            with self.assertRaises(FileExistsError):
                package_skill(Path(tmp))
            self.assertEqual(package, package_skill(Path(tmp), replace=True))

    def test_cannot_overwrite_unrelated_folder(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / SKILL_NAME
            target.mkdir()
            (target / "personal-data.txt").write_text("do not delete")
            with self.assertRaises(ValueError):
                package_skill(Path(tmp), replace=True)
            self.assertTrue((target / "personal-data.txt").exists())


if __name__ == "__main__":
    unittest.main()
