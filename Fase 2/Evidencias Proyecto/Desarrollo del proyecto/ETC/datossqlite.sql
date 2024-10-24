INSERT INTO
    STORE_TIPOPRODUCTO (ID_TIPO, NOMBRETIPO)
VALUES
    (1, 'Instrumentos de Cuerdas');

INSERT INTO
    STORE_TIPOPRODUCTO (ID_TIPO, NOMBRETIPO)
VALUES
    (2, 'Percusión');

INSERT INTO
    STORE_TIPOPRODUCTO (ID_TIPO, NOMBRETIPO)
VALUES
    (3, 'Amplificadores');

INSERT INTO
    STORE_TIPOPRODUCTO (ID_TIPO, NOMBRETIPO)
VALUES
    (4, 'Accesorios varios');

INSERT INTO
    STORE_CATEGORIA (ID_CATEGORIA, NOMBRECATEGORIA, TIPO_PRODUCTO_ID)
VALUES
    (1, 'Guitarras', 1);

INSERT INTO
    STORE_CATEGORIA (ID_CATEGORIA, NOMBRECATEGORIA, TIPO_PRODUCTO_ID)
VALUES
    (2, 'Bajos', 1);

INSERT INTO
    STORE_CATEGORIA (ID_CATEGORIA, NOMBRECATEGORIA, TIPO_PRODUCTO_ID)
VALUES
    (3, 'pianos', 1);

INSERT INTO
    STORE_CATEGORIA (ID_CATEGORIA, NOMBRECATEGORIA, TIPO_PRODUCTO_ID)
VALUES
    (4, 'Baterías Acústicas', 2);

INSERT INTO
    STORE_CATEGORIA (ID_CATEGORIA, NOMBRECATEGORIA, TIPO_PRODUCTO_ID)
VALUES
    (5, 'Batería Electrónicas', 2);

INSERT INTO
    STORE_CATEGORIA (ID_CATEGORIA, NOMBRECATEGORIA, TIPO_PRODUCTO_ID)
VALUES
    (6, 'Cabezales', 3);

INSERT INTO
    STORE_CATEGORIA (ID_CATEGORIA, NOMBRECATEGORIA, TIPO_PRODUCTO_ID)
VALUES
    (7, 'Cajas', 3);

INSERT INTO
    STORE_CATEGORIA (ID_CATEGORIA, NOMBRECATEGORIA, TIPO_PRODUCTO_ID)
VALUES
    (8, 'Accesorios', 4);

INSERT INTO
    STORE_PROVEEDOR (
        ID_PROVEEDOR,
        NOMBREPROVEEDOR,
        DIRECCION,
        TELEFONO,
        EMAIL,
        FECHA_REGISTRO
    )
VALUES
    (
        1,
        'dodgeRogers',
        'Calle Falsa 123',
        '+56912345678',
        'dodgerogers@mail.com',
        datetime('now')
    );

INSERT INTO
    STORE_PROVEEDOR (
        ID_PROVEEDOR,
        NOMBREPROVEEDOR,
        DIRECCION,
        TELEFONO,
        EMAIL,
        FECHA_REGISTRO
    )
VALUES
    (
        2,
        'Marshall',
        'Avenida Siempre Viva 456',
        '+56923456789',
        'marshall@mail.com',
        datetime('now')
    );

INSERT INTO
    STORE_PROVEEDOR (
        ID_PROVEEDOR,
        NOMBREPROVEEDOR,
        DIRECCION,
        TELEFONO,
        EMAIL,
        FECHA_REGISTRO
    )
VALUES
    (
        3,
        'melenmusic',
        'Pasaje de los Vientos 789',
        '+56934567890',
        'melenmusic@mail.com',
        datetime('now')
    );

INSERT INTO
    STORE_PROVEEDOR (
        ID_PROVEEDOR,
        NOMBREPROVEEDOR,
        DIRECCION,
        TELEFONO,
        EMAIL,
        FECHA_REGISTRO
    )
