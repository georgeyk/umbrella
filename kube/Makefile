.PHONY: clean alias stop ex1 ex2 ex3 ex4 ex5 ex6 ex7 ex8

KCMD := minikube kubectl --

clean:
	minikube delete --all

stop:
	minikube stop

# pods
ex1:
	# run and wait
	${KCMD} apply -f 100/nginx.yaml
	# after creation
	${KCMD} port-forward nginx 3000:80
	# see the welcome page on localhost:3000

	# logs
	# ${KCMD} logs --follow nginx

	# del
	# ${KCMD} delete pod nginx

# deployments
ex2:
	${KCMD} apply -f 200/deployment.yaml
	# things to check
	# get deployments / get pods (inspect output)
	# kill a pod and see the outputs again
	# scale up apply -f 200/scale-to-5.yaml
	# scale down (apply deployment.yaml)
	#
	# dep-surge-and-unavailable.yaml -> example of rollout strategy
	#
	# bad-release.yaml -> example of a buggy release
	# - check outputs from get deployments, get pods and pod describe
	# - kubectl describe pod <pod>
	# - kubectl rollout undo deployment appname
	#
	# healthy-check.yaml -> example of livenessProbe

# services
ex3:
	${KCMD} apply -f 300/service.yaml
	# ${KCMD} apply -f 300/deployment.yaml
	# things to check:
	# kubectl get service
	# open localhost:30001, see the welcome page from nginx (no port-forward)
	# TODO: multi-service examples (clusterip, loadbalancer, dns)

# configs
ex4:
	${KCMD} apply -f 400/deployment.yaml
	# see the environment variables inside pod:
	# kubectl exec -it <pod> -- env
	#
	# config-file.yaml -> Example of configmap as files (mounted on volume)
	# kubectl exec -it <pod> -- bash (then inspect /config/THIS_FILE)
	#
	# secrets.yaml -> example of using secrets
	# Note that secrets are stored encrypted in the master node and distributed
	# to worker nodes (encoded in base64 without stringData).

# jobs
ex5:
	${KCMD} apply -f 500/jobs.yaml
	# thins to check:
	# kubectl get jobs / get pods
	# kubectl logs <pod>
	#
	# cron.yaml -> example of scheduled job
	# "kubectl get pods --watch" helps to see the pods

# namespaces
ex6:
	${KCMD} apply -f 600/namespace.yaml
	# things to check:
	# kubectl get namespaces
	# kubectl get pods -n <namespace>
	# kubectl get pods  --all-namespaces
	#
	# pods.yaml -> pod in namespace

# ingress
ex7:
	# for minikube: "minikube addons enable ingress"
	${KCMD} apply -f 700/nginx.yaml
	${KCMD} apply -f 700/caddy.yaml
	${KCMD} apply -f 700/ingress.yaml
	# things to check
	# - kubectl get pods, get svc
	# - kubectl get ingress

# helm/dash
800:
	# Install dash
	# helm repo add kubernetes-dashboard https://kubernetes.github.io/dashboard/
	# helm upgrade --install kubernetes-dashboard kubernetes-dashboard/kubernetes-dashboard --create-namespace --namespace kubernetes-dashboard

	# Create service account
	${KCMD} apply -f 700/service-account.yaml
	# ${KCMD} create token admin


# INFO:
# see: ~/.kube/config
# things to note: switching config (ie, local x prod)
# kubectl config current-context
# kubectl config use-context <>
# kubectl get pods --context <>

# TODO:
# resource management
# - requirements for pods: needs X amount of cpu/mem, etc
# - limiting pods: limit resource utilization
# - limit range: to define constraints on containers
#
# ingress
# debug ....
#
# dash
# debug ....
