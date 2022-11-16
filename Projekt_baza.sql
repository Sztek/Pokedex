CREATE DATABASE  IF NOT EXISTS `pokedex` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `pokedex`;
-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: pokedex
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `druzyna`
--

DROP TABLE IF EXISTS `druzyna`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `druzyna` (
  `Id_druzyny` int NOT NULL,
  `Nazwa` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Id_druzyny`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `druzyna`
--

LOCK TABLES `druzyna` WRITE;
/*!40000 ALTER TABLE `druzyna` DISABLE KEYS */;
INSERT INTO `druzyna` VALUES (1,'niebieska');
/*!40000 ALTER TABLE `druzyna` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pokedex_poki`
--

DROP TABLE IF EXISTS `pokedex_poki`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pokedex_poki` (
  `id` int NOT NULL,
  `nazwa` varchar(45) DEFAULT NULL,
  `typ` varchar(45) DEFAULT NULL,
  `atak` int DEFAULT '1',
  `defensywa` int DEFAULT '1',
  `wytrzymalosc` int DEFAULT '1',
  `szybkosc` int DEFAULT '1',
  PRIMARY KEY (`id`),
  UNIQUE KEY `idnew_table_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pokedex_poki`
--

LOCK TABLES `pokedex_poki` WRITE;
/*!40000 ALTER TABLE `pokedex_poki` DISABLE KEYS */;
INSERT INTO `pokedex_poki` VALUES (1,'fletch','latajacy',4,3,2,4),(2,'flu','latajacy',6,3,3,5),(3,'alterseal','woda',2,4,4,3),(4,'psyster','normalny',5,3,2,3),(5,'unick','normalny',3,3,5,5),(6,'don ','latajacy',4,5,2,3),(7,'ceno','normalny',7,4,6,4),(8,'goat','lod',5,6,6,4),(9,'twinpig','ogien',2,4,4,2),(10,'icy','lod',6,6,4,5),(11,'ant','ziemia',5,4,4,4),(12,'fant','latajacy',5,5,3,5),(13,'turtle','woda',3,5,5,3),(14,'fred','normalny',4,3,3,2),(15,'aisoul','legendarny',7,7,7,7),(16,'magoat','normalny',6,4,3,5),(17,'redouse','ogien',3,2,2,2),(18,'magitic','woda',3,3,2,2),(19,'leafy','ziemia',4,3,3,4),(20,'headfire','ogien',5,3,3,2),(21,'onetale','ziemia',4,3,2,4),(22,'penesum','normalny',3,3,3,2),(23,'zapuno','legendarny',7,7,7,7),(24,'dogro','ogien',3,4,4,3),(25,'hotdog','ogien',5,2,2,5),(26,'raster','normalny',2,3,3,2),(27,'phant','normalny',2,3,5,3),(28,'ele','ziemia',2,3,5,3),(29,'netoper','latajacy',3,2,3,6),(30,'PFC','ogien',5,2,4,3);
/*!40000 ALTER TABLE `pokedex_poki` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pokemony`
--

DROP TABLE IF EXISTS `pokemony`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pokemony` (
  `id` int NOT NULL,
  `nazwa` varchar(45) DEFAULT NULL,
  `iv` varchar(45) DEFAULT NULL,
  `wlasciciel` varchar(45) DEFAULT NULL,
  `zdrowie` varchar(45) DEFAULT NULL,
  `poziom` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pokemony`
--

LOCK TABLES `pokemony` WRITE;
/*!40000 ALTER TABLE `pokemony` DISABLE KEYS */;
INSERT INTO `pokemony` VALUES (1,'ele','30','gracz','3','2');
/*!40000 ALTER TABLE `pokemony` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trenerzy`
--

DROP TABLE IF EXISTS `trenerzy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trenerzy` (
  `id_gracza` int NOT NULL,
  `nazwa` varchar(45) DEFAULT NULL,
  `druzyna` varchar(45) DEFAULT NULL,
  `ubranie` varchar(45) DEFAULT NULL,
  `X` int DEFAULT '0',
  `Y` int DEFAULT '0',
  PRIMARY KEY (`id_gracza`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trenerzy`
--

LOCK TABLES `trenerzy` WRITE;
/*!40000 ALTER TABLE `trenerzy` DISABLE KEYS */;
INSERT INTO `trenerzy` VALUES (1,'gracz','niebieska','3',2,1);
/*!40000 ALTER TABLE `trenerzy` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-14 21:16:33
