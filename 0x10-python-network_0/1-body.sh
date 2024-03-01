#!/bin/bash
# sending a get request to the url and displays the response body
curl -s  -w "%{http_code}" "$1" | awk '/^200/{f=1} f{print}'
