DROP TABLE IF EXISTS TipoUsuario;

CREATE TABLE tbTipoUsuario (
    idTipoUsuario  NUMERIC (12) PRIMARY KEY
                                UNIQUE
                                NOT NULL,
    strTupoUsuario CHAR (140)   NOT NULL
);
