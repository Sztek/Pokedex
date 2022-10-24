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
-- Table structure for table `pokedex_poki`
--

DROP TABLE IF EXISTS `pokedex_poki`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pokedex_poki` (
  `id` int NOT NULL,
  `nazwa` varchar(45) DEFAULT NULL,
  `typ` varchar(45) DEFAULT NULL,
  `atak` varchar(45) DEFAULT NULL,
  `defensywa` varchar(45) DEFAULT NULL,
  `wytrzymalosc` varchar(45) DEFAULT NULL,
  `szybkosc` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idnew_table_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pokedex_poki`
--

LOCK TABLES `pokedex_poki` WRITE;
/*!40000 ALTER TABLE `pokedex_poki` DISABLE KEYS */;
INSERT INTO `pokedex_poki` VALUES (1,'hant',' ogień',NULL,NULL,NULL,NULL);
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
  PRIMARY KEY (`id_gracza`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trenerzy`
--

LOCK TABLES `trenerzy` WRITE;
/*!40000 ALTER TABLE `trenerzy` DISABLE KEYS */;
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

-- Dump completed on 2022-10-19 16:58:33
