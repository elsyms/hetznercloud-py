SERVER_STATUS_RUNNING = "running"
SERVER_STATUS_INITIALIZING = "initializing"
SERVER_STATUS_STARTING = "starting"
SERVER_STATUS_STOPPING = "stopping"
SERVER_STATUS_OFF = "off"
SERVER_STATUS_DELETING = "deleting"
SERVER_STATUS_MIGRATING = "migrating"
SERVER_STATUS_REBUILDING = "rebuilding"
SERVER_STATUS_UNKNOWN = "unknown"

ACTION_STATUS_SUCCESS = "success"
ACTION_STATUS_RUNNING = "running"
ACTION_STATUS_ERROR = "error"

RESCUE_TYPE_FREEBSD = "freebsd64"
RESCUE_TYPE_LINUX = "linux64"
RESCUE_TYPE_LINUX32 = "linux32"

SERVER_TYPE_1CPU_2GB = "cx11"
SERVER_TYPE_1CPU_2GB_CEPH = "cx11-ceph"
SERVER_TYPE_2CPU_4GB = "cx21"
SERVER_TYPE_2CPU_4GB_CEPH = "cx21-ceph"
SERVER_TYPE_2CPU_8GB = "cx31"
SERVER_TYPE_2CPU_8GB_CEPH = "cx31-ceph"
SERVER_TYPE_4CPU_16GB = "cx41"
SERVER_TYPE_4CPU_16GB_CEPH = "cx41-ceph"
SERVER_TYPE_8CPU_32GB = "cx41"
SERVER_TYPE_8CPU_32GB_CEPH = "cx41-ceph"

IMAGE_UBUNTU_1604 = "ubuntu-16.04"
IMAGE_DEBIAN_9 = "debian-9"
IMAGE_CENTOS_7 = "centos-7"
IMAGE_FEDORA_27 = "fedora-27"

IMAGE_TYPE_BACKUP = "backup"
IMAGE_TYPE_SNAPSHOT = "snapshot"

DATACENTER_FALKENSTEIN_1 = "fsn1-dc8"
DATACENTER_NUREMBERG_1 = "nbg1-dc3"

BACKUP_WINDOW_10PM_2AM = "22-02"
BACKUP_WINDOW_2AM_6AM = "02-06"
BACKUP_WINDOW_6AM_10AM = "06-10"
BACKUP_WINDOW_10AM_2PM = "10-14"
BACKUP_WINDOW_2PM_6PM = "14-18"
BACKUP_WINDOW_6PM_10PM = "18-22"

SORT_BY_ID_ASC = "id:asc"
SORT_BY_ID_DESC = "id:desc"
SORT_BY_NAME_ASC = "name:asc"
SORT_BY_NAME_DESC = "name:desc"
SORT_BY_CREATED_ASC = "created:asc"
SORT_BY_CREATED_DESC = "created:desc"

FLOATING_IP_TYPE_IPv4 = "ipv4"
FLOATING_IP_TYPE_IPv6 = "ipv6"