import unittest
import re
from pathlib import Path


class TestAssets(unittest.TestCase):
    def test_local_src_files_exist(self):
        repo_root = Path(__file__).resolve().parents[1]
        html_path = repo_root / "index.html"
        html = html_path.read_text(encoding="utf-8")
        src_values = re.findall(r'src="([^"]+)"', html)
        self.assertTrue(src_values, "No src attributes found in index.html")

        for src in src_values:
            if src.startswith("http://") or src.startswith("https://"):
                continue
            asset_path = repo_root / src
            self.assertTrue(asset_path.exists(), f"Missing asset: {src}")


if __name__ == "__main__":
    unittest.main()
