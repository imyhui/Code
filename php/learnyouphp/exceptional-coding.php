<?php
$filePaths = $argv;
array_shift($filePaths);

foreach($filePaths as $filePath) {
    try{
        echo (new SplFileObject($filePath))->getBasename(). "\n";
    } catch (RuntimeException $e) {
        echo "Unable to open file at path '" .$filePath. "'\n";
    }
}