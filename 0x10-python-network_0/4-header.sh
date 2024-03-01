#!/bin/bash
# sending a get url request to aurl and display the body of response
curl -H "X-School-User-Id: 98" -X GET "$1" -s
