CREATE DATABASE  IF NOT EXISTS `user_dashboard` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `user_dashboard`;
-- MySQL dump 10.13  Distrib 5.7.9, for osx10.9 (x86_64)
--
-- Host: 127.0.0.1    Database: user_dashboard
-- ------------------------------------------------------
-- Server version	5.5.42

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `message_id` int(11) NOT NULL,
  `contents` varchar(255) DEFAULT NULL,
  `user_id` varchar(255) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
INSERT INTO `comments` VALUES (4,3,'he is!','4','2016-06-22 00:32:21','2016-06-22 00:32:21'),(5,1,'I\'m great!','4','2016-06-22 00:32:41','2016-06-22 00:32:41'),(6,4,'commenting on my own message!','4','2016-06-22 00:40:05','2016-06-22 00:40:05'),(7,3,'I am!','9','2016-06-22 01:02:26','2016-06-22 01:02:26'),(8,4,'Second comment! ya!','9','2016-06-22 01:02:40','2016-06-22 01:02:40'),(9,1,'are you guys brothers?=','9','2016-06-22 01:21:13','2016-06-22 01:21:13'),(10,6,'wat up?','9','2016-06-22 01:25:56','2016-06-22 01:25:56'),(11,2,'I love you too!','5','2016-06-22 01:30:30','2016-06-22 01:30:30'),(12,5,'great meeting you!','5','2016-06-22 01:30:37','2016-06-22 01:30:37'),(13,3,'you are?','5','2016-06-22 01:31:19','2016-06-22 01:31:19'),(14,3,'He is a master legend!','10','2016-06-22 02:48:49','2016-06-22 02:48:49'),(15,10,'Definitely!\r\nsounds like a dream.','3','2016-06-22 02:50:22','2016-06-22 02:50:22'),(16,8,'he did!','5','2016-06-22 11:25:54','2016-06-22 11:25:54'),(17,4,'this comment!  boo yA!\r\n','5','2016-06-22 11:26:10','2016-06-22 11:26:10'),(18,6,'bhey!','5','2016-06-22 12:27:36','2016-06-22 12:27:36');
/*!40000 ALTER TABLE `comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `messages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `contents` varchar(255) DEFAULT NULL,
  `from_user_id` int(11) NOT NULL,
  `to_user_id` int(11) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
INSERT INTO `messages` VALUES (1,'Hey Eatay!\r\nHow are you?',3,4,'2016-06-22 00:06:34','2016-06-22 00:06:34'),(2,'Kendall!\r\nI love you.',3,5,'2016-06-22 00:07:20','2016-06-22 00:07:20'),(3,'Bruce Lee!\r\nYou\'re a kung fu legend!',3,9,'2016-06-22 00:08:01','2016-06-22 00:08:01'),(4,'Your first message!',4,3,'2016-06-22 00:21:53','2016-06-22 00:21:53'),(5,'It was nice to meet you!',4,5,'2016-06-22 00:22:18','2016-06-22 00:22:18'),(6,'Hey Bruce!',4,9,'2016-06-22 00:26:51','2016-06-22 00:26:51'),(7,'I\'m a kung fu man.  are you great?',9,4,'2016-06-22 01:07:58','2016-06-22 01:07:58'),(8,'did you make this website?',9,3,'2016-06-22 01:26:48','2016-06-22 01:26:48'),(9,'My first post!',10,10,'2016-06-22 02:15:50','2016-06-22 02:15:50'),(10,'Could you come work for apple?',10,3,'2016-06-22 02:19:54','2016-06-22 02:19:54'),(11,'what are you doing for dinner?',5,3,'2016-06-22 11:26:47','2016-06-22 11:26:47'),(12,'what up!',5,9,'2016-06-22 12:27:31','2016-06-22 12:27:31');
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(255) DEFAULT NULL,
  `firstname` varchar(255) DEFAULT NULL,
  `lastname` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `user_level` int(11) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (3,'shechtera80@gmail.com','Adam','Shechter','I am the admin!\r\nhahaha!',9,'$2b$12$FVUzGEEYC5sL3lU5DgnRbebw03CD6hJXvjGBRWN.KK/mvMl9SGrcq','2016-06-21 14:22:38','2016-06-21 18:05:21'),(4,'eatay@gmail.com','Eatay Ben','Shechter','I am the Admin\'s brother!',1,'$2b$12$xvVJspaf1mDkBrRK5EL.nOKhsmj1HSjNhOQQajEraTvVfnzTp60Na','2016-06-21 14:49:51','2016-06-21 18:33:42'),(5,'kendall@markham.com','Kendall','Markham','Kendall is amazing!',1,'$2b$12$NimCe3r1twWqx0.z2DKE8OPKnbqv8WtC6weaOubxyzq//1pzf7vq2','2016-06-21 15:59:49','2016-06-21 18:25:27'),(9,'bruce@lee.com','Bruce','Lee','Kung Fu Master!',9,'$2b$12$6MD2tWiVlJMbGtDCf56nfe7.TEs6nZEuPylaMVo/N1HQpv.Cwj7bW','2016-06-21 18:28:17','2016-06-21 18:33:48'),(10,'steve@jobs.com','Steve','Jobs',NULL,1,'$2b$12$aSm.OFZEVevoZw8e5qhMh.F.b.ev0mrHigWFsG7ZoX54VV3Q9yQHC','2016-06-22 02:15:29','2016-06-22 02:15:29');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-06-23 14:33:27
