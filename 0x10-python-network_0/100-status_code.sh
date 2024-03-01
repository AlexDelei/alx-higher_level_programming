#!/bin/bash
# Sending a request to a server and display only the status code
curl -o /dev/null -w "%{http_code}" -s "$1"
