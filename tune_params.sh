#! /bin/bash
declare -a models=('SVR' 'RBF' 'DTR' 'KNNR' 'MLPCR')

pushd () {
    command pushd "$@" > /dev/null;
}
popd () {
    command popd "$@" > /dev/null;
}

PREFIX_PATH="../models/scripts"

containsElement () {
    local e match="$1"
    shift
    for e; do [[ "$e" == "$match" ]] && return 0; done
    return 1
}

function run {
    # Please do NOT code like this
    model=$1
    path="$PREFIX_PATH/$model";
    irace --deterministic 1 -p $path/parameters.txt --exec-dir $path/ -l ../../param_results/$model.Rdata;

    # Output results in a csv
    pushd ../models/param_results
    program='library("irace"); load("'$model'.Rdata"); write.csv(getFinalElites(iraceResults, n = 0), file = "'$model'.csv"); q();'
    echo $program | R --no-save > /dev/null;
    popd;
}


# MAIN ----------------------------------------------------------------------

cd tuning/

if containsElement "$1" "${models[@]}"; then
   model=$1;
   run $model;
elif [ "$1" = "ALL" ]; then
    for model in "${models[@]}"; do
        run $model;
    done
elif [ "$1" = "CLEAR" ]; then
    for model in "${models[@]}"; do
        path="$PREFIX_PATH/$model"
        rm $path/*.stdout $path/*.stderr;
    done
elif [ "$1" = "CLEARALL" ]; then
    for model in "${models[@]}"; do
        path="$PREFIX_PATH/$model"
        rm $path/*.stdout $path/*.stderr
    done
    rm ../models/param_results/*.csv ../models/param_results/*.Rdata
else
    # If the number of arguments is 0 or the argument is incorrect, show help message
    echo -e "${bold}Please, specify a valid model as fisrt argument:";
    echo -e "Models:"
    for model in "${models[@]}"; do
        echo -e "- $model";
    done
    echo -e "";
    echo -e "${bold}Or specify a valid command as fisrt argument:";
    echo -e "Commands:";
    echo -e "- ALL -- Run all models sequentially";
    echo -e "- CLEAR -- Delete all *.stderr and *.stdout files";
    echo -e "- CLEARALL -- As CLEAR but also deletes all results files (*.Rdata and *.csv)";

    # Exit with error
    exit 1;
fi

# Trap ctrl-c and other exit signals and delete all temporary files
trap TrapError 1 2 3 15;
function TrapError() {
    echo "Saliendo...";
    exit;
}
