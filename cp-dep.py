#!/usr/bin/python

import graphviz

g = graphviz.Digraph('G', filename='control-plane.gv', engine='sfdp', format='png',
                     node_attr={'color': 'lightblue2', 'style': 'filled'})

g.edge('kube-api', 'etcd')
g.edge('openshift-api', 'etcd')
g.edge('kube-apiserver-operator', 'kube-api')
g.edge('etcd-operator', 'kube-api')
g.edge('kube-controller-manager', 'kube-api')
g.edge('kube-controller-manager-operator', 'kube-api')
g.edge('openshift-kube-scheduler', 'kube-api')
g.edge('openshift-kube-scheduler-operator', 'kube-api')
g.edge('openshift-apiserver-operator', 'kube-api')
g.edge('openshift-controller-manager', 'kube-api')
g.edge('openshift-controller-manager-operator', 'kube-api')
g.edge('openshift-oauth-apiserver', 'openshift-api')
g.edge('openshift-authentication', 'openshift-api')
g.edge('openshift-authentication-operator', 'openshift-api')


g.view()
