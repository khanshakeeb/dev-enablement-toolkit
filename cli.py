import click
from modules.k8s_health import check_health

@click.group()
def cli():
    """Dev Enablement Toolkit - helping engineers ship faster."""
    pass

@cli.command()
@click.option("--namespace", "-n", default="default", help="Kubernetes namespace")
def health(namespace):
    """Check Kubernetes deployment health."""
    check_health(namespace)

@cli.command()
def trigger():
    """Trigger a GitHub Actions workflow."""
    click.echo("Triggering workflow...")

@cli.command()
def report():
    """Generate deployment report."""
    click.echo("Generating report...")

if __name__ == "__main__":
    cli()