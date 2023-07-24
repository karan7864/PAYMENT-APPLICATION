-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 05, 2022 at 12:00 PM
-- Server version: 10.4.20-MariaDB
-- PHP Version: 7.4.22

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `loan_management_system`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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
(25, 'Can add contact', 7, 'add_contact'),
(26, 'Can change contact', 7, 'change_contact'),
(27, 'Can delete contact', 7, 'delete_contact'),
(28, 'Can view contact', 7, 'view_contact'),
(29, 'Can add loan application', 8, 'add_loanapplication'),
(30, 'Can change loan application', 8, 'change_loanapplication'),
(31, 'Can delete loan application', 8, 'delete_loanapplication'),
(32, 'Can view loan application', 8, 'view_loanapplication'),
(33, 'Can add loan type', 9, 'add_loantype'),
(34, 'Can change loan type', 9, 'change_loantype'),
(35, 'Can delete loan type', 9, 'delete_loantype'),
(36, 'Can view loan type', 9, 'view_loantype'),
(37, 'Can add user profile', 10, 'add_userprofile'),
(38, 'Can change user profile', 10, 'change_userprofile'),
(39, 'Can delete user profile', 10, 'delete_userprofile'),
(40, 'Can view user profile', 10, 'view_userprofile'),
(41, 'Can add loan schedule', 11, 'add_loanschedule'),
(42, 'Can change loan schedule', 11, 'change_loanschedule'),
(43, 'Can delete loan schedule', 11, 'delete_loanschedule'),
(44, 'Can view loan schedule', 11, 'view_loanschedule'),
(45, 'Can add loan defaulters reminder', 12, 'add_loandefaultersreminder'),
(46, 'Can change loan defaulters reminder', 12, 'change_loandefaultersreminder'),
(47, 'Can delete loan defaulters reminder', 12, 'delete_loandefaultersreminder'),
(48, 'Can view loan defaulters reminder', 12, 'view_loandefaultersreminder');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$320000$c8tQOOvJFhULnNUm9UspMT$SdO+q6vtXAZwRCHVOiGHiliBEsZuTsT1+hoyavwNSGU=', '2022-06-05 09:31:50.284361', 0, 'Pulkit', '', '', '', 0, 1, '2022-05-29 05:59:12.000000'),
(2, 'pbkdf2_sha256$320000$UsDPD0ZtDXOO9TCIgL3HK1$pVth/JnxfVarivjYtFTyQKjK5euaNl53wVAYfH+Lp2o=', '2022-06-05 09:32:31.419564', 1, 'admin', '', '', '', 1, 1, '2022-06-05 09:13:19.905391');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2022-06-05 09:24:47.662220', '1', 'Pulkit', 2, '[{\"changed\": {\"fields\": [\"Staff status\", \"Superuser status\"]}}]', 4, 2);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(7, 'loan_app', 'contact'),
(8, 'loan_app', 'loanapplication'),
(12, 'loan_app', 'loandefaultersreminder'),
(11, 'loan_app', 'loanschedule'),
(9, 'loan_app', 'loantype'),
(10, 'loan_app', 'userprofile'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2022-05-29 05:54:41.001234'),
(2, 'auth', '0001_initial', '2022-05-29 05:54:52.045745'),
(3, 'admin', '0001_initial', '2022-05-29 05:54:54.818535'),
(4, 'admin', '0002_logentry_remove_auto_add', '2022-05-29 05:54:56.337285'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2022-05-29 05:54:56.415427'),
(6, 'contenttypes', '0002_remove_content_type_name', '2022-05-29 05:54:57.149692'),
(7, 'auth', '0002_alter_permission_name_max_length', '2022-05-29 05:54:58.366791'),
(8, 'auth', '0003_alter_user_email_max_length', '2022-05-29 05:54:58.616788'),
(9, 'auth', '0004_alter_user_username_opts', '2022-05-29 05:54:58.710534'),
(10, 'auth', '0005_alter_user_last_login_null', '2022-05-29 05:54:59.335607'),
(11, 'auth', '0006_require_contenttypes_0002', '2022-05-29 05:54:59.413682'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2022-05-29 05:54:59.476218'),
(13, 'auth', '0008_alter_user_username_max_length', '2022-05-29 05:54:59.648034'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2022-05-29 05:54:59.789119'),
(15, 'auth', '0010_alter_group_name_max_length', '2022-05-29 05:54:59.960522'),
(16, 'auth', '0011_update_proxy_permissions', '2022-05-29 05:55:00.023021'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2022-05-29 05:55:00.226176'),
(18, 'loan_app', '0001_initial', '2022-05-29 05:55:11.101599'),
(19, 'sessions', '0001_initial', '2022-05-29 05:55:12.103566');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('2g0chq4bt333tmzr9dslqdifu3kgq2cf', '.eJxVjDsOwjAQRO_iGln-4B8lPWewdtcbHECOFCcV4u4kUgqYct6beYsM61Lz2nnOYxEXYcTpt0OgJ7cdlAe0-yRpass8otwVedAub1Ph1_Vw_w4q9Lqt2SataEtwbIKLqSjAYtUAFgavkSJGCKgZiRHCmRygMuSTh4Q6WfH5Ag7KOQ8:1nxmcZ:_91ZW4p1wmtal8ZRGm_zKG2tppe75FzOovmLKGLWEyg', '2022-06-05 21:32:31.540584');

-- --------------------------------------------------------

--
-- Table structure for table `loan_app_contact`
--

CREATE TABLE `loan_app_contact` (
  `id` bigint(20) NOT NULL,
  `name` varchar(60) NOT NULL,
  `email` varchar(80) NOT NULL,
  `subject` varchar(200) NOT NULL,
  `message` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `loan_app_loanapplication`
--

CREATE TABLE `loan_app_loanapplication` (
  `id` bigint(20) NOT NULL,
  `application_id` varchar(100) DEFAULT NULL,
  `full_name` varchar(60) NOT NULL,
  `contact_no` varchar(10) NOT NULL,
  `pan_no` varchar(10) NOT NULL,
  `aadhar_no` varchar(12) NOT NULL,
  `residential_address` varchar(200) NOT NULL,
  `service_type` varchar(60) NOT NULL,
  `official_address` varchar(200) NOT NULL,
  `income` varchar(30) NOT NULL,
  `existing_loan` varchar(10) NOT NULL,
  `expected_loan_amount` double NOT NULL,
  `expected_loan_tenure` varchar(30) NOT NULL,
  `collateral_name` varchar(200) DEFAULT NULL,
  `collateral_value` double NOT NULL,
  `profile_photo` varchar(100) NOT NULL,
  `pan_image` varchar(100) NOT NULL,
  `aadhar_image` varchar(100) NOT NULL,
  `account_number` varchar(100) NOT NULL,
  `bank_name` varchar(100) NOT NULL,
  `bank_ifsc_code` varchar(30) NOT NULL,
  `remarks` varchar(300) DEFAULT NULL,
  `reject_reason` varchar(1000) DEFAULT NULL,
  `loan_application_status` varchar(50) DEFAULT NULL,
  `is_approved` tinyint(1) NOT NULL,
  `approved_date` datetime(6) DEFAULT NULL,
  `rejected_date` datetime(6) DEFAULT NULL,
  `is_disbursed` tinyint(1) NOT NULL,
  `disbursed_date` datetime(6) DEFAULT NULL,
  `first_payment_date` date DEFAULT NULL,
  `tenure_left` int(11) DEFAULT NULL,
  `payment_schedule` varchar(100) DEFAULT NULL,
  `loan_completed` tinyint(1) NOT NULL,
  `created_on` datetime(6) NOT NULL,
  `loan_applied_for_id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `loan_app_loandefaultersreminder`
--

CREATE TABLE `loan_app_loandefaultersreminder` (
  `id` bigint(20) NOT NULL,
  `status` varchar(100) DEFAULT NULL,
  `recovered_amount` double DEFAULT NULL,
  `recovery_date` datetime(6) DEFAULT NULL,
  `remarks` longtext DEFAULT NULL,
  `created_on` datetime(6) NOT NULL,
  `updated_on` datetime(6) NOT NULL,
  `loan_id_id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `loan_app_loanschedule`
--

CREATE TABLE `loan_app_loanschedule` (
  `id` bigint(20) NOT NULL,
  `payment_date` date DEFAULT NULL,
  `monthly_amount` double DEFAULT NULL,
  `emi_paid` tinyint(1) NOT NULL,
  `emi_paid_date` date DEFAULT NULL,
  `razorpay_payment_id` varchar(200) DEFAULT NULL,
  `loan_id_id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `loan_app_loantype`
--

CREATE TABLE `loan_app_loantype` (
  `id` bigint(20) NOT NULL,
  `loan_name` varchar(200) NOT NULL,
  `loan_desc` longtext NOT NULL,
  `max_loan_amount` double NOT NULL,
  `loan_roi` double NOT NULL,
  `max_loan_duration` varchar(4) NOT NULL,
  `loan_category` varchar(100) NOT NULL,
  `need_security` tinyint(1) DEFAULT NULL,
  `loan_image` varchar(100) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `loan_app_loantype`
--

INSERT INTO `loan_app_loantype` (`id`, `loan_name`, `loan_desc`, `max_loan_amount`, `loan_roi`, `max_loan_duration`, `loan_category`, `need_security`, `loan_image`, `created_at`, `updated_at`) VALUES
(1, 'Home Loans', 'Buying a house is a dream for many and involves a lot of financial planning. LOANPAY Loans makes it simpler for those who want to realise this dream.', 10000000, 8.5, '360', 'Secured', 1, '/media/home_loan.jpg', '2022-06-05 09:37:39.039341', '2022-06-05 09:42:57.318966'),
(2, 'Education Loans', 'Going abroad for higher studies? Or there’s a course that is domestic and expensive? Whatever be your reason for higher studies, it’s understood that higher education is often very expensive, with the rising cost of education. But that shouldn’t stop you!  We, at LOANPAY, understand about your career aspirations and offer the needed Student Loans, for successfully aiding your journey to higher education.', 100000, 9.5, '60', 'Unsecured', 0, '/media/education_loan.jpg', '2022-06-05 09:42:36.214656', '2022-06-05 09:43:35.249956'),
(3, 'Personal Loans', 'We understand that in these unprecedented times, our plans for travelling and have destination weddings have got postponed & new needs have emerged. A need for a safe and comfortable lifestyle, a need to have a safety net to tackle any unplanned/immediate requirement.  ​​​​​And to help you fulfil all these needs during these challenging times, LOANPAY is ‘There For You’ with its instant Personal Loan.', 100000, 12.5, '60', 'Unsecured', 0, '/media/personal_loan.jpg', '2022-06-05 09:46:24.540849', '2022-06-05 09:47:08.009599'),
(4, 'Car Loans', 'With the advancement of latest technologies, life is changing faster and so do the car models. New facelift versions and new variants are launching quite frequently making it difficult to resist the temptation for upgrading to the car of latest technology.  These new car models complimented with various financing schemes offered by LOANPAY Car Loans make it easier to upgrade to the car of your choice with attractive rate of interest.', 500000, 6.5, '60', 'Secured', 1, '/media/car_loan.jpg', '2022-06-05 09:48:58.304462', '2022-06-05 09:51:57.952763'),
(5, 'Gold Loans', 'LOANPAY offers loan against gold jewellery. A customer can quickly avail of a Gold Loan for any value upto 1 Lakh with simple and easy documentation process.', 100000, 12.5, '24', 'Unsecured', 0, '/media/gold_loan.jpg', '2022-06-05 09:55:47.976936', '2022-06-05 09:55:47.976936');

-- --------------------------------------------------------

--
-- Table structure for table `loan_app_userprofile`
--

CREATE TABLE `loan_app_userprofile` (
  `id` bigint(20) NOT NULL,
  `contact` varchar(10) NOT NULL,
  `full_name` varchar(200) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `loan_app_contact`
--
ALTER TABLE `loan_app_contact`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `loan_app_loanapplication`
--
ALTER TABLE `loan_app_loanapplication`
  ADD PRIMARY KEY (`id`),
  ADD KEY `loan_app_loanapplica_loan_applied_for_id_e27c2d97_fk_loan_app_` (`loan_applied_for_id`),
  ADD KEY `loan_app_loanapplication_user_id_5ada8561_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `loan_app_loandefaultersreminder`
--
ALTER TABLE `loan_app_loandefaultersreminder`
  ADD PRIMARY KEY (`id`),
  ADD KEY `loan_app_loandefault_loan_id_id_13dae732_fk_loan_app_` (`loan_id_id`),
  ADD KEY `loan_app_loandefaultersreminder_user_id_ce78e32a_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `loan_app_loanschedule`
--
ALTER TABLE `loan_app_loanschedule`
  ADD PRIMARY KEY (`id`),
  ADD KEY `loan_app_loanschedul_loan_id_id_0ab68b64_fk_loan_app_` (`loan_id_id`),
  ADD KEY `loan_app_loanschedule_user_id_720f36d8_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `loan_app_loantype`
--
ALTER TABLE `loan_app_loantype`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `loan_app_userprofile`
--
ALTER TABLE `loan_app_userprofile`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `loan_app_contact`
--
ALTER TABLE `loan_app_contact`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `loan_app_loanapplication`
--
ALTER TABLE `loan_app_loanapplication`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `loan_app_loandefaultersreminder`
--
ALTER TABLE `loan_app_loandefaultersreminder`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `loan_app_loanschedule`
--
ALTER TABLE `loan_app_loanschedule`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `loan_app_loantype`
--
ALTER TABLE `loan_app_loantype`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `loan_app_userprofile`
--
ALTER TABLE `loan_app_userprofile`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `loan_app_loanapplication`
--
ALTER TABLE `loan_app_loanapplication`
  ADD CONSTRAINT `loan_app_loanapplica_loan_applied_for_id_e27c2d97_fk_loan_app_` FOREIGN KEY (`loan_applied_for_id`) REFERENCES `loan_app_loantype` (`id`),
  ADD CONSTRAINT `loan_app_loanapplication_user_id_5ada8561_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `loan_app_loandefaultersreminder`
--
ALTER TABLE `loan_app_loandefaultersreminder`
  ADD CONSTRAINT `loan_app_loandefault_loan_id_id_13dae732_fk_loan_app_` FOREIGN KEY (`loan_id_id`) REFERENCES `loan_app_loanapplication` (`id`),
  ADD CONSTRAINT `loan_app_loandefaultersreminder_user_id_ce78e32a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `loan_app_loanschedule`
--
ALTER TABLE `loan_app_loanschedule`
  ADD CONSTRAINT `loan_app_loanschedul_loan_id_id_0ab68b64_fk_loan_app_` FOREIGN KEY (`loan_id_id`) REFERENCES `loan_app_loanapplication` (`id`),
  ADD CONSTRAINT `loan_app_loanschedule_user_id_720f36d8_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `loan_app_userprofile`
--
ALTER TABLE `loan_app_userprofile`
  ADD CONSTRAINT `loan_app_userprofile_user_id_c56f3cee_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
