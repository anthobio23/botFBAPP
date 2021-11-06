#!/usr/bin/bash

ls_folder_image=$(ls ../img_convert/image/)
$ls_folder_image |sort -R |tail -$N 
while read file; do
    $file
done

