#!/bin/bash

SCRIPT_DIR=$(dirname "$0")
ROOT_DIR=$(git rev-parse --show-toplevel)
TAG=$(git rev-parse --short=6 HEAD)

docker build -t samwelborn/scope-operator:$TAG -f $SCRIPT_DIR/Containerfile $ROOT_DIR
