#!/bin/bash
# Passing a json format request to a POST request
curl -X POST -H "Content-type: application/json" -d "@$2" -s "$1"
