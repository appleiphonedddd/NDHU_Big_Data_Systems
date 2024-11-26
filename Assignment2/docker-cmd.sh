#!/bin/bash
set +e

message() {
    echo "Please run:" >&2
    echo "            $0 clear                  rancher clear" >&2
    echo "            $0 svlog                  rancher save log" >&2
    echo "            $0 loglv [options]        rancher log level info/debug/trace" >&2
    echo "            $0 push <tag>" >&2
}

do_unmount_and_remove() {
    awk -v path="$1" '$2 ~ ("^" path) { print $2 }' /proc/self/mounts | sort -r | xargs -r -t -n 1 sh -c 'umount "$0" && rm -rf "$0"'
}

rancher_content_clear() {
    do_unmount_and_remove '/run/k3s';
    do_unmount_and_remove '/var/lib/rancher/k3s';
    do_unmount_and_remove '/var/lib/kubelet/pods';
    do_unmount_and_remove '/run/netns/cni-';

    sleep 1
    # node certificate error
    rm -rf /etc/kubernetes/

    rm -rf /var/lib/cni/
    rm -rf /var/lib/calico/
    rm -rf /var/lib/etcd/
    rm -rf /var/lib/kubelet/
    rm -rf /var/lib/rancher/

    # Remove CNI namespaces
    ip netns show 2>/dev/null | grep cni- | xargs -r -t -n 1 ip netns delete

    # Delete network interface(s) that match 'master cni0'
    ip link show 2>/dev/null | grep 'master cni0' | while read ignore iface ignore; do
        iface=${iface%%@*}
        [ -z "$iface" ] || ip link delete $iface
    done

    # delete bridge interface
    ip link delete cni0
    ip link delete flannel.1

    # clear iptables
    iptables-save | grep -v KUBE- | grep -v CNI- | iptables-restore
}

rancher_clear() {
    echo "clearing rancher server data..."
    docker stop rancher #stop rancher first
    docker rm $(docker stop $(docker ps -a -q))   #remove all containers
    docker rm $(docker stop $(docker ps -a -q --filter="name=k8s_"))   #remove containers name with k8s_
    docker rm $(docker ps -a -f status=exited -q)   #remove containers name with status exit

    rancher_content_clear;
}

rancher_save_log() {
    docker logs rancher >& rancher.log
}

rancher_clear_log() {
    truncate -s 0 $(docker inspect --format='{{.LogPath}}' rancher)
}

rancher_set_log_level() {
    docker exec -it rancher loglevel --set $1   #info/debug/trace
}

<<COMMENT
MULTILINE COMMAND
COMMENT

case "$1" in
    clear)
        sleep 1
        rancher_clear;
        exit 0
        ;;
    svlog)
        sleep 1
        rancher_save_log;
        exit 0
        ;;
    loglv)
        if [ "$#" -ne 2 ]; then
            message;
            exit 1
        fi
        rancher_set_log_level $2;
        exit 0
        ;;
    *)
        message;
        exit 1
        ;;
esac
exit 0