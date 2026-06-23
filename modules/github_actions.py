import requests
import time
import os
from dotenv import load_dotenv
from rich.console import Console

load_dotenv()

console = Console()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_OWNER = os.getenv("GITHUB_OWNER")
GITHUB_REPO = os.getenv("GITHUB_REPO")

HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}


def trigger_workflow(workflow_file="ci.yml"):
    """Trigger a GitHub Actions workflow and monitor its status."""

    # Step 1 — Trigger the workflow
    url = f"https://api.github.com/repos/{GITHUB_OWNER}/{GITHUB_REPO}/actions/workflows/{workflow_file}/dispatches"

    payload = {"ref": "master"}

    response = requests.post(url, headers=HEADERS, json=payload)

    if response.status_code == 204:
        console.print("[green]✅ Workflow triggered successfully![/green]")
    else:
        console.print(
            f"[red]❌ Failed to trigger workflow: {response.status_code} — {response.text}[/red]")
        return

    # Step 2 — Wait briefly then poll for status
    console.print("[yellow]⏳ Waiting for workflow to start...[/yellow]")
    time.sleep(5)

    runs_url = f"https://api.github.com/repos/{GITHUB_OWNER}/{GITHUB_REPO}/actions/runs"

    for attempt in range(10):
        runs_response = requests.get(runs_url, headers=HEADERS)
        runs = runs_response.json().get("workflow_runs", [])

        if runs:
            latest = runs[0]
            status = latest["status"]
            conclusion = latest["conclusion"]
            run_url = latest["html_url"]

            console.print(
                f"[cyan]Status:[/cyan] {status} | [cyan]Conclusion:[/cyan] {conclusion or 'in progress'}")

            if status == "completed":
                if conclusion == "success":
                    console.print(
                        "[green]✅ Workflow completed successfully![/green]")
                else:
                    console.print(
                        f"[red]❌ Workflow failed: {conclusion}[/red]")
                console.print(f"[blue]🔗 {run_url}[/blue]")
                return

        console.print(f"[yellow]Polling... attempt {attempt + 1}/10[/yellow]")
        time.sleep(10)

    console.print("[red]Timed out waiting for workflow to complete.[/red]")
