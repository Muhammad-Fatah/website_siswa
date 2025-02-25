CREATE DATABASE IF NOT EXISTS siswa_db;
USE siswa_db;

CREATE TABLE IF NOT EXISTS siswa (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(100) NOT NULL,
    kelas VARCHAR(50) NOT NULL
);

INSERT INTO siswa (nama, kelas) VALUES
('Budi Santoso', '10A'),
('Siti Aminah', '11B'),
('Andi Wijaya', '12C');
