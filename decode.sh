files=`find /home/maomao/LOG-analysis/Error_logs/202111 -name "*.gz"`
#echo $files
set -x
for path in $files
do
	echo $path
	filename=$(basename $path)
	filename=$(echo $filename | cut -d . -f1)
	#echo $filename
	dir=/home/maomao/LOG-analysis/Error_logs/$filename
	echo $dir
	echo $path
	mkdir $dir
	tar xvf $path -C $dir
done

