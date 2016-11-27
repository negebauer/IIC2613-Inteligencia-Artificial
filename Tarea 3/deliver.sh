set_vars() {
  dir=tarea2_
  list=list
}

temp_clean() {
  echo 'Cleaning'
  rm -rf $dir
  rm -rf $list
}

temp_create() {
  echo 'Creating temp stuff'
  mkdir $dir
  touch $list
}

files_load() {
  echo 'Prepping file list'
  ls | grep '.py' | grep -v '.pyc' >> $list
  ls | grep 's3' | grep -v '.py' >> $list
  # ls | grep '.zip' >> $list
  ls | grep '.txt' >> $list
  ls | grep '.sh' >> $list
  echo 'logs/' >> $list
  echo "File list"
  for file in $(cat list); do echo -e "\t$file"; done
}

files_copy() {
  echo 'Copying'
  for file in $(cat list); do
    echo -e "\tCopying: $file"
    if [ -d $file ]; then
      ditto $file "$dir/$file"
    elif [ -f $PASSED ]; then
      ditto $file $dir
    fi
  done
}

set_vars
rm -rf "$dir.zip"
temp_clean
temp_create
files_load
files_copy
zip -r $dir $dir
temp_clean
echo "Zip ready $dir.zip"
