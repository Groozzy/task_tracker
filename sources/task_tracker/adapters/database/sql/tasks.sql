-- :name select_user_tasks :many
SELECT * FROM tasks WHERE user_id = :user_id

-- :name select_uncompleted_user_tasks :many
SELECT * FROM (:include:select_user_tasks) WHERE completed = FALSE

-- :name select_user_tasks_with_deadline_over :many
SELECT * FROM (:include:select_uncompleted_user_tasks) WHERE deadline > :deadline

-- :name insert
INSERT INTO tasks (author, title, description, deadline, completed)
       VALUES (:task.author, :task.title, :task.description, :task.deadline, :task.completed)

-- :name delete
DELETE FROM tasks WHERE id = :task.id
