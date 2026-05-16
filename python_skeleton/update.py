from pathlib import Path

from pre_commit.commands.autoupdate import autoupdate


def update_project_files(project_dir: Path) -> None:
    autoupdate(
        project_dir / ".pre-commit-config.yaml", tags_only=True, freeze=True
    )
