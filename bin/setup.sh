# setup kali environment
#
# source this file from your ~/.bashrc
#
# relative to <kali>/bin/
OSS=$(cd "$(dirname "$BASH_SOURCE")/.."; pwd)
OSS_CYTHON=$(cd "$(dirname "$BASH_SOURCE")/../python"; pwd)
# OSS_CYTHON_LIB=$(cd "$(dirname "$BASH_SOURCE")/../lib"; pwd)

export OSS
export PYTHONPATH="$OSS_CYTHON:$PYTHONPATH"
# export PYTHONPATH="$OSS_CYTHON_LIB:$PYTHONPATH"
echo "notice: oss tools have been set up."
