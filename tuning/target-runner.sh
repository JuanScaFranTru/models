#!/bin/bash
###############################################################################
# This script is the command that is executed every run.
# Check the examples in examples/
#
# This script is run in the execution directory (execDir, --exec-dir).
#
# PARAMETERS:
# $1 is the candidate configuration number
# $2 is the instance ID
# $3 is the seed
# $4 is the instance name
# The rest ($* after `shift 4') are parameters to the run
#
# RETURN VALUE:
# This script should print one numerical value: the cost that must be minimized.
# Exit with 0 if no error, with 1 in case of error
###############################################################################
EXE="script.py"
PYTHON="python"
FIXED_PARAMS=""

CONFIG_ID=$1
INSTANCE_ID=$2
SEED=$3
INSTANCE=$4
shift 4 || exit 1
CONFIG_PARAMS=$*

STDOUT=c${CONFIG_ID}-${INSTANCE_ID}.stdout
STDERR=c${CONFIG_ID}-${INSTANCE_ID}.stderr

if [ ! -s "${EXE}" ]; then
    error "${EXE}: not found (pwd: $(pwd))"
fi

# If the program just prints a number, we can use 'exec' to avoid
# creating another process, but there can be no other commands after exec.
#exec $EXE ${FIXED_PARAMS} -i $INSTANCE ${CONFIG_PARAMS}
# exit 1
#
# Otherwise, save the output to a file, and parse the result from it.
# (If you wish to ignore segmentation faults you can use '{}' around
# the command.)
$PYTHON $EXE -i $INSTANCE ${CONFIG_PARAMS} 1> ${STDOUT} 2> ${STDERR}

error() {
    echo "`TZ=UTC date`: error: $@"
    exit 1
}

# This is an example of reading a number from the output.
# It assumes that the objective value is the first number in
# the first column of the last line of the output.
if [ -s "${STDOUT}" ]; then
    COST=$(tail -n 1 ${STDOUT} | grep -e '^[[:space:]]*[+-]\?[0-9]' | cut -f1)
    echo "$COST"
    rm -f "${STDOUT}" "${STDERR}"
    exit 0
else
    error "${STDOUT}: No such file or directory"
fi