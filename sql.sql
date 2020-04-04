SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";
CREATE DATABASE IF NOT EXISTS `DBgethref` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `DBgethref`;
CREATE TABLE `0xfindurl` (
  `id` int(11) NOT NULL,
  `uid` text NOT NULL,
  `target` text NOT NULL,
  `ip` text NOT NULL,
  `links` text CHARACTER SET utf8,
  `header` text CHARACTER SET utf8,
  `whoisip` text NOT NULL,
  `sublinks` text CHARACTER SET utf8,
  `created` text CHARACTER SET utf8
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
ALTER TABLE `0xfindurl`
  ADD PRIMARY KEY (`id`);
ALTER TABLE `0xfindurl`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=0;
