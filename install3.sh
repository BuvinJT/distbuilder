case "$(uname -s)" in
    Linux*)     context=Linux;;
    Darwin*)    context=Mac;;
    CYGWIN*)    context=Cygwin;;
    MINGW*)     context=MinGw;;
    *)          context=UNKNOWN;;
esac

if [ "${context}" == "Linux" ]; then
    thisScriptPath=`realpath $0`
    thisDirPath=`dirname ${thisScriptPath}`
elif [ "${context}" == "Mac" ]; then
    thisDirPath=$(cd "$(dirname "$0")"; pwd)
else
    # this will work as well as not having any of this...
    thisDirPath=.
fi
cd "${thisDirPath}"

python3 -m pip install .
echo Press enter to continue; read dummy;
