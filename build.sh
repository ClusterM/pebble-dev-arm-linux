#!/bin/bash

docker build -t clustermeerkat/pebble-dev-arm-linux:1.0 -t clustermeerkat/pebble-dev-arm-linux:latest "$@" .
