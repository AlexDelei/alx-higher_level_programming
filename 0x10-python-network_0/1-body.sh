#!/bin/bash
# sending a get request to the url and displays the response body
curl -X GET "$1" -s -w "%{http_code}" | awk '/^200$/{getline;print}'
