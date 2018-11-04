'''Template queryes.'''


CHECK_TABLE_EXISTS = r'''(SELECT if(count(`table_schema`)>0, 1, 0) as `exists`
FROM `information_schema`.`columns`
WHERE  `table_schema`=DATABASE()
AND `table_name`='entries' LIMIT 1)'''

CREATE_TABLE_ENTRIES = r'''CREATE TABLE `entries` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `link` varchar(200) NOT NULL,
  `image` longblob,
  `note` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8'''

GET_LIST = r'SELECT * FROM wishlist.entries;',
