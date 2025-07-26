# AWX Installation on Ubuntu machine

Commands:

## Step 1: Install Docker

[https://docs.docker.com/engine/instal...](https://docs.docker.com/engine/install/ubuntu/)

## Step 2: Install Minikube & start

[https://minikube.sigs.k8s.io/docs/start/](https://minikube.sigs.k8s.io/docs/start/?arch=%2Flinux%2Fx86-64%2Fstable%2Fbinary+download)

```javascript
minikube start --cpus=4 --memory=6g --addons=ingress
```

```javascript
set the alias:- alias kubectl="minikube kubectl --"
```

## Step 3: Install AWX Operator

#### Create the File: *kustomization.yaml*

```javascript
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  - github.com/ansible/awx-operator/config/default?ref=2.19.1
images:
  - name: quay.io/ansible/awx-operator
    newTag: 2.19.1
namespace: awx
```

#### Once you have created the file, run the Command: 

```javascript
kubectl apply -k .
```

#### Set the default namespace:- 

```javascript
kubectl config set-context --current --namespace=awx
```

## Step4: Install awx

###### file: *awx-server.yaml*

```javascript
---
apiVersion: awx.ansible.com/v1beta1
kind: AWX
metadata:
  name: awx-server
spec:
  service_type: nodeport`
```
##### update *kustomization.yaml* resources

```javascript
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  - github.com/ansible/awx-operator/config/default?ref=2.19.1
  - awx-server.yaml
images:
  - name: quay.io/ansible/awx-operator
    newTag: 2.19.1
namespace: awx
```

###### Once the File *kustomization.yaml* is updated the run the below Command: 

```javascript
kubectl apply -k .
```

If you want to Check installation logs then you can run the below command:   

```javascript
`kubectl logs -f deployments/awx-operator-controller-manager -c awx-manager -n awx`
```

## Step5: Enable external access

```javascript
kubectl port-forward service/awx-server-service -n awx  --address 0.0.0.0 30080:80
```
