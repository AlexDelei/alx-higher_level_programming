#!/bin/bash
# sending a post request to passed URL and displays the body of response
curl -X POST -d "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD" -s "$1"
