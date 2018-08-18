<?php

$address = $argv[1];
$port = $argv[2];
$server = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
socket_bind($server,$address, $port);
socket_listen($server);
$client = socket_accept($server);

$data = (new DateTime())->format('Y-m-d H:i:s') . "\n";
socket_write($client, $data, strlen($data));
socket_close($server);
socket_close($client);