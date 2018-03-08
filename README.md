# tmw contentful example
Sample Python - Openshift hosted demo to pull and render data from contentful

## Implementation Notes


```
oc new-app https://github.com/OpenShiftDemos/os-sample-python.git
```

1) Create python 2.7 Openshift project
2) Point to this github build
3) It will fail, that's ok
4) Go to Build -> environment ->  and add proxy settings (https_proxy and http_proxy)
5) start new build - takes about 3-5 minutes
