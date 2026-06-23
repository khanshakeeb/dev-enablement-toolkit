# pyrefly: ignore [missing-import]
import click
from modules.k8s_health import check_health
from modules.github_actions import trigger_workflow


@click.group()
def cli():
    """Dev Enablement Toolkit - helping engineers ship faster."""
    pass


@cli.command()
@click.option("--namespace", "-n", default="default",
              help="Kubernetes namespace")
def health(namespace):
    """Check Kubernetes deployment health."""
    check_health(namespace)


@cli.command()
@click.option("--workflow", "-w", default="ci.yml",
              help="Workflow file to trigger")
def trigger(workflow):
    """Trigger a GitHub Actions workflow."""
    trigger_workflow(workflow)


@cli.command()
def report():
    """Generate deployment report."""
    click.echo("Generating report...")


if __name__ == "__main__":
    cli()
