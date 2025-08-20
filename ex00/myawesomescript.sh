if [ $# -ne 1 ]; then
    echo "usage:  ./myawesomescript.s link"
    exit 1
fi
OUTPUT=$(curl -s $1)
LINK=$(echo "$OUTPUT" | grep -o 'http[^"]*')
echo "$LINK"

