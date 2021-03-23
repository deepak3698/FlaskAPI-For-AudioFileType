-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 23, 2021 at 09:01 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 7.4.15

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `audio`
--

-- --------------------------------------------------------

--
-- Table structure for table `audiobook`
--

CREATE TABLE `audiobook` (
  `ID` int(11) NOT NULL,
  `Title` varchar(100) NOT NULL,
  `Author` varchar(100) NOT NULL,
  `Narrator` varchar(100) NOT NULL,
  `Duration` int(11) NOT NULL,
  `Uploaded_time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `audiobook`
--

INSERT INTO `audiobook` (`ID`, `Title`, `Author`, `Narrator`, `Duration`, `Uploaded_time`) VALUES
(1, 'First audiobook', 'dt', 'hi ', 100, '2022-12-12 00:00:00'),
(2, 'First audiobook', 'dt', 'hi ', 100, '2022-12-12 00:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `podcast`
--

CREATE TABLE `podcast` (
  `ID` int(11) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Duration` int(11) NOT NULL,
  `Uploaded_time` datetime NOT NULL,
  `Host` varchar(100) NOT NULL,
  `Participants` varchar(500) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `podcast`
--

INSERT INTO `podcast` (`ID`, `Name`, `Duration`, `Uploaded_time`, `Host`, `Participants`) VALUES
(1, 'First podcast', 200, '2022-12-12 00:00:00', 'DTTTT', 'Ram Ravi'),
(2, 'podcast1', 200, '2021-03-10 00:00:00', 'dt', 'dd dd');

-- --------------------------------------------------------

--
-- Table structure for table `song`
--

CREATE TABLE `song` (
  `ID` int(11) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Duration` int(11) NOT NULL,
  `UploadedTime` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `song`
--

INSERT INTO `song` (`ID`, `Name`, `Duration`, `UploadedTime`) VALUES
(1, 'Soorma song', 100, '2022-12-12 00:00:00');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `audiobook`
--
ALTER TABLE `audiobook`
  ADD UNIQUE KEY `ID` (`ID`);

--
-- Indexes for table `podcast`
--
ALTER TABLE `podcast`
  ADD UNIQUE KEY `ID` (`ID`);

--
-- Indexes for table `song`
--
ALTER TABLE `song`
  ADD UNIQUE KEY `ID` (`ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
