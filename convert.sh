sed 's/,/ /g' data/bc.csv > data/bc.txt
sed '1d' data/bc.txt > data/breast-cancer.txt
rm data/bc.txt