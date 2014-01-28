#!/usr/bin/env python
## EXITS 0 IF DOCKER CONTAINER IS RUNNING, 1 IF NOT RUNNING.


import json
import sys


container_data = json.loads(sys.stdin.read())
if container_data[0]['State']['Running']:
    sys.exit(0)
else:
    sys.exit(1)
