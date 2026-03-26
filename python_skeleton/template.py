from collections.abc import Iterator
from pathlib import Path
import re

from jinja2 import Environment, FileSystemLoader

from .context import Context


class TemplateRenderer:
    """Renders templates."""

    _DOTFILE_RE = re.compile(r"dot-(.*)")

    def __init__(self, templates_dir: Path, project_dir: Path, package_name: str) -> None:
        self.templates_dir = templates_dir
        self.project_dir = project_dir
        self.package_name = package_name
        self.env = self._make_env(templates_dir)

    def render(self, template_path: Path, context: Context) -> Path:
        """Render a template returning the generated file path."""
        target = self._get_target_path(template_path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(self._render(template_path, context))
        return target

    def _make_env(self, templates_dir: Path) -> Environment:
        env = Environment(loader=FileSystemLoader(templates_dir))

        def gh_var(s: str) -> str:
            return f"${{{{ {s} }}}}"

        env.globals["gh_var"] = gh_var  # type: ignore

        return env

    def _get_target_path(self, template_path: Path) -> Path:
        """Return the name of the target file/directory from the source one."""

        def rename(name: str) -> str:
            name = self._DOTFILE_RE.sub(r".\1", name)
            name = name.replace("skeleton", self.package_name)
            return name

        return self.project_dir / Path(*(rename(part) for part in template_path.parts))

    def _render(self, template_path: Path, context: Context) -> str:
        """Render the template with the specified context."""
        template = self.env.get_template(str(template_path))
        text = template.render(context)
        # Jinja strips ending newline from templates
        if not text.endswith("\n"):
            text += "\n"
        return text 
