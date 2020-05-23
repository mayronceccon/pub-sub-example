<?php

require_once dirname(__FILE__) . '/../vendor/autoload.php';

use RedisClient\RedisClient;

$redis = new RedisClient([
    'timeout' => 0,
]);

$redis->subscribe('topic_create_file', function($type, $channel, $message) {
    if ($type === 'message') {
        $jsonDecoded = json_decode($message, true);
        
        $csvFileName = './files/file_php.csv';
        $fp = fopen($csvFileName, 'w');
        foreach($jsonDecoded as $row){
            fputcsv($fp, $row);
        }
        fclose($fp);
        echo "File php CSV\n";
    }
    return true;
});
