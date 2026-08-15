import app


def test_add_task():
    app.tasks.clear()

    task = app.add_task("Learn Git", "high")

    assert task["title"] == "Learn Git"
    assert task["completed"] is False
    assert task["priority"] == "high"


def test_delete_task():
    app.tasks.clear()

    app.add_task("Learn Git")
    result = app.delete_task(1)

    assert result is True
    assert app.tasks == []


def test_get_tasks():
    app.tasks.clear()

    app.add_task("Learn Git")

    assert len(app.get_tasks()) == 1
    assert app.get_tasks()[0]["title"] == "Learn Git"
