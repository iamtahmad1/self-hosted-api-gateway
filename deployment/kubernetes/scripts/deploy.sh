kubectl create configmap haproxy-config --from-file=../deployment/gateway/conf/haproxy.cfg -n haproxy
kubectl create configmap nginx-config --from-file=../deployment/gateway/conf/nginx.conf -n nginx