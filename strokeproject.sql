-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Oct 06, 2023 at 11:08 AM
-- Server version: 8.0.31
-- PHP Version: 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `strokeproject`
--
CREATE DATABASE IF NOT EXISTS `strokeproject` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `strokeproject`;

-- --------------------------------------------------------

--
-- Table structure for table `ada_algo`
--

DROP TABLE IF EXISTS `ada_algo`;
CREATE TABLE IF NOT EXISTS `ada_algo` (
  `XG_ID` int NOT NULL AUTO_INCREMENT,
  `Accuracy` longtext NOT NULL,
  `Precession` longtext NOT NULL,
  `F1_Score` longtext NOT NULL,
  `Recall` longtext NOT NULL,
  `Name` longtext NOT NULL,
  PRIMARY KEY (`XG_ID`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `ada_algo`
--

INSERT INTO `ada_algo` (`XG_ID`, `Accuracy`, `Precession`, `F1_Score`, `Recall`, `Name`) VALUES
(1, '77.98', '78.27', '77.95', '78.04', 'ADA Boost Algorithm'),
(2, '77.98', '78.27', '77.95', '78.04', 'ADA Boost Algorithm'),
(3, '77.98', '78.27', '77.95', '78.04', 'ADA Boost Algorithm'),
(4, '77.98', '78.27', '77.95', '78.04', 'ADA Boost Algorithm');

-- --------------------------------------------------------

--
-- Table structure for table `anm_algo`
--

DROP TABLE IF EXISTS `anm_algo`;
CREATE TABLE IF NOT EXISTS `anm_algo` (
  `ANM_ID` int NOT NULL AUTO_INCREMENT,
  `Accuracy` longtext NOT NULL,
  `Precession` longtext NOT NULL,
  `F1_Score` longtext NOT NULL,
  `Recall` longtext NOT NULL,
  `Name` longtext NOT NULL,
  PRIMARY KEY (`ANM_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `ann_algo`
--

DROP TABLE IF EXISTS `ann_algo`;
CREATE TABLE IF NOT EXISTS `ann_algo` (
  `ANN_ID` int NOT NULL AUTO_INCREMENT,
  `Accuracy` longtext NOT NULL,
  `Precession` longtext NOT NULL,
  `F1_Score` longtext NOT NULL,
  `Recall` longtext NOT NULL,
  `Name` longtext NOT NULL,
  PRIMARY KEY (`ANN_ID`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `ann_algo`
--

INSERT INTO `ann_algo` (`ANN_ID`, `Accuracy`, `Precession`, `F1_Score`, `Recall`, `Name`) VALUES
(1, '85.6', '86.56', '85.52', '85.7', 'Gradient Boost Algorithm'),
(2, '85.6', '86.56', '85.52', '85.7', 'Gradient Boost Algorithm'),
(3, '85.6', '86.56', '85.52', '85.7', 'Gradient Boost Algorithm');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=77 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add predict_details', 7, 'add_predict_details'),
(26, 'Can change predict_details', 7, 'change_predict_details'),
(27, 'Can delete predict_details', 7, 'delete_predict_details'),
(28, 'Can view predict_details', 7, 'view_predict_details'),
(29, 'Can add user models', 8, 'add_usermodels'),
(30, 'Can change user models', 8, 'change_usermodels'),
(31, 'Can delete user models', 8, 'delete_usermodels'),
(32, 'Can view user models', 8, 'view_usermodels'),
(33, 'Can add ad a_algo', 9, 'add_ada_algo'),
(34, 'Can change ad a_algo', 9, 'change_ada_algo'),
(35, 'Can delete ad a_algo', 9, 'delete_ada_algo'),
(36, 'Can view ad a_algo', 9, 'view_ada_algo'),
(37, 'Can add an m_algo', 10, 'add_anm_algo'),
(38, 'Can change an m_algo', 10, 'change_anm_algo'),
(39, 'Can delete an m_algo', 10, 'delete_anm_algo'),
(40, 'Can view an m_algo', 10, 'view_anm_algo'),
(41, 'Can add an n_algo', 11, 'add_ann_algo'),
(42, 'Can change an n_algo', 11, 'change_ann_algo'),
(43, 'Can delete an n_algo', 11, 'delete_ann_algo'),
(44, 'Can view an n_algo', 11, 'view_ann_algo'),
(45, 'Can add dataset', 12, 'add_dataset'),
(46, 'Can change dataset', 12, 'change_dataset'),
(47, 'Can delete dataset', 12, 'delete_dataset'),
(48, 'Can view dataset', 12, 'view_dataset'),
(49, 'Can add d t_algo', 13, 'add_dt_algo'),
(50, 'Can change d t_algo', 13, 'change_dt_algo'),
(51, 'Can delete d t_algo', 13, 'delete_dt_algo'),
(52, 'Can view d t_algo', 13, 'view_dt_algo'),
(53, 'Can add kn n_algo', 14, 'add_knn_algo'),
(54, 'Can change kn n_algo', 14, 'change_knn_algo'),
(55, 'Can delete kn n_algo', 14, 'delete_knn_algo'),
(56, 'Can view kn n_algo', 14, 'view_knn_algo'),
(57, 'Can add logistic', 15, 'add_logistic'),
(58, 'Can change logistic', 15, 'change_logistic'),
(59, 'Can delete logistic', 15, 'delete_logistic'),
(60, 'Can view logistic', 15, 'view_logistic'),
(61, 'Can add random forest', 16, 'add_randomforest'),
(62, 'Can change random forest', 16, 'change_randomforest'),
(63, 'Can delete random forest', 16, 'delete_randomforest'),
(64, 'Can view random forest', 16, 'view_randomforest'),
(65, 'Can add sv m_algo', 17, 'add_svm_algo'),
(66, 'Can change sv m_algo', 17, 'change_svm_algo'),
(67, 'Can delete sv m_algo', 17, 'delete_svm_algo'),
(68, 'Can view sv m_algo', 17, 'view_svm_algo'),
(69, 'Can add upload_dataset_model', 18, 'add_upload_dataset_model'),
(70, 'Can change upload_dataset_model', 18, 'change_upload_dataset_model'),
(71, 'Can delete upload_dataset_model', 18, 'delete_upload_dataset_model'),
(72, 'Can view upload_dataset_model', 18, 'view_upload_dataset_model'),
(73, 'Can add x g_algo', 19, 'add_xg_algo'),
(74, 'Can change x g_algo', 19, 'change_xg_algo'),
(75, 'Can delete x g_algo', 19, 'delete_xg_algo'),
(76, 'Can view x g_algo', 19, 'view_xg_algo');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `dataset`
--

DROP TABLE IF EXISTS `dataset`;
CREATE TABLE IF NOT EXISTS `dataset` (
  `DS_ID` int NOT NULL AUTO_INCREMENT,
  `Age` int NOT NULL,
  `Glucose` int NOT NULL,
  `BloodPressure` int NOT NULL,
  `SkinThickness` int NOT NULL,
  `Insulin` int NOT NULL,
  `BMI` int NOT NULL,
  `DiabetesPedigreeFunction` int NOT NULL,
  `Pregnancies` int NOT NULL,
  PRIMARY KEY (`DS_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'usersapp', 'predict_details'),
(8, 'usersapp', 'usermodels'),
(9, 'adminsapp', 'ada_algo'),
(10, 'adminsapp', 'anm_algo'),
(11, 'adminsapp', 'ann_algo'),
(12, 'adminsapp', 'dataset'),
(13, 'adminsapp', 'dt_algo'),
(14, 'adminsapp', 'knn_algo'),
(15, 'adminsapp', 'logistic'),
(16, 'adminsapp', 'randomforest'),
(17, 'adminsapp', 'svm_algo'),
(18, 'adminsapp', 'upload_dataset_model'),
(19, 'adminsapp', 'xg_algo');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-10-05 13:40:30.103792'),
(2, 'auth', '0001_initial', '2023-10-05 13:40:31.060856'),
(3, 'admin', '0001_initial', '2023-10-05 13:40:31.385005'),
(4, 'admin', '0002_logentry_remove_auto_add', '2023-10-05 13:40:31.396171'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2023-10-05 13:40:31.412179'),
(6, 'adminsapp', '0001_initial', '2023-10-05 13:40:31.549939'),
(7, 'contenttypes', '0002_remove_content_type_name', '2023-10-05 13:40:31.693498'),
(8, 'auth', '0002_alter_permission_name_max_length', '2023-10-05 13:40:31.770285'),
(9, 'auth', '0003_alter_user_email_max_length', '2023-10-05 13:40:31.845340'),
(10, 'auth', '0004_alter_user_username_opts', '2023-10-05 13:40:31.855433'),
(11, 'auth', '0005_alter_user_last_login_null', '2023-10-05 13:40:31.910331'),
(12, 'auth', '0006_require_contenttypes_0002', '2023-10-05 13:40:31.914332'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2023-10-05 13:40:31.925331'),
(14, 'auth', '0008_alter_user_username_max_length', '2023-10-05 13:40:31.993107'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2023-10-05 13:40:32.061367'),
(16, 'auth', '0010_alter_group_name_max_length', '2023-10-05 13:40:32.129950'),
(17, 'auth', '0011_update_proxy_permissions', '2023-10-05 13:40:32.208128'),
(18, 'auth', '0012_alter_user_first_name_max_length', '2023-10-05 13:40:32.271122'),
(19, 'sessions', '0001_initial', '2023-10-05 13:40:32.354049'),
(20, 'usersapp', '0001_initial', '2023-10-05 13:40:32.386247'),
(21, 'usersapp', '0002_predict_details_smoking', '2023-10-06 06:26:26.174584');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('06550w9fzgfi46bmt3g42xa2t79hzeqx', 'eyJlbWFpbCI6InRhYnJhekBnbWFpbC5jb20ifQ:1qodb3:_tnYZkiJDAB05Nbvr8yPUZOfmixwtxL1LsA2lwDc06E', '2023-10-20 05:41:57.567949'),
('5nee5qfh3y3mn7l5rjk1orq2v4nbmll7', 'eyJlbWFpbCI6InRhYnJhc0BnbWFpbC5jb20iLCJ1c2VyX2lkIjo1fQ:1qoids:KJgIF3wkkdqgL8iFU_KGVmvEI-ky2vxPIM_SnEJVh8s', '2023-10-20 11:05:12.957580'),
('gfbf623b95au3y4n46pgjj69vrxenpet', 'eyJ1c2VyX2lkIjo0LCJlbWFpbCI6Im1hcmtAZ21haWwuY29tIn0:1qoiYc:obzGq619UkM-rFuhGqkzfXMACD_QU4MhdkTn4pWmkMU', '2023-10-20 10:59:46.392823');

-- --------------------------------------------------------

--
-- Table structure for table `dt_algo`
--

DROP TABLE IF EXISTS `dt_algo`;
CREATE TABLE IF NOT EXISTS `dt_algo` (
  `DT_ID` int NOT NULL AUTO_INCREMENT,
  `Accuracy` longtext NOT NULL,
  `Precession` longtext NOT NULL,
  `F1_Score` longtext NOT NULL,
  `Recall` longtext NOT NULL,
  `Name` longtext NOT NULL,
  PRIMARY KEY (`DT_ID`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `dt_algo`
--

INSERT INTO `dt_algo` (`DT_ID`, `Accuracy`, `Precession`, `F1_Score`, `Recall`, `Name`) VALUES
(1, '97.38', '97.48', '97.38', '97.41', 'Decision Tree Algorithm'),
(2, '97.38', '97.48', '97.38', '97.41', 'Decision Tree Algorithm'),
(3, '97.22', '97.34', '97.22', '97.26', 'Decision Tree Algorithm');

-- --------------------------------------------------------

--
-- Table structure for table `knn_algo`
--

DROP TABLE IF EXISTS `knn_algo`;
CREATE TABLE IF NOT EXISTS `knn_algo` (
  `XG_ID` int NOT NULL AUTO_INCREMENT,
  `Accuracy` longtext NOT NULL,
  `Precession` longtext NOT NULL,
  `F1_Score` longtext NOT NULL,
  `Recall` longtext NOT NULL,
  `Name` longtext NOT NULL,
  PRIMARY KEY (`XG_ID`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `knn_algo`
--

INSERT INTO `knn_algo` (`XG_ID`, `Accuracy`, `Precession`, `F1_Score`, `Recall`, `Name`) VALUES
(1, '92.95', '93.76', '92.93', '93.04', 'KNN Algorithm'),
(2, '92.95', '93.76', '92.93', '93.04', 'KNN Algorithm'),
(3, '92.95', '93.76', '92.93', '93.04', 'KNN Algorithm');

-- --------------------------------------------------------

--
-- Table structure for table `logistic`
--

DROP TABLE IF EXISTS `logistic`;
CREATE TABLE IF NOT EXISTS `logistic` (
  `Logistic_ID` int NOT NULL AUTO_INCREMENT,
  `Accuracy` longtext NOT NULL,
  `Precession` longtext NOT NULL,
  `F1_Score` longtext NOT NULL,
  `Recall` longtext NOT NULL,
  `Name` longtext NOT NULL,
  PRIMARY KEY (`Logistic_ID`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `logistic`
--

INSERT INTO `logistic` (`Logistic_ID`, `Accuracy`, `Precession`, `F1_Score`, `Recall`, `Name`) VALUES
(1, '75.77', '75.84', '75.77', '75.8', 'Logistic Regression Algorithm'),
(2, '75.77', '75.84', '75.77', '75.8', 'Logistic Regression Algorithm'),
(3, '75.77', '75.84', '75.77', '75.8', 'Logistic Regression Algorithm');

-- --------------------------------------------------------

--
-- Table structure for table `predict_detail`
--

DROP TABLE IF EXISTS `predict_detail`;
CREATE TABLE IF NOT EXISTS `predict_detail` (
  `predict_id` int NOT NULL AUTO_INCREMENT,
  `gender` varchar(60) DEFAULT NULL,
  `age` varchar(60) DEFAULT NULL,
  `hypertension` longtext,
  `heart` varchar(60) DEFAULT NULL,
  `married` varchar(60) DEFAULT NULL,
  `work` varchar(60) DEFAULT NULL,
  `residence` varchar(60) DEFAULT NULL,
  `bmi` longtext,
  `glucose` longtext,
  `smoking` longtext,
  PRIMARY KEY (`predict_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `randomforest`
--

DROP TABLE IF EXISTS `randomforest`;
CREATE TABLE IF NOT EXISTS `randomforest` (
  `Random_ID` int NOT NULL AUTO_INCREMENT,
  `Accuracy` longtext NOT NULL,
  `Precession` longtext NOT NULL,
  `F1_Score` longtext NOT NULL,
  `Recall` longtext NOT NULL,
  `Name` longtext NOT NULL,
  PRIMARY KEY (`Random_ID`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `randomforest`
--

INSERT INTO `randomforest` (`Random_ID`, `Accuracy`, `Precession`, `F1_Score`, `Recall`, `Name`) VALUES
(1, '99.02', '99.03', '99.02', '99.03', 'Random Forest Algorithm'),
(2, '99.23', '99.23', '99.23', '99.24', 'Random Forest Algorithm'),
(3, '99.13', '99.13', '99.13', '99.14', 'Random Forest Algorithm');

-- --------------------------------------------------------

--
-- Table structure for table `svm_algo`
--

DROP TABLE IF EXISTS `svm_algo`;
CREATE TABLE IF NOT EXISTS `svm_algo` (
  `SXM_ID` int NOT NULL AUTO_INCREMENT,
  `Accuracy` longtext NOT NULL,
  `Precession` longtext NOT NULL,
  `F1_Score` longtext NOT NULL,
  `Recall` longtext NOT NULL,
  `Name` longtext NOT NULL,
  PRIMARY KEY (`SXM_ID`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `svm_algo`
--

INSERT INTO `svm_algo` (`SXM_ID`, `Accuracy`, `Precession`, `F1_Score`, `Recall`, `Name`) VALUES
(1, '75.0', '75.14', '74.98', '75.04', 'svm Algorithm'),
(2, '75.0', '75.14', '74.98', '75.04', 'svm Algorithm'),
(3, '75.0', '75.14', '74.98', '75.04', 'svm Algorithm');

-- --------------------------------------------------------

--
-- Table structure for table `upload_dataset`
--

DROP TABLE IF EXISTS `upload_dataset`;
CREATE TABLE IF NOT EXISTS `upload_dataset` (
  `User_id` int NOT NULL AUTO_INCREMENT,
  `Dataset` varchar(100) DEFAULT NULL,
  `File_size` varchar(100) NOT NULL,
  `Date_Time` datetime(6) NOT NULL,
  PRIMARY KEY (`User_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `upload_dataset`
--

INSERT INTO `upload_dataset` (`User_id`, `Dataset`, `File_size`, `Date_Time`) VALUES
(1, 'stroke_clean_hEbeC0d.csv', '321.9365234375 kb', '2023-10-06 06:31:04.442414'),
(2, 'stroke_clean_8RoqqtZ.csv', '321.9365234375 kb', '2023-10-06 10:26:52.220132'),
(3, 'stroke_clean_9QjndTW.csv', '321.9365234375 kb', '2023-10-06 10:49:55.173966');

-- --------------------------------------------------------

--
-- Table structure for table `user_details`
--

DROP TABLE IF EXISTS `user_details`;
CREATE TABLE IF NOT EXISTS `user_details` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `name` longtext,
  `contact` longtext,
  `email` varchar(200) DEFAULT NULL,
  `password` longtext,
  `file` varchar(100) DEFAULT NULL,
  `user_status` longtext,
  `Otp_Status` longtext NOT NULL,
  `otp` int DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `user_details`
--

INSERT INTO `user_details` (`user_id`, `date`, `name`, `contact`, `email`, `password`, `file`, `user_status`, `Otp_Status`, `otp`) VALUES
(5, '2023-10-06', 'khadija arif', '1234567888', 'mark@gmail.com', '1111', 'images/zzzz.jpg', 'accepted', 'verified', 9896);

-- --------------------------------------------------------

--
-- Table structure for table `xg_algo`
--

DROP TABLE IF EXISTS `xg_algo`;
CREATE TABLE IF NOT EXISTS `xg_algo` (
  `XG_ID` int NOT NULL AUTO_INCREMENT,
  `Accuracy` longtext NOT NULL,
  `Precession` longtext NOT NULL,
  `F1_Score` longtext NOT NULL,
  `Recall` longtext NOT NULL,
  `Name` longtext NOT NULL,
  PRIMARY KEY (`XG_ID`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `xg_algo`
--

INSERT INTO `xg_algo` (`XG_ID`, `Accuracy`, `Precession`, `F1_Score`, `Recall`, `Name`) VALUES
(1, '97.12', '97.24', '97.12', '97.15', 'XG Boost Algorithm'),
(2, '97.12', '97.24', '97.12', '97.15', 'XG Boost Algorithm'),
(3, '97.12', '97.24', '97.12', '97.15', 'XG Boost Algorithm');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
