import subprocess

cmd = "kubectl apply -f db-persistent-volume.yaml"
subprocess.run(cmd, shell=True)

cmd = "kubectl apply -f db-volume-claim.yaml"
subprocess.run(cmd, shell=True)

cmd = "kubectl apply -f db-configmap.yaml"
subprocess.run(cmd, shell=True)

cmd = "kubectl apply -f db-deployment.yaml"
subprocess.run(cmd, shell=True)

cmd = "kubectl apply -f db-service.yaml"
subprocess.run(cmd, shell=True)