VALUES
    (
        4,
        'Drums R Us',
        'Calle del Ritmo 321',
        '+56945678901',
        'drumsrus@mail.com',
        datetime('now')
    );

INSERT INTO
    STORE_PROVEEDOR (
        ID_PROVEEDOR,
        NOMBREPROVEEDOR,
        DIRECCION,
        TELEFONO,
        EMAIL,
        FECHA_REGISTRO
    )
VALUES
    (
        5,
        'Music Depot',
        'Avenida de la Música 654',
        '+56956789012',
        'musicdepot@mail.com',
        datetime('now')
    );

INSERT INTO
    STORE_PROVEEDOR (
        ID_PROVEEDOR,
        NOMBREPROVEEDOR,
        DIRECCION,
        TELEFONO,
        EMAIL,
        FECHA_REGISTRO
    )
VALUES
    (
        6,
        'Bass Central',
        'Calle del Bajo 987',
        '+56967890123',
        'basscentral@mail.com',
        datetime('now')
    );

INSERT INTO
    STORE_PROVEEDOR (
        ID_PROVEEDOR,
        NOMBREPROVEEDOR,
        DIRECCION,
        TELEFONO,
        EMAIL,
        FECHA_REGISTRO
    )
VALUES
    (
        7,
        'Musician''s Friend',
        'Avenida de los Acordes 147',
        '+56978901234',
        'musiciansfriend@mail.com',
        datetime('now')
    );

INSERT INTO
    STORE_PROVEEDOR (
        ID_PROVEEDOR,
        NOMBREPROVEEDOR,
        DIRECCION,
        TELEFONO,
        EMAIL,
        FECHA_REGISTRO
    )
VALUES
    (
        8,
        'Sam Ash Music',
        'Calle del Sonido 258',
        '+56989012345',
        'samashmusic@mail.com',
        datetime('now')
    );

INSERT INTO
    STORE_PROVEEDOR (
        ID_PROVEEDOR,
        NOMBREPROVEEDOR,
        DIRECCION,
        TELEFONO,
        EMAIL,
        FECHA_REGISTRO
    )
VALUES
    (
        9,
        'Sweetwater',
        'Avenida de la Grabación 369',
        '+56990123456',
        'sweetwater@mail.com',
        datetime('now')
    );

INSERT INTO
    STORE_PROVEEDOR (
        ID_PROVEEDOR,
        NOMBREPROVEEDOR,
        DIRECCION,
        TELEFONO,
        EMAIL,
        FECHA_REGISTRO
    )
VALUES
    (
        10,
        'ZZounds',
        'Calle del Equipo 753',
        '+56901234567',
        'zzounds@mail.com',
        datetime('now')
    );

INSERT INTO
    STORE_PROVEEDOR (
        ID_PROVEEDOR,
        NOMBREPROVEEDOR,
        DIRECCION,
        TELEFONO,
        EMAIL,
        FECHA_REGISTRO
    )
VALUES
    (
        11,
        'Guitar Emporium',
        'Avenida de las Guitarras 852',
        '+56912345678',
        'guitaremporium@mail.com',
        datetime('now')
    );

INSERT INTO
    STORE_PROVEEDOR (
        ID_PROVEEDOR,
        NOMBREPROVEEDOR,
        DIRECCION,
        TELEFONO,
        EMAIL,
        FECHA_REGISTRO
    )
VALUES
    (
        12,
        'Music Store',
        'Calle de los Instrumentos 951',
        '+56923456789',
        'musicstore@mail.com',
        datetime('now')
    );

INSERT INTO
    STORE_SUBCATEGORIA (
        ID_SUBCATEGORIA,
        NOMBRE_SUBCATEGORIA,
        CATEGORIA_ID
    )
VALUES
    (1, 'Guitarras Cuerpo Solido', 1);

