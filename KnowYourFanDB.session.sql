-- Cria a tabela de fãs
CREATE TABLE fans (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    favorite_player VARCHAR(100),
    join_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Cria a tabela de interações
CREATE TABLE interactions (
    id SERIAL PRIMARY KEY,
    fan_id INTEGER REFERENCES fans(id) ON DELETE CASCADE,
    interaction_type VARCHAR(100) NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Cria a tabela de pontuação
CREATE TABLE scores (
    id SERIAL PRIMARY KEY,
    fan_id INTEGER REFERENCES fans(id) ON DELETE CASCADE,
    points INTEGER NOT NULL,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
