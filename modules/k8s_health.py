from kubernetes import client, config
from rich.console import Console
from rich.table import Table

console = Console()

def check_health(namespace="default"):
    try:
        config.load_kube_config()
        v1 = client.CoreV1Api()
        
        pods = v1.list_namespaced_pod(namespace=namespace)
        
        table = Table(title=f"Cluster Health — Namespace: {namespace}")
        table.add_column("Pod", style="cyan")
        table.add_column("Status", style="green")
        table.add_column("Restarts", style="yellow")
        table.add_column("Issues", style="red")

        for pod in pods.items:
            name = pod.metadata.name
            phase = pod.status.phase

            restarts = 0
            issues = []

            for container in pod.status.container_statuses or []:
                restarts += container.restart_count
                
                if container.state.waiting:
                    reason = container.state.waiting.reason
                    if reason in ["CrashLoopBackOff", "ImagePullBackOff", "Error"]:
                        issues.append(reason)

            status_color = "green" if phase == "Running" else "red"
            issue_text = ", ".join(issues) if issues else "None"

            table.add_row(
                name,
                f"[{status_color}]{phase}[/{status_color}]",
                str(restarts),
                issue_text
            )

        console.print(table)

    except Exception as e:
        console.print(f"[red]Error connecting to cluster: {e}[/red]")