INSERT INTO
    STORE_SUBCATEGORIA (
        ID_SUBCATEGORIA,
        NOMBRE_SUBCATEGORIA,
        CATEGORIA_ID
    )
VALUES
    (2, 'Guitarras Acústicas', 1);

INSERT INTO
    STORE_SUBCATEGORIA (
        ID_SUBCATEGORIA,
        NOMBRE_SUBCATEGORIA,
        CATEGORIA_ID
    )
VALUES
    (3, 'Guitarras Eléctricas', 1);

INSERT INTO
    STORE_SUBCATEGORIA (
        ID_SUBCATEGORIA,
        NOMBRE_SUBCATEGORIA,
        CATEGORIA_ID
    )
VALUES
    (4, 'Bajos Cuatro Cuerdas', 2);

INSERT INTO
    STORE_SUBCATEGORIA (
        ID_SUBCATEGORIA,
        NOMBRE_SUBCATEGORIA,
        CATEGORIA_ID
    )
VALUES
    (5, 'Bajos Cinco Cuerdas', 2);

INSERT INTO
    STORE_SUBCATEGORIA (
        ID_SUBCATEGORIA,
        NOMBRE_SUBCATEGORIA,
        CATEGORIA_ID
    )
VALUES
    (6, 'Bajos Activos', 2);

INSERT INTO
    STORE_SUBCATEGORIA (
        ID_SUBCATEGORIA,
        NOMBRE_SUBCATEGORIA,
        CATEGORIA_ID
    )
VALUES
    (7, 'Bajos Pasivos', 2);

INSERT INTO
    STORE_SUBCATEGORIA (
        ID_SUBCATEGORIA,
        NOMBRE_SUBCATEGORIA,
        CATEGORIA_ID
    )
VALUES
    (8, 'Piano de media cola', 3);

INSERT INTO
    STORE_SUBCATEGORIA (
        ID_SUBCATEGORIA,
        NOMBRE_SUBCATEGORIA,
        CATEGORIA_ID
    )
VALUES
    (9, 'Piano de cola entera', 3);

INSERT INTO
    STORE_SUBCATEGORIA (
        ID_SUBCATEGORIA,
        NOMBRE_SUBCATEGORIA,
        CATEGORIA_ID
    )
VALUES
    (10, 'Pianolas', 3);

INSERT INTO
    STORE_SUBCATEGORIA (
        ID_SUBCATEGORIA,
        NOMBRE_SUBCATEGORIA,
        CATEGORIA_ID
    )
VALUES
    (11, 'Tama', 4);

INSERT INTO
    STORE_SUBCATEGORIA (
        ID_SUBCATEGORIA,
        NOMBRE_SUBCATEGORIA,
        CATEGORIA_ID
    )
VALUES
    (12, 'Pearl', 4);

INSERT INTO
    STORE_SUBCATEGORIA (
        ID_SUBCATEGORIA,
        NOMBRE_SUBCATEGORIA,
        CATEGORIA_ID
    )
VALUES
    (13, 'Sonor', 4);

INSERT INTO
    STORE_SUBCATEGORIA (
        ID_SUBCATEGORIA,
        NOMBRE_SUBCATEGORIA,
        CATEGORIA_ID
    )
VALUES
    (14, 'Mapex', 4);

INSERT INTO
    STORE_SUBCATEGORIA (
        ID_SUBCATEGORIA,
        NOMBRE_SUBCATEGORIA,
        CATEGORIA_ID
    )
VALUES
    (15, 'Roland', 5);

INSERT INTO
    STORE_SUBCATEGORIA (
        ID_SUBCATEGORIA,
        NOMBRE_SUBCATEGORIA,
        CATEGORIA_ID
    )
VALUES
    (16, 'Alesis', 5);

INSERT INTO
    STORE_SUBCATEGORIA (
        ID_SUBCATEGORIA,
        NOMBRE_SUBCATEGORIA,
        CATEGORIA_ID
    )
VALUES
    (17, 'ENGL', 6);

