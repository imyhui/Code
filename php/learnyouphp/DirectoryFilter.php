<?php

class DirectoryFilter
{
    public function filter($filepath,$filetype)
    {
        $res = "";
        foreach (new DirectoryIterator($filepath) as $file)
        if($file->getExtension() == $filetype)
        {
            $res .= $file."\n";
        }
        return $res;
    }
}