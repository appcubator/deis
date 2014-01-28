#!/usr/bin/env python
## EXITS 1 IF DOCKER CONTAINER IS RUNNING, 0 IF NOT RUNNING.


import json
import sys


container_data = json.loads(sys.stdin.read())
if len(container_data) == 0:
    sys.exit(1)
if container_data[0]['State']['Running']:
    sys.exit(1)
else:
    sys.exit(0)
