for x in $(seq 1 1000)
do
    python occupy.py
done >results.txt
# fgrep "debug" occupy.py |wc -w

while IFS= read -r line
do
    echo "$line: "
    grep -c "$line" results.txt
done < "dict.txt" >stats.txt
