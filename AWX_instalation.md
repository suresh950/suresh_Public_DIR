Commands:
Step1: Install Docker
#############################################################
https://docs.docker.com/engine/instal...
https://docs.docker.com/engine/instal...


Step2: Install Minikube & start
#############################################################
https://minikube.sigs.k8s.io/docs/start/

minikube start --cpus=4 --memory=6g --addons=ingress
set the alias:- alias kubectl="minikube kubectl --"

Step3: Install AWX Operator
#############################################################
-------------------------------------------------------------
file: kustomization.yaml
~~~~~~~~~~~~~~~~~~~~~~~~~~~
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
github.com/ansible/awx-operator/config/default?ref=2.0.1
images:
name: quay.io/ansible/awx-operator
    newTag: 2.1.0
namespace: awx
-------------------------------------------------------------
Command: kubectl apply -k .
-------------------------------------------------------------
set the default namespace:- kubectl config set-context --current --namespace=awx

Step4: Install awx
#############################################################
update kustomization.yaml resources

file: awx-server.yaml
~~~~~~~~~~~~~~~~~~~~~~~~~~~
`---
apiVersion: awx.ansible.com/v1beta1
kind: AWX
metadata:
  name: awx-server
spec:
  service_type: nodeport`
-------------------------------------------------------------
Command: `kubectl apply -k .`
-------------------------------------------------------------
check installation logs:   `kubectl logs -f deployments/awx-operator-controller-manager -c awx-manager -n awx`

Step5: Enable external access
############################################################
`kubectl port-forward service/awx-server-service -n awx  --address 0.0.0.0 30080:80`
