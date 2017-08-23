#! /bin/bash
declare -a models=('SVR' 'RBF')


# If the number of arguments is 0, show an error message and exit
if [ $# -eq 0 ]
then
    echo -e "${bold}Falta el argumento del modelo";
    echo -e "Modelos disponibles:"
    for model in "${models[@]}"; do
        echo -e "- $model"
    done
    echo -e "- ALL"

    # Exit with error
    exit 1;
fi


cd tuning/

if [ "$1" = "all" ]; then
    for model in "${models[@]}"; do
        path="../models/$model"
        irace -p $path/parameters.txt --exec-dir $path/ > $path/results.results;
    done
else
    model=$1
    path="../models/$model"
    irace -p $path/parameters.txt --exec-dir $path/ > $path/results.results;
fi

# Trap ctrl-c and other exit signals and delete all temporary files
trap TrapError 1 2 3 15;
function TrapError() {
    echo "Saliendo...";
    exit;
}
