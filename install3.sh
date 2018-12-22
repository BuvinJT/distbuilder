thisScriptPath=`realpath $0`
thisDirPath=`dirname ${thisScriptPath}`
cd "${thisDirPath}"

sudo python3 -m pip install .
echo Press enter to continue; read dummy;
