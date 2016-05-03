#!/bin/bash

echo "Where should the counter start?";
read countstart;

echo "What is the original filename?";
read originalfile;

echo "What is the file extension? (Don't enter a period)";
read fileext;

echo "What would you like the new filename to be?";
read newname;

echo "Changing $originalfile.$fileext to $newname.$fileext";

j=$countstart;
for i in $originalfile.$fileext;
do mv "$i" $newname"_""$j".$fileext;
let j++;
done
