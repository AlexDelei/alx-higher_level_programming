#!/bin/bash
# sending a get request to the url and displays the response body
curl -s -o /dev/null -w "%{http_code}" "$1"
