from pathlib import Path
import subprocess


def init_git_repo(target_dir: Path) -> None:
    process = subprocess.run(
        ["git", "-C", str(target_dir), "init"],
        capture_output=True,
    )
    process.check_returncode()
