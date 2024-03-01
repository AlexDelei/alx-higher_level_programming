#!/bin/bash
# sending a message from a server
curl -X PUT -Ls -d "You got me!"  0.0.0.0:5000/catch_me --output /dev/null"
