from pathlib import Path
from shutil import which
import subprocess

from pre_commit.commands.autoupdate import autoupdate
from structlog import BoundLogger


def update_project_files(project_dir: Path, logger: BoundLogger) -> None:
    autoupdate(
        str(project_dir / ".pre-commit-config.yaml"),
        tags_only=True,
        freeze=True,
    )
    if which("pinact"):
        workflows_dir = project_dir / ".github" / "workflows"
        paths = (str(p) for p in workflows_dir.glob("*.yaml"))
        cmd = ["pinact", "run", "--update", "--", *paths]
        subprocess.run(cmd, check=True, capture_output=True)
    else:
        logger.info("pinact not found, skipping actions update")
