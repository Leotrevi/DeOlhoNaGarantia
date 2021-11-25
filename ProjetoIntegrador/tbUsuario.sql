
DROP TABLE IF EXISTS tbUsuario;


CREATE TABLE tbUsuario (
    IdUsuario    INTEGER (12) PRIMARY KEY AUTOINCREMENT,

    strEmail      CHAR (140)   NOT NULL
                               UNIQUE,
    strSenha      CHAR (140)   NOT NULL,
    dtInclusao    DATE         NOT NULL,
    idTipoUsuario NUMERIC (12) REFERENCES tbTipoUsuario (idTipoUsuario)
                               NOT NULL
                               DEFAULT (1)
);