INSERT INTO
    STORE_SUBCATEGORIA (
        ID_SUBCATEGORIA,
        NOMBRE_SUBCATEGORIA,
        CATEGORIA_ID
    )
VALUES
    (18, 'Marshall', 6);

INSERT INTO
    STORE_SUBCATEGORIA (
        ID_SUBCATEGORIA,
        NOMBRE_SUBCATEGORIA,
        CATEGORIA_ID
    )
VALUES
    (19, 'Pavey', 6);

INSERT INTO
    STORE_SUBCATEGORIA (
        ID_SUBCATEGORIA,
        NOMBRE_SUBCATEGORIA,
        CATEGORIA_ID
    )
VALUES
    (20, 'EVH', 6);

INSERT INTO
    STORE_SUBCATEGORIA (
        ID_SUBCATEGORIA,
        NOMBRE_SUBCATEGORIA,
        CATEGORIA_ID
    )
VALUES
    (21, 'ENGL de Caja', 7);

INSERT INTO
    STORE_SUBCATEGORIA (
        ID_SUBCATEGORIA,
        NOMBRE_SUBCATEGORIA,
        CATEGORIA_ID
    )
VALUES
    (22, 'Marshall de Caja', 7);

INSERT INTO
    STORE_SUBCATEGORIA (
        ID_SUBCATEGORIA,
        NOMBRE_SUBCATEGORIA,
        CATEGORIA_ID
    )
VALUES
    (23, 'Pavey de Caja', 7);

INSERT INTO
    STORE_SUBCATEGORIA (
        ID_SUBCATEGORIA,
        NOMBRE_SUBCATEGORIA,
        CATEGORIA_ID
    )
VALUES
    (24, 'EVH de Caja', 7);

INSERT INTO
    STORE_SUBCATEGORIA (
        ID_SUBCATEGORIA,
        NOMBRE_SUBCATEGORIA,
        CATEGORIA_ID
    )
VALUES
    (25, 'Audífonos', 8);

INSERT INTO
    STORE_SUBCATEGORIA (
        ID_SUBCATEGORIA,
        NOMBRE_SUBCATEGORIA,
        CATEGORIA_ID
    )
VALUES
    (26, 'Monitores', 8);

INSERT INTO
    STORE_SUBCATEGORIA (
        ID_SUBCATEGORIA,
        NOMBRE_SUBCATEGORIA,
        CATEGORIA_ID
    )
VALUES
    (27, 'Parlantes', 8);

INSERT INTO
    STORE_SUBCATEGORIA (
        ID_SUBCATEGORIA,
        NOMBRE_SUBCATEGORIA,
        CATEGORIA_ID
    )
VALUES
    (28, 'Cables', 8);

INSERT INTO
    STORE_SUBCATEGORIA (
        ID_SUBCATEGORIA,
        NOMBRE_SUBCATEGORIA,
        CATEGORIA_ID
    )
VALUES
    (29, 'Micrófonos', 8);

INSERT INTO
    STORE_SUBCATEGORIA (
        ID_SUBCATEGORIA,
        NOMBRE_SUBCATEGORIA,
        CATEGORIA_ID
    )
VALUES
    (30, 'Interfaces', 8);

INSERT INTO
    STORE_SUBCATEGORIA (
        ID_SUBCATEGORIA,
        NOMBRE_SUBCATEGORIA,
        CATEGORIA_ID
    )
VALUES
    (31, 'Mixers', 8);

INSERT INTO
    STORE_MARCA (ID_MARCA, NOMBRE_MARCA)
VALUES
    (1, 'Martin');

INSERT INTO
    STORE_MARCA (ID_MARCA, NOMBRE_MARCA)
VALUES
    (2, 'Taylor');

INSERT INTO
    STORE_MARCA (ID_MARCA, NOMBRE_MARCA)
VALUES
    (3, 'Gretsch');

INSERT INTO
    STORE_MARCA (ID_MARCA, NOMBRE_MARCA)
