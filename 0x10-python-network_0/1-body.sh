#!/bin/bash
# sending a get request to the url and displays the response body
curl -s "$1" | awk 'NR==1 {status=$1} NR>1  {if(status==200) print}'
