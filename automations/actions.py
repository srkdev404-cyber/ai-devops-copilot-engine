import subprocess

def restart_ecs(service):
    subprocess.run(["aws", "ecs", "update-service", "--force-new-deployment"])

def rerun_pipeline():
    print("Triggering pipeline...")
