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
    py2=python
elif [ "${context}" == "Mac" ]; then
    thisDirPath=$(cd "$(dirname "$0")"; pwd)
    # using HomeBrew install of Py2, rather than stock...
    py2=python2
else
    # this will work as well as not having any of this...
    thisDirPath=.
    py2=python
fi
cd "${thisDirPath}"

${py2} -m pip install . 
echo Press enter to continue; read dummy;
