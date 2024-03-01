#!/bin/bash
# This takes in a URL, sends the request to it and displays size
curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}'
