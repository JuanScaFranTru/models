#! /bin/bash
PACKAGE_NAME=models;
ENV=environment.yml
ENV_NAME=$(head -n 1 $ENV | sed 's|name: ||')

function install_all {
    # Install environment and package
    conda env create -f $ENV;
    source activate $ENV_NAME;
    python setup.py install;
}

function uninstall_all {
    source deactivate $ENV_NAME;
    python setup.py install --record uninstall_files.txt > /dev/null;
    cat uninstall_files.txt | xargs rm -rf;
    rm -fr models.egg-info build dist uninstall_files.txt;
    conda remove --name $ENV_NAME --all;
}

# MAIN ----------------------------------------------------------------------

if [ "$1" = "uninstall" ]; then
    uninstall_all;

elif [ "$1" = "install" ]; then
    install_all;

else
    echo -e "Missing argument:";
    echo -e "Usage:"
    echo -e "./installer.sh install|uninstall"
fi

# Trap ctrl-c and other exit signals
trap TrapError 1 2 3 15;
function TrapError() {
    echo "Something went wrong...";
    exit 1;
}
