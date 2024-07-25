#!/bin/bash

interfaces=$(ip -o link show | awk -F': ' '{print $2}')
echo "$interfaces"

