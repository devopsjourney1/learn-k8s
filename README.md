
# Minikube commands
```
minikube config set driver docker
minikube start // stop
minikube status
minikube dashboard --url
minikube service <applicaiton-service-name>
```

# Kubectl Configuration
```
cat ~/.kube/config  // kubectl config view
alias k='kubectl'
```

# Kubectl commands
```
kubectl get namespace
kubectl get deployment
kubectl get replicasetP
kubectl get configmap
kubectl get nodes
kubectl describe nodes
kubectl get events
minikube service mywebapp
```

# Cluster Management
```
kubectl cluster-info
kubectl get nodes
kubectl describe node minikube
kubectl cordon minikube
kubectl drain minikube --ignore-daemonsets=true --force
kubectl uncordon minikube
```

# Namespaces
```
kubectl get namespace
kubectl create namespace dev
kubectl create namespace test
kubectl delete namespace test
k create -f namespaces/namespace-prod.yaml
k describe namespace prod

# OPTIONAL
kubectl config set-context --current --namespace=<NAMESPACE NAME>
```

# Your Hello World Kubernetes Project
```
kubectl get get pods
kubectl get pods -n dev 

kubectl create deployment hello-node --image=k8s.gcr.io/echoserver:1.4
kubectl create deployment hello-node --image=k8s.gcr.io/echoserver:1.4 -n dev
kubectl get deployments --all-namespaces
kubectl get events -n dev
kubectl expose deployment hello-node --type=LoadBalancer --port=8080
kubectl get services
minikube service hello-node
//On cloud providers that support load balancers, an external IP address would be provisioned to access the Service. On minikube, the LoadBalancer type makes the Service accessible through the minikube service command.
```

# Create V1 of app
- pod creation

# Create V2 of app (load Balancer and scaling)
- Service creation
- will get warning because used appy but service didnt exist yet
- scale up to 5, apply, show off name

# Create V3 of app - config maps/rolling back
- show of how the container works
- add config map
- map to it in container
- apply, show off.
- mention that if you make a change, should create a new config map, and map to the new one

# Create v4 of app - resources
- talk about the resource config
- apply, describe


# Extra
k describe deployment mydeployment
### Logs
k logs -f -l app=mywebapp
### Rollouts
kubectl rollout 
k rollout restart deployment mydeployment









https://minikube.sigs.k8s.io/docs/handbook/pushing/
```
& minikube -p minikube docker-env --shell powershell | Invoke-Expression
```


```
k apply -f test.yml
```