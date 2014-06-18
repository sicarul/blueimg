#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

. $DIR/bin/activate
python $DIR/gen_image.py $1 $2 $3 $4 $5 $6 $7 $8

