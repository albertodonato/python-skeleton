from collections.abc import Iterator
import logging
from pathlib import Path

import click
import structlog

from .actions import init_git_repo
from .context import Context, ContextError, get_context
from .template import TemplateRenderer


@click.command()
@click.option(
    "--debug", is_flag=True, default=False, help="Enable debug messages"
)
@click.option(
    "--skip-git-init",
    is_flag=True,
    default=False,
    help="Skip initializing git repository",
)
@click.option(
    "--templates",
    type=click.Path(
        exists=True, file_okay=False, dir_okay=True, path_type=Path
    ),
    default=Path("templates"),
    help="Directory containing project templates",
)
@click.option(
    "--project-details",
    type=click.Path(exists=True, path_type=Path),
    help=(
        "Project details to generate the tree. "
        "If not provided, the project directory is assumed to exist and "
        "details will be parsed from the existing project"
    ),
)
@click.argument("project-dir", type=click.Path(path_type=Path))
def main(
    debug: bool,
    skip_git_init: bool,
    templates: Path,
    project_details: Path | None,
    project_dir: Path,
) -> None:
    """Build tree structure for a Python project."""
    logger = _get_logger(debug)

    if project_details:
        logger.info("loading project details", path=str(project_details))
    else:
        logger.info("gathering project_details", path=str(project_dir))
        if not project_dir.is_dir():
            raise click.ClickException(
                "Project directory not found and no details file provided"
            )

    try:
        context = get_context(project_dir, project_details)
    except ContextError as e:
        raise click.ClickException(str(e))

    if debug:
        logger.debug("template context", context=context.model_dump())

    _generate_project_tree(templates, project_dir, context, logger)

    if not skip_git_init and not (project_dir / ".git").exists():
        logger.info("initializing git repository", path=str(project_dir))
        init_git_repo(project_dir)


def _get_logger(debug: bool) -> structlog.BoundLogger:
    """Return the logger."""
    wrapper_class = structlog.make_filtering_bound_logger(
        logging.DEBUG if debug else logging.INFO
    )
    structlog.configure(wrapper_class=wrapper_class)
    return structlog.get_logger()


def _generate_project_tree(
    templates_dir: Path,
    project_dir: Path,
    context: Context,
    logger: structlog.BoundLogger,
) -> None:
    """Generate the project tree."""
    renderer = TemplateRenderer(
        templates_dir, project_dir, context.project.package
    )
    for template_path in _iter_paths(templates_dir, context):
        output_path = renderer.render(
            template_path.relative_to(templates_dir), context
        )
        logger.info(
            "rendered template",
            source=str(template_path),
            destination=str(output_path),
        )


def _iter_paths(base_path: Path, context: Context) -> Iterator[Path]:
    for path in base_path.rglob("*"):
        if path.is_dir():
            continue

        if not context.config.include_docs and (
            "docs" in path.parts or path.name == "dot-readthedocs.yaml"
        ):
            continue

        yield path
