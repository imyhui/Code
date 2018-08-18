<?php
array_shift($argv);
array_map(function ($fileDir) {
    $fileObj = new SplFileObject($fileDir);
    echo $fileObj->getBasename() . "\n";
},array_filter($argv,function($file){
    return file_exists($file);
}));