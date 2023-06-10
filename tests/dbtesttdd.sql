-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 10-06-2023 a las 23:53:21
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `dbtesttdd`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `delete_app`
--

CREATE TABLE `delete_app` (
  `token` varchar(50) NOT NULL,
  `owner_name` varchar(50) NOT NULL,
  `app_name` varchar(50) NOT NULL,
  `prueba` varchar(50) NOT NULL,
  `coderesponse` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `delete_app`
--

INSERT INTO `delete_app` (`token`, `owner_name`, `app_name`, `prueba`, `coderesponse`) VALUES
('f8089fa89e9c5cf1f2733de33fa80a0c79965fed', 'sdviana-unicesar.edu.co', 'prueba', '\r\ndeleteAPP2', 404),
('a17ac3eeb3287a4e4a11af8c99c3f72995ec7146', 'ValeRodriguezV', 'Ejercicio', 'deleteAPP', 200);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `get_app`
--

CREATE TABLE `get_app` (
  `token` varchar(50) NOT NULL,
  `display_name` varchar(50) NOT NULL,
  `app_name` varchar(50) NOT NULL,
  `prueba` varchar(50) NOT NULL,
  `coderesponse` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `get_app`
--

INSERT INTO `get_app` (`token`, `display_name`, `app_name`, `prueba`, `coderesponse`) VALUES
('c3ac3cb4ff2631ddf05178923363b1f44825efe1', 'prueba3', 'prueba3', 'getAPP', 200);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `get_users`
--

CREATE TABLE `get_users` (
  `token` varchar(50) NOT NULL,
  `id` varchar(70) NOT NULL,
  `display_name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `avatar_url` varchar(50) DEFAULT NULL,
  `can_change_password` varchar(50) NOT NULL,
  `created_at` varchar(50) NOT NULL,
  `origin` varchar(50) NOT NULL,
  `coderesponse` int(11) NOT NULL,
  `prueba` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `get_users`
--

INSERT INTO `get_users` (`token`, `id`, `display_name`, `email`, `name`, `avatar_url`, `can_change_password`, `created_at`, `origin`, `coderesponse`, `prueba`) VALUES
('44553a4d814c683dba358422dd900ae70f0a3d97', '4dcfca95-eacb-43bf-814a-9656ff0c2dd9', 'SNEIDER VIANA', 'sdviana@unicesar.edu.co', 'sdviana-unicesar.edu.co', 'None', 'False', '2023-05-11T23:36:40.331Z', 'appcenter', 200, 'perfilUsuario'),
('8949f300d5de19da375418cbc224250d9340b9a9', '7020326b-7451-4773-9950-3370b0178f8d', 'Vale Rodriguez', 'vrodriguezv@unicesar.edu.co', 'ValeRodriguezV', 'None', 'False', '2023-05-09T23:41:24.403Z', 'appcenter', 200, 'perfilUsuario'),
('12345667788', '13213hv3u1yv3v13y13', 'prueba Fallida', 'pruebaFallida', 'pruebaFallida', 'None', 'False', 'eqobdakdakd', 'adaddad', 401, 'token_incorrecto');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `patch_user`
--

CREATE TABLE `patch_user` (
  `token` varchar(50) NOT NULL,
  `display_name` varchar(50) NOT NULL,
  `coderesponse` int(11) NOT NULL,
  `prueba` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `patch_user`
--

INSERT INTO `patch_user` (`token`, `display_name`, `coderesponse`, `prueba`) VALUES
('44553a4d814c683dba358422dd900ae70f0a3d97', 'valentina rodriguez', 200, 'ModificaCP7'),
('44553a4d814c683dba358422dd900ae', 'SNEIDER VIANA', 401, 'ModificaCP8');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `post_orgs`
--

CREATE TABLE `post_orgs` (
  `token` varchar(50) NOT NULL,
  `display_name` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `prueba` varchar(50) NOT NULL,
  `coderesponse` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `post_orgs`
--

INSERT INTO `post_orgs` (`token`, `display_name`, `name`, `prueba`, `coderesponse`) VALUES
('c3ac3cb4ff2631ddf05178923363b1f44825efe1', 'org-preba13', 'ORG-CP3', 'pruebaCP13', 201);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
