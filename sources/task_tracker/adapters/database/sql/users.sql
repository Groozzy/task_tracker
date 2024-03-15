-- :name select_all :many
SELECT * FROM users

-- :name select_by_email :one
SELECT * FROM users WHERE email = :email

-- :name insert
INSERT INTO users (name, email) VALUES (:name, :email);

-- :name delete
DELETE FROM users WHERE id = :user.id