VALUES
    (4, 'Ibanez');

INSERT INTO
    STORE_MARCA (ID_MARCA, NOMBRE_MARCA)
VALUES
    (5, 'Epiphone');

INSERT INTO
    STORE_MARCA (ID_MARCA, NOMBRE_MARCA)
VALUES
    (6, 'Ernie Ball Music Man');

INSERT INTO
    STORE_MARCA (ID_MARCA, NOMBRE_MARCA)
VALUES
    (7, 'Jackson');

INSERT INTO
    STORE_MARCA (ID_MARCA, NOMBRE_MARCA)
VALUES
    (8, 'PRS');

INSERT INTO
    STORE_PRODUCTO (
        ID_PRODUCTO,
        SKU,
        NOMBRE_PRODUCTO,
        PRECIO_COMPRA,
        PRECIO_VENTA,
        PRECIO_OFERTA,
        STOCK,
        IMAGEN_PRODUCTO,
        ACTIVO,
        MARCA_ID,
        SUBCAT_PRODUCTO_ID,
        CATEGORIA_PRODUCTO_ID,
        PROVEEDOR_ID,
        TIPO_PRODUCTO_ID
    )
VALUES
    (
        1,
        'sku005',
        'Bajo Squier',
        800000,
        1000000,
        760000,
        5,
        'productos/images_1.jfif',
        1,
        4,
        4,
        2,
        6,
        1
    );

INSERT INTO
    STORE_PRODUCTO (
        ID_PRODUCTO,
        SKU,
        NOMBRE_PRODUCTO,
        PRECIO_COMPRA,
        PRECIO_VENTA,
        PRECIO_OFERTA,
        STOCK,
        IMAGEN_PRODUCTO,
        ACTIVO,
        MARCA_ID,
        SUBCAT_PRODUCTO_ID,
        CATEGORIA_PRODUCTO_ID,
        PROVEEDOR_ID,
        TIPO_PRODUCTO_ID
    )
VALUES
    (
        2,
        'sku006',
        'Guitarra Martin',
        1200000,
        1500000,
        1300000,
        3,
        'productos/images.jfif',
        1,
        1,
        2,
        1,
        8,
        1
    );

INSERT INTO
    STORE_PRODUCTO (
        ID_PRODUCTO,
        SKU,
        NOMBRE_PRODUCTO,
        PRECIO_COMPRA,
        PRECIO_VENTA,
        PRECIO_OFERTA,
        STOCK,
        IMAGEN_PRODUCTO,
        ACTIVO,
        MARCA_ID,
        SUBCAT_PRODUCTO_ID,
        CATEGORIA_PRODUCTO_ID,
        PROVEEDOR_ID,
        TIPO_PRODUCTO_ID
    )
VALUES
    (
        3,
        'sku007',
        'Pedal de efectos Boss',
        350000,
        450000,
        360000,
        8,
        'productos/shopping_1.webp',
        1,
        1,
        30,
        8,
        5,
        4
    );

INSERT INTO
    STORE_PRODUCTO (
        ID_PRODUCTO,
        SKU,
        NOMBRE_PRODUCTO,
        PRECIO_COMPRA,
        PRECIO_VENTA,
        PRECIO_OFERTA,
        STOCK,
        IMAGEN_PRODUCTO,
        ACTIVO,
        MARCA_ID,
        SUBCAT_PRODUCTO_ID,
        CATEGORIA_PRODUCTO_ID,
        PROVEEDOR_ID,
        TIPO_PRODUCTO_ID
    )
VALUES
    (
        4,
        'PROD-001',
        'Guitarra eléctrica Ibanez',
        500000,
        750000,
        550000,
        10,
        'productos/descargar_1.jfif',
        1,
        4,
        1,
        1,
        11,
        1
    );

