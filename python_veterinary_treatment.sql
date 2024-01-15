 Server: localhost -  Database: python_veterinary_treatment
-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Feb 15, 2023 at 04:43 PM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";

--
-- Database: `python_veterinary_treatment`
--

-- --------------------------------------------------------

--
-- Table structure for table `patient_appointment_details`
--

CREATE TABLE `patient_appointment_details` (
  `id` int(100) NOT NULL,
  `full_name` varchar(100) NOT NULL,
  `email_id` varchar(100) NOT NULL,
  `phone_num` int(100) NOT NULL,
  `pet_name` varchar(100) NOT NULL,
  `species` varchar(100) NOT NULL,
  `reason` varchar(100) NOT NULL,
  `date` varchar(100) NOT NULL,
  `time` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `report` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `patient_appointment_details`
--

INSERT INTO `patient_appointment_details` (`id`, `full_name`, `email_id`, `phone_num`, `pet_name`, `species`, `reason`, `date`, `time`, `status`, `report`) VALUES
(1, 'NARAIN KARTHIK J', 'Narainjkans@gmail.com', 2147483647, 'Luna', 'Dog', 'New Clinet', '2023-02-16', '02:59', '0', '0'),
(2, 'NARAIN KARTHIK J', 'Narainjkans@gmail.com', 875433830, 'Luna', 'Bird', 'New Clinet', '2023-02-23', '16:53', '0', '0'),
(3, 'NARAIN KARTHIK J', 'Narainjkans@gmail.com', 2147483647, 'Luna', 'Dog', 'exam', '2023-03-02', '16:57', '0', '0'),
(4, 'NARAIN KARTHIK J', 'Narainjkans@gmail.com', 2147483647, 'Luna', 'Dog', 'exam', '2023-02-24', '22:52', '0', '0');

-- --------------------------------------------------------

--
-- Table structure for table `patient_details`
--

CREATE TABLE `patient_details` (
  `id` int(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `contact` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `report` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `patient_details`
--

INSERT INTO `patient_details` (`id`, `name`, `contact`, `email`, `address`, `username`, `password`, `status`, `report`) VALUES
(1, 'NARAIN KARTHIK J', '8754338390', 'Narainjkans@gmail.com', '13-1 VOC NAGAR 1st STREET KOOTHAPAR ROAD THIRUVERMBUR', 'narain1010', 'Narain1010@#', '0', '0');

-- --------------------------------------------------------

--
-- Table structure for table `patient_profile`
--

CREATE TABLE `patient_profile` (
  `id` int(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `phone` varchar(100) NOT NULL,
  `age` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `report` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `patient_profile`
--

INSERT INTO `patient_profile` (`id`, `name`, `phone`, `age`, `email`, `address`, `status`, `report`) VALUES
(1, 'NARAIN KARTHIK J', '08754338390', '19', 'Narainjkans@gmail.com', '13-1 VOC NAGAR 1st STREET KOOTHAPAR ROAD THIRUVERMBUR', '0', '0'),
(2, 'NARAIN KARTHIK J', '08754338390', '19', 'Narainjkans@gmail.com', '13-1 VOC NAGAR 1st STREET KOOTHAPAR ROAD THIRUVERMBUR', '0', '0');

