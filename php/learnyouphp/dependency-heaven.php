<?php

require_once __DIR__ . '/vendor/autoload.php';
use Stringy\Stringy as S;
$klein = new \Klein\Klein();
$klein->respond('POST', '/[:action]', function ($request, $response) {
    $data = $request->data;
    $stringy = S::create($data);
    switch ($request->action) {
        case "reverse":
            return $response->json(["result" => $stringy->reverse()->__toString()]);
        case "swapcase":
            return $response->json(["result" => $stringy->swapCase()->__toString()]);
        case "titleize":
            return $response->json(["result" => $stringy->titleize()->__toString()]);
    }
});
$klein->dispatch();