INSERT INTO
    STORE_PRODUCTO (
        ID_PRODUCTO,
        SKU,
        NOMBRE_PRODUCTO,
        PRECIO_COMPRA,
        PRECIO_VENTA,
        PRECIO_OFERTA,
        STOCK,
        IMAGEN_PRODUCTO,
        ACTIVO,
        MARCA_ID,
        SUBCAT_PRODUCTO_ID,
        CATEGORIA_PRODUCTO_ID,
        PROVEEDOR_ID,
        TIPO_PRODUCTO_ID
    )
VALUES
    (
        5,
        'PROD-002',
        'Guitarra acústica Taylor',
        800000,
        1200000,
        900000,
        5,
        'productos/D_NQ_NP_824167-MLC43470802747_092020-O.webp',
        1,
        2,
        2,
        1,
        1,
        1
    );

INSERT INTO
    STORE_PRODUCTO (
        ID_PRODUCTO,
        SKU,
        NOMBRE_PRODUCTO,
        PRECIO_COMPRA,
        PRECIO_VENTA,
        PRECIO_OFERTA,
        STOCK,
        IMAGEN_PRODUCTO,
        ACTIVO,
        MARCA_ID,
        SUBCAT_PRODUCTO_ID,
        CATEGORIA_PRODUCTO_ID,
        PROVEEDOR_ID,
        TIPO_PRODUCTO_ID
    )
VALUES
    (
        6,
        'PROD-003',
        'Bajo eléctrico PRS',
        600000,
        900000,
        750000,
        3,
        'productos/imagen_2023-05-16_035757311.png',
        1,
        8,
        4,
        2,
        7,
        1
    );

INSERT INTO
    STORE_PRODUCTO (
        ID_PRODUCTO,
        SKU,
        NOMBRE_PRODUCTO,
        PRECIO_COMPRA,
        PRECIO_VENTA,
        PRECIO_OFERTA,
        STOCK,
        IMAGEN_PRODUCTO,
        ACTIVO,
        MARCA_ID,
        SUBCAT_PRODUCTO_ID,
        CATEGORIA_PRODUCTO_ID,
        PROVEEDOR_ID,
        TIPO_PRODUCTO_ID
    )
VALUES
    (
        7,
        'G001',
        'Guitarra eléctrica',
        10000000,
        15000000,
        13000000,
        10,
        'productos/shopping.webp',
        1,
        3,
        3,
        1,
        12,
        1
    );

INSERT INTO
    STORE_PRODUCTO (
        ID_PRODUCTO,
        SKU,
        NOMBRE_PRODUCTO,
        PRECIO_COMPRA,
        PRECIO_VENTA,
        PRECIO_OFERTA,
        STOCK,
        IMAGEN_PRODUCTO,
        ACTIVO,
        MARCA_ID,
        SUBCAT_PRODUCTO_ID,
        CATEGORIA_PRODUCTO_ID,
        PROVEEDOR_ID,
        TIPO_PRODUCTO_ID
    )
VALUES
    (
        8,
        'G002',
        'Guitarra acústica',
        800000,
        1200000,
        900000,
        5,
        'productos/imagen_2023-05-15_201432085.png',
        1,
        2,
        2,
        1,
        3,
        1
    );

INSERT INTO
    STORE_PRODUCTO (
        ID_PRODUCTO,
        SKU,
        NOMBRE_PRODUCTO,
        PRECIO_COMPRA,
        PRECIO_VENTA,
        PRECIO_OFERTA,
        STOCK,
        IMAGEN_PRODUCTO,
        ACTIVO,
        MARCA_ID,
        SUBCAT_PRODUCTO_ID,
        CATEGORIA_PRODUCTO_ID,
        PROVEEDOR_ID,
        TIPO_PRODUCTO_ID
    )
VALUES
    (
        9,
        'B001',
        'Bajo eléctrico',
        1200000,
        1800000,
        1400000,
        3,
        'productos/descargar_jPHOJwm.jfif',
        1,
        4,
        4,
        2,
        2,
        1
